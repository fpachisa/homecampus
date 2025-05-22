'''
Created on Feb 07, 2013

@author: Farhat Pachisa

Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random

def GenerateIdeas(order):
    
    fees = float(random.randint(301,400))/100
    number2 = random.randint(3,9)
    number1 =  fees * number2
    
    if len(str(number1).partition(".")[2])==1:
        number1 = str(number1)+"0"

    Ideas = [[0,'How much did you pay for your morning coffee?','e.g.: 2.85'],
             [1,'Put a tiny percentage of what a math tutor would charge you per HOUR:','Hint: 5.88'],
             [2,'Enter a small fraction of your monthly Internet bill:','e.g.: 3.45'],
             [3,'Enter a small percentage of fees that our competitors are charging:','Hint: 3.68'],
             [4,'Input a tiny fraction of your monthly cable bill:','e.g.: 4.38'],
             [5,'What is the value of PI?','Hint: 3.14'],
             [6,str(number1)+' &divide; '+str(number2)+' =','Hint: '+str(fees)],
             [7,"What is your child's education worth?",'You Decide'],
             [8,'How many litres are 1 US gallon?','Hint: 3.78'],
             ]
    if order == "any":
        return random.choice(Ideas)
    else:
        try:
            return Ideas[int(order)]
        except IndexError:
            return Ideas[0]