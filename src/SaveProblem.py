import SubmitProblem

class SaveProblem():    
    def SaveProblem(self,student_id,template_values):
        ProblemObject = {
                      "student_id":student_id,
                      "concept":template_values["concept"],
                      "problem_type":template_values["problem_type"],
                      "problem":template_values["problem"],
                      "answer":template_values["answer"],}

        ProblemObject["grade"] = 99
        ProblemObject["concept"]="DUMMY"
        try:
            ProblemObject["dollar_unit"]=template_values['dollar_unit']
        except KeyError:
            pass
        try:
            ProblemObject["unit"]=template_values['unit']
        except KeyError:
            pass                  
        try:
            ProblemObject["template"]=template_values['template']
        except KeyError:
            pass
        try:
            ProblemObject["answer1"]=str(template_values['answer1'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answer2"]=str(template_values['answer2'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answer3"]=str(template_values['answer3'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answer4"]=str(template_values['answer4'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerM1"]=str(template_values['answerM1'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerM2"]=str(template_values['answerM2'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerM3"]=str(template_values['answerM3'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerM4"]=str(template_values['answerM4'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerN1"]=str(template_values['answerN1'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerN2"]=str(template_values['answerN2'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerN3"]=str(template_values['answerN3'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerN4"]=str(template_values['answerN4'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerD1"]=str(template_values['answerD1'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerD2"]=str(template_values['answerD2'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerD3"]=str(template_values['answerD3'])
        except KeyError:
            pass                    
        try:
            ProblemObject["answerD4"]=str(template_values['answerD4'])
        except KeyError:
            pass 
        try:
            ProblemObject["value1"]=str(template_values['value1'])
        except KeyError:
            pass                    
        try:
            ProblemObject["value2"]=str(template_values['value2'])
        except KeyError:
            pass                    
        try:
            ProblemObject["value3"]=str(template_values['value3'])
        except KeyError:
            pass                    
        try:
            ProblemObject["value4"]=str(template_values['value4'])
        except KeyError:
            pass                    
        try:
            ProblemObject["explain"]=str(template_values['explain']['explain_text'])
        except KeyError:
            pass                    
        try:
            ProblemObject["FunctionCall"]=template_values['FunctionCall']
        except KeyError:
            pass 
        try:
            ProblemObject["FractionAnswer"]=template_values['FractionAnswer']
        except KeyError:
            pass 
        try:
            ProblemObject["CheckAnswerType"]=template_values['CheckAnswerType']
        except KeyError:
            pass 
        
        SubmitProblem.SubmitProblem(ProblemObject)
