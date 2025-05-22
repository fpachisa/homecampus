'''
Created on June 30, 2012

@author: Farhat Pachisa

Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''

import random
import logging

#Data Analysis Find Average
P5DAFA = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3a','ProblemTypeMCQ3a','ProblemType3b','ProblemTypeMCQ3b']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          random.choice(['ProblemType5','ProblemTypeMCQ5']),
          random.choice(['ProblemType6','ProblemTypeMCQ6']),
          random.choice(['ProblemType7','ProblemTypeMCQ7']),
          random.choice(['ProblemType8a','ProblemTypeMCQ8a','ProblemType8b','ProblemTypeMCQ8b']),
          ]

#Data Analysis Find Total
P5DAFT = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          random.choice(['ProblemType5','ProblemTypeMCQ5']),
          random.choice(['ProblemType6','ProblemTypeMCQ6']),
          random.choice(['ProblemType7','ProblemTypeMCQ7']),
          random.choice(['ProblemType8','ProblemTypeMCQ8']),
          random.choice(['ProblemType9a','ProblemTypeMCQ9a','ProblemType9b','ProblemTypeMCQ9b']),
          ]

#Data Analysis Word Problems
P5DAWP = ['ProblemType1','ProblemType2','ProblemType3','ProblemType4','ProblemType5a','ProblemType5b',]

#Decimal Multiply Divide
P5DCMD = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4a','ProblemTypeMCQ4a','ProblemType4b','ProblemTypeMCQ4b']),
          random.choice(['ProblemType5','ProblemTypeMCQ5']),
          random.choice(['ProblemType6a','ProblemTypeMCQ6a','ProblemType6b','ProblemTypeMCQ6b']),
          random.choice(['ProblemType7a','ProblemTypeMCQ7a','ProblemType7b','ProblemTypeMCQ7b']),
          random.choice(['ProblemType8a','ProblemTypeMCQ8a','ProblemType8b','ProblemTypeMCQ8b','ProblemType8c','ProblemTypeMCQ8c']),
          ]

#Decimal Rounding
P5DCRO = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          random.choice(['ProblemType5','ProblemTypeMCQ5']),
          random.choice(['ProblemType6','ProblemTypeMCQ6']),
          random.choice(['ProblemType7a','ProblemTypeMCQ7a','ProblemType7b','ProblemTypeMCQ7b','ProblemType7c','ProblemTypeMCQ7c','ProblemType7d','ProblemTypeMCQ7d']),
          random.choice(['ProblemType8','ProblemTypeMCQ8']),
          ]

#Decimal Word Problems
P5DCWP = [random.choice(['ProblemType1','ProblemType1a','ProblemType2','ProblemType2a',]),
          random.choice(['ProblemType3',]),
          random.choice(['ProblemType4','ProblemType4a']),
          random.choice(['ProblemType5',]),
          random.choice(['ProblemType6',]),
          random.choice(['ProblemType7',]),
          random.choice(['ProblemType8',]),
          random.choice(['ProblemType9',]),
          random.choice(['ProblemType10',]),
          random.choice(['ProblemType11','ProblemType12']),
          random.choice(['ProblemType13','ProblemType14']),
          ]

#Fractions Add Sub Mixed
P5FRAS = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          ]

#Fractions Add Sub Proper
P5FRAP = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          ]

#Fractions Divide Proper Fraction
P5FRDP = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          ]

#Fractions Multiply Mixed Fraction
P5FRMM = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          ]

#Fractions Multiply Proper Improper
P5FRMP = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          ]

#Fractions Word Problems
P5FRWP = [random.choice(['ProblemType1','ProblemType2','ProblemType3','ProblemType4']),
          random.choice(['ProblemType5','ProblemType6','ProblemType7','ProblemType8']),
          random.choice(['ProblemType9','ProblemType10',]),
          random.choice(['ProblemType11',]),
          random.choice(['ProblemType12',]),
          random.choice(['ProblemType13','ProblemType14',]),
          random.choice(['ProblemType15',]),
          random.choice(['ProblemType16',]),
          random.choice(['ProblemType17',]),
          random.choice(['ProblemType18',]),
          random.choice(['ProblemType19',]),
          random.choice(['ProblemType20','ProblemType21',]),
          random.choice(['ProblemType22',]),
          ]

#Geometry Angels
P5GTAG = ['ProblemType1','ProblemType2','ProblemType3','ProblemType4','ProblemType5','ProblemType6','ProblemType7',]

#Geometry 4 sided figures
P5GT4S = ['ProblemType1','ProblemType2','ProblemType3',]

#Geometry Triangles
P5GTTG = ['ProblemType1','ProblemType2','ProblemType3',]

#Measurement Area of Triangle
P5MTAT = ['ProblemType1','ProblemType2','ProblemType3','ProblemType4',]

#Measurement Unit Conversion
P5MTUC = ['ProblemType1','ProblemType2',]

#Measurement Volume
P5MTVL = ['ProblemType1','ProblemType2',
          random.choice(['ProblemType3','ProblemType4','ProblemType5',]),
          'ProblemType6','ProblemType7',
          ]

#Measurement Word Problems
P5MTWP = [random.choice(['ProblemType1a','ProblemType1b']),
          'ProblemType2','ProblemType3','ProblemType4','ProblemType5',
          ]

#Percentage Express as Decimal
P5PRED = ['ProblemType1']

#Percentage Express as Fraction
P5PREF = ['ProblemType1']

#Percentage Express as Percent
P5PREP = ['ProblemType1',
          'ProblemType2',
          'ProblemType3',]

#Percentage Word Problems
P5PRWP = ['ProblemType1','ProblemType2',
          random.choice(['ProblemType3a','ProblemType3b',]),
          'ProblemType4','ProblemType5','ProblemType6','ProblemType7a','ProblemType8',
          ]

#Ratio Missing Number
P5RTMN = ['ProblemType1']

#Ratio Simplest Form
P5RTSF = ['ProblemType1']

#Ratio Word Problems
P5RTWP = [random.choice(['ProblemType1a','ProblemType1b','ProblemType1c','ProblemType1d']),
          'ProblemType2','ProblemType3','ProblemType4','ProblemType5','ProblemType6','ProblemType7','ProblemType8','ProblemType9',
          ]

#Whole Numbers Approximation Estimation
P5WNAE = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          ]

#Whole Numbers Comparing and Ordering
P5WNCO = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          'ProblemTypeMCQ5','ProblemTypeMCQ6',
          ]

#Whole Numbers Find Pattern
P5WNFP = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          ]

#Whole Numbers Multiply Divide
P5WNMD = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          ]

#Whole Numbers Order of Operation
P5WNOO = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          ]

#Whole Numbers Place Value
P5WNPV = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          random.choice(['ProblemType5','ProblemTypeMCQ5']),
          random.choice(['ProblemType6','ProblemTypeMCQ6']),
          random.choice(['ProblemType7','ProblemTypeMCQ7']),
          random.choice(['ProblemType8','ProblemTypeMCQ8']),
          ]

#Whole Numbers Write in figures
P5WNWF = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          random.choice(['ProblemType5','ProblemTypeMCQ5']),
          ]

#Whole Numbers Write in words
P5WNWW = [random.choice(['ProblemType1','ProblemTypeMCQ1']),
          random.choice(['ProblemType2','ProblemTypeMCQ2']),
          random.choice(['ProblemType3','ProblemTypeMCQ3']),
          random.choice(['ProblemType4','ProblemTypeMCQ4']),
          random.choice(['ProblemType5','ProblemTypeMCQ5']),
          ]

#Whole Numbers Word Problems
P5WNWP = [random.choice(['ProblemType1','ProblemType2','ProblemType3','ProblemType4','ProblemType5',]),
          random.choice(['ProblemType6','ProblemType7','ProblemType8','ProblemType9',]),
          random.choice(['ProblemType10','ProblemType11','ProblemType12',]),
          random.choice(['ProblemType13','ProblemType14','ProblemType15',]),
          random.choice(['ProblemType16','ProblemType17','ProblemType18','ProblemType19','ProblemType20','ProblemType21','ProblemType22',]),
          random.choice(['ProblemType23','ProblemType24','ProblemType25','ProblemType26',]),
          random.choice(['ProblemType27','ProblemType28','ProblemType29','ProblemType30',]),
          random.choice(['ProblemType31','ProblemType32',]),
          random.choice(['ProblemType33','ProblemType34',]),
          random.choice(['ProblemType35','ProblemType36','ProblemType37',]),
          random.choice(['ProblemType38','ProblemType39',]),
          random.choice(['ProblemType40','ProblemType41','ProblemType42',]),
          'ProblemType43',
          'ProblemType44',
          random.choice(['ProblemType45','ProblemType46',]),
          'ProblemType47',
          'ProblemType48',
          'ProblemType49',
          random.choice(['ProblemType50','ProblemType51',]),
          random.choice(['ProblemType52','ProblemType53','ProblemType54','ProblemType55',]),
          random.choice(['ProblemType56','ProblemType57','ProblemType58','ProblemType59',]),
          random.choice(['ProblemType60','ProblemType61','ProblemType62',]),
          'ProblemType63',
          'ProblemType64',
          random.choice(['ProblemType65','ProblemType66',]),
          random.choice(['ProblemType67','ProblemType68','ProblemType69',]),
          'ProblemType70',
          random.choice(['ProblemType71','ProblemType72',]),
          random.choice(['ProblemType73','ProblemType74','ProblemType75',]),
          'ProblemType76',
          random.choice(['ProblemType77','ProblemType78',]),
          random.choice(['ProblemType79','ProblemType80',]),
          random.choice(['ProblemType82','ProblemType83',]),
          random.choice(['ProblemType84','ProblemType85','ProblemType86',]),
          random.choice(['ProblemType87','ProblemType88','ProblemType89','ProblemType90',]),
          'ProblemType91',
          'ProblemType92',
          random.choice(['ProblemType93','ProblemType94','ProblemType95','ProblemType96','ProblemType97','ProblemType98',]),
          random.choice(['ProblemType99','ProblemType100',]),
          random.choice(['ProblemType101','ProblemType102','ProblemType103',]),
          'ProblemType104',
          random.choice(['ProblemType105','ProblemType106',]),
          random.choice(['ProblemType107','ProblemType108',]),
          'ProblemType109',
          random.choice(['ProblemType110','ProblemType111','ProblemType112','ProblemType113','ProblemType114',]),
          random.choice(['ProblemType115','ProblemType116',]),
          random.choice(['ProblemType117','ProblemType118',]),
          random.choice(['ProblemType119','ProblemType120','ProblemType121',]),
          random.choice(['ProblemType122','ProblemType123',]),
          ]

ConceptsID = {'P5DataAnalysisAverage':P5DAFA,
              'P5DataAnalysisTotal':P5DAFT,
              'P5DataAnalysisWordProblems':P5DAWP,
              'P5DecimalsMultiplyDivide':P5DCMD,
              'P5DecimalsRounding':P5DCRO,
              'P5DecimalsWordProblems':P5DCWP,
              'P5FractionsAddSubMixedFractions':P5FRAS,
              'P5FractionsAddSubProperFractions':P5FRAP,
              'P5FractionsMultProperImproperFractions':P5FRMP,
              'P5FractionsMultMixedFractions':P5FRMM,
              'P5FractionsDivideProperFractions':P5FRDP,
              'P5FractionsWordProblems':P5FRWP,
              'P5GeometryAngles':P5GTAG,
              'P5GeometryFourSided':P5GT4S,
              'P5GeometryTriangles':P5GTTG,
              'P5MeasurementAreaOfTriangle':P5MTAT,
              'P5MeasurementUnitConversion':P5MTUC,
              'P5MeasurementVolume':P5MTVL,
              'P5MeasurementWordProblems':P5MTWP,
              'P5PercentageExpressAsDecimal':P5PRED,
              'P5PercentageExpressAsFraction':P5PREF,
              'P5PercentageExpressAsPercent':P5PREP,
              'P5PercentageWordProblems':P5PRWP,
              'P5RatioMissingNumber':P5RTMN,
              'P5RatioSimplestForm':P5RTSF,
              'P5RatioWordProblems':P5RTWP,
              'P5WholeNumbersWordProblems':P5WNWP,
              'P5WholeNumbersApproximationEstimation':P5WNAE,
              'P5WholeNumbersComparingAndOrdering':P5WNCO,
              'P5WholeNumbersFindPattern':P5WNFP,
              'P5WholeNumbersMultiplyDivide':P5WNMD,
              'P5WholeNumbersOrderOfOperation':P5WNOO,
              'P5WholeNumbersPlaceValue':P5WNPV,
              'P5WholeNumbersWriteInFigures':P5WNWF,
              'P5WholeNumbersWriteInWords':P5WNWW,
              }

Concepts = {'P5DA':[['P5DataAnalysisAverage',30,P5DAFA],
                    ['P5DataAnalysisTotal',30,P5DAFT],
                    ['P5DataAnalysisWordProblems',40,P5DAWP],
                   ],
            'P5DC':[['P5DecimalsMultiplyDivide',20,P5DCMD],
                    ['P5DecimalsRounding',20,P5DCRO],
                    ['P5DecimalsWordProblems',60,P5DCWP],
                   ],
            'P5FR':[['P5FractionsAddSubMixedFractions',5,P5FRAS],
                    ['P5FractionsAddSubProperFractions',10,P5FRAP],
                    ['P5FractionsMultProperImproperFractions',5,P5FRMP],
                    ['P5FractionsMultMixedFractions',5,P5FRMM],
                    ['P5FractionsDivideProperFractions',5,P5FRDP],
                    ['P5FractionsWordProblems',70,P5FRWP],
                   ],
            'P5GT':[['P5GeometryAngles',60,P5GTAG],
                    ['P5GeometryFourSided',20,P5GT4S],
                    ['P5GeometryTriangles',20,P5GTTG],
                   ],            
            'P5MT':[['P5MeasurementAreaOfTriangle',20,P5MTAT],
                    ['P5MeasurementUnitConversion',10,P5MTUC],
                    ['P5MeasurementVolume',30,P5MTVL],
                    ['P5MeasurementWordProblems',40,P5MTWP]
                   ],
            'P5PR':[['P5PercentageExpressAsDecimal',10,P5PRED],
                    ['P5PercentageExpressAsFraction',10,P5PREF],
                    ['P5PercentageExpressAsPercent',20,P5PREP],
                    ['P5PercentageWordProblems',60,P5PRWP]
                   ],            
            'P5RT':[['P5RatioMissingNumber',10,P5RTMN],
                    ['P5RatioSimplestForm',10,P5RTSF],
                    ['P5RatioWordProblems',80,P5RTWP]
                   ],
            'P5WN':[['P5WholeNumbersWordProblems',90,P5WNWP],
                    ['P5WholeNumbersApproximationEstimation',1,P5WNAE],
                    ['P5WholeNumbersComparingAndOrdering',2,P5WNCO],
                    ['P5WholeNumbersFindPattern',1,P5WNFP],
                    ['P5WholeNumbersMultiplyDivide',1,P5WNMD],
                    ['P5WholeNumbersOrderOfOperation',1,P5WNOO],
                    ['P5WholeNumbersPlaceValue',2,P5WNPV],
                    ['P5WholeNumbersWriteInFigures',1,P5WNWF],
                    ['P5WholeNumbersWriteInWords',1,P5WNWW],
                   ]            
            }


def P5ConceptList(questions,concept):
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