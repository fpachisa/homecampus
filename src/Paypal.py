'''
PayPal on Python, v. 0.6

$LastChangedDate: 2010-02-05 09:21:47 -0500 (Fri, 05 Feb 2010) $
$LastChangedRevision: 1871 $

Implements the Paypal NVP interface.
Sample usage:

import paypal
pp = paypal.PayPal(MY_USERNAME, MY_PASSWORD,
                   MY_SIGNATURE)
pp.DoDirectPayment(paymentaction='Sale', ipaddress='1.2.3.4', ...)

See the PayPal NVP documentation for a description of which parameters
are required for each API call.

https://cms.paypal.com/cms_content/US/en_US/files/developer/PP_NVPAPI_DeveloperGuide.pdf


Modified by farhat@homecampus.com.sg on 02-Dec-2012 based on new HomeCampus requirement and new Paypal documentation
Modified by faraht@homecampus.com.sg on 19-Aug-2013 to cater to recurring payment

'''

#------------------------------------------------------------------------------
# Changes:
#
# version 0.6:
# * Fix date handling.
# * Change license from Affero GPL to GPL.
# * Implement recurring payments.
# * Implement Fraud Management Filters.
# * Implement reference transactions.

################################################################################
# Copyright 2009 Edmund M. Sullivan, Chicken Wing Software
# www.chickenwingsw.com
#
#     This program is free software: you can redistribute it and/or
#     modify it under the terms of the GNU General Public
#     License as published by the Free Software Foundation, either
#     version 3 of the License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public
#     License along with this program.  If not, see
#     <http://www.gnu.org/licenses/>.
################################################################################
    
from urllib import urlopen, urlencode
import cgi
from cgi import parse_qs
from decimal import Decimal
from datetime import date, datetime
from google.appengine.api import urlfetch
import logging

# Uncomment this for some debugging info:
#logging.basicConfig(level=logging.DEBUG)

# These are the example credentials from the PayPal developer site.
#PAYPAL_TEST_USERNAME = 'admin_1354263385_biz_api1.homecampus.com.sg'
#PAYPAL_TEST_PASSWORD = '1354263422'
#PAYPAL_TEST_SIGNATURE = 'A4KUl3FdOZrCjKCfKOGbZuaGnRVBAn2dh0y84v.B9nibmvvBvlmbGFFs'

#TEST
#PAYPAL_SIG_URL = 'https://api-3t.sandbox.paypal.com/nvp'

#PRODUCTION
PAYPAL_SIG_URL = 'https://api-3t.paypal.com/nvp'

SKIP_AMT_VALIDATION = True

