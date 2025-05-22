'''
Created on July 17, 2012

@author: Farhat Pachisa

Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random

#Algebra Evaluation
P6AGEA = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          random.choice(['ProblemType5','ProblemTypeMCQ5']),
          random.choice(['ProblemType6','ProblemTypeMCQ6']),
          random.choice(['ProblemType7','ProblemTypeMCQ7']),
          random.choice(['ProblemType8','ProblemTypeMCQ8']),
          random.choice(['ProblemType9','ProblemTypeMCQ9']),
          ]

#Algebra Simplifying
P6AGSA = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          'ProblemTypeMCQ5',
          ]

#Algebra Word Problems
P6AGWP = ['ProblemType1','ProblemType2','ProblemTypeMCQ3',
          random.choice(['ProblemType4b','ProblemTypeMCQ4a']),
          random.choice(['ProblemType5b','ProblemTypeMCQ5a']),
          random.choice(['ProblemType6b','ProblemTypeMCQ6a']),
          random.choice(['ProblemType7b','ProblemTypeMCQ7a']),
          ]

#Data Analysis Word Problems
P6DAWP = [random.choice(['ProblemType1a','ProblemType1b','ProblemType1c',]),
          random.choice(['ProblemType1d','ProblemType1e',]),
          random.choice(['ProblemType2a','ProblemType2b',]),
          random.choice(['ProblemType2c','ProblemType2d',]),
          random.choice(['ProblemType2e','ProblemType2f',]),
          random.choice(['ProblemType3a','ProblemType3b','ProblemType3c',]),
          ]

#Fractions Divide Proper Fractions
P6FRDP = ['ProblemType1','ProblemTypeMCQ1',]

#Fractions Divide Whole Number
P6FRDW = ['ProblemType1','ProblemTypeMCQ1',]

#Fractions Word Problems
P6FRWP = ['ProblemType1',
          random.choice(['ProblemType2a','ProblemType2b',]),
          random.choice(['ProblemType3a','ProblemTypeMCQ3b',]),
          'ProblemType4',
          random.choice(['ProblemType5a','ProblemTypeMCQ5b','ProblemTypeMCQ5c',]),
          ]

#Measurement Circle Area
P6MTCA = ['ProblemType1','ProblemType2',]

#Measurement Circle Circumference
P6MTCC = ['ProblemType1','ProblemType2',]

#Measurement Circle Radius
P6MTCR = ['ProblemType1','ProblemType2','ProblemType3','ProblemType4',]

#Measurement Composite Figures
P6MTCF = [random.choice(['ProblemType1a','ProblemType1',]),
          random.choice(['ProblemType2a','ProblemType2',]),
          random.choice(['ProblemType3a','ProblemType3',]),
          random.choice(['ProblemType4a','ProblemType4',]),
          random.choice(['ProblemType5a','ProblemType5',]),
          'ProblemType6','ProblemType7','ProblemType8',
          random.choice(['ProblemType9a','ProblemType9',]),
          random.choice(['ProblemType10a','ProblemType10',]),
          ]

#Measurement SemiCircleArea
P6MTSA = ['ProblemType1','ProblemType2','ProblemType3',]

#Measurement SemiCirclePerimeter
P6MTSP = ['ProblemType1','ProblemType2','ProblemType3',]

#Measurement Volume of Cube Cuboid
P6MTVC = ['ProblemType1','ProblemType2','ProblemType3',]

#Percentage Word Problems
P6PRWP = ['ProblemType1','ProblemType2','ProblemType3','ProblemType4','ProblemType5','ProblemType6','ProblemType7','ProblemType8',
          'ProblemType9','ProblemType10','ProblemType11','ProblemType12','ProblemType13','ProblemType14','ProblemType15','ProblemType16',
          'ProblemType17','ProblemType18',]

#Percentage Increase Decrease
P6PRID = [random.choice(['ProblemType1','ProblemTypeMCQ1',]),
          random.choice(['ProblemType2','ProblemTypeMCQ2',]),
          random.choice(['ProblemType3','ProblemTypeMCQ3',]),
          ]

#Percentage Whole Part
P6PRPW = [random.choice(['ProblemType1','ProblemTypeMCQ1',]),
          random.choice(['ProblemType2','ProblemTypeMCQ2',]),
          random.choice(['ProblemType3','ProblemTypeMCQ3',]),
          ]

#Ratio Word Problems
P6RTWP = [random.choice(['ProblemType1','ProblemType2']),'ProblemType3','ProblemType4','ProblemType5','ProblemType6','ProblemType7','ProblemType8',
          'ProblemType9','ProblemType10','ProblemType11','ProblemType12','ProblemType13','ProblemType14','ProblemType15','ProblemType16',
          'ProblemType17','ProblemType18','ProblemType19',]

#Speed Word Problems
P6SPWP = ['ProblemType1','ProblemType2','ProblemTypeMCQ3','ProblemType4','ProblemType5','ProblemType6','ProblemType7','ProblemType8',
          'ProblemType9','ProblemTypeMCQ10','ProblemType11',random.choice(['ProblemType12','ProblemTypeMCQ12']),
          ]

#Distance time speed
P6SPDT = [random.choice(['ProblemType1','ProblemTypeMCQ1',]),
          random.choice(['ProblemType2','ProblemTypeMCQ2',]),
          random.choice(['ProblemType3','ProblemTypeMCQ3',]),
          ]

ConceptsID = {'P6AGEvaluationExpression':P6AGEA,
              'P6AGSimplifyingExpression':P6AGSA,
              'P6AGWordProblems':P6AGWP,
              'P6DAWordProblems':P6DAWP,
              'P6FRDivideProperFraction':P6FRDP,
              'P6FRDivideWholeNumber':P6FRDW,
              'P6FRWordProblems':P6FRWP,
              'P6MTArea':P6MTCA,
              'P6MTCircumference':P6MTCC,
              'P6MTRadius':P6MTCR,
              'P6MTComposite':P6MTCF,
              'P6MTSemiArea':P6MTSA,
              'P6MTSemiPerimeter':P6MTSP,
              'P6MTVolume':P6MTVC,
              'P6PRWordProblems':P6PRWP,
              'P6PRIncDec':P6PRID,
              'P6PRFindWhole':P6PRPW,
              'P6RTWordProblems':P6RTWP,
              'P6SPWordProblems':P6SPWP,
              'P6SPDTS':P6SPDT,
              }
          
Concepts = {'P6AG':[['P6AGEvaluationExpression',40,P6AGEA],
                    ['P6AGSimplifyingExpression',20,P6AGSA],
                    ['P6AGWordProblems',40,P6AGWP],
                   ],
            'P6DA':[['P6DAWordProblems',100,P6DAWP],
                   ],
            'P6FR':[['P6FRDivideProperFraction',25,P6FRDP],
                    ['P6FRDivideWholeNumber',25,P6FRDW],
                    ['P6FRWordProblems',50,P6FRWP],
                   ],
            'P6MT':[['P6MTArea',10,P6MTCA],
                    ['P6MTCircumference',10,P6MTCC],
                    ['P6MTRadius',10,P6MTCR],
                    ['P6MTComposite',45,P6MTCF],
                    ['P6MTSemiArea',10,P6MTSA],
                    ['P6MTSemiPerimeter',10,P6MTSP],
                    ['P6MTVolume',5,P6MTVC],
                   ],            
            'P6PR':[['P6PRWordProblems',80,P6PRWP],
                    ['P6PRIncDec',10,P6PRID],
                    ['P6PRFindWhole',10,P6PRPW],
                   ],
            'P6RT':[['P6RTWordProblems',100,P6RTWP],
                   ],
            'P6SP':[['P6SPWordProblems',90,P6SPWP],
                    ['P6SPDTS',10,P6SPDT],
                   ],
            }


def P6ConceptList(questions,concept):
    ConceptList = []
    '''For individual sub topics there is no Concepts dictionary'''
    if not concept in Concepts:
        Concepts.update({concept:[[concept,99,ConceptsID[concept]]]})
       
    for i in range(len(Concepts[concept])):
        ConceptQuestions = Concepts[concept][i][1]*questions/100+1
        try:
            ProblemTypes = random.sample(Concepts[concept][i][2],ConceptQuestions)
        except ValueError:
            ProblemTypes = []
            p = 0
            for _k in range(ConceptQuestions):                
                ProblemTypes.append(Concepts[concept][i][2][p])
                '''17-APR-2013: Logic to rotate all problems if number of problems in a topic is less than problems required for worksheet'''
                if p+1>=len(Concepts[concept][i][2]):
                    p = 0
                else:
                    p = p + 1
        for j in range(ConceptQuestions):
            ConceptList.append([Concepts[concept][i][0],ProblemTypes[j]])
    return ConceptList