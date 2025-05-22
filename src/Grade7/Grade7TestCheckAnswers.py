'''
Created on May 14, 2014

@author: Farhat Pachisa

Copyright:
    Copyright (c) 2011, Home Campus.  All Rights Reserved.

Usage:
  
History:
'''
from Database import HCGrade7TestQuestions

def CheckAnswerForFMRTT1_7(student_id,test_id,answer_id,entered_answer):
    Grade7TestQuestionsData = HCGrade7TestQuestions.HCGrade7TestQuestions.gql("where student_id = '"+student_id+"' and test_id ='"+test_id+"' and question_id = 'FMRTT1_7'").fetch(6)
    answerCheck = False
    check1 = False
    check2 = False
    check3 = False
    
    entered_answer_dict = {}
    correct_answers = [[65,546],[130,273],[182,195],[91,390]]
    for q in Grade7TestQuestionsData:
        try:
            entered_answer_dict.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass
    try:
        #saving the answer which triggered this check..as the answer which triggers doesn't get saved tp database in the CheckAndSaveAnswer method in Grade7Test Module
        entered_answer_dict[answer_id]=int(entered_answer)
        pair1 = [entered_answer_dict["FMRTT1_7_1_answer"],entered_answer_dict["FMRTT1_7_2_answer"]]
        pair2 = [entered_answer_dict["FMRTT1_7_3_answer"],entered_answer_dict["FMRTT1_7_4_answer"]]
        pair3 = [entered_answer_dict["FMRTT1_7_5_answer"],entered_answer_dict["FMRTT1_7_6_answer"]]
        pair1.sort()
        pair2.sort()
        pair3.sort()
        if pair1 in correct_answers:
            check1 = True
        if pair2 != pair1 and pair2!= pair3 and pair2 in correct_answers:
            check2 = True
        if pair3 != pair1 and pair3!=pair2 and pair3 in correct_answers:
            check3 = True           
        if check1 and check2 and check3:
            answerCheck = True
    except (KeyError, ValueError):
        pass
    
    for q in Grade7TestQuestionsData:
        q.correct = answerCheck
        if q.answer_id == answer_id:
            q.entered_answer = entered_answer
        if answerCheck:
            q.scored_marks = q.question_marks
        else:
            q.scored_marks = 0
        q.put()     
    return answerCheck

def CheckAnswerForFMRTT1_11(student_id,test_id,answer_id,entered_answer):
    Grade7TestQuestionsData = HCGrade7TestQuestions.HCGrade7TestQuestions.gql("where student_id = '"+student_id+"' and test_id ='"+test_id+"' and question_id = 'FMRTT1_11'").fetch(4)
    answerCheck = False
    check1 = False
    check2 = False
    
    entered_answer_dict = {}
    correct_answers = [[10,60],[20,30]]
    for q in Grade7TestQuestionsData:
        try:
            entered_answer_dict.update({q.answer_id:(int(q.entered_answer))})
        except ValueError:
            pass
    try:
        #saving the answer which triggered this check..as the answer which triggers doesn't get saved tp database in the CheckAndSaveAnswer method in Grade7Test Module
        entered_answer_dict[answer_id]=int(entered_answer)        
        pair1 = [entered_answer_dict["FMRTT1_11_1_answer"],entered_answer_dict["FMRTT1_11_2_answer"]]
        pair2 = [entered_answer_dict["FMRTT1_11_3_answer"],entered_answer_dict["FMRTT1_11_4_answer"]]
        pair1.sort()
        pair2.sort()      
        if pair1 in correct_answers:
            check1 = True
        if pair2 != pair1 and pair2 in correct_answers:
            check2 = True
            
        if check1 and check2:
            answerCheck = True
    except (KeyError, ValueError):
        pass
    
    for q in Grade7TestQuestionsData:
        q.correct = answerCheck
        if q.answer_id == answer_id:
            q.entered_answer = entered_answer        
        if answerCheck:
            q.scored_marks = q.question_marks
        else:
            q.scored_marks = 0
        q.put()      
    return answerCheck