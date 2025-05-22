from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import login_required,UserRequiredIfAuthenticatedMiddleware,user_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin

rules = [Rule('/Notes', endpoint='NotesPage.html', handler='Notes.NotesPage'),
         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
        
         Rule('/Notes/Primary5/WholeNumbers/Figures-to-Words', endpoint='', handler='Notes.WNFiguresToWords'),
         Rule('/Notes/Primary5/WholeNumbers/Words-to-Figures', endpoint='', handler='Notes.WNWordsToFigures'),
         Rule('/Notes/Primary5/WholeNumbers/Place-Values', endpoint='', handler='Notes.WNPlaceValues'),
         Rule('/Notes/Primary5/WholeNumbers/Comparison-Ordering-Pattern', endpoint='', handler='Notes.P5WNComparisonOrdering'),
         Rule('/Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-1', endpoint='', handler='Notes.P5WNApproximationEstimation'),
         Rule('/Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-2', endpoint='', handler='Notes.P5WNApproximationEstimation'),
         Rule('/Notes/Primary5/WholeNumbers/Multiply-by-10-100-1000', endpoint='', handler='Notes.P5WNMultiply'),
         Rule('/Notes/Primary5/WholeNumbers/Divide-by-10-100-1000', endpoint='', handler='Notes.P5WNDivide'),
         Rule('/Notes/Primary5/WholeNumbers/Order-of-Operations', endpoint='', handler='Notes.P5WNOperations'),
         Rule('/Notes/Primary5/Fractions/What-Is-a-Fraction', endpoint='', handler='Notes.P5FRWhatIsFractions'),
         Rule('/Notes/Primary5/Fractions/Types-of-Fractions', endpoint='', handler='Notes.P5FRTypesFractions'),
         Rule('/Notes/Primary5/Fractions/Improper-Mixed-Fractions', endpoint='', handler='Notes.P5FRImproperMixedFractions'),
         Rule('/Notes/Primary5/Fractions/Simplifying-Fractions-GCF', endpoint='', handler='Notes.P5FRSimplifyingFractions'),
         Rule('/Notes/Primary5/Fractions/Unlike-Fractions-LCM-Part-1', endpoint='', handler='Notes.P5FRUnlikeFractions'),
         Rule('/Notes/Primary5/Fractions/Unlike-Fractions-LCM-Part-2', endpoint='', handler='Notes.P5FRUnlikeFractions'),
         Rule('/Notes/Primary5/Fractions/Addition-Proper-Fractions', endpoint='', handler='Notes.P5FRAddProperFractions'),
         Rule('/Notes/Primary5/Fractions/Subtraction-Proper-Fractions', endpoint='', handler='Notes.P5FRSubProperFractions'),
         Rule('/Notes/Primary5/Fractions/Addition-Mixed-Fractions', endpoint='', handler='Notes.P5FRAddMixedFractions'),
         Rule('/Notes/Primary5/Fractions/Subtraction-Mixed-Fractions', endpoint='', handler='Notes.P5FRSubMixedFractions'),
         Rule('/Notes/Primary5/Fractions/Multiplication-Fractions', endpoint='', handler='Notes.P5FRMultFractions'),
         Rule('/Notes/Primary5/Fractions/Multiplication-Mixed-Fractions', endpoint='', handler='Notes.P5FRMultMixedFractions'),
         Rule('/Notes/Primary5/Fractions/Division-Proper-Fraction', endpoint='', handler='Notes.P5FRDivisionFractions'),
         Rule('/Notes/Primary5/Fractions/Fraction-as-Division', endpoint='', handler='Notes.P5FRFractionDivision'),
         Rule('/Notes/Primary5/Fractions/Fractions-Decimals', endpoint='', handler='Notes.P5FRFractionDecimal'),
         Rule('/Notes/Primary5/Decimal/Multiply-by-10s-100s-1000s', endpoint='', handler='Notes.P5DCMultiply'),
         Rule('/Notes/Primary5/Decimal/Divide-by-10s-100s-1000s', endpoint='', handler='Notes.P5DCDivide'),
         Rule('/Notes/Primary5/Decimal/Rounding-Off-Decimal-Numbers', endpoint='', handler='Notes.P5DCRoundingOff'),
         Rule('/Notes/Primary5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers', endpoint='', handler='Notes.P5DCEstimation'),         
         Rule('/Notes/Primary5/Percentage/Introduction', endpoint='', handler='Notes.P5PRIntroduction'),
         Rule('/Notes/Primary5/Percentage/Percentage-and-Fractions', endpoint='', handler='Notes.P5PRFractions'),
         Rule('/Notes/Primary5/Percentage/Percentage-and-Decimals', endpoint='', handler='Notes.P5PRDecimals'),
         Rule('/Notes/Primary5/Ratio/Introduction', endpoint='', handler='Notes.P5RTIntroduction'),
         Rule('/Notes/Primary5/Ratio/Equivalent', endpoint='', handler='Notes.P5RTEquivalent'),
         Rule('/Notes/Primary5/Ratio/Simplifying', endpoint='', handler='Notes.P5RTSimplifying'),
         Rule('/Notes/Primary5/Measurement/Triangle-Base-Height', endpoint='', handler='Notes.P5MTTriangleBH'),
         Rule('/Notes/Primary5/Measurement/Area-of-Triangle', endpoint='', handler='Notes.P5MTTriangleArea'),
         Rule('/Notes/Primary5/Measurement/Volume-Cube-Cuboid', endpoint='', handler='Notes.P5MTCubeVolume'),
         Rule('/Notes/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-1', endpoint='', handler='Notes.P5MTCubeVolume'),
         Rule('/Notes/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-2', endpoint='', handler='Notes.P5MTCubeVolume'),
         Rule('/Notes/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-3', endpoint='', handler='Notes.P5MTCubeVolume'),
         Rule('/Notes/Primary5/Geometry/Finding-unknown-angles', endpoint='', handler='Notes.P5GeometryAngles'),
         Rule('/Notes/Primary5/Geometry/Types-of-triangles', endpoint='', handler='Notes.P5GeometryTriangles'),
         Rule('/Notes/Primary5/Geometry/Angle-sum-of-triangle', endpoint='', handler='Notes.P5GeometryAngleSum'),
         Rule('/Notes/Primary5/Geometry/Triangle-Finding-unknown-angles', endpoint='', handler='Notes.P5GeometryTriangleAngle'),
         Rule('/Notes/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments', endpoint='', handler='Notes.P5GeometryDrawingTriangles'),
         Rule('/Notes/Primary5/Geometry/Four-sided-figures-types-and-properties', endpoint='', handler='Notes.P5GeometryFourSided'),
         Rule('/Notes/Primary5/Geometry/Four-sided-figures-finding-unknown-angles', endpoint='', handler='Notes.P5GeometryFourSidedAngles'),
         Rule('/Notes/Primary5/Geometry/Drawing-four-sided-figures', endpoint='', handler='Notes.P5GeometryFourSidedFigures'),
         Rule('/Notes/Primary5/Data-Analysis/Finding-Average', endpoint='', handler='Notes.P5DataAnalysisAverage'),
         Rule('/Notes/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction', endpoint='', handler='Notes.P6WholeNumberProperFraction'),
         Rule('/Notes/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction', endpoint='', handler='Notes.P6ProperFractionProperFraction'),
         Rule('/Notes/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions', endpoint='', handler='Notes.P6AlgebraWhatIsAlgebra'),
         Rule('/Notes/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions', endpoint='', handler='Notes.P6AlgebraSimplifying'),
]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_response(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session

        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
        })

        return super(BaseHandler, self).render_response(filename, **kwargs)
      
