'''
Created on Jul 26, 2011

@author: Farhat Pachisa
'''
from Database import SubmitProblemsTable
from Database import TestsMaster
from Database import TestProblems
from Database import HCGoals
from Models import HomeCampusUser
import CodeTranslation
import HCRank
from datetime import datetime
import logging
import simplejson as json
import HCGoalsTargets

class GenerateReports():
    
    def __init__(self):
        pass
    
    def GenerateReport(self, user):
        ChildUserName = []
        ChildTestData = []
        counter = 0
        if user.IsParent:
            IsParent = True
            ChildUserQuery = HomeCampusUser.gql("where email = '"+user.email+"' and IsParent = False")
            ChildUserData = ChildUserQuery.fetch(100)
            for c in ChildUserData:
                ChildTestData = []
                counter = counter + 1
                TestQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+c.username+"' and status = 'Completed'")
                TestData = TestQuery.fetch(10000)
                for t in TestData:
                    ChildTestData.append({'test_id':t.test_id,'test_name':t.test_name})
                ChildUserName.append({'name':c.first_name,'id':c.username,'grade':c.skill,'counter':str(counter),'test_data':ChildTestData})
        else:
            IsParent = False
            counter = counter + 1
            TestQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+user.username+"' and status = 'Completed'")
            TestData = TestQuery.fetch(10000)
            for t in TestData:
                ChildTestData.append({'test_id':t.test_id,'test_name':t.test_name})            
            ChildUserName.append({'name':user.first_name,'id':user.username,'grade':user.skill,'counter':str(counter),'test_data':ChildTestData})            
        return {'Children':ChildUserName,'IsParent':IsParent}

    def GenerateSummaryReport(self, current_user, StudentId, grade):
        
        ChildUserQuery = HomeCampusUser.gql("where username = '"+StudentId+"'")
        logging.info(StudentId)
        ChildUserData = ChildUserQuery.fetch(1)
        for c in ChildUserData:
            ChildUserName = c.first_name

        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+StudentId+"' and grade = "+str(CodeTranslation.Grade[grade]))
        Data = Query.fetch(10000)
        total_problems = 0
        time_spent = 0
        HCScore = 0
        concept_list = CodeTranslation.Topics[grade]
        
        Title1 = "Total questions attempted v/s solved correctly by "+ChildUserName            
        Title1 = json.dumps(Title1)
        
        Title2 = "Time spent by "+ChildUserName+" at HC"            
        Title2 = json.dumps(Title2)        
        
        GradeStats = []
        GradeChartData1 = []
        GradeChartData1.append(['Topic','Total Questions','Correct Answers'])
        GradeChartData2 = []

        for i in range(len(concept_list)):
            correct = 0
            total_problems = 0
            time_spent = 0
            HCScore = 0
            concept = concept_list[i][0]
            concept_id = concept_list[i][1]
            
            for r in Data:
                try:
                    MainConcept = CodeTranslation.MainConcept[r.concept]
                except KeyError:
                    MainConcept = "Others"
                if MainConcept == concept_list[i][0]:
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
            #11-Mar-2012: Fixed HCRank if HCScore is greater than 1000
            try:
                HCNinja = HCRank.HCRank[HCScore]
            except KeyError:
                HCNinja = 'Sage'
            
            GradeChartData1.append([concept,total_problems,correct])
            GradeChartData2.append([concept,time_spent])
            if time_spent >= 60:
                hrs,min = divmod(time_spent,60)
                time_spent = str(hrs)+" hrs "+str(min)+" minutes"
            elif time_spent >1 and time_spent<=60:
                time_spent = str(time_spent)+" minutes"
            else:
                time_spent = str(time_spent)+" minute"
            GradeStats.append({"concept_id":concept_id,"concept":concept,"attempted":total_problems,"correct":correct,"HCScore":HCScore,"Score100":Score100,"time_spent":time_spent,"HCRank":HCNinja})
        GradeChartData1 = json.dumps(GradeChartData1)
        GradeChartData2 = json.dumps(GradeChartData2)
        FunctionCall1 = "drawGoogleColumnChart("+GradeChartData1+","+Title1+");"
        FunctionCall2 = "drawGooglePieChart("+GradeChartData2+","+Title2+");"

        return {'ChildId':StudentId,'child':ChildUserName,'GradeStats':GradeStats,"SummaryReport1":FunctionCall1,"SummaryReport2":FunctionCall2,"grade":CodeTranslation.Grade[grade]}

    def GenerateGoalsReport(self, current_user, StudentId, grade, topic):
        
        Children = []
        if current_user.IsParent:
            IsParent = True
            if StudentId is None:
                return {'Error':"Please select a child name to view goals!!",'IsParent':IsParent}
            else:
                ChildrenQuery = HomeCampusUser.gql("where email = '"+current_user.email+"' and IsParent = False")
                ChildrenData = ChildrenQuery.fetch(100)
                for c in ChildrenData:
                    Children.append({'name':c.first_name,'id':c.username,'grade':c.skill})                
        else:
            StudentId = current_user.username
            IsParent = False
            Children.append({'name':current_user.first_name,'id':current_user.username,'grade':current_user.skill})
                                    
        ChildUserQuery = HomeCampusUser.gql("where username = '"+StudentId+"'")
        ChildUserData = ChildUserQuery.fetch(1)
        for c in ChildUserData:
            ChildUserName = c.first_name

        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+StudentId+"' and grade = "+str(CodeTranslation.Grade[grade]))
        Data = Query.fetch(10000)
        
        Title1 = "% Completed"            
        Title1 = json.dumps(Title1)
        GradeChartData1 = [] 
        
        concept_list = CodeTranslation.SubTopics[topic]
        
        GradeStats = []
        
        for i in range(len(concept_list)):
            GoalsQuery = HCGoals.HCGoals.gql("where student_id = '"+StudentId+"' and subTopic='"+concept_list[i]+"'")
            GoalsData = GoalsQuery.fetch(1)
            if GoalsData != []:
                for g in GoalsData:
                    goal = g.target
            else:
                try:
                    goal = HCGoalsTargets.HCGoalsDict[concept_list[i]]
                except KeyError:
                    goal = 30
                                   
            correct = 0
            total_problems = 0
            concept = CodeTranslation.Concept_List[concept_list[i]]

            concept_id = concept_list[i]
            
            for r in Data:
                if r.concept == concept_list[i]:
                    total_problems = total_problems + 1
                    if r.correct:
                        correct = correct + 1
            
            GradeStats.append({"concept_id":concept_id,"concept":concept,"attempted":total_problems,"correct":correct,"goal":goal})
            GradeChartData1.append([concept,int(float(correct*100)/goal)])
        
        GradeChartData1 = json.dumps(GradeChartData1)
        FunctionCall1 = "drawGoogleGoalBarChart("+GradeChartData1+","+Title1+");"
        
        return {'ChildId':StudentId,'child':ChildUserName,'Children':Children,'GradeStats':GradeStats,'IsParent':IsParent,'FunctionCall1':FunctionCall1,
                "grade":CodeTranslation.Grade[grade],"topic":CodeTranslation.TestConceptList_Brief[topic]}

    def GenerateDetailReport(self, current_user, StudentId, grade, topic, TopicName):        
        ChildUserQuery = HomeCampusUser.gql("where username = '"+StudentId+"'")
        logging.info(StudentId)
        ChildUserData = ChildUserQuery.fetch(1)
        for c in ChildUserData:
            ChildUserName = c.first_name

        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+StudentId+"' and grade = "+str(CodeTranslation.Grade[grade]))
        Data = Query.fetch(10000)
        total_problems = 0
        time_spent = 0
        HCScore = 0
        concept_list = CodeTranslation.SubTopics[topic]
        
        Title1 = "Total questions attempted v/s solved correctly by "+ChildUserName            
        Title1 = json.dumps(Title1)
        
        Title2 = "Time spent by "+ChildUserName+" at HC"            
        Title2 = json.dumps(Title2)        
        
        GradeStats = []
        GradeChartData1 = []
        GradeChartData1.append(['Topic','Total Questions','Correct Answers'])
        GradeChartData2 = []

        for i in range(len(concept_list)):
            correct = 0
            total_problems = 0
            time_spent = 0
            HCScore = 0
            concept = CodeTranslation.Concept_List[concept_list[i]]
            concept_id = concept_list[i]
            
            for r in Data:
                if r.concept == concept_list[i]:
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
            #11-Mar-2012: Fixed HCRank if HCScore is greater than 1000
            try:
                HCNinja = HCRank.HCRank[HCScore]
            except KeyError:
                HCNinja = 'Sage'
            
            GradeChartData1.append([concept,total_problems,correct])
            GradeChartData2.append([concept,time_spent])
            if time_spent >= 60:
                hrs,mins = divmod(time_spent,60)
                time_spent = str(hrs)+" hrs "+str(mins)+" minutes"
            elif time_spent >1 and time_spent<=60:
                time_spent = str(time_spent)+" minutes"
            else:
                time_spent = str(time_spent)+" minute"
            GradeStats.append({"concept_id":concept_id,"concept":concept,"attempted":total_problems,"correct":correct,"HCScore":HCScore,"Score100":Score100,"time_spent":time_spent,"HCRank":HCNinja})
        GradeChartData1 = json.dumps(GradeChartData1)
        GradeChartData2 = json.dumps(GradeChartData2)
        FunctionCall1 = "drawGoogleColumnChart("+GradeChartData1+","+Title1+");"
        FunctionCall2 = "drawGooglePieChart("+GradeChartData2+","+Title2+");"
        logging.info(TopicName)
        return {'ChildId':StudentId,'child':ChildUserName,'GradeStats':GradeStats,"FunctionCall1":FunctionCall1,"FunctionCall2":FunctionCall2,"grade":CodeTranslation.Grade[grade],'TopicName':TopicName}

    def GenerateProblemReport(self, current_user, StudentId, grade, topic, TopicName):
        
        ChildUserQuery = HomeCampusUser.gql("where username = '"+StudentId+"'")
        logging.info(StudentId)
        ChildUserData = ChildUserQuery.fetch(1)
        for c in ChildUserData:
            ChildUserName = c.first_name

        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+StudentId+"' and concept = '"+topic+"' order by submit_date desc")
        ProblemData = Query.fetch(20)
        problems = []
        counter = 0
        for p in ProblemData:
            counter = counter + 1
            explain = str(p.explain).partition("ANSWERSEPARATOR")[2]
            if explain == "" or explain is None:
                explain = "Not available. Coming Soon!!"
            answer_submitted = ""
            if p.answer_submitted == "None" or p.answer_submitted == "" or p.answer_submitted is None:
                answer_submitted = "No answer provided!!"
            else:
                answer_submitted = p.answer_submitted
                if p.template == "FractionMCQTypeProblems.html":
                    if "/" in answer_submitted: 
                        answer_submitted = GenerateFractions(answer_submitted.partition("/")[0],answer_submitted.partition("/")[2].partition("/")[0],answer_submitted.partition("/")[2].partition("/")[2])
                    else:
                        answer_submitted = answer_submitted[1:-1].split(", ")
                        answer_submitted = GenerateFractions(answer_submitted[0],answer_submitted[1],answer_submitted[2])
                elif p.template == "AlgebraFractionMCQTypeProblems.html":
                    '''special treatment for algebra fractions as there are alphanumeric characters and not all are numbers'''
                  
                    answer_submitted = answer_submitted[1:-1].split(", ")
                    answer_submitted0 = answer_submitted[0]
                    answer_submitted1 = answer_submitted[1]
                    answer_submitted2 = answer_submitted[2]
                    
                    if answer_submitted0[0] == "'":
                        answer_submitted0 = answer_submitted0[1:-1]
                    if answer_submitted1[0] == "'":
                        answer_submitted1 = answer_submitted1[1:-1]
                    if answer_submitted2[0] == "'":
                        answer_submitted2 = answer_submitted2[1:-1]
                                                                
                    answer_submitted = GenerateFractions(answer_submitted0,answer_submitted1,answer_submitted2)

            '''unit for user's answer so if not submitted then unit also is not shown'''
            unit = p.unit
            if unit == "None" or unit is None or answer_submitted=="No answer provided!!":
                unit = ""
            dollar_unit = p.dollar_unit
            if dollar_unit == "None" or dollar_unit is None or answer_submitted=="No answer provided!!":
                dollar_unit = ""
            '''units for original answer'''
            qunit = p.unit
            if qunit == "None" or qunit is None:
                qunit = ""
            qdollar_unit = p.dollar_unit
            if qdollar_unit == "None" or qdollar_unit is None:
                qdollar_unit = ""
                                
            #for Fractions answer it has to be in fraction form.
            answer = p.answer
            if p.template == "FractionMCQTypeProblems.html":
                answer = answer[1:-1].split(", ")
                answer = GenerateFractions(answer[0],answer[1],answer[2])
            elif p.template == "AlgebraFractionMCQTypeProblems.html":
                '''special treatment for algebra fractions as there are alphanumeric characters and not all are numbers'''
                answer = answer[1:-1].split(", ")
                answer0 = answer[0]
                answer1 = answer[1]
                answer2 = answer[2]
                
                if answer0[0] == "'":
                    answer0 = answer0[1:-1]
                if answer1[0] == "'":
                    answer1 = answer1[1:-1]
                if answer2[0] == "'":
                    answer2 = answer2[1:-1]                                                            
                answer = GenerateFractions(answer0,answer1,answer2)
            elif p.FractionAnswer == 'Y':
                answer = answer.split(",")
                answer0 = answer[0]
                answer1 = answer[1]
                answer2 = answer[2]
                answer = GenerateFractionsWithUnit(answer0,answer1,answer2,qunit)
                
            '''in some multiple choice answer I'm removing the white space but user should see the answer in the report the one which he sees in the question. so showing the value instead of answer'''
            if p.template == "MCQTypeProblems.html" or p.template=="MCQType3Choices.html":
                if answer_submitted == p.value1:
                    answer_submitted = p.answer1
                elif answer_submitted == p.value2:
                    answer_submitted = p.answer2
                elif answer_submitted == p.value3:
                    answer_submitted = p.answer3
                elif answer_submitted == p.value4:
                    answer_submitted = p.answer4
            
            '''FunctionCall is only required for drawing figures in html 5'''
            FunctionCall = p.FunctionCall
            '''If no function call then calling a dummy function so it doesn't give error in test_report.html'''
            if FunctionCall == "None" or FunctionCall == "" or FunctionCall is None:
                FunctionCall = "DummyFunction()"

            problems.append({'counter':counter,'question':p.problem,'answer':answer,'answer_submitted':answer_submitted,'explain':explain,'correct':p.correct,'FunctionCall':FunctionCall,
                             'unit':unit,'dollar_unit':dollar_unit,'qunit':qunit,'qdollar_unit':qdollar_unit,'FractionAnswer':p.FractionAnswer,'submit_date':p.submit_date})
                    
        return {'problems':problems,'child':ChildUserName,'grade':str(grade)[1],'TopicName':TopicName}

    def GenerateTestSummaryReport(self,user,StudentId,grade):
        
        ChildUserQuery = HomeCampusUser.gql("where username = '"+StudentId+"'")
        ChildUserData = ChildUserQuery.fetch(1)
        for c in ChildUserData:
            ChildUserName = c.first_name

        TestMasterQuery = TestsMaster.TestsMasterTable.gql("where student_id = '"+StudentId+"' and grade = "+str(CodeTranslation.Grade[grade])+" and status='Completed'")
        Data = TestMasterQuery.fetch(10000)
        
        Title1 = "Average %"            
        Title1 = json.dumps(Title1)        

        Title2 = "Number of worksheets completed on each topic"            
        Title2 = json.dumps(Title2)        
        
        TopicList = []
        TestStats = []
        GradeChartData1 = []        
        GradeChartData2 = []
        
        for r in Data:
            if CodeTranslation.TestConceptList_Brief[r.concept] not in TopicList:
                TopicList.append(CodeTranslation.TestConceptList_Brief[r.concept])
        
        for c in range(len(TopicList)):
            TotalScore = 0
            count = 0 
            for r in Data:
                if CodeTranslation.TestConceptList_Brief[r.concept] == TopicList[c]:
                    if r.score is not None:
                        TotalScore = TotalScore + r.score
                    count = count + 1
            
            AverageScore = int(float(TotalScore)/count)
            GradeChartData1.append([TopicList[c],AverageScore]) 
            GradeChartData2.append([TopicList[c],count])
        
        for r in Data:
            test_id = r.test_id
            test_name = r.test_name
            topic = CodeTranslation.TestConceptList_Brief[r.concept]
            Date_finished = r.complete_date.strftime("%d %b %Y")
            question = r.questions
            TestProblemQuery = TestProblems.TestProblems.gql("where test_id = '"+r.test_id+"'")
            ProblemsData = TestProblemQuery.fetch(1000)
            correct = 0
            for t in ProblemsData:
                if t.correct:
                    correct = correct + 1
            acheived = int(100 * float(correct)/question)  
            TestStats.append({'test_id':test_id,'test_name':test_name,'topic':topic,'date_finished':Date_finished,'question':question,'acheived':acheived,'correct':correct})

        GradeChartData1 = json.dumps(GradeChartData1)
        GradeChartData2 = json.dumps(GradeChartData2)

        FunctionCall1 = "drawGoogleBarChart("+GradeChartData1+","+Title1+");"
        FunctionCall2 = "drawGoogleTestReportPieChart("+GradeChartData2+","+Title2+");"
        
        logging.info(TestStats)
        return {'child':ChildUserName,'TestStats':TestStats,"WorksheetSummaryReport1":FunctionCall1,"WorksheetSummaryReport2":FunctionCall2,'grade':CodeTranslation.Grade[grade]}
            
        
    def GenerateConceptReport(self, user, StudentId):
        
        ChildUserQuery = HomeCampusUser.gql("where username = '"+StudentId+"'")
        logging.info(StudentId)
        ChildUserData = ChildUserQuery.fetch(1)
        for c in ChildUserData:
            ChildUserName = c.first_name

        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+StudentId+"'")
        Data = Query.fetch(10000)
        total_problems = 0
        time_spent = 0
        HCScore = 0
        concept_list = []
        Stats = []
        for r in Data:
            if r.concept not in concept_list:
                concept_list.append(r.concept)
        
        concept_list.sort()
        for i in range(len(concept_list)):
            correct = 0
            total_problems = 0
            time_spent = 0
            HCScore = 0
            try:
                concept = CodeTranslation.Concept_List[concept_list[i]]
            except KeyError:
                concept = concept_list[i]
            
            for r in Data:
                if r.concept == concept_list[i]:
                    total_problems = total_problems + 1
                    if r.time_taken is not None:
                        time_spent = time_spent + r.time_taken                    
                    if r.correct:
                        correct = correct + 1
                        if not r.HCScore:
                            r.HCScore = 5
                        HCScore = HCScore + r.HCScore
            time_spent = time_spent / 60
            if time_spent == 0:
                time_spent = "< 1 minute"
            
            try:
                Score100 = correct*100/total_problems
            except ZeroDivisionError:
                Score100 = 0
            #11-Mar-2012: Fixed HCRank if HCScore is greater than 1000
            try:
                HCNinja = HCRank.HCRank[HCScore]
            except KeyError:
                HCNinja = 'Sage'
            
            Stats.append({"concept":concept,"attempted":total_problems,"correct":correct,"HCScore":HCScore,"Score100":Score100,"time_spent":time_spent,"HCRank":HCNinja})

        return {'child':ChildUserName,'Stats':Stats}
    
    def GenerateTestReport(self,user,TestId):
        TestMasterQuery = TestsMaster.TestsMasterTable.gql("where test_id = '"+TestId+"'")
        TestMasterData = TestMasterQuery.fetch(1)
        logging.info("Test id in Generate Test Report = "+TestId)
        for t in TestMasterData:
            if t.status != "Completed":
                t.status = "Completed"
                t.complete_date = datetime.now()
                t.update_date = datetime.now()
            questions = t.questions
            name = t.test_name
            try:
                sub_topic = CodeTranslation.TestConceptList_Brief[t.concept]+" - "+CodeTranslation.Concept_List[t.sub_concept]
            except KeyError:
                '''For older tests there is no sub topics'''
                sub_topic = CodeTranslation.TestConceptList_Brief[t.concept]+" - "+"All Topics"             
            t.put()
        TestProblemQuery = TestProblems.TestProblems.gql("where test_id = '"+TestId+"' order by counter asc")
        TestProblemData = TestProblemQuery.fetch(questions)
        problems = []
        correct_answers = 0
        for p in TestProblemData:
            explain = str(p.explain).partition("ANSWERSEPARATOR")[2]
            if explain == "" or explain is None:
                explain = "Not available. Coming Soon!!"
            if p.correct:
                correct_answers = correct_answers + 1
            answer_submitted = ""
            if p.answer_submitted == "None" or p.answer_submitted == "" or p.answer_submitted is None:
                answer_submitted = "Question not attempted"
            else:
                answer_submitted = p.answer_submitted
                if p.template == "FractionMCQTypeProblems.html":
                    if "," in answer_submitted:
                        answer_submitted = answer_submitted[1:-1].split(", ")
                        answer_submitted = GenerateFractions(answer_submitted[0],answer_submitted[1],answer_submitted[2])
                    elif "/" in answer_submitted:
                        answer_submitted = GenerateFractions(answer_submitted.partition("/")[0],answer_submitted.partition("/")[2].partition("/")[0],answer_submitted.partition("/")[2].partition("/")[2])
                        
                elif p.template == "AlgebraFractionMCQTypeProblems.html":
                    '''special treatment for algebra fractions as there are alphanumeric characters and not all are numbers'''
                  
                    answer_submitted = answer_submitted[1:-1].split(", ")
                    answer_submitted0 = answer_submitted[0]
                    answer_submitted1 = answer_submitted[1]
                    answer_submitted2 = answer_submitted[2]
                    
                    if answer_submitted0[0] == "'":
                        answer_submitted0 = answer_submitted0[1:-1]
                    if answer_submitted1[0] == "'":
                        answer_submitted1 = answer_submitted1[1:-1]
                    if answer_submitted2[0] == "'":
                        answer_submitted2 = answer_submitted2[1:-1]
                                                                
                    answer_submitted = GenerateFractions(answer_submitted0,answer_submitted1,answer_submitted2)

            '''unit for user's answer so if not submitted then unit also is not shown'''
            unit = p.unit
            if unit == "None" or unit is None or answer_submitted=="Question not attempted":
                unit = ""
            dollar_unit = p.dollar_unit
            if dollar_unit == "None" or dollar_unit is None or answer_submitted=="Question not attempted":
                dollar_unit = ""
            '''units for original answer'''
            qunit = p.unit
            if qunit == "None" or qunit is None:
                qunit = ""
            qdollar_unit = p.dollar_unit
            if qdollar_unit == "None" or qdollar_unit is None:
                qdollar_unit = ""
                                
            #for Fractions answer it has to be in fraction form.
            answer = p.answer
            if p.template == "FractionMCQTypeProblems.html":
                answer = answer[1:-1].split(", ")
                answer = GenerateFractions(answer[0],answer[1],answer[2])
            elif p.template == "AlgebraFractionMCQTypeProblems.html":
                '''special treatment for algebra fractions as there are alphanumeric characters and not all are numbers'''
                answer = answer[1:-1].split(", ")
                answer0 = answer[0]
                answer1 = answer[1]
                answer2 = answer[2]
                
                if answer0[0] == "'":
                    answer0 = answer0[1:-1]
                if answer1[0] == "'":
                    answer1 = answer1[1:-1]
                if answer2[0] == "'":
                    answer2 = answer2[1:-1]                                                            
                answer = GenerateFractions(answer0,answer1,answer2)
            elif p.FractionAnswer == 'Y':
                answer = answer.split(",")
                answer0 = answer[0]
                answer1 = answer[1]
                answer2 = answer[2]
                answer = GenerateFractionsWithUnit(answer0,answer1,answer2,qunit)
                
            '''in some multiple choice answer I'm removing the white space but user should see the answer in the report the one which he sees in the question. so showing the value instead of answer'''
            if p.template == "MCQTypeProblems.html" or p.template == "MCQType3Choices.html":
                if answer_submitted == p.value1:
                    answer_submitted = p.answer1
                elif answer_submitted == p.value2:
                    answer_submitted = p.answer2
                elif answer_submitted == p.value3:
                    answer_submitted = p.answer3
                elif answer_submitted == p.value4:
                    answer_submitted = p.answer4
            
            '''FunctionCall is only required for drawing figures in html 5'''
            FunctionCall = p.FunctionCall
            '''If no function call then calling a dummy function so it doesn't give error in test_report.html'''
            if FunctionCall == "None" or FunctionCall == "" or FunctionCall is None:
                FunctionCall = "DummyFunction()"

            problems.append({'counter':p.counter,'question':p.problem,'answer':answer,'answer_submitted':answer_submitted,'explain':explain,'correct':p.correct,'FunctionCall':FunctionCall,
                             'unit':unit,'dollar_unit':dollar_unit,'qunit':qunit,'qdollar_unit':qdollar_unit,'FractionAnswer':p.FractionAnswer,
                             'test_id':TestId,'problem_type':p.problem_type})
        score = int(correct_answers*100/questions)

        TestMasterData = TestMasterQuery.fetch(1)
        for t in TestMasterData:
            #if t.score == "None" or t.score is None:
            t.score = score
            t.put()
            
        # @riyaz: getting student's name for display if the current user is parent
        prettyName = ""
        if user.IsParent:
            # getting student_id from test and then getting the stduent's name
            std_id = TestMasterData[0].student_id
            _usr = HomeCampusUser.gql("where username='" + std_id +"'")
            try:
                prettyName = _usr[0].first_name
            except:
                pass
            
        return {'problems':problems,'total_questions':questions,'correct_answers':correct_answers,'score':score,'name':name,'IsTeacher':user.IsTeacher,
                'sub_topic':sub_topic, 'userPrettyName': prettyName}

