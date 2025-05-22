'''
Created on Jan 27, 2012
Module: Factors
Find all the factors of a given number.

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''

class Factors():
           
    def find_factors(self,number):
        factors = [1]
        divisor = 2
        while divisor<=number/2:
            if number%divisor == 0:
                factors.append(divisor)
            divisor = divisor + 1
        factors.append(number)
        return factors

    def find_common_factors(self,number1,number2):
        factors1 = [1]
        factors2 = [1]
        common_factors = []
        divisor1 = 2
        divisor2 = 2
        while divisor1<=number1/2:
            if number1%divisor1 == 0:
                factors1.append(divisor1)
            divisor1 = divisor1 + 1
        factors1.append(number1)
        
        while divisor2<=number2/2:
            if number2%divisor2 == 0:
                factors2.append(divisor2)
            divisor2 = divisor2 + 1
        factors2.append(number2)
        
        for i in range(len(factors1)):
            if factors1[i] in factors2:
                common_factors.append(factors1[i])
        
        return common_factors
        return factors1
    