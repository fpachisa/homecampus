'''
Module: Figures2Words
It writes the given figure (upto 999 trillion) in words.

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2010, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''

class Figures2Words():
    
    def __init__(self):
        """ Sets up the key words which will be used in writing words"""
        self.setup()
        
    def setup(self):
        self.setSmallWords()
        self.setMediumWords()
              
    def setSmallWords(self):
        self.smallWords = {"1":"one","2":"two","3":"three",
                           "4":"four","5":"five","6":"six",
                           "7":"seven","8":"eight","9":"nine",
                           "10":"ten","11":"eleven","12":"twelve",
                           "13":"thirteen","14":"fourteen","15":"fifteen",
                           "16":"sixteen","17":"seventeen","18":"eighteen",
                           "19":"nineteen"}
        
    def setMediumWords(self):
        self.mediumWords = {"2":"twenty","3":"thirty","4":"forty",
                            "5":"fifty","6":"sixty","7":"seventy",
                            "8":"eighty","9":"ninety"}
        
    def toWords(self,figure):
        """ This function does the following:
            1. It breaks down the given figure into chunks of three digits (upto trillion)
            2. Each 3 digits chunk is passed to writeHundTens function to write those in words
            3. And it adds the keyword million or billion to the output of step 2
            4. Lastly "and" clause is added to figure which doesn't have and for last 3 digits.
                e.g. 90001 is written as: nine thousand and one instead of nine thousand one
        """
        trillion = str(figure)[-15:-12]
        billion = str(figure)[-12:-9]
        million = str(figure)[-9:-6]
        thousand = str(figure)[-6:-3]
        hundred = str(figure)[-3:]
        words = ""
        if (len(trillion)>0 and int(trillion)!=0):
            words = self.writeHundTens(int(trillion))+" trillion, "
        if (len(billion)>0 and int(billion)!=0):
            words = words + self.writeHundTens(int(billion))+" billion, "
        if (len(million)>0 and int(million)!=0):
            words = words + self.writeHundTens(int(million))+" million, "        
        if (len(thousand)>0 and int(thousand)!=0):
            words = words + self.writeHundTens(int(thousand))+" thousand, "
        if (figure>1000 and int(hundred)!=0 and "and" not in self.writeHundTens(int(hundred))):
            words = words +"and "+ self.writeHundTens(int(hundred))
        else:
            words = words + self.writeHundTens(int(hundred))
        return words.capitalize()
    
    def writeHundTens(self,figure):
        """ This gets the hundred and tens part of the given figure and
        adds keyword "and" appropriately """
        hundred = self.getHundreds(figure)
        tens = self.getTens(figure)
        if(len(hundred)>0 and len(tens)>0):
            return (hundred+" and "+tens)
        elif(len(hundred)>0 and len(tens)==0):
            return (hundred)
        elif(len(hundred)==0):
            return (tens)
        
              
    def getTens(self,figure):
        """ Separates the tens part from the figure and uses small and medium keywords
        to create the words"""
        figure = divmod(figure,100)[1]
        if (figure!=0):
            div, mod = divmod(figure,10)
            if (div==0 or div==1):
                return self.smallWords[str(figure)]
            elif(mod==0):
                return self.mediumWords[str(div)]
            else:
                return self.mediumWords[str(div)]+" "+self.smallWords[str(mod)]
        return ""
    
    def getHundreds(self,figure):
        """ Separates the hundreds part from the figure and uses small keywords
        to create the words"""
        figure = divmod(figure,1000)[1]
        if(figure!=0):
            div,mod = divmod(figure,100)
            if (div==0):
                return ""
            else:
                return self.smallWords[str(div)]+" "+"hundred"
        return ""                       
    