def GenerateFractions(m,n,d):
        Fraction = "<table class='FractionsTable' style='color:black'>"
        Fraction = Fraction + "<tr>"
        if m is None or str(m) == '0':
            Fraction = Fraction
        else:
            Fraction = Fraction + "<td>"+str(m)+"</td>"
        if n!='0':
            Fraction = Fraction + "<td>"
            if d!='1':
                Fraction = Fraction + "<u>"+"&nbsp;"*(len(d)/2)+n+"&nbsp;"*(len(d)/2)+"</u><br>"+"&nbsp;"*(len(n)/2)+d+"&nbsp;"*(len(n)/2)
            else:
                Fraction = Fraction + n
            Fraction = Fraction + "</td>"
        Fraction = Fraction + "</tr></table>"
        return Fraction

def GenerateFractionsWithUnit(m,n,d,unit):
        Fraction = "<table class='FractionsTable' style='color:black'>"
        Fraction = Fraction + "<tr>"
        if m is None or str(m) == '0':
            Fraction = Fraction
        else:
            Fraction = Fraction + "<td>"+str(m)+"</td>"
        if n!='0':
            Fraction = Fraction + "<td>"
            if d!='1':
                Fraction = Fraction + "<u>"+"&nbsp;"*(len(d)/2)+n+"&nbsp;"*(len(d)/2)+"</u><br>"+"&nbsp;"*(len(n)/2)+d+"&nbsp;"*(len(n)/2)
            else:
                Fraction = Fraction + n
            Fraction = Fraction + "</td>"
        Fraction = Fraction + "<td>&nbsp;"+unit+"</td>"
        Fraction = Fraction + "</tr></table>"
        return Fraction    