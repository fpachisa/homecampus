'''
Created on Feb 20, 2011
Module: LcmGcf
It fins the LCM or GCF of any two given numbers.

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2010, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''

class LcmGcf():
           
    def find_gcf(self,number1,number2):
        divisor = 0
        if number1>number2:
            dividend = number1
            divisor = number2
        else:
            dividend = number2
            divisor = number1
        remainder=-1
        while remainder !=0:
            try:
                remainder=dividend%divisor
            except ZeroDivisionError:
                return 1
           
            if remainder !=0:
                dividend=divisor
                divisor=remainder
        return divisor

    def find_lcm(self,number1,number2):
        gcf = self.find_gcf(number1, number2)
        lcm=(number1*number2)/gcf
        return lcm
              