class NotesPage(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('LearnPage.html', section='content')
    
class WNFiguresToWords(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/WholeNumbers/Figures-to-Words.html', section='content')    

class WNWordsToFigures(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/WholeNumbers/Words-to-Figures.html', section='content') 

class WNPlaceValues(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/WholeNumbers/Place-Value.html', section='content') 

class P5WNComparisonOrdering(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/WholeNumbers/Comparison-Ordering-Pattern.html', section='content') 

class P5WNApproximationEstimation(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/WholeNumbers/Approximation-Estimation.html', section='content') 

class P5WNMultiply(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/WholeNumbers/Multiply-by-10-100-1000.html', section='content') 

class P5WNDivide(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/WholeNumbers/Divide-by-10-100-1000.html', section='content') 

class P5WNOperations(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/WholeNumbers/Order-of-Operations.html', section='content') 

class P5FRWhatIsFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/What-Is-a-Fraction.html', section='content')

class P5FRTypesFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Types-of-Fractions.html', section='content')
    
class P5FRImproperMixedFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Improper-Mixed-Fractions.html', section='content')

class P5FRSimplifyingFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Simplifying-Fractions-GCF.html', section='content')

class P5FRUnlikeFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Unlike-Fractions-LCM.html', section='content')

class P5FRAddProperFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Addition-Proper-Fractions.html', section='content')

class P5FRSubProperFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Subtraction-Proper-Fractions.html', section='content')

class P5FRAddMixedFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Addition-Mixed-Fractions.html', section='content')

class P5FRSubMixedFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Subtraction-Mixed-Fractions.html', section='content')

class P5FRMultFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Multiplication-Fractions.html', section='content')

class P5FRMultMixedFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Multiplication-Mixed-Fractions.html', section='content')

class P5FRDivisionFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Division-Proper-Fraction.html', section='content')

class P5FRFractionDivision(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Fraction-as-Division.html', section='content')

class P5FRFractionDecimal(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Fractions/Fractions-Decimals.html', section='content')

class P5DCMultiply(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Decimal/multiplying-decimal-numbers-by-10s-100s-1000s.html', section='content')

class P5DCDivide(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Decimal/dividing-decimal-numbers-by-10s-100s-1000s.html', section='content')

class P5DCRoundingOff(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Decimal/rounding-off-decimal-numbers.html', section='content')

class P5DCEstimation(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Decimal/estimation-in-calculations-with-decimal-numbers.html', section='content')

class P5PRIntroduction(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Percentage/introduction-to-percentage.html', section='content')

class P5PRFractions(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Percentage/percentage-and-fraction.html', section='content')

class P5PRDecimals(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Percentage/percentage-and-decimals.html', section='content')

class P5RTIntroduction(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Ratio/introduction-to-ratio.html', section='content')

class P5RTEquivalent(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Ratio/equivalent-ratios.html', section='content')

class P5RTSimplifying(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Ratio/simplifying-ratios.html', section='content')

class P5MTTriangleBH(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Measurement/triangle-base-height-measurement.html', section='content')

class P5MTTriangleArea(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Measurement/finding-area-of-triangle.html', section='content')

class P5MTCubeVolume(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-1.html', section='content')

class P5GeometryAngles(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Geometry/finding-unknown-angles.html', section='content')

class P5GeometryTriangles(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Geometry/types-of-triangles.html', section='content')

class P5GeometryAngleSum(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Geometry/angle-sum-of-triangles.html', section='content')

class P5GeometryTriangleAngle(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Geometry/triangle-finding-unknown-angles.html', section='content')

class P5GeometryDrawingTriangles(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Geometry/drawing-triangles-using-geometrical-instruments.html', section='content')

class P5GeometryFourSided(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Geometry/four-sided-figures-types-and-properties.html', section='content')

class P5GeometryFourSidedAngles(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Geometry/four-sided-figures-finding-unknown-angles.html', section='content')

class P5GeometryFourSidedFigures(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/Geometry/drawing-four-sided-figures.html', section='content')

class P5DataAnalysisAverage(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary5/DataAnalysis/average.html', section='content')

class P6WholeNumberProperFraction(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction.html', section='content')

class P6ProperFractionProperFraction(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction.html', section='content')

class P6AlgebraWhatIsAlgebra(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions.html', section='content')

class P6AlgebraSimplifying(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions.html', section='content')
    
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()