'''
Created on May 14, 2014

@author: Farhat Pachisa

Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''
from Database import HCGrade7Questions


def CheckAnswerForPCMedium_1(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PCMedium_1'").fetch(6)
    answerCheck = False
    firstAnswerCorrect = False
    secondAnswerCorrect = False
    thirdAnswerCorrect = False
    entered_answers = {}
    for q in Grade7QuestionData:
        try:
            entered_answers.update({q.answer_id:int(q.entered_answer)})
        except ValueError:
            pass
    '''grouping the answer to check the correct pair'''
    try:
        entered_answers_list = [[entered_answers["PCMedium_1_1_answer"],entered_answers["PCMedium_1_2_answer"],],
                                [entered_answers["PCMedium_1_3_answer"],entered_answers["PCMedium_1_4_answer"],],
                                [entered_answers["PCMedium_1_5_answer"],entered_answers["PCMedium_1_6_answer"],],
                                ]
        entered_answers_list_1 = [[entered_answers["PCMedium_1_2_answer"],entered_answers["PCMedium_1_1_answer"],],
                                [entered_answers["PCMedium_1_4_answer"],entered_answers["PCMedium_1_3_answer"],],
                                [entered_answers["PCMedium_1_6_answer"],entered_answers["PCMedium_1_5_answer"],],
                                ]        
        correct_answers_list = [[5,7],[11,13],[17,19],[29,31],[41,43],[59,61],[71,73]]
        if entered_answers_list[0] in correct_answers_list or entered_answers_list_1[0] in correct_answers_list:
            firstAnswerCorrect = True
        if entered_answers_list[1]!=entered_answers_list[0] and entered_answers_list_1[1]!=entered_answers_list[0] and (entered_answers_list[1] in correct_answers_list or entered_answers_list_1[1] in correct_answers_list) :
            secondAnswerCorrect = True
        if entered_answers_list[2]!=entered_answers_list[1] and entered_answers_list_1[2]!=entered_answers_list[1] and (entered_answers_list[2] in correct_answers_list or entered_answers_list_1[2] in correct_answers_list):
            thirdAnswerCorrect = True
        if firstAnswerCorrect and secondAnswerCorrect and thirdAnswerCorrect:
            answerCheck = True          
    except (KeyError, ValueError):
        pass
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPCMedium_2(student_id,question_id,sum_required):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = '"+question_id+"'").fetch(3)
    answerCheck = False
    '''first checking if the number is prime..second the sum is what is required'''
    prime_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103]
    number_sum = 0
    firstCheck = False
    secondCheck = False

    for q in Grade7QuestionData:
        try:
            firstCheck = False
            number_sum = number_sum + int(q.entered_answer)
            if int(q.entered_answer) in prime_numbers:
                firstCheck = True
        except ValueError:
            pass

    if number_sum == sum_required:
        secondCheck = True

    if firstCheck and secondCheck:
        answerCheck = True
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPCAdvanced_2(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PCAdvanced_2'").fetch(1)
    answerCheck = False
    firstCheck = False #entered answer have more than 3 numbers
    secondCheck = False #all 3 numbers are different
    thirdCheck = False #numbers are from the correct answer list
    entered_answer = []
    correct_answer = [101, 131, 151, 181, 191]
    for q in Grade7QuestionData:
        try:
            entered_answer = str(q.entered_answer).split(",")
            if len(entered_answer)>=3:
                firstCheck = True
        except ValueError:
            pass

    for i in range(len(entered_answer)):
        thirdCheck = False
        try:
            if i > 0:
                if int(entered_answer[i])!=int(entered_answer[i-1]):
                    secondCheck = True
            if int(entered_answer[i]) in correct_answer:
                thirdCheck = True
        except ValueError:
            pass      

    if firstCheck and secondCheck and thirdCheck:
        answerCheck = True
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPFEasy_1(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PFEasy_1'").fetch(4)
    answerCheck = False
    entered_answer = []
    correct_answer = [2,3,7,11]
    for q in Grade7QuestionData:
        try:
            entered_answer.append(int(q.entered_answer))
        except ValueError:
            pass
    entered_answer.sort()

    if entered_answer==correct_answer:
        answerCheck = True
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPFEasy_6(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PFEasy_6'").fetch(5)
    answerCheck = False
    entered_answer = {}
    correct_answer = [5,7,2,11,2]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass

    '''5 x 7^2 x 11^2 is correct and 5 x 11^ x 7^2 is also correct'''
    try:
        correct_order_entered_answer = [entered_answer["PFEasy_6_1_answer"],entered_answer["PFEasy_6_2_answer"],entered_answer["PFEasy_6_3_answer"],entered_answer["PFEasy_6_4_answer"],entered_answer["PFEasy_6_5_answer"]]
        alternate_correct_answer = [5,11,2,7,2]
        if correct_order_entered_answer==correct_answer or correct_order_entered_answer==alternate_correct_answer:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPFEasy_7(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PFEasy_7'").fetch(5)
    answerCheck = False
    entered_answer = {}
    correct_answer = [2,3,2,7,3]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass

    '''2 x 3^2 x 7^3 is correct and 2 x 7^3 x 3^2 is also correct'''
    try:
        correct_order_entered_answer = [entered_answer["PFEasy_7_1_answer"],entered_answer["PFEasy_7_2_answer"],entered_answer["PFEasy_7_3_answer"],entered_answer["PFEasy_7_4_answer"],entered_answer["PFEasy_7_5_answer"]]
        alternate_correct_answer = [2,7,3,3,2]
        if correct_order_entered_answer==correct_answer or correct_order_entered_answer==alternate_correct_answer:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPFEasy_13(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PFEasy_13'").fetch(6)
    answerCheck = False
    entered_answer = {}
    correct_answer = [2,3,3,2,5,13]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass

    '''2 x 3^2 x 7^3 is correct and 2 x 7^3 x 3^2 is also correct'''
    try:
        correct_order_entered_answer = [entered_answer["PFEasy_13_1_answer"],entered_answer["PFEasy_13_2_answer"],entered_answer["PFEasy_13_3_answer"],entered_answer["PFEasy_13_4_answer"],entered_answer["PFEasy_13_5_answer"],entered_answer["PFEasy_13_6_answer"]]
        alternate_correct_answer_1 = [3,2,2,3,5,13]
        alternate_correct_answer_2 = [3,2,2,3,13,5]
        alternate_correct_answer_3 = [2,3,3,2,13,5]
        if correct_order_entered_answer==correct_answer or correct_order_entered_answer==alternate_correct_answer_1 or correct_order_entered_answer==alternate_correct_answer_2 or correct_order_entered_answer==alternate_correct_answer_3:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPFMedium_1(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PFMedium_1'").fetch(4)
    answerCheck = False
    entered_answer = {}
    correct_answer = [2,5,7,2]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass

    '''2 x 3^2 x 7^3 is correct and 2 x 7^3 x 3^2 is also correct'''
    try:
        correct_order_entered_answer = [entered_answer["PFMedium_1_1_answer"],entered_answer["PFMedium_1_2_answer"],entered_answer["PFMedium_1_3_answer"],entered_answer["PFMedium_1_4_answer"]]
        alternate_correct_answer_1 = [5,2,7,2]
        if correct_order_entered_answer==correct_answer or correct_order_entered_answer==alternate_correct_answer_1:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPFMedium_2(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PFMedium_2'").fetch(4)
    answerCheck = False
    entered_answer = {}
    correct_answer = [2,8,3,3]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass

    '''2 x 3^2 x 7^3 is correct and 2 x 7^3 x 3^2 is also correct'''
    try:
        correct_order_entered_answer = [entered_answer["PFMedium_2_1_answer"],entered_answer["PFMedium_2_2_answer"],entered_answer["PFMedium_2_3_answer"],entered_answer["PFMedium_2_4_answer"]]
        alternate_correct_answer_1 = [3,3,2,8]
        if correct_order_entered_answer==correct_answer or correct_order_entered_answer==alternate_correct_answer_1:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPFMedium_3(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PFMedium_3'").fetch(7)
    answerCheck = False
    entered_answer = {}
    correct_answers = [[2,4,3,3,5,2,7],[2,4,5,2,3,3,7],[3,3,2,4,5,2,7],[3,3,5,2,2,4,7],[5,2,2,4,3,3,7],[5,2,3,3,2,4,7]]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass
    try:
        correct_order_entered_answer = [entered_answer["PFMedium_3_1_answer"],entered_answer["PFMedium_3_2_answer"],entered_answer["PFMedium_3_3_answer"],entered_answer["PFMedium_3_4_answer"],entered_answer["PFMedium_3_5_answer"],entered_answer["PFMedium_3_6_answer"],entered_answer["PFMedium_3_7_answer"]]
        if correct_order_entered_answer in correct_answers:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForPFAdvanced_1(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'PFAdvanced_1'").fetch(3)
    answerCheck = False
    entered_answer = {}
    correct_answer = [1350,1575,1890]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass
    try:
        correct_order_entered_answer = [entered_answer["PFAdvanced_1_1_answer"],entered_answer["PFAdvanced_1_2_answer"],entered_answer["PFAdvanced_1_3_answer"]]
        correct_order_entered_answer.sort()
        if correct_order_entered_answer == correct_answer:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForHCFAdvanced_6(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'HCFAdvanced_6'").fetch(2)
    answerCheck = False
    entered_answer = {}
    correct_answers = [[36,180],[180,36]]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass

    try:
        correct_order_entered_answer = [entered_answer["HCFAdvanced_6_1_answer"],entered_answer["HCFAdvanced_6_2_answer"]]
        correct_order_entered_answer.sort()
        if correct_order_entered_answer in correct_answers:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForSSREasy_7(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'SSREasy_7'").fetch(5)
    answerCheck = False
    entered_answer = {}
    correct_answers = [[2,3,3,2,5],[3,2,2,3,5]]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass
    try:
        correct_order_entered_answer = [entered_answer["SSREasy_7_1_answer"],entered_answer["SSREasy_7_2_answer"],entered_answer["SSREasy_7_3_answer"],entered_answer["SSREasy_7_4_answer"],entered_answer["SSREasy_7_5_answer"]]
        if correct_order_entered_answer in correct_answers:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForCCREasy_7(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'CCREasy_7'").fetch(5)
    answerCheck = False
    entered_answer = {}
    correct_answers = [[2,3,3,2,5],[3,2,2,3,5]]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass
    try:
        correct_order_entered_answer = [entered_answer["CCREasy_7_1_answer"],entered_answer["CCREasy_7_2_answer"],entered_answer["CCREasy_7_3_answer"],entered_answer["CCREasy_7_4_answer"],entered_answer["CCREasy_7_5_answer"]]
        if correct_order_entered_answer in correct_answers:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

def CheckAnswerForC9SFEAdvanced_1(student_id):
    Grade7QuestionData = HCGrade7Questions.HCGrade7Questions.gql("where student_id = '"+student_id+"' and question_id = 'C9SFEAdvanced_1'").fetch(2)
    answerCheck = False
    entered_answer = {}
    correct_answers = [[33,-16],[-33,16]]
    for q in Grade7QuestionData:
        try:
            entered_answer.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass

    '''2 x 3^2 x 7^3 is correct and 2 x 7^3 x 3^2 is also correct'''
    try:
        correct_order_entered_answer = [entered_answer["C9SFEAdvanced_1_1_answer"],entered_answer["C9SFEAdvanced_1_2_answer"]]
        if correct_order_entered_answer in correct_answers:
            answerCheck = True
    except KeyError:
        pass
    
    for q in Grade7QuestionData:
        q.correct = answerCheck
        q.put()      
    return

