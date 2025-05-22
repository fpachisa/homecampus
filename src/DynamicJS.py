'''
Created on 30-Sep-2016

@author: Riyaz Ali


CURRENTLY NOT IN USE!!!
'''
from tipfy import RequestHandler, Tipfy, Rule, Response
import jinja2
import os

#The Jinja2 Environment
JINJA2_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader("/js"),
                                trim_blocks=True)   #This option will trim leading and trailing whitespace in the rendered template

class UnifiedGradeIndex(RequestHandler):
    def get(self):
        grade = self.request.args.get("grade")
        intent = self.request.args.get("intent")
        ctx = {}
        ctx['grade'] = grade
        ctx['intent'] = intent
        return Response(JINJA2_ENV.get_template("unified_grade_index.js").render(ctx))
    
app = Tipfy(rules=[
                Rule("/js/unified_grade_index.js", handler="DynamicJS.UnifiedGradeIndex"),
            ])

if __name__ == "__main__":
    app.run()