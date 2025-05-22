'''
Created on Sep 21, 2013

@author: Farhat Pachisa
'''
from Database import TestsMaster,HCClass, HCStudents, SubmitProblemsTable
import CodeTranslation
import logging
import simplejson as json


class GenerateReports():
    
    def __init__(self):
        pass
    
    def GenerateReport(self, user):
        ClassInfo = []
        ClassTestData = []
        counter = 0

        ClassNameData = HCClass.HCClass.gql("where teacher_username = '"+user.username+"' order by create_date desc").fetch(100)
        for c in ClassNameData:
            ClassTestData = []
            test_id = ""
            test_name = ""
            counter = counter + 1
            TestData = TestsMaster.TestsMasterTable.gql("where student_id = '"+c.class_name+"' and created_by = '"+user.username+"' order by create_date desc").fetch(1000)
            for t in TestData:
                test_id = t.test_id
                test_name = t.test_name
                ClassTestData.append({'test_id':test_id,'test_name':test_name})
            '''if len(ClassTestData) == 0:
                ClassTestData.append({'test_id':test_id,'test_name':test_name})'''
            ClassInfo.append({'class_name':c.class_name,'class_skill':c.class_skill,'counter':str(counter),'test_data':ClassTestData})
        return {'ClassInfo':ClassInfo}

    def GenerateClassWorksheetSummaryReport(self, current_user, class_name, class_skill, test_id):

        WorksheetData = []
        TestData = TestsMaster.TestsMasterTable.gql("where test_id = '"+test_id+"'").fetch(1)
        for t in TestData:
            WorksheetData.append({'test_id':t.test_id,
                                  'test_name':t.test_name,
                                  'test_concept':CodeTranslation.TestConceptList_Brief[t.concept]+" - "+CodeTranslation.Concept_List[t.sub_concept],
                                  'create_date':t.create_date.strftime("%d %B %Y")})
        StudentData = HCStudents.HCStudents.gql("where teacher_username = '"+current_user.username+"' and class_name = '"+class_name+"' order by student_rollno asc").fetch(100)
        NoStudentAdded = False
        if len(StudentData) == 0:
            NoStudentAdded = True
        StudentTestData = []
             
        for s in StudentData:
            StudentWorksheetData = TestsMaster.TestsMasterTable.gql("where test_id = '"+test_id+unicode(s.student_username)+"'").fetch(1)
            StudentTestDataDict = {'student_username':unicode(s.student_username),
                                   'student_name':unicode(s.student_first_name)+" "+unicode(s.student_last_name),}
            test_score = 0
            test_status = ""
            complete_date = ""
            for sw in StudentWorksheetData:
                if sw.complete_date is not None:
                    complete_date = sw.complete_date.strftime("%d %B %Y")

                test_score = sw.score
                test_status = sw.status
                if test_score is None:
                    test_score = 0
                StudentTestDataDict.update({'test_score':test_score,
                                            'test_status':test_status,
                                            'complete_date':complete_date})
                
            StudentTestData.append(StudentTestDataDict)
        logging.info(StudentTestData)
        Title1 = "Worksheet score %"            
        Title1 = json.dumps(Title1)    
        
        StudentWorksheetScoreChartData = []
        StudentWorksheetScoreChartData.append(['Name','Score'])
        
        for std in StudentTestData:
            try:
                StudentWorksheetScoreChartData.append([std['student_name'],std['test_score']])
            except KeyError:
                StudentWorksheetScoreChartData.append([std['student_name'],0])

        StudentWorksheetScoreChartData = json.dumps(StudentWorksheetScoreChartData)
        StudentWorksheetScore = "drawGoogleStudentWorksheetScoreChart("+StudentWorksheetScoreChartData+","+Title1+");"

        return {'WorksheetData':WorksheetData,'StudentTestData':StudentTestData,'class_name':class_name,'StudentWorksheetScore':StudentWorksheetScore,
                "NoStudentAdded":NoStudentAdded,'StudentData':StudentData}


    def GenerateClassConceptSummaryReport(self, current_user, class_name, class_skill, student_data, concept_selected):

        CompleteConceptList = []
        
        concept_list = CodeTranslation.Topics[class_skill]
        
        for i in range(len(concept_list)):
            for j in range(len(CodeTranslation.SubTopics[concept_list[i][1]])):
                CompleteConceptList.append({'concept_id':CodeTranslation.SubTopics[concept_list[i][1]][j],'concept_name':concept_list[i][0]+" - "+CodeTranslation.Concept_List[CodeTranslation.SubTopics[concept_list[i][1]][j]]})
        if concept_selected is not None:
            SelectedConceptId = concept_selected
            SelectedConceptName = CodeTranslation.Concept_List[concept_selected]
        else:
            SelectedConceptId = CompleteConceptList[0]['concept_id']
            SelectedConceptName = CompleteConceptList[0]['concept_name']
        ClassStats = []
        GradeChartData1 = []
        GradeChartData1.append(['Student Name','Total Questions','Correct Answers'])
        for s in student_data:
            Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+s.student_username+"' and grade = "+str(CodeTranslation.Grade[class_skill])+" and concept='"+SelectedConceptId+"'")
            Data = Query.fetch(10000)
            student_name = s.student_first_name + " " + s.student_last_name
            student_rollno = s.student_rollno
            student_username = s.student_username

            total_problems = 0
            time_spent = 0
            HCScore = 0
            correct = 0
            for r in Data:
                total_problems = total_problems + 1
                if r.time_taken is not None:
                    time_spent = time_spent + r.time_taken                    
                if r.correct:
                    correct = correct + 1
                    if not r.HCScore:
                        r.HCScore = 5
                    HCScore = HCScore + r.HCScore
            if time_spent < 60 and time_spent > 0:
                time_spent = 60
            time_spent = time_spent / 60          
            
            try:
                Score100 = correct*100/total_problems
            except ZeroDivisionError:
                Score100 = 0
            
            GradeChartData1.append([s.student_first_name,total_problems,correct])
            if time_spent >= 60:
                hrs,min = divmod(time_spent,60)
                time_spent = str(hrs)+" hrs "+str(min)+" minutes"
            elif time_spent >1 and time_spent<=60:
                time_spent = str(time_spent)+" minutes"
            else:
                time_spent = str(time_spent)+" minute"
            ClassStats.append({"student_rollno":student_rollno,"student_username":student_username,"student_name":student_name,"attempted":total_problems,"correct":correct,"HCScore":HCScore,"Score100":Score100,"time_spent":time_spent})
        
        Title1 = "Total questions attempted v/s solved correctly on "+SelectedConceptName            
        Title1 = json.dumps(Title1)  
        GradeChartData1 = json.dumps(GradeChartData1)
        FunctionCall1 = "drawStudentConceptScoreChart("+GradeChartData1+","+Title1+");"

        return {'ClassStats':ClassStats,"StudentConceptScoreChart":FunctionCall1,'CompleteConceptList':CompleteConceptList}
