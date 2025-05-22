'''
Created on Apr 14, 2013

@author: Farhat Pachisa
'''

from Models import HomeCampusUser
from Database import TestsMaster, HCClass, HCStudents, TestProblems
from google.appengine.api import memcache
from CodeTranslation import TestConceptList, Grade, TestConceptList_Brief, Concept_List
import logging

class GenerateWorksheets():
    
    def __init__(self):
        pass
    
    def GenerateWorksheetsPage(self, user, concept, sub_concept):
        ChildUser = []
        NewTest = []
        InProgressTest = []
        CompletedTest = []
        ClassInfo = []
        TeacherWorksheets = []
        
        if user.IsParent:
            ChildUserQuery = HomeCampusUser.gql("where email = '"+user.email+"' and IsParent = False")
            ChildUserData = ChildUserQuery.fetch(100)
            CountNew = 0
            CountInProgress = 0
            CountCompleted = 0
            for c in ChildUserData:
                ChildUser.append([c.username,c.first_name])
                if sub_concept == "All Topics":
                    NewTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+c.username+"' and concept = '"+concept+"' and status = 'New' order by create_date desc")
                    InProgressTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+c.username+"' and concept = '"+concept+"' and status = 'InProgress' order by update_date desc")
                    CompletedTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+c.username+"' and concept = '"+concept+"' and status = 'Completed' order by update_date desc")
                else:
                    NewTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+c.username+"' and sub_concept = '"+sub_concept+"' and status = 'New' order by create_date desc")
                    InProgressTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+c.username+"' and sub_concept = '"+sub_concept+"' and status = 'InProgress' order by update_date desc")
                    CompletedTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+c.username+"' and sub_concept = '"+sub_concept+"' and status = 'Completed' order by update_date desc")
                    
                NewTestData = NewTestDataQuery.fetch(5)
                InProgressTestData = InProgressTestDataQuery.fetch(5)
                CompletedTestData = CompletedTestDataQuery.fetch(1000)
                
                
                for n in NewTestData:
                    CountNew = CountNew + 1
                    try:
                        sub_topic = TestConceptList_Brief[n.concept]+" - "+Concept_List[n.sub_concept]
                    except KeyError:
                        '''For older tests there is no sub topics'''
                        sub_topic = TestConceptList_Brief[n.concept]+" - "+"All Topics"
                    NewTest.append({"username":c.username,"test_id":n.test_id,"test_name":n.test_name,
                                    "concept":TestConceptList[n.concept],"grade":n.grade,"count":str(CountNew),
                                    "create_date":n.create_date.strftime("%d %B %Y"),"sub_topic":sub_topic
                                    })
                
                for i in InProgressTestData:
                    CountInProgress = CountInProgress + 1
                    try:
                        sub_topic = TestConceptList_Brief[i.concept]+" - "+Concept_List[i.sub_concept]
                    except KeyError:
                        '''For older tests there is no sub topics'''
                        sub_topic = TestConceptList_Brief[i.concept]+" - "+"All Topics"
                    InProgressTest.append({"username":c.username,"test_id":i.test_id,"test_name":i.test_name,
                                           "concept":TestConceptList[i.concept],"grade":i.grade,"count":str(CountInProgress),
                                           "update_date":i.update_date.strftime("%d %B %Y"),"sub_topic":sub_topic})
                
                for i in CompletedTestData:
                    try:
                        sub_topic = TestConceptList_Brief[i.concept]+" - "+Concept_List[i.sub_concept]
                    except KeyError:
                        '''For older tests there is no sub topics'''
                        sub_topic = TestConceptList_Brief[i.concept]+" - "+"All Topics"
                    CountCompleted = CountCompleted + 1
                    CompletedTest.append({"username":c.username,"test_id":i.test_id,"test_name":i.test_name,
                                           "concept":TestConceptList[i.concept],"grade":i.grade,"count":str(CountCompleted),
                                           "complete_date":i.complete_date.strftime("%d %B %Y"),"score":str(i.score),"sub_topic":sub_topic
                                           })

        elif user.IsTeacher:
            HCClassData = HCClass.HCClass.gql("where teacher_username = '"+user.username+"' and class_skill = '"+str(concept)[:2]+"'").fetch(100)
            for cd in HCClassData:
                ClassInfo.append({"class_name":cd.class_name,"class_skill":"Grade "+str(Grade[cd.class_skill])})
                if sub_concept == "All Topics":
                    TeacherWorksheetsData = TestsMaster.TestsMasterTable.gql("where created_by = '"+user.username+"' and student_id =  '"+cd.class_name+"' and concept = '"+concept+"' order by create_date desc").fetch(1000)
                else:
                    TeacherWorksheetsData = TestsMaster.TestsMasterTable.gql("where created_by = '"+user.username+"' and student_id =  '"+cd.class_name+"' and sub_concept = '"+sub_concept+"' order by create_date desc").fetch(1000)
                for tw in TeacherWorksheetsData:
                    try:
                        sub_topic = TestConceptList_Brief[tw.concept]+"-"+Concept_List[tw.sub_concept]
                    except KeyError:
                        '''For older tests there is no sub topics'''
                        sub_topic = TestConceptList_Brief[tw.concept]+" - "+"All Topics"
                    TeacherWorksheets.append({"class_name":cd.class_name,"test_id":tw.test_id,"test_name":tw.test_name,
                                           "concept":TestConceptList[tw.concept],"grade":tw.grade,
                                           "create_date":tw.create_date.strftime("%d %B %Y"),"sub_topic":sub_topic})
                    
        else:
            ChildUser.append([user.username,user.first_name])
            #A student can only in one class at most
            ChildClassInfo = HCStudents.HCStudents.gql("where student_username = '"+user.username+"'").fetch(1)
            class_name = ""
            join_date = ""
            for c in ChildClassInfo:
                class_name = c.class_name
                join_date = c.join_date
            if class_name != "":
                DateString = str(join_date.year)+"-"+str(join_date.month)+"-"+str(join_date.day)                
                TeacherWorksheets = TestsMaster.TestsMasterTable.gql("where student_id = '"+class_name+"' and concept = '"+concept+"' and create_date > Date('"+DateString+"')").fetch(1000)
                StudentsAllWorksheets = TestsMaster.TestsMasterTable.gql("where student_id = '"+user.username+"' and concept = '"+concept+"'").fetch(10000)
                StudentAllWorksheetsID = []
                for s in StudentsAllWorksheets:
                    StudentAllWorksheetsID.append(s.test_id)
                for t in TeacherWorksheets:
                    if t.test_id+unicode(user.username) not in StudentAllWorksheetsID:
                        self.AddTeacherWorksheet(t,user.username)

            if sub_concept == "All Topics":
                NewTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+user.username+"' and concept = '"+concept+"' and status = 'New' order by create_date desc")
                InProgressTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+user.username+"' and concept = '"+concept+"' and status = 'InProgress' order by update_date desc")
                CompletedTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+user.username+"' and concept = '"+concept+"' and status = 'Completed' order by update_date desc")
            else:
                NewTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+user.username+"' and sub_concept = '"+sub_concept+"' and status = 'New' order by create_date desc")
                InProgressTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+user.username+"' and sub_concept = '"+sub_concept+"' and status = 'InProgress' order by update_date desc")
                CompletedTestDataQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+user.username+"' and sub_concept = '"+sub_concept+"' and status = 'Completed' order by update_date desc")
                
            NewTestData = NewTestDataQuery.fetch(5)
            InProgressTestData = InProgressTestDataQuery.fetch(5)
            CompletedTestData = CompletedTestDataQuery.fetch(1000)
            
            CountNew = 0
            for n in NewTestData:
                CountNew = CountNew + 1
                try:
                    sub_topic = TestConceptList_Brief[n.concept]+" - "+Concept_List[n.sub_concept]
                except KeyError:
                    '''For older tests there is no sub topics'''
                    sub_topic = TestConceptList_Brief[n.concept]+" - "+"All Topics"
                NewTest.append({"username":user.username,"test_id":n.test_id,"test_name":n.test_name,
                                "concept":TestConceptList[n.concept],"grade":n.grade,"count":str(CountNew),
                                "create_date":n.create_date.strftime("%d %B %Y"),"sub_topic":sub_topic
                                })
                logging.info("Test id in HCTEST = "+unicode(n.test_id))
            CountInProgress = 0
            for i in InProgressTestData:
                CountInProgress = CountInProgress + 1
                try:
                    sub_topic = TestConceptList_Brief[i.concept]+" - "+Concept_List[i.sub_concept]
                except KeyError:
                    '''For older tests there is no sub topics'''
                    sub_topic = TestConceptList_Brief[i.concept]+" - "+"All Topics"                
                InProgressTest.append({"username":user.username,"test_id":i.test_id,"test_name":i.test_name,
                                       "concept":TestConceptList[i.concept],"grade":i.grade,"count":str(CountInProgress),
                                       "update_date":i.update_date.strftime("%d %B %Y"),"sub_topic":sub_topic
                                       })
            CountCompleted = 0
            for i in CompletedTestData:
                CountCompleted = CountCompleted + 1
                try:
                    sub_topic = TestConceptList_Brief[i.concept]+" - "+Concept_List[i.sub_concept]
                except KeyError:
                    '''For older tests there is no sub topics'''
                    sub_topic = TestConceptList_Brief[i.concept]+" - "+"All Topics"                                
                CompletedTest.append({"username":user.username,"test_id":i.test_id,"test_name":i.test_name,
                                       "concept":TestConceptList[i.concept],"grade":i.grade,"count":str(CountCompleted),
                                       "complete_date":i.complete_date.strftime("%d %B %Y"),"score":str(i.score),"sub_topic":sub_topic
                                       })
        
        memcache.Client().delete(unicode(user)+"_NewTest")
        memcache.Client().delete(unicode(user)+"_InProgressTest")
        memcache.Client().delete(unicode(user)+"_CompletedTest")
        memcache.Client().add(unicode(user)+"_NewTest",NewTest,3600)
        memcache.Client().add(unicode(user)+"_InProgressTest",InProgressTest,3600)
        memcache.Client().add(unicode(user)+"_CompletedTest",CompletedTest,3600)

        return {'Children':ChildUser,'NewTest':NewTest,'InProgressTest':InProgressTest,'CompletedTest':CompletedTest,
                'ClassInfo':ClassInfo,'TeacherWorksheets':TeacherWorksheets}
        
    def AddTeacherWorksheet(self,test_data,username):
        TestMaster = TestsMaster.TestsMasterTable(test_id = test_data.test_id+unicode(username),
                                                  test_name = test_data.test_name,
                                                  student_id = username,
                                                  grade = test_data.grade,
                                                  concept = test_data.concept,
                                                  sub_concept = test_data.sub_concept,
                                                  created_by = test_data.created_by,
                                                  create_date = test_data.create_date,
                                                  status='New',
                                                  update_date = test_data.update_date,
                                                  questions = test_data.questions,
                                                  TestIndicator = test_data.TestIndicator)
        TestMaster.put()        

        TeacherTestProblems = TestProblems.TestProblems.gql("where test_id ='"+test_data.test_id+"'").fetch(50)
        for n in TeacherTestProblems:
            TestProblemsInfo = TestProblems.TestProblems(test_id=test_data.test_id+unicode(username),
                                                     concept=n.concept,
                                                     counter=n.counter,
                                                     problem_type=n.problem_type,
                                                     problem=n.problem,
                                                    dollar_unit=n.dollar_unit,
                                                    unit=n.unit,
                                                    answer=n.answer,
                                                    complexity_level=n.complexity_level,
                                                    template=n.template,
                                                    answer1=n.answer1,
                                                    answer2=n.answer2,
                                                    answer3=n.answer3,
                                                    answer4=n.answer4,
                                                    answerM1=n.answerM1,
                                                    answerM2=n.answerM2,
                                                    answerM3=n.answerM3,
                                                    answerM4=n.answerM4,
                                                    answerN1=n.answerN1,
                                                    answerN2=n.answerN2,
                                                    answerN3=n.answerN3,
                                                    answerN4=n.answerN4,
                                                    answerD1=n.answerD1,
                                                    answerD2=n.answerD2,
                                                    answerD3=n.answerD3,
                                                    answerD4=n.answerD4,
                                                    value1=n.value1,
                                                    value2=n.value2,
                                                    value3=n.value3,
                                                    value4=n.value4,
                                                    explain=n.explain,
                                                    CheckAnswerType=n.CheckAnswerType,
                                                    FunctionCall=n.FunctionCall,
                                                    FractionAnswer=n.FractionAnswer
                                                     )
            TestProblemsInfo.put()