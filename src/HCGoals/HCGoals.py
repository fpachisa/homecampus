'''
Created on Oct 10, 2012

@author: Farhat Pachisa
'''

from Models import HomeCampusUser
from Database import SubmitProblemsTable
from Database import HCGoals
from datetime import datetime
import CodeTranslation 
import logging
import HCGoalsTargets

class GenerateGoals():
    
    def __init__(self):
        pass
    
    def GenerateGoalPage(self, user):
        ChildUserName = []
        if user.IsParent:
            IsParent = True
            ChildUserQuery = HomeCampusUser.gql("where email = '"+user.email+"' and IsParent = False")
            ChildUserData = ChildUserQuery.fetch(100)
            for c in ChildUserData:
                ChildUserName.append({'name':c.first_name,'id':c.username,'grade':c.skill})
        else:
            IsParent = False
            ChildUserName.append({'name':user.first_name,'id':user.username,'grade':user.skill})          
        return {'Children':ChildUserName,'IsParent':IsParent}


    def GenerateGoals(self, grade, topic, StudentId, current_user):
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

        Query = SubmitProblemsTable.ProblemsTable.gql("where student_id = '"+StudentId+"' and grade = "+str(grade))
        Data = Query.fetch(10000)
        
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
        return {'ChildId':StudentId,'child':ChildUserName,'Children':Children,'GradeStats':GradeStats,'IsParent':IsParent}

    
    def SaveGoals(self, user, StudentId, grade, topic, DataArray):
        ChildUserName = []
        if user.IsParent:
            IsParent = True
            ChildUserQuery = HomeCampusUser.gql("where email = '"+user.email+"' and IsParent = False")
            ChildUserData = ChildUserQuery.fetch(100)
            for c in ChildUserData:
                ChildUserName.append({'name':c.first_name,'id':c.username,'grade':c.skill})
        else:
            IsParent = False
            ChildUserName.append({'name':user.first_name,'id':user.username,'grade':user.skill})
            
        for i in range(len(DataArray)):
            GoalsQuery = HCGoals.HCGoals.gql("where student_id = '"+StudentId+"' and subTopic='"+DataArray[i][0]+"'")
            GoalsData = GoalsQuery.fetch(1)
            if GoalsData == []:
                GoalsToSave = HCGoals.HCGoals(student_id=StudentId,
                                              grade=int(grade),
                                              topic=topic,
                                              subTopic=DataArray[i][0],
                                              goalName="Minimun Correct Questions",
                                              target=int(DataArray[i][1]),
                                              created_by=user.username,
                                              create_date=datetime.now(),
                                              )
                GoalsToSave.put()
            else:
                for g in GoalsData:
                    if g.target!=int(DataArray[i][1]):                   
                        g.target=int(DataArray[i][1])
                        g.update_date=datetime.now()
                        g.update_by=user.username
                        g.put()
                     
        return {'Children':ChildUserName,'IsParent':IsParent}