class PayPalException(Exception):
    '''
    An exception for when something goes wrong communicating with
    PayPal.
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value.__str__()

class ShortDate(object):
    '''
    Represents a short date - just year and month.
    '''
    def __init__(self, year, month):
        self.dateObj = date(year, month, 1)
        
    def __str__(self):
        # Convert to MMYYYY - No day #s required for PayPal credit card dates.
        return self.dateObj.strftime('%m%Y')
        
class Param(object):
    '''
    Represents one parameter to a Paypal NVP call.
    '''
    def __init__(self, name, maxLen=None, paramType=str, optional=False, minLen=None, allowedChars=None,
                 allowedValues=None, validatorFun=None, minAmt=None, maxAmt=None):
        self.name = name
        self.paramType = paramType
        self.maxLen = maxLen
        self.minLen = minLen
        self.allowedChars = allowedChars
        self.optional = optional
        self.allowedValues = allowedValues
        self.validatorFun = validatorFun
        self.minAmt = minAmt
        self.maxAmt = maxAmt
        self.val = None

    def __str__(self):
        return self.name

    def toLongString(self):
        return '%s:%s' % (self.name, self.val)

    def validate(self, value):
        '''
        Checks to make sure value is appropriate for this parameter.
        '''
        if isinstance(value, unicode) and self.paramType is str:
            value = value.encode('utf-8')
        if type(value) is not self.paramType:
            raise PayPalException('Parameter %s incorrect type, wanted %s, got %s' %\
                                      (self.name, self.paramType, type(value)))
        # Convert types
        if self.paramType is bool:
            if value:
                value = '1'
            else:
                value = '0'
        elif self.paramType is date:
            value = datetime(value.year, value.month, value.day).isoformat()

        if self.maxLen != None and len(str(value)) > self.maxLen:
            raise PayPalException('Parameter %s too long' % self.name)
        if self.minLen != None and len(str(value)) < self.minLen:
            raise PayPalException('Parameter %s too short' % self.name)
        
        if self.paramType is int and self.minAmt != None and value < self.minAmt:
            raise PayPalException('Parameter %s below minimum value %s' % (self.name, self.minAmt))
        
        if self.paramType is int and self.maxAmt != None and value > self.maxAmt:
            raise PayPalException('Parameter %s exceeds maximum value %s' % (self.name, self.maxAmt))
        if self.allowedChars != None:
            for ch in value:
                if ch not in self.allowedChars:
                    raise PayPalException('Parameter %s has invalid character' % self.name)
        if self.allowedValues != None and value not in self.allowedValues:
            raise PayPalException('Parameter %s has disallowed value' % self.name)
        if self.validatorFun:
            self.validatorFun(value)
        # All good
        self.val = value

    def __str__(self):
        return str(self.val)

    def __unicode__(self):
        return unicode(self.val)
        

# ES: Go through ParamList fields, checking "optional" value.
class ParamList(Param):
    def validate(self, valueList):
        for val in valueList:
            Param.validate(self, val)

    
# Note: This is limited to US currency
def validateAmt(val):
    '''
    Validates a dollar amount.
    '''
    if SKIP_AMT_VALIDATION:
        return
    if val[-3] != '.':
        raise PayPalException('Amount must have two decimal places')
    # Ignore the optional thousands separator.
    val = val.replace(',', '')
    if Decimal(val) > 10000:
        raise PayPalException('Amount too big')

def validateIp(val):
    '''
    Validates an IP address.
    '''
    nums = val.split('.')
    if len(nums) != 4:
        raise PayPalException('Invalid IP address value (wrong number of dots): %s' % val)
    for numStr in nums:
        try:
            num = int(numStr)
            if num < 0 or num > 255:
                raise PayPalException('Invalid IP address value (%d out of range): %s' % (num, val))
        except ValueError:
            raise PayPalException('Invalid IP address value (%s not an integer): %s' % (numStr, val))

NUMBERS='0123456789'
HEX_DIGITS=NUMBERS+'abcdefABCDEF'
ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ALPHANUM=ALPHA+NUMBERS

def ParamAmt(name='PAYMENTREQUEST_0_AMT', optional=False):
    '''
    Creates a parameter for a dollar amount.
    '''
    # Note: This is limited to US currency
    return Param(name, maxLen=8, allowedChars=NUMBERS+'.,-',
                 validatorFun=validateAmt, optional=optional)

def ParamListAmt(name='PAYMENTREQUEST_0_AMT', optional=False):
    # Note: This is limited to US currency
    return ParamList(name, maxLen=8, allowedChars=NUMBERS+'.,-',
                     validatorFun=validateAmt, optional=optional)

def ParamColor(name, optional=False):
    '''
    Creates a parameter for a color as hex digits.
    '''
    return Param(name, maxLen=6, minLen=6, allowedChars=HEX_DIGITS, optional=optional)

def ParamCurrencyCode(name='PAYMENTREQUEST_0_CURRENCYCODE', optional=False):
    '''
    Creates a parameter for a currency code.
    '''
    return Param(name, maxLen=3, optional=optional)
        
# Methods in the PayPal API
METHODS = {   
    'SetExpressCheckout': (
        ParamAmt(),
        ParamCurrencyCode(optional=True),
        ParamAmt('MAXAMT', optional=True),
        Param('RETURNURL', 2048),
        Param('CANCELURL', 2048),
        ParamAmt('L_PAYMENTREQUEST_0_AMT0', optional=True),
        Param('PAYMENTREQUEST_0_PAYMENTACTION',optional=True),
        Param('L_PAYMENTREQUEST_0_ITEMCATEGORY0',optional=True),
        Param('L_PAYMENTREQUEST_0_NAME0',optional=True),
        Param('L_PAYMENTREQUEST_0_QTY0',optional=True),
        Param('L_BILLINGTYPE0'),
        Param('L_BILLINGAGREEMENTDESCRIPTION0'),
        ),

    'GetExpressCheckoutDetails': (
        Param('TOKEN', maxLen=20),
        ),

    'DoExpressCheckoutPayment': (
        Param('TOKEN', maxLen=20),
        Param('PAYERID', maxLen=13, allowedChars=ALPHANUM),

        # Payment details type fields
        ParamAmt(),
        ParamCurrencyCode(),
        ParamAmt('L_PAYMENTREQUEST_0_AMT0', optional=True),
        Param('PAYMENTREQUEST_0_PAYMENTACTION',optional=True),
        Param('L_PAYMENTREQUEST_0_ITEMCATEGORY0',optional=True),
        Param('L_PAYMENTREQUEST_0_NAME0',optional=True),
        Param('L_PAYMENTREQUEST_0_QTY0',optional=True),        
        ),
    
    'RefundTransaction':(
        Param('TRANSACTIONID'),
        Param('REFUNDTYPE'),
        ParamAmt('AMT', optional=True),
        ParamCurrencyCode('CURRENCYCODE'),
        Param('NOTE'),
        ),           
    
    'CreateRecurringPaymentsProfile':(
        Param('TOKEN'),
        # Recurring Payments Profile Details Fields
        Param('PROFILESTARTDATE', paramType=date),
        # ScheduleDetails Fields        
        Param('DESC'),
        Param('MAXFAILEDPAYMENTS', optional=True, paramType=int),
        Param('AUTOBILLOUTAMT', optional=True,
              allowedValues=('NoAutoBill', 'AddToNextBilling')),        
        # Billing Period Details Type
        Param('BILLINGPERIOD', allowedValues=('Day', 'Week', 'SemiMonth',
                                              'Month', 'Year')),
        Param('BILLINGFREQUENCY', paramType=int, minAmt=1),
        ParamAmt('AMT'),
        Param('CURRENCYCODE'),
        ParamAmt('L_PAYMENTREQUEST_0_AMT0', optional=True),
        Param('L_PAYMENTREQUEST_0_ITEMCATEGORY0',optional=True),
        Param('L_PAYMENTREQUEST_0_NAME0',optional=True),
        Param('L_PAYMENTREQUEST_0_QTY0',optional=True),
        Param('EMAIL'),
        ParamAmt('INITAMT')         
        ),

    'ManageRecurringPaymentsProfileStatus':(
        Param('PROFILEID', maxLen=19),
        Param('ACTION', allowedValues=('Cancel', 'Suspend', 'Reactivate')),
        Param('NOTE', optional=True),
        ),
           
    'BillOutstandingAmount':(
        Param('PROFILEID', maxLen=19),
        ParamAmt(optional=True),
        Param('NOTE', optional=True),
        ),                                
    }

class PayPal(object):
    '''
    The main class for the PayPal NVP interface.
    '''
    def __init__(self, userName, password, signature, apiUrl=PAYPAL_SIG_URL):
        self.userName = userName
        self.password = password
        self.signature = signature
        self.apiUrl = apiUrl

    def __getattr__(self, name):
        try:
            method = METHODS[name]
        except:
            raise AttributeError
        def callable(*args, **kwargs):
            logging.info(name)
            self.validateCall(name, method, **kwargs)
            return self.makeCall(name, method)
        return callable
            
    def validateCall(self, methodName, method, **kwparams):
        # method is a list of params.
        # Make sure all required params are present, in the right format
        #goodParams = {}
        for p in method:
            # ES: Make all this logic part of Param/ParamList object???
            if type(p) is Param:
                if p.name not in kwparams:
                    if not p.optional:
                        raise PayPalException('Missing required parameter to %s: %s' % (methodName, p.name))
                    else:
                        continue
                p.validate(kwparams[p.name])
                #goodParams[p.name] = kwparams[p.name]
                del(kwparams[p.name])
            elif type(p) is ParamList:
                i = 0
                paramName = 'l_%s%d' % (p.name, i)
                while paramName in kwparams:
                    p.validate(kwparams[paramName])
                    #goodParams[paramName] = kwparams[paramName]
                    del(kwparams[paramName])
                    i += 1
                    paramName = 'l_%s%d' % (p.name, i)
        if len(kwparams) != 0:
            raise PayPalException('Extra parameters to %s: %s' % (methodName, ','.join([str(k) for k in kwparams.keys()])))
    

    def makeCall(self, methodName, method):
        params = dict([(p.name, p.val) for p in method if p.val is not None])
        params['method'] = methodName
        params['user'] = self.userName
        params['pwd'] = self.password
        params['version'] = '65.1'
        if self.signature:
            params['signature'] = self.signature
        else:
            params['certificate'] = self.certificate
        paramString = urlencode(params)
        #response = urlopen(self.apiUrl, paramString).read()
        response = urlfetch.fetch(url=self.apiUrl,payload=paramString,method=urlfetch.POST,headers={},deadline=60)
        parsedResponse = cgi.parse_qs(response.content)
        if parsedResponse['ACK'][0] not in ('Success', 'SuccessWithWarning'):
            raise PayPalException(getMultipleVals(parsedResponse, 'LONGMESSAGE'))
        return parsedResponse

def getMultipleVals(resp, valName):
    ret = []
    index = 0
    while True:
        itemName = 'L_%s%s' % (valName, index)
        if not itemName in resp:
            break
        ret.extend(resp[itemName])
        index += 1
    return ret

def creditCardTypeFromNumber(numStringIn):
    # Filter out non-digits
    numString = ''
    for ch in numStringIn:
        if ch.isdigit():
            numString += ch
    if len(numString) in (13, 16) and numString[0] == '4':
        return 'Visa'
    if len(numString) == 16 and numString[0] == '5' and numString[1] in '12345':
        return 'MasterCard'
    if len(numString) == 15 and numString[0] == '3' and numString[1] in '47':
        return 'Amex'
    if len(numString) == 16 and numString[0:4] == '6011':
        return 'Discover'
    # TODO: Handle Maestro and Solo
    return None


################################################################################
## Some values for Django forms use.

COUNTRY_CODES = (("US", "United States"),
                 ("AL", "Albania"),
                 ("DZ", "Algeria"),
                 ("AD", "Andorra"),
                 ("AO", "Angola"),
                 ("AI", "Anguilla"),
                 ("AG", "Antigua and Barbuda"),
                 ("AR", "Argentina"),
                 ("AM", "Armenia"),
                 ("AW", "Aruba"),
                 ("AU", "Australia"),
                 ("AT", "Austria"),
                 ("AZ", "Azerbaijan Republic"),
                 ("BS", "Bahamas"),
                 ("BH", "Bahrain"),
                 ("BB", "Barbados"),
                 ("BE", "Belgium"),
                 ("BZ", "Belize"),
                 ("BJ", "Benin"),
                 ("BM", "Bermuda"),
                 ("BT", "Bhutan"),
                 ("BO", "Bolivia"),
                 ("BA", "Bosnia and Herzegovina"),
                 ("BW", "Botswana"),
                 ("BR", "Brazil"),
                 ("VG", "British Virgin Islands"),
                 ("BN", "Brunei"),
                 ("BG", "Bulgaria"),
                 ("BF", "Burkina Faso"),
                 ("BI", "Burundi"),
                 ("KH", "Cambodia"),
                 ("CA", "Canada"),
                 ("CV", "Cape Verde"),
                 ("KY", "Cayman Islands"),
                 ("TD", "Chad"),
                 ("CL", "Chile"),
                 ("C2", "China"),
                 ("CO", "Colombia"),
                 ("KM", "Comoros"),
                 ("CK", "Cook Islands"),
                 ("CR", "Costa Rica"),
                 ("HR", "Croatia"),
                 ("CY", "Cyprus"),
                 ("CZ", "Czech Republic"),
                 ("CD", "Democratic Republic of the Congo"),
                 ("DK", "Denmark"),
                 ("DJ", "Djibouti"),
                 ("DM", "Dominica"),
                 ("DO", "Dominican Republic"),
                 ("EC", "Ecuador"),
                 ("SV", "El Salvador"),
                 ("ER", "Eritrea"),
                 ("EE", "Estonia"),
                 ("ET", "Ethiopia"),
                 ("FK", "Falkland Islands"),
                 ("FO", "Faroe Islands"),
                 ("FM", "Federated States of Micronesia"),
                 ("FJ", "Fiji"),
                 ("FI", "Finland"),
                 ("FR", "France"),
                 ("GF", "French Guiana"),
                 ("PF", "French Polynesia"),
                 ("GA", "Gabon Republic"),
                 ("GM", "Gambia"),
                 ("DE", "Germany"),
                 ("GI", "Gibraltar"),
                 ("GR", "Greece"),
                 ("GL", "Greenland"),
                 ("GD", "Grenada"),
                 ("GP", "Guadeloupe"),
                 ("GT", "Guatemala"),
                 ("GN", "Guinea"),
                 ("GW", "Guinea Bissau"),
                 ("GY", "Guyana"),
                 ("HN", "Honduras"),
                 ("HK", "Hong Kong"),
                 ("HU", "Hungary"),
                 ("IS", "Iceland"),
                 ("IN", "India"),
                 ("ID", "Indonesia"),
                 ("IE", "Ireland"),
                 ("IL", "Israel"),
                 ("IT", "Italy"),
                 ("JM", "Jamaica"),
                 ("JP", "Japan"),
                 ("JO", "Jordan"),
                 ("KZ", "Kazakhstan"),
                 ("KE", "Kenya"),
                 ("KI", "Kiribati"),
                 ("KW", "Kuwait"),
                 ("KG", "Kyrgyzstan"),
                 ("LA", "Laos"),
                 ("LV", "Latvia"),
                 ("LS", "Lesotho"),
                 ("LI", "Liechtenstein"),
                 ("LT", "Lithuania"),
                 ("LU", "Luxembourg"),
                 ("MG", "Madagascar"),
                 ("MW", "Malawi"),
                 ("MY", "Malaysia"),
                 ("MV", "Maldives"),
                 ("ML", "Mali"),
                 ("MT", "Malta"),
                 ("MH", "Marshall Islands"),
                 ("MQ", "Martinique"),
                 ("MR", "Mauritania"),
                 ("MU", "Mauritius"),
                 ("YT", "Mayotte"),
                 ("MX", "Mexico"),
                 ("MN", "Mongolia"),
                 ("MS", "Montserrat"),
                 ("MA", "Morocco"),
                 ("MZ", "Mozambique"),
                 ("NA", "Namibia"),
                 ("NR", "Nauru"),
                 ("NP", "Nepal"),
                 ("NL", "Netherlands"),
                 ("AN", "Netherlands Antilles"),
                 ("NC", "New Caledonia"),
                 ("NZ", "New Zealand"),
                 ("NI", "Nicaragua"),
                 ("NE", "Niger"),
                 ("NU", "Niue"),
                 ("NF", "Norfolk Island"),
                 ("NO", "Norway"),
                 ("OM", "Oman"),
                 ("PW", "Palau"),
                 ("PA", "Panama"),
                 ("PG", "Papua New Guinea"),
                 ("PE", "Peru"),
                 ("PH", "Philippines"),
                 ("PN", "Pitcairn Islands"),
                 ("PL", "Poland"),
                 ("PT", "Portugal"),
                 ("QA", "Qatar"),
                 ("CG", "Republic of the Congo"),
                 ("RE", "Reunion"),
                 ("RO", "Romania"),
                 ("RU", "Russia"),
                 ("RW", "Rwanda"),
                 ("VC", "Saint Vincent and the Grenadines"),
                 ("WS", "Samoa"),
                 ("SM", "San Marino"),
                 ("ST", "Sao Tome and Principe"),
                 ("SA", "Saudi Arabia"),
                 ("SN", "Senegal"),
                 ("SC", "Seychelles"),
                 ("SL", "Sierra Leone"),
                 ("SG", "Singapore"),
                 ("SK", "Slovakia"),
                 ("SI", "Slovenia"),
                 ("SB", "Solomon Islands"),
                 ("SO", "Somalia"),
                 ("ZA", "South Africa"),
                 ("KR", "South Korea"),
                 ("ES", "Spain"),
                 ("LK", "Sri Lanka"),
                 ("SH", "St. Helena"),
                 ("KN", "St. Kitts and Nevis"),
                 ("LC", "St. Lucia"),
                 ("PM", "St. Pierre and Miquelon"),
                 ("SR", "Suriname"),
                 ("SJ", "Svalbard and Jan Mayen Islands"),
                 ("SZ", "Swaziland"),
                 ("SE", "Sweden"),
                 ("CH", "Switzerland"),
                 ("TW", "Taiwan"),
                 ("TJ", "Tajikistan"),
                 ("TZ", "Tanzania"),
                 ("TH", "Thailand"),
                 ("TG", "Togo"),
                 ("TO", "Tonga"),
                 ("TT", "Trinidad and Tobago"),
                 ("TN", "Tunisia"),
                 ("TR", "Turkey"),
                 ("TM", "Turkmenistan"),
                 ("TC", "Turks and Caicos Islands"),
                 ("TV", "Tuvalu"),
                 ("UG", "Uganda"),
                 ("UA", "Ukraine"),
                 ("AE", "United Arab Emirates"),
                 ("GB", "United Kingdom"),
                 ("UY", "Uruguay"),
                 ("VU", "Vanuatu"),
                 ("VA", "Vatican City State"),
                 ("VE", "Venezuela"),
                 ("VN", "Vietnam"),
                 ("WF", "Wallis and Futuna Islands"),
                 ("YE", "Yemen"),
                 ("ZM", "Zambia"))

STATE_CODES = (("AK", "AK"),
               ("AL", "AL"),
               ("AR", "AR"),
               ("AZ", "AZ"),
               ("CA", "CA"),
               ("CO", "CO"),
               ("CT", "CT"),
               ("DC", "DC"),
               ("DE", "DE"),
               ("FL", "FL"),
               ("GA", "GA"),
               ("HI", "HI"),
               ("IA", "IA"),
               ("ID", "ID"),
               ("IL", "IL"),
               ("IN", "IN"),
               ("KS", "KS"),
               ("KY", "KY"),
               ("LA", "LA"),
               ("MA", "MA"),
               ("MD", "MD"),
               ("ME", "ME"),
               ("MI", "MI"),
               ("MN", "MN"),
               ("MO", "MO"),
               ("MS", "MS"),
               ("MT", "MT"),
               ("NC", "NC"),
               ("ND", "ND"),
               ("NE", "NE"),
               ("NH", "NH"),
               ("NJ", "NJ"),
               ("NM", "NM"),
               ("NV", "NV"),
               ("NY", "NY"),
               ("OH", "OH"),
               ("OK", "OK"),
               ("OR", "OR"),
               ("PA", "PA"),
               ("RI", "RI"),
               ("SC", "SC"),
               ("SD", "SD"),
               ("TN", "TN"),
               ("TX", "TX"),
               ("UT", "UT"),
               ("VA", "VA"),
               ("VT", "VT"),
               ("WA", "WA"),
               ("WI", "WI"),
               ("WV", "WV"),
               ("WY", "WY"),
               ("AA", "AA"),
               ("AE", "AE"),
               ("AP", "AP"),
               ("AS", "AS"),
               ("FM", "FM"),
               ("GU", "GU"),
               ("MH", "MH"),
               ("MP", "MP"),
               ("PR", "PR"),
               ("PW", "PW"),
               ("VI", "VI"))

PROVINCE_CODES = (("Alberta", "Alberta"),
                  ("British Columbia", "British Columbia"),
                  ("Manitoba", "Manitoba"),
                  ("New Brunswick", "New Brunswick"),
                  ("Newfoundland", "Newfoundland and Labrador"),
                  ("Nova Scotia", "Nova Scotia"),
                  ("Nunavut", "Nunavut"),
                  ("Northwest Territories", "Northwest Territories"),
                  ("Ontario", "Ontario"),
                  ("Prince Edward Island", "Prince Edward Island"),
                  ("Quebec", "Quebec"),
                  ("Saskatchewan", "Saskatchewan"),
                  ("Yukon", "Yukon"))


