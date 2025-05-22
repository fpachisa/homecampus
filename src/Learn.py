from tipfy import RequestHandler
from tipfy import Rule
from Config import config
from tipfy import Tipfy
from tipfy.auth import login_required,UserRequiredIfAuthenticatedMiddleware,user_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
from Database import HCSubscription, TestsMaster
from tipfy.app import Response
import logging

'''27-July-2012: Changed the links to include Grade also along with Primary'''
rules = [Rule('/Learn', endpoint='LearnPage.html', handler='Learn.LearnPage'),
         Rule('/auth/login', endpoint='auth/login', handler='Handlers.LoginHandler'),
         Rule('/auth/logout', endpoint='auth/logout', handler='Handlers.LogoutHandler'),
         Rule('/auth/signup', endpoint='auth/signup', handler='Handlers.SignupHandler'),
         Rule('/auth/register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/Register', endpoint='auth/register', handler='Handlers.RegisterHandler'),
         Rule('/SignIn', endpoint='auth/login', handler='Handlers.LoginHandler'),
         
         Rule('/Learn/Primary_Grade_3_Mathematics', endpoint='', handler='Learn.P3Notes'),
         Rule('/Learn/Primary_Grade_4_Mathematics', endpoint='', handler='Learn.P4Notes'),
         Rule('/Learn/Primary_Grade_5_Mathematics', endpoint='', handler='Learn.P5Notes'),
         Rule('/Learn/Primary_Grade_6_Mathematics', endpoint='', handler='Learn.P6Notes'),
         
         Rule('/Learn/Primary5/WholeNumbers/Figures-to-Words', endpoint='', handler='Learn.P5WNFiguresToWords'),
         Rule('/Learn/Primary5/WholeNumbers/Words-to-Figures', endpoint='', handler='Learn.P5WNWordsToFigures'),
         Rule('/Learn/Primary5/WholeNumbers/Place-Values', endpoint='', handler='Learn.P5WNPlaceValue'),
         Rule('/Learn/Primary5/WholeNumbers/Comparison-Ordering-Pattern', endpoint='', handler='Learn.P5WNComparisonOrdering'),
         Rule('/Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-1', endpoint='', handler='Learn.P5WNApproximationEstimation1'),
         Rule('/Learn/Primary5/WholeNumbers/Approximation-Estimation-Part-2', endpoint='', handler='Learn.P5WNApproximationEstimation2'),
         Rule('/Learn/Primary5/WholeNumbers/Multiply-by-10-100-1000', endpoint='', handler='Learn.P5WNMultiply'),
         Rule('/Learn/Primary5/WholeNumbers/Divide-by-10-100-1000', endpoint='', handler='Learn.P5WNDivide'),
         Rule('/Learn/Primary5/WholeNumbers/Order-of-Operations', endpoint='', handler='Learn.P5WNOperations'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems-Video-List', endpoint='', handler='Learn.P5WNWordProblems'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems1', endpoint='', handler='Learn.P5WNWordProblems1'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems2', endpoint='', handler='Learn.P5WNWordProblems2'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems3', endpoint='', handler='Learn.P5WNWordProblems3'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems4', endpoint='', handler='Learn.P5WNWordProblems4'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems5', endpoint='', handler='Learn.P5WNWordProblems5'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems6', endpoint='', handler='Learn.P5WNWordProblems6'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems7', endpoint='', handler='Learn.P5WNWordProblems7'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems8', endpoint='', handler='Learn.P5WNWordProblems8'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems9', endpoint='', handler='Learn.P5WNWordProblems9'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems10', endpoint='', handler='Learn.P5WNWordProblems10'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems11', endpoint='', handler='Learn.P5WNWordProblems11'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems12', endpoint='', handler='Learn.P5WNWordProblems12'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems13', endpoint='', handler='Learn.P5WNWordProblems13'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems14', endpoint='', handler='Learn.P5WNWordProblems14'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems15', endpoint='', handler='Learn.P5WNWordProblems15'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems16', endpoint='', handler='Learn.P5WNWordProblems16'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems17', endpoint='', handler='Learn.P5WNWordProblems17'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems18', endpoint='', handler='Learn.P5WNWordProblems18'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems19', endpoint='', handler='Learn.P5WNWordProblems19'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems20', endpoint='', handler='Learn.P5WNWordProblems20'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems21', endpoint='', handler='Learn.P5WNWordProblems21'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems22', endpoint='', handler='Learn.P5WNWordProblems22'),
         Rule('/Learn/Primary5/WholeNumbers/Word-Problems23', endpoint='', handler='Learn.P5WNWordProblems23'),
         Rule('/Learn/Primary5/Fractions/What-Is-a-Fraction', endpoint='', handler='Learn.P5FRWhatIsFractions'),
         Rule('/Learn/Primary5/Fractions/Types-of-Fractions', endpoint='', handler='Learn.P5FRTypesFractions'),
         Rule('/Learn/Primary5/Fractions/Improper-Mixed-Fractions', endpoint='', handler='Learn.P5FRImproperMixedFractions'),
         Rule('/Learn/Primary5/Fractions/Simplifying-Fractions-GCF', endpoint='', handler='Learn.P5FRSimplifyingFractions'),
         Rule('/Learn/Primary5/Fractions/Unlike-Fractions-LCM-Part-1', endpoint='', handler='Learn.P5FRUnlikeFractions1'),
         Rule('/Learn/Primary5/Fractions/Unlike-Fractions-LCM-Part-2', endpoint='', handler='Learn.P5FRUnlikeFractions2'),
         Rule('/Learn/Primary5/Fractions/Addition-Proper-Fractions', endpoint='', handler='Learn.P5FRAddProperFractions'),
         Rule('/Learn/Primary5/Fractions/Subtraction-Proper-Fractions', endpoint='', handler='Learn.P5FRSubProperFractions'),
         Rule('/Learn/Primary5/Fractions/Addition-Mixed-Fractions', endpoint='', handler='Learn.P5FRAddMixedFractions'),
         Rule('/Learn/Primary5/Fractions/Subtraction-Mixed-Fractions', endpoint='', handler='Learn.P5FRSubMixedFractions'),
         Rule('/Learn/Primary5/Fractions/Multiplication-Fractions', endpoint='', handler='Learn.P5FRMultFractions'),
         Rule('/Learn/Primary5/Fractions/Multiplication-Mixed-Fractions', endpoint='', handler='Learn.P5FRMultMixedFractions'),
         Rule('/Learn/Primary5/Fractions/Division-Proper-Fraction', endpoint='', handler='Learn.P5FRDivisionFractions'),
         Rule('/Learn/Primary5/Fractions/Fraction-as-Division', endpoint='', handler='Learn.P5FRFractionDivision'),
         Rule('/Learn/Primary5/Fractions/Fractions-Decimals', endpoint='', handler='Learn.P5FRFractionDecimal'),
         Rule('/Learn/Primary5/Decimal/Multiply-by-10-100-1000', endpoint='', handler='Learn.P5DCMultiply'),
         Rule('/Learn/Primary5/Decimal/Divide-by-10-100-1000', endpoint='', handler='Learn.P5DCDivide'),
         Rule('/Learn/Primary5/Decimal/Rounding-Off-Decimal-Numbers', endpoint='', handler='Learn.P5DCRounding'),
         Rule('/Learn/Primary5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers', endpoint='', handler='Learn.P5DCEstimation'),
         Rule('/Learn/Primary5/Percentage/Introduction', endpoint='', handler='Learn.P5PRIntroduction'),
         Rule('/Learn/Primary5/Percentage/Percentage-and-Fractions', endpoint='', handler='Learn.P5PRFractions'),
         Rule('/Learn/Primary5/Percentage/Percentage-and-Decimals', endpoint='', handler='Learn.P5PRDecimals'),
         Rule('/Learn/Primary5/Ratio/Introduction', endpoint='', handler='Learn.P5RTIntroduction'),
         Rule('/Learn/Primary5/Ratio/Equivalent', endpoint='', handler='Learn.P5RTEquivalent'),
         Rule('/Learn/Primary5/Ratio/Simplifying', endpoint='', handler='Learn.P5RTSimplifying'),
         Rule('/Learn/Primary5/Measurement/Triangle-Base-Height', endpoint='', handler='Learn.P5MTTriangleBH'),
         Rule('/Learn/Primary5/Measurement/Area-of-Triangle', endpoint='', handler='Learn.P5MTTriangleArea'),
         Rule('/Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-1', endpoint='', handler='Learn.P5MTVolume1'),
         Rule('/Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-2', endpoint='', handler='Learn.P5MTVolume2'),
         Rule('/Learn/Primary5/Measurement/Introduction-to-volume-of-cube-cuboid-part-3', endpoint='', handler='Learn.P5MTVolume3'),
         Rule('/Learn/Primary5/Data-Analysis/Finding-Average', endpoint='', handler='Learn.P5DAAverage'),
         Rule('/Learn/Primary5/Geometry/What-is-an-angle', endpoint='', handler='Learn.P5GeometryWhatIsAngle'),
         Rule('/Learn/Primary5/Geometry/Finding-unknown-angles', endpoint='', handler='Learn.P5GeometryAngles'),
         Rule('/Learn/Primary5/Geometry/Types-of-triangles', endpoint='', handler='Learn.P5GeometryTriangles'),
         Rule('/Learn/Primary5/Geometry/Angle-sum-of-triangle', endpoint='', handler='Learn.P5GeometryAngleSum'),
         Rule('/Learn/Primary5/Geometry/Triangle-Finding-unknown-angles', endpoint='', handler='Learn.P5GeometryTriangleAngle'),
         Rule('/Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-1', endpoint='', handler='Learn.P5GeometryDrawingTriangles1'),
         Rule('/Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-2', endpoint='', handler='Learn.P5GeometryDrawingTriangles2'),
         Rule('/Learn/Primary5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-3', endpoint='', handler='Learn.P5GeometryDrawingTriangles3'),
         Rule('/Learn/Primary5/Geometry/Four-sided-figures-types-and-properties', endpoint='', handler='Learn.P5GeometryFourSided'),
         Rule('/Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-1', endpoint='', handler='Learn.P5GeometryFourSidedAngles1'),
         Rule('/Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-2', endpoint='', handler='Learn.P5GeometryFourSidedAngles2'),
         Rule('/Learn/Primary5/Geometry/Four-sided-figures-finding-unknown-angles-part-3', endpoint='', handler='Learn.P5GeometryFourSidedAngles3'),
         Rule('/Learn/Primary5/Geometry/Drawing-a-parallelogram', endpoint='', handler='Learn.P5GeometryFourSidedFigures1'),
         Rule('/Learn/Primary5/Geometry/Drawing-a-rhombus', endpoint='', handler='Learn.P5GeometryFourSidedFigures2'),
         Rule('/Learn/Primary5/Geometry/Drawing-a-trapezium', endpoint='', handler='Learn.P5GeometryFourSidedFigures3'),
         Rule('/Learn/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction', endpoint='', handler='Learn.P6WholeNumberProperFraction'),
         Rule('/Learn/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction', endpoint='', handler='Learn.P6ProperFractionProperFraction'),
         Rule('/Learn/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions', endpoint='', handler='Learn.P6AlgebraWhatIsAlgebra'),
         Rule('/Learn/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions', endpoint='', handler='Learn.P6AlgebraSimplifying'),
         Rule('/Learn/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage', endpoint='', handler='Learn.P6PRFindWhole'),
         Rule('/Learn/Primary6/Percentage/Finding-Percentage-Increase-Decrease', endpoint='', handler='Learn.P6PRIncDec'),
         Rule('/Learn/Primary6/Percentage/Advanced-Word-Problems', endpoint='', handler='Learn.P6PercentageWordProblems'),
         Rule('/Learn/Primary6/Speed/Distance-Time-Speed', endpoint='', handler='Learn.P6SpeedDistanceTime'),  
         Rule('/Learn/Primary6/Speed/Average-Speed', endpoint='', handler='Learn.P6SpeedAverage'),
         Rule('/Learn/Primary6/Speed/Advanced-Word-Problems', endpoint='', handler='Learn.P6SpeedAdvancedWordProblems'),
         Rule('/Learn/Primary6/Data-Analysis/Pie-Chart', endpoint='', handler='Learn.P6DataAnalysisPieChart'),
         Rule('/Learn/Primary6/Data-Analysis/Pie-Chart-Word-Problems', endpoint='', handler='Learn.P6DataAnalysisPieChartWordProblems'),
         Rule('/Learn/Primary2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12', endpoint='', handler='Learn.P2TimesTable'),
         Rule('/Learn/Primary6/Ratio/Word-Problems', endpoint='', handler='Learn.P6RatioWordProblems'),
         Rule('/Learn/Primary6/Ratio/Ratio-and-Fraction', endpoint='', handler='Learn.P6RatioFraction'),
         Rule('/Learn/Primary6/Ratio/Equivalent-Fraction-and-Ratio', endpoint='', handler='Learn.P6RatioEquivalentFraction'),
         Rule('/Learn/Primary6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems', endpoint='', handler='Learn.P6MeasurementWordProblems'),
         # this have to be removed after few days as in the April Newsletter this link has been sent by mistake
         Rule('/Learn/Primary5/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems', endpoint='', handler='Learn.P6MeasurementWordProblems'),
         Rule('/Learn/Primary6/Measurement/Radius-and-Diameter-of-Circle', endpoint='', handler='Learn.P6MeasurementRadiusDiameter'),
         Rule('/Learn/Primary6/Measurement/Circumference-of-Circle', endpoint='', handler='Learn.P6MeasurementCircleCircumference'),
         Rule('/Learn/Primary6/Measurement/Area-of-Circle', endpoint='', handler='Learn.P6MeasurementCircleArea'),
         Rule('/Learn/Primary6/Area-and-Perimeter-of-Composite-Figures', endpoint='', handler='Learn.P6MeasurementComposite'),
         Rule('/Learn/Primary6/Geometry/Finding-Unknown-Angles-Advanced-Problems', endpoint='', handler='Learn.P6GeometryAdvancedProblems'),
         Rule('/Learn/Primary4/Data-Analysis/Tables-and-Bar-Graphs', endpoint='', handler='Learn.P4DataAnalysisTablesBar'),
         Rule('/Learn/Primary4/Data-Analysis/Line-Graphs', endpoint='', handler='Learn.P4DataAnalysisLineGraphs'),
         Rule('/Learn/Primary4/Geometry/Perpendicular-and-Parallel-Lines', endpoint='', handler='Learn.P4GeometryParallelPerpendicular'),
         Rule('/Learn/Primary4/Geometry/Understanding-Angles', endpoint='', handler='Learn.P4GeometryUnderstandingAngles'),
         Rule('/Learn/Primary4/Geometry/What-is-an-angle-how-to-measure-it', endpoint='', handler='Learn.P4GeometryWhatisanAngle'),
         Rule('/Learn/Primary4/Geometry/Drawing-Angles', endpoint='', handler='Learn.P4GeometryDrawingAngles'),
         Rule('/Learn/Primary4/Geometry/Angles-Turns-and-Directions', endpoint='', handler='Learn.P4GeometryAnglesTurnsDirections'),
         Rule('/Learn/Primary4/Geometry/Quadrilaterals-Rectangles-and-Squares', endpoint='', handler='Learn.P4GeometryQuadrilateral'),
         Rule('/Learn/Primary4/Geometry/Symmetric-Figures-Shapes-and-Patterns', endpoint='', handler='Learn.P4GeometrySymmetry'),
         Rule('/Learn/Primary4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares', endpoint='', handler='Learn.P4MeasurementRectangleSquare'),
         Rule('/Learn/Primary4/Measurement/Time-Seconds-24-Hour-Clock-Duration', endpoint='', handler='Learn.P4MeasurementTime'),
         Rule('/Learn/Primary4/Whole-Numbers/Word-Problems', endpoint='', handler='Learn.P4WNWordProblems'),
         Rule('/Learn/Primary4/Whole-Numbers/Factors-Multiples', endpoint='', handler='Learn.P4WNFactorsMultiples'),
         Rule('/Learn/Primary4/Whole-Numbers/Numbers-Up-to-100000', endpoint='', handler='Learn.P4WNUpto100000'),
         Rule('/Learn/Primary4/Whole-Numbers/Multiplication-Division-by-1-and-2-Digit-Numbers', endpoint='', handler='Learn.P4WNMultiplyDivide'),
         Rule('/Learn/Primary4/Decimal/Understanding-Tenths-Hundredths-Thousandths', endpoint='', handler='Learn.P4Decimal10s100s1000s'),
         Rule('/Learn/Primary4/Decimal/Decimals-Addition', endpoint='', handler='Learn.P4DecimalAddition'),
         Rule('/Learn/Primary4/Decimal/Decimals-Subtraction', endpoint='', handler='Learn.P4DecimalSubtraction'),
         Rule('/Learn/Primary4/Decimal/Decimals-Multiplication', endpoint='', handler='Learn.P4DecimalMultiplication'),
         Rule('/Learn/Primary4/Decimal/Decimals-Division', endpoint='', handler='Learn.P4DecimalDivision'),
         Rule('/Learn/Primary4/Decimal/Word-Problems', endpoint='', handler='Learn.P4DecimalWordProblems'),
         Rule('/Learn/Primary4/Fractions/Fractions-Word-Problems-Grade-4', endpoint='', handler='Learn.P4FractionsWordProblems'),

         Rule('/Learn/Primary-Grade-5/WholeNumbers/Figures-to-Words', endpoint='', handler='Learn.P5WNFiguresToWords'),
         Rule('/Learn/Primary-Grade-5/WholeNumbers/Words-to-Figures', endpoint='', handler='Learn.P5WNWordsToFigures'),
         Rule('/Learn/Primary-Grade-5/WholeNumbers/Place-Values', endpoint='', handler='Learn.P5WNPlaceValue'),
         Rule('/Learn/Primary-Grade-5/WholeNumbers/Comparison-Ordering-Pattern', endpoint='', handler='Learn.P5WNComparisonOrdering'),
         Rule('/Learn/Primary-Grade-5/WholeNumbers/Approximation-Estimation-Part-1', endpoint='', handler='Learn.P5WNApproximationEstimation1'),
         Rule('/Learn/Primary-Grade-5/WholeNumbers/Approximation-Estimation-Part-2', endpoint='', handler='Learn.P5WNApproximationEstimation1'),
         Rule('/Learn/Primary-Grade-5/WholeNumbers/Multiply-by-10-100-1000', endpoint='', handler='Learn.P5WNMultiply'),
         Rule('/Learn/Primary-Grade-5/WholeNumbers/Divide-by-10-100-1000', endpoint='', handler='Learn.P5WNDivide'),
         Rule('/Learn/Primary-Grade-5/WholeNumbers/Order-of-Operations', endpoint='', handler='Learn.P5WNOperations'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems-Solving-Model-Method', endpoint='', handler='Learn.P5WNWordProblems'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems1', endpoint='', handler='Learn.P5WNWordProblems1'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems2', endpoint='', handler='Learn.P5WNWordProblems2'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems3', endpoint='', handler='Learn.P5WNWordProblems3'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems4', endpoint='', handler='Learn.P5WNWordProblems4'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems5', endpoint='', handler='Learn.P5WNWordProblems5'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems6', endpoint='', handler='Learn.P5WNWordProblems6'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems7', endpoint='', handler='Learn.P5WNWordProblems7'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems8', endpoint='', handler='Learn.P5WNWordProblems8'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems9', endpoint='', handler='Learn.P5WNWordProblems9'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems10', endpoint='', handler='Learn.P5WNWordProblems10'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems11', endpoint='', handler='Learn.P5WNWordProblems11'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems12', endpoint='', handler='Learn.P5WNWordProblems12'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems13', endpoint='', handler='Learn.P5WNWordProblems13'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems14', endpoint='', handler='Learn.P5WNWordProblems14'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems15', endpoint='', handler='Learn.P5WNWordProblems15'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems16', endpoint='', handler='Learn.P5WNWordProblems16'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems17', endpoint='', handler='Learn.P5WNWordProblems17'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems18', endpoint='', handler='Learn.P5WNWordProblems18'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems19', endpoint='', handler='Learn.P5WNWordProblems19'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems20', endpoint='', handler='Learn.P5WNWordProblems20'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems21', endpoint='', handler='Learn.P5WNWordProblems21'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems22', endpoint='', handler='Learn.P5WNWordProblems22'),
         Rule('/Learn/Primary-Grade-5/Whole-Numbers/Word-Problems23', endpoint='', handler='Learn.P5WNWordProblems23'),
         Rule('/Learn/Primary-Grade-5/Fractions/What-Is-a-Fraction', endpoint='', handler='Learn.P5FRWhatIsFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Types-of-Fractions', endpoint='', handler='Learn.P5FRTypesFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Improper-Mixed-Fractions', endpoint='', handler='Learn.P5FRImproperMixedFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Simplifying-Fractions-GCF', endpoint='', handler='Learn.P5FRSimplifyingFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Unlike-Fractions-LCM-Part-1', endpoint='', handler='Learn.P5FRUnlikeFractions1'),
         Rule('/Learn/Primary-Grade-5/Fractions/Unlike-Fractions-LCM-Part-2', endpoint='', handler='Learn.P5FRUnlikeFractions2'),
         Rule('/Learn/Primary-Grade-5/Fractions/Addition-Proper-Fractions', endpoint='', handler='Learn.P5FRAddProperFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Subtraction-Proper-Fractions', endpoint='', handler='Learn.P5FRSubProperFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Addition-Mixed-Fractions', endpoint='', handler='Learn.P5FRAddMixedFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Subtraction-Mixed-Fractions', endpoint='', handler='Learn.P5FRSubMixedFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Multiplication-Fractions', endpoint='', handler='Learn.P5FRMultFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Multiplication-Mixed-Fractions', endpoint='', handler='Learn.P5FRMultMixedFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Division-Proper-Fraction', endpoint='', handler='Learn.P5FRDivisionFractions'),
         Rule('/Learn/Primary-Grade-5/Fractions/Fraction-as-Division', endpoint='', handler='Learn.P5FRFractionDivision'),
         Rule('/Learn/Primary-Grade-5/Fractions/Fractions-Decimals', endpoint='', handler='Learn.P5FRFractionDecimal'),
         Rule('/Learn/Primary-Grade-5/Decimal/Multiply-by-10-100-1000', endpoint='', handler='Learn.P5DCMultiply'),
         Rule('/Learn/Primary-Grade-5/Decimal/Divide-by-10-100-1000', endpoint='', handler='Learn.P5DCDivide'),
         Rule('/Learn/Primary-Grade-5/Decimal/Rounding-Off-Decimal-Numbers', endpoint='', handler='Learn.P5DCRounding'),
         Rule('/Learn/Primary-Grade-5/Decimal/Estimation-in-Calculations-with-Decimal-Numbers', endpoint='', handler='Learn.P5DCEstimation'),
         Rule('/Learn/Primary-Grade-5/Percentage/Introduction', endpoint='', handler='Learn.P5PRIntroduction'),
         Rule('/Learn/Primary-Grade-5/Percentage/Percentage-and-Fractions', endpoint='', handler='Learn.P5PRFractions'),
         Rule('/Learn/Primary-Grade-5/Percentage/Percentage-and-Decimals', endpoint='', handler='Learn.P5PRDecimals'),
         Rule('/Learn/Primary-Grade-5/Ratio/Introduction', endpoint='', handler='Learn.P5RTIntroduction'),
         Rule('/Learn/Primary-Grade-5/Ratio/Equivalent', endpoint='', handler='Learn.P5RTEquivalent'),
         Rule('/Learn/Primary-Grade-5/Ratio/Simplifying', endpoint='', handler='Learn.P5RTSimplifying'),
         Rule('/Learn/Primary-Grade-5/Measurement/Triangle-Base-Height', endpoint='', handler='Learn.P5MTTriangleBH'),
         Rule('/Learn/Primary-Grade-5/Measurement/Area-of-Triangle', endpoint='', handler='Learn.P5MTTriangleArea'),
         Rule('/Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-1', endpoint='', handler='Learn.P5MTVolume1'),
         Rule('/Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-2', endpoint='', handler='Learn.P5MTVolume2'),
         Rule('/Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-3', endpoint='', handler='Learn.P5MTVolume3'),
         Rule('/Learn/Primary-Grade-5/Data-Analysis/Finding-Average', endpoint='', handler='Learn.P5DAAverage'),
         Rule('/Learn/Primary-Grade-5/Geometry/What-is-an-angle', endpoint='', handler='Learn.P5GeometryWhatIsAngle'),
         Rule('/Learn/Primary-Grade-5/Geometry/Finding-unknown-angles', endpoint='', handler='Learn.P5GeometryAngles'),
         Rule('/Learn/Primary-Grade-5/Geometry/Types-of-triangles', endpoint='', handler='Learn.P5GeometryTriangles'),
         Rule('/Learn/Primary-Grade-5/Geometry/Angle-sum-of-triangle', endpoint='', handler='Learn.P5GeometryAngleSum'),
         Rule('/Learn/Primary-Grade-5/Geometry/Triangle-Finding-unknown-angles', endpoint='', handler='Learn.P5GeometryTriangleAngle'),
         Rule('/Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-1', endpoint='', handler='Learn.P5GeometryDrawingTriangles1'),
         Rule('/Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-2', endpoint='', handler='Learn.P5GeometryDrawingTriangles2'),
         Rule('/Learn/Primary-Grade-5/Geometry/Drawing-Triangles-Using-geometrical-instruments-part-3', endpoint='', handler='Learn.P5GeometryDrawingTriangles3'),
         Rule('/Learn/Primary-Grade-5/Geometry/Four-sided-figures-types-and-properties', endpoint='', handler='Learn.P5GeometryFourSided'),
         Rule('/Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-1', endpoint='', handler='Learn.P5GeometryFourSidedAngles1'),
         Rule('/Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-2', endpoint='', handler='Learn.P5GeometryFourSidedAngles2'),
         Rule('/Learn/Primary-Grade-5/Geometry/Four-sided-figures-finding-unknown-angles-part-3', endpoint='', handler='Learn.P5GeometryFourSidedAngles3'),
         Rule('/Learn/Primary-Grade-5/Geometry/Drawing-a-parallelogram', endpoint='', handler='Learn.P5GeometryFourSidedFigures1'),
         Rule('/Learn/Primary-Grade-5/Geometry/Drawing-a-rhombus', endpoint='', handler='Learn.P5GeometryFourSidedFigures2'),
         Rule('/Learn/Primary-Grade-5/Geometry/Drawing-a-trapezium', endpoint='', handler='Learn.P5GeometryFourSidedFigures3'),
         Rule('/Learn/Primary-Grade-6/Fractions/Dividing-Whole-Number-by-Proper-Fraction', endpoint='', handler='Learn.P6WholeNumberProperFraction'),
         Rule('/Learn/Primary-Grade-6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction', endpoint='', handler='Learn.P6ProperFractionProperFraction'),
         Rule('/Learn/Primary-Grade-6/Algebra/What-is-Algebra-and-Algebraic-Expressions', endpoint='', handler='Learn.P6AlgebraWhatIsAlgebra'),
         Rule('/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions', endpoint='', handler='Learn.P6AlgebraSimplifying'),
         Rule('/Learn/Primary-Grade-6/Percentage/Finding-Whole-Given-Part-and-Percentage', endpoint='', handler='Learn.P6PRFindWhole'),
         Rule('/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease', endpoint='', handler='Learn.P6PRIncDec'),
         Rule('/Learn/Primary-Grade-6/Percentage/Advanced-Word-Problems', endpoint='', handler='Learn.P6PercentageWordProblems'),
         Rule('/Learn/Primary-Grade-6/Speed/Distance-Time-Speed', endpoint='', handler='Learn.P6SpeedDistanceTime'),  
         Rule('/Learn/Primary-Grade-6/Speed/Average-Speed', endpoint='', handler='Learn.P6SpeedAverage'),
         Rule('/Learn/Primary-Grade-6/Speed/Advanced-Word-Problems', endpoint='', handler='Learn.P6SpeedAdvancedWordProblems'),
         Rule('/Learn/Primary-Grade-6/Data-Analysis/Pie-Chart', endpoint='', handler='Learn.P6DataAnalysisPieChart'),
         Rule('/Learn/Primary-Grade-6/Data-Analysis/Pie-Chart-Word-Problems', endpoint='', handler='Learn.P6DataAnalysisPieChartWordProblems'),
         Rule('/Learn/Primary-Grade-2/WholeNumbers/Tips-To-Remember-(Multiplication)Times-Table-Of-2-To-12', endpoint='', handler='Learn.P2TimesTable'),
         Rule('/Learn/Primary-Grade-6/Ratio/Word-Problems', endpoint='', handler='Learn.P6RatioWordProblems'),
         Rule('/Learn/Primary-Grade-6/Ratio/Ratio-and-Fraction', endpoint='', handler='Learn.P6RatioFraction'),
         Rule('/Learn/Primary-Grade-6/Ratio/Equivalent-Fraction-and-Ratio', endpoint='', handler='Learn.P6RatioEquivalentFraction'),
         Rule('/Learn/Primary-Grade-6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems', endpoint='', handler='Learn.P6MeasurementWordProblems'),
         Rule('/Learn/Primary-Grade-6/Measurement/Radius-and-Diameter-of-Circle', endpoint='', handler='Learn.P6MeasurementRadiusDiameter'),
         Rule('/Learn/Primary-Grade-6/Measurement/Circumference-of-Circle', endpoint='', handler='Learn.P6MeasurementCircleCircumference'),
         Rule('/Learn/Primary-Grade-6/Measurement/Area-of-Circle', endpoint='', handler='Learn.P6MeasurementCircleArea'),
         Rule('/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures', endpoint='', handler='Learn.P6MeasurementComposite'),
         Rule('/Learn/Primary-Grade-6/Geometry/Finding-Unknown-Angles-Advanced-Problems', endpoint='', handler='Learn.P6GeometryAdvancedProblems'),
         Rule('/Learn/Primary-Grade-4/Data-Analysis/Tables-and-Bar-Graphs', endpoint='', handler='Learn.P4DataAnalysisTablesBar'),
         Rule('/Learn/Primary-Grade-4/Data-Analysis/Line-Graphs', endpoint='', handler='Learn.P4DataAnalysisLineGraphs'),
         Rule('/Learn/Primary-Grade-4/Geometry/Perpendicular-and-Parallel-Lines', endpoint='', handler='Learn.P4GeometryParallelPerpendicular'),
         Rule('/Learn/Primary-Grade-4/Geometry/Understanding-Angles', endpoint='', handler='Learn.P4GeometryUnderstandingAngles'),
         Rule('/Learn/Primary-Grade-4/Geometry/What-is-an-angle-how-to-measure-it', endpoint='', handler='Learn.P4GeometryWhatisanAngle'),
         Rule('/Learn/Primary-Grade-4/Geometry/Drawing-Angles', endpoint='', handler='Learn.P4GeometryDrawingAngles'),
         Rule('/Learn/Primary-Grade-4/Geometry/Angles-Turns-and-Directions', endpoint='', handler='Learn.P4GeometryAnglesTurnsDirections'),
         Rule('/Learn/Primary-Grade-4/Geometry/Quadrilaterals-Rectangles-and-Squares', endpoint='', handler='Learn.P4GeometryQuadrilateral'),
         Rule('/Learn/Primary-Grade-4/Geometry/Symmetric-Figures-Shapes-and-Patterns', endpoint='', handler='Learn.P4GeometrySymmetry'),
         Rule('/Learn/Primary-Grade-4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares', endpoint='', handler='Learn.P4MeasurementRectangleSquare'),
         Rule('/Learn/Primary-Grade-4/Measurement/Time-Seconds-24-Hour-Clock-Duration', endpoint='', handler='Learn.P4MeasurementTime'),
         Rule('/Learn/Primary-Grade-4/Whole-Numbers/Word-Problems', endpoint='', handler='Learn.P4WNWordProblems'),
         Rule('/Learn/Primary-Grade-4/Whole-Numbers/Factors-Multiples', endpoint='', handler='Learn.P4WNFactorsMultiples'),
         Rule('/Learn/Primary-Grade-4/Whole-Numbers/Numbers-Up-to-100000', endpoint='', handler='Learn.P4WNUpto100000'),
         Rule('/Learn/Primary-Grade-4/Whole-Numbers/Multiplication-Division-by-1-and-2-Digit-Numbers', endpoint='', handler='Learn.P4WNMultiplyDivide'),
         Rule('/Learn/Primary-Grade-4/Decimal/Understanding-Tenths-Hundredths-Thousandths', endpoint='', handler='Learn.P4Decimal10s100s1000s'),
         Rule('/Learn/Primary-Grade-4/Decimal/Decimals-Addition', endpoint='', handler='Learn.P4DecimalAddition'),
         Rule('/Learn/Primary-Grade-4/Decimal/Decimals-Subtraction', endpoint='', handler='Learn.P4DecimalSubtraction'),
         Rule('/Learn/Primary-Grade-4/Decimal/Decimals-Multiplication', endpoint='', handler='Learn.P4DecimalMultiplication'),
         Rule('/Learn/Primary-Grade-4/Decimal/Decimals-Division', endpoint='', handler='Learn.P4DecimalDivision'),
         Rule('/Learn/Primary-Grade-4/Decimal/Word-Problems', endpoint='', handler='Learn.P4DecimalWordProblems'),
         Rule('/Learn/Primary-Grade-4/Fractions/Fractions-Word-Problems-Grade-4', endpoint='', handler='Learn.P4FractionsWordProblems'),
         Rule('/Learn/Primary-Grade-4/Fractions/Fraction-of-a-Set', endpoint='', handler='Learn.P4FractionsOfSet'),
         Rule('/Learn/Primary-Grade-4/Types-of-Fractions', endpoint='', handler='Learn.P5FRTypesFractions'),
         Rule('/Learn/Primary-Grade-4/Fractions/Simplifying-Fractions-GCF', endpoint='', handler='Learn.P5FRSimplifyingFractions'),
         Rule('/Learn/Primary-Grade-4/Fractions/Mixed-Numbers-Improper-Fractions', endpoint='', handler='Learn.P5FRImproperMixedFractions'),
         Rule('/Learn/Primary-Grade-4/Fractions/Addition-Proper-Fractions', endpoint='', handler='Learn.P5FRAddProperFractions'),
         Rule('/Learn/Primary-Grade-4/Fractions/Subtraction-Proper-Fractions', endpoint='', handler='Learn.P5FRSubProperFractions'),   
        
         #Primary 3 notes
         
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/Number-Notations-Place-Values-Up-to-10000', endpoint='', handler='Learn.P3WNUpto10000'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Figures-to-Words-Up-to-10000', endpoint='', handler='Learn.P3WNFiguresToWordsUpto10000'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Words-to-Figures-Up-to-10000', endpoint='', handler='Learn.P3WNWordsToFiguresUpto10000'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/Number-Patterns', endpoint='', handler='Learn.P3WNNumberPatterns'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/Comparing-Ordering', endpoint='', handler='Learn.P3WNComparingOrdering'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/Addition', endpoint='', handler='Learn.P3WNAddition'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/Subtraction', endpoint='', handler='Learn.P3WNSubtraction'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/Multiplication-Tables-of-6-7-8-9', endpoint='', handler='Learn.P3WNTimesTables6789'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers/2-Step-Word-Problems', endpoint='', handler='Learn.P3WNWordProblems'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers-Multiplication', endpoint='', handler='Learn.P3WNMultiplication'),
         #Rule('/Learn/Primary-Grade-3/Whole-Numbers-Division', endpoint='', handler='Learn.P3WNDivision'),
         
         
         Rule( r'/Learn/Primary-Grade-3/<topic>/<subtopic>', handler="Learn.Primary3Handler1"),
         Rule( r'/Learn/Primary-Grade-3/<subtopic>', handler="Learn.Primary3Handler2"),
         
         Rule('/Learn/Primary-Grade-3/Fractions/What-Is-a-Fraction', endpoint='', handler='Learn.P5FRWhatIsFractions'),
         Rule('/Learn/Primary-Grade-3/Money-Word-Problems', endpoint='', handler='Learn.P3MOWordProblems'),
         Rule('/Learn/Primary-Grade-3/Addition-of-Money', endpoint='', handler='Learn.P3MOAddition'),
         Rule('/Learn/Primary-Grade-3/Subtraction-of-Money', endpoint='', handler='Learn.P3MOSubtraction'),
         Rule('/Learn/Primary-Grade-3/Telling-Time', endpoint='', handler='Learn.P3TITellingTime'),
         Rule('/Learn/Primary-Grade-3/Time-Conversion-Hours-Minutes', endpoint='', handler='Learn.P3TITimeConversion'),
         Rule('/Learn/Primary-Grade-3/Time-Addition', endpoint='', handler='Learn.P3TITimeAddition'),
         Rule('/Learn/Primary-Grade-3/Time-Subtraction', endpoint='', handler='Learn.P3TITimeSubtraction'),
         Rule('/Learn/Primary-Grade-3/Time-Finding-Duration-Start-Finish', endpoint='', handler='Learn.P3TITimeDuration'),
         Rule('/Learn/Primary-Grade-3/Time-Problem-Sums', endpoint='', handler='Learn.P3TITimeWordProblems'),
         Rule('/Learn/Primary-Grade-3/Metres-Centimetres', endpoint='', handler='Learn.P3LMVMetresCentimetres'),
         Rule('/Learn/Primary-Grade-3/KiloMetres-Metres', endpoint='', handler='Learn.P3LMVKiloMetresMetres'),
         Rule('/Learn/Primary-Grade-3/Kilograms-Grams', endpoint='', handler='Learn.P3LMVKilogramsGrams'),
         Rule('/Learn/Primary-Grade-3/Litres-Millilitres', endpoint='', handler='Learn.P3LMVLitresMillilitres'),
         Rule('/Learn/Primary-Grade-3/Length-Mass-Volume-1-Step-Story-Sums', endpoint='', handler='Learn.P3LMV1StepWordProblems'),
         Rule('/Learn/Primary-Grade-3/Length-Mass-Volume-2-Step-Story-Sums', endpoint='', handler='Learn.P3LMV2StepWordProblems'),
         Rule('/Learn/Primary-Grade-3/Equivalent-Fractions', endpoint='', handler='Learn.P3FREquivalentFractions'),
         Rule('/Learn/Primary-Grade-3/Simplifying-Fractions', endpoint='', handler='Learn.P3FRSimplifyingFractions'),
         Rule('/Learn/Primary-Grade-3/Comparing-and-Ordering-Fractions', endpoint='', handler='Learn.P3FRComparingOrderingFractions'),
         Rule('/Learn/Primary-Grade-3/Adding-Fractions', endpoint='', handler='Learn.P3FRAddingFractions'),
         Rule('/Learn/Primary-Grade-3/Subtracting-Fractions', endpoint='', handler='Learn.P3FRSubtractingFractions'),
         Rule('/Learn/Primary-Grade-3/Area-in-Square-Units', endpoint='', handler='Learn.P3APSquareUnits'),
         Rule('/Learn/Primary-Grade-3/Area-in-Square-Centimetres-Square-Metres', endpoint='', handler='Learn.P3APSquareCmM'),
         Rule('/Learn/Primary-Grade-3/Area-of-Squares-and-Rectangles', endpoint='', handler='Learn.P3APArea'),
         Rule('/Learn/Primary-Grade-3/Perimeter-of-Squares-and-Rectangles', endpoint='', handler='Learn.P3APPerimeter'),
         Rule('/Learn/Primary-Grade-3/Area-Perimeter-Problem-Sums', endpoint='', handler='Learn.P3APWordProblems'),
         Rule('/Learn/Primary-Grade-3/Identifying-Angles-in-Figures', endpoint='', handler='Learn.P3ANIdentifying'),
         Rule('/Learn/Primary-Grade-3/Right-Angles', endpoint='', handler='Learn.P3ANRightAngles'),
         Rule('/Learn/Primary-Grade-3/Bar-Graphs', endpoint='', handler='Learn.P3BGBarGraphs'),
         Rule('/Learn/Primary-Grade-3/Identifying-Perpendicular-Parallel-Lines', endpoint='', handler='Learn.P3PPPerpendicularParallel'),
         Rule('/Learn/Calculator-Perimeter-Area-Rectangle-Square', endpoint='', handler='Learn.CalculatorAPRS'),
         Rule('/Learn/Times-Tables/Free-Printable-Chart-From-2-to-15', endpoint='', handler='Learn.TimesChart2To15'),
         Rule('/Learn/Times-Tables/Free-Printable-Chart-From-16-to-30', endpoint='', handler='Learn.TimesChart16To30'),
         Rule('/Learn/Calculator-Times-Table-Multiplication-Chart-2-to-100', endpoint='', handler='Learn.CalculatorTimesTable'),
         Rule('/Learn/Calculator-Radius-of-Circle-Given-Diameter-Circumference-Area', endpoint='', handler='Learn.CalculatorRadius'),
         Rule('/Learn/Calculator-Diameter-of-Circle-Elementary-Grade-Math', endpoint='', handler='Learn.CalculatorDiameter'),
         Rule('/Learn/Calculator-Circumference-of-Circle-Grade-6-Elementary-Math', endpoint='', handler='Learn.CalculatorCircumference'),
         Rule('/Learn/Calculator-Area-of-Circle-Grade-6-Elementary-Math', endpoint='', handler='Learn.CalculatorArea'),
         Rule('/Math-Calculators', endpoint='', handler='Learn.MathCalculators'),
         Rule('/Learn/Time-Units-Converter', endpoint='', handler='Learn.TimeUnitsConverter'),
         Rule('/Learn/Hours-Unit-Converter', endpoint='', handler='Learn.HoursUnitConverter'),
         Rule('/Learn/Hours-to-Minutes-Converter', endpoint='', handler='Learn.HoursToMinutesConverter'),
         Rule('/Learn/Hours-to-Seconds-Converter', endpoint='', handler='Learn.HoursToSecondsConverter'),
         Rule('/Learn/Hours-to-Milliseconds-Converter', endpoint='', handler='Learn.HoursToMillisecondsConverter'),
         Rule('/Learn/Hours-to-Days-Converter', endpoint='', handler='Learn.HoursToDaysConverter'),
         Rule('/Learn/Hours-to-Weeks-Converter', endpoint='', handler='Learn.HoursToWeeksConverter'),
         Rule('/Learn/Hours-to-Months-Converter', endpoint='', handler='Learn.HoursToMonthsConverter'),
         Rule('/Learn/Hours-to-Years-Converter', endpoint='', handler='Learn.HoursToYearsConverter'),
         Rule('/Learn/Hours-to-Decades-Converter', endpoint='', handler='Learn.HoursToDecadesConverter'),
         Rule('/Learn/Hours-to-Centuries-Converter', endpoint='', handler='Learn.HoursToCenturiesConverter'),
         Rule('/Learn/Hours-to-Millenniums-Converter', endpoint='', handler='Learn.HoursToMillenniumsConverter'),
         Rule('/Learn/Hours-to-Microseconds-Converter', endpoint='', handler='Learn.HoursToMicrosecondsConverter'),
         Rule('/Learn/Hours-to-Nanoseconds-Converter', endpoint='', handler='Learn.HoursToNanosecondsConverter'),
         Rule('/Learn/Hours-to-Picoseconds-Converter', endpoint='', handler='Learn.HoursToPicosecondsConverter'),
         Rule('/Learn/Calculator-Two-Number-Comparison-Greater-Smaller-Equal-To', endpoint='', handler='Learn.CalculatorNumberComparison'),
         Rule('/Learn/Time-Duration-Calculator', endpoint='', handler='Learn.CalculatorTimeDuration'),
         Rule('/Learn/Length-Units-Converter', endpoint='', handler='Learn.LengthUnitsConverter'),
         Rule('/Learn/Meter-Unit-Converter', endpoint='', handler='Learn.MeterUnitConverter'),
         Rule('/Learn/Meter-to-Centimeter-Converter', endpoint='', handler='Learn.MeterToCentimeterConverter'),
         Rule('/Learn/Meter-to-Millimeter-Converter', endpoint='', handler='Learn.MeterToMillimeterConverter'),
         Rule('/Learn/Meter-to-Kilometre-Converter', endpoint='', handler='Learn.MeterToKilometreConverter'),
         Rule('/Learn/Meter-to-Inches-Converter', endpoint='', handler='Learn.MeterToInchesConverter'),
         Rule('/Learn/Meter-to-Feet-Converter', endpoint='', handler='Learn.MeterToFeetConverter'),
         Rule('/Learn/Meter-to-Feet-and-Inches-Conversion', endpoint='', handler='Learn.MeterToFeetInchesConverter'),
         Rule('/Learn/Meter-to-Miles-Conversion', endpoint='', handler='Learn.MeterToMilesConverter'),
         Rule('/Learn/Meter-to-Yards-Conversion', endpoint='', handler='Learn.MeterToYardsConverter'),
         Rule('/Learn/Equivalent-Fractions-Calculator', endpoint='', handler='Learn.EquivalentFractionsCalculator'),
         Rule('/Learn/Simplifying-Fractions-Calculator', endpoint='', handler='Learn.SimplifyingFractionsCalculator'),
         Rule('/Learn/Compare-Fractions-Calculator', endpoint='', handler='Learn.CompareFractionsCalculator'),
         Rule('/Learn/Add-Fractions-Calculator', endpoint='', handler='Learn.AddFractionsCalculator'),
         Rule('/Learn/Subtract-Fractions-Calculator', endpoint='', handler='Learn.SubtractFractionsCalculator'),
         
         Rule('/Math-Worksheets', endpoint='', handler='Learn.MathWorksheets'),
         Rule('/math-worksheets', endpoint='', handler='Learn.MathWorksheets'),
         Rule('/Free-Math-Worksheets/Perimeter-of-Rectangles', endpoint='', handler='Learn.WorksheetsPerimeterRectangles'),
         Rule('/Free-Math-Worksheets/Perimeter-of-Squares', endpoint='', handler='Learn.WorksheetsPerimeterSquares'),
         Rule('/Free-Math-Worksheets/Area-of-Rectangles', endpoint='', handler='Learn.WorksheetsAreaRectangles'),
         Rule('/Free-Math-Worksheets/Area-of-Squares', endpoint='', handler='Learn.WorksheetsAreaSquares'),
         Rule('/Free-Math-Worksheets/Circumference-of-Cirlce', endpoint='', handler='Learn.WorksheetsCircumferenceCircle'),
         Rule('/Free-Math-Worksheets/Circumference-of-Circle', endpoint='', handler='Learn.WorksheetsCircumferenceCircle'),
         Rule('/Free-Math-Worksheets/Diameter-Radius-of-Cirlce', endpoint='', handler='Learn.WorksheetsDiameterRadiusCircle'),
         Rule('/Free-Math-Worksheets/Diameter-Radius-of-Circle', endpoint='', handler='Learn.WorksheetsDiameterRadiusCircle'),
         Rule('/Free-Math-Worksheets/Numbers-Place-Value-Up-To-10000', endpoint='', handler='Learn.WorksheetsNumbersUpTo10000'),
         Rule('/Free-Math-Worksheets/Write-Figures-To-Words-Up-To-10000', endpoint='', handler='Learn.WorksheetsFiguresToWordsUpTo10000'),
         Rule('/Free-Math-Worksheets/Convert-Words-To-Figures-Up-To-10000', endpoint='', handler='Learn.WorksheetsWordsToFiguresUpTo10000'),
         Rule('/Free-Math-Worksheets/Number-Pattern-Worksheets-for-Grade-3', endpoint='', handler='Learn.WorksheetsBasicNumberPatterns'),
         Rule('/Free-Math-Worksheets/Comparing-Ordering-Numbers-Worksheets', endpoint='', handler='Learn.WorksheetsCompareOrder4Digits'),
         Rule('/Free-Math-Worksheets/Addition-of-Four-Digit-Numbers-Up-To-10000', endpoint='', handler='Learn.WorksheetsAdditionUpTo10000'),
         Rule('/Free-Math-Worksheets/Basic-Subtraction-of-Four-Digit-Numbers-Up-To-10000', endpoint='', handler='Learn.WorksheetsSubtractionUpTo10000'),
         Rule('/Free-Math-Worksheets/Multiplication-of-Three-Digit-Numbers', endpoint='', handler='Learn.WorksheetsMultiplication3Digits'),
         Rule('/Free-Math-Worksheets/Long-Division-of-Two-Digit-Numbers-with-Remainders', endpoint='', handler='Learn.WorksheetsDivision2Digits'),
         Rule('/Free-Math-Worksheets/Whole-Numbers-2-Step-Word-Problems-4-Operations', endpoint='', handler='Learn.WorksheetsWholeNumbersWordProblems'),
         Rule('/Free-Math-Worksheets/Adding-Money-With-Cents-Worksheets', endpoint='', handler='Learn.WorksheetsMoneyAddition'),
         Rule('/Free-Math-Worksheets/Money-Subtraction-With-Cents-Worksheets', endpoint='', handler='Learn.WorksheetsMoneySubtraction'),
         Rule('/Free-Math-Worksheets/Money-Word-Problems-Singapore-Math-Worksheets', endpoint='', handler='Learn.WorksheetsMoneyWordProblems'),
         Rule('/Free-Math-Worksheets/Reading-and-Telling-Time-Worksheets', endpoint='', handler='Learn.WorksheetsTellingTime'),
         Rule('/Free-Math-Worksheets/Hours-to-Minutes-Converter-Worksheets', endpoint='', handler='Learn.WorksheetsHoursToMinutes'),
         Rule('/Free-Math-Worksheets/How-to-Add-Hours-and-Minutes-Time-Addition', endpoint='', handler='Learn.WorksheetsTimeAddition'),
         Rule('/Free-Math-Worksheets/How-to-Subtract-Hours-and-Minutes-Time-Subtraction', endpoint='', handler='Learn.WorksheetsTimeSubtraction'),
         Rule('/Free-Math-Worksheets/Calculate-Time-Duration-Start-Finish-Time', endpoint='', handler='Learn.WorksheetsTimeDuration'),
         Rule('/Free-Math-Worksheets/Time-Duration-Singapore-Math-Word-Problems-Story-Sum', endpoint='', handler='Learn.WorksheetsTimeWordProblems'),
         Rule('/free-math-worksheets/how-to-convert-metres-to-centimetres', endpoint='', handler='Learn.WorksheetsConvertMetresCentimetres'),
         Rule('/free-math-worksheets/how-to-convert-kilometers-to-meters', endpoint='', handler='Learn.WorksheetsConvertKilometersMeters'),
         Rule('/free-math-worksheets-1-kilograms-equal-to-1000-grams', endpoint='', handler='Learn.WorksheetsConvertKilogramsGrams'),
         Rule('/free-math-worksheets-how-to-convert-litres-to-millilitres', endpoint='', handler='Learn.WorksheetsConvertLitresMillilitres'),
         Rule('/free-math-worksheets-solve-1-step-word-problems-length-mass-volume', endpoint='', handler='Learn.WorksheetsLMV1StepWP'),
         Rule('/free-math-worksheets-solve-2-step-word-problems-length-mass-volume', endpoint='', handler='Learn.WorksheetsLMV2StepWP'),
         Rule('/free-math-worksheets-what-is-a-fraction', endpoint='', handler='Learn.WorksheetsWhatIsAFraction'),
         Rule('/what-are-equivalent-fractions-free-math-worksheets', endpoint='', handler='Learn.WorksheetsEquivalentFraction'),
         Rule('/how-to-simplify-fractions-free-math-worksheets', endpoint='', handler='Learn.WorksheetsSimplifyingFraction'),
         Rule('/comparing-and-ordering-fractions-free-math-worksheets', endpoint='', handler='Learn.WorksheetsCnOFraction'),
         Rule('/how-to-add-fractions-singapore-math-free-math-worksheets', endpoint='', handler='Learn.WorksheetsAddFractions'),
         Rule('/how-to-subtract-fractions-singapore-math-free-math-worksheets', endpoint='', handler='Learn.WorksheetsSubtractFractions'),
         Rule('/free-math-worksheets-area-in-square-units', endpoint='', handler='Learn.WorksheetsSquareUnits'),
         Rule('/area-in-square-centimeters-meters-free-math-worksheets', endpoint='', handler='Learn.WorksheetsSquareCmM'),
         Rule('/how-to-calculate-area-of-a-square-free-math-worksheets', endpoint='', handler='Learn.WorksheetsAreaSquare'),
         Rule('/identifying-angles-in-a-figure-free-math-worksheets', endpoint='', handler='Learn.WorksheetsIdentifyingAngles'),
         Rule('/what-is-a-right-angle-free-math-worksheets', endpoint='', handler='Learn.WorksheetsRightAngles'),
         Rule('/what-is-a-bar-graph-free-math-worksheets-for-grade-3', endpoint='', handler='Learn.WorksheetsBarGraphs'),
         
         Rule('/What-are-Properties-of-Triangles', endpoint='', handler='Learn.PropertiesTriangle'),
         
         Rule('/Math-Glossary', endpoint='', handler='Learn.MathGlossary'),
         Rule('/Rectangle', endpoint='', handler='Learn.Rectangle'),
         Rule('/Square', endpoint='', handler='Learn.Square'),
         ]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]

    def render_response(self, filename, **kwargs):
        auth_session = None
        if self.auth.session:
            auth_session = self.auth.session
        
        
        TRIAL = "N"
        if self.auth.user:
            HCUser = HCSubscription.HCSubscription.gql("where email = '"+self.auth.user.email+"' and status='ACTIVE'").fetch(1)
            for h in HCUser:
                if h.paypal_token in ["TRIAL","WAIVED"]:
                    TRIAL = "Y"

        UnfinishedWorksheetsCount = 0    
        if self.auth.user and not self.auth.user.IsParent and not self.auth.user.IsTeacher:
            UnfinishedWorksheetData = TestsMaster.TestsMasterTable.gql("where student_id = '"+self.auth.user.username+"'").fetch(10)
            for u in UnfinishedWorksheetData:
                if u.status!='Completed':
                    UnfinishedWorksheetsCount = UnfinishedWorksheetsCount + 1
            if UnfinishedWorksheetsCount > 6:
                UnfinishedWorksheetsCount = "5+"

        kwargs.update({
            'auth_session': auth_session,
            'current_user': self.auth.user,
            'login_url':    self.auth.login_url(),
            'logout_url':   self.auth.logout_url(),
            'current_url':  self.request.url,
            'TRIAL':TRIAL,
            'UnfinishedWorksheetsCount':UnfinishedWorksheetsCount
        })

        return super(BaseHandler, self).render_response(filename, **kwargs)
      

class Primary3Handler1(BaseHandler):
    def get(self, **kwargs):
        from LearnMappings import Grade3Mapper as mapper
        try:
            topic = kwargs['topic']
            subTopic = kwargs['subtopic']
            fn, data = mapper.getMapping(subTopic, topic=topic)
            filename = "Notes/Primary3" + fn
            return self.render_response(filename, **data)
        except KeyError:
            self.abort(404)          

class Primary3Handler2(BaseHandler):
    def get(self, **kwargs):
        from LearnMappings import Grade3Mapper as mapper
        try:
            subTopic = kwargs['subtopic']
            fn, data = mapper.getMapping(subTopic)
            filename = "Notes/Primary3" + fn
            return self.render_response(filename, **data)
        except KeyError:
            self.abort(404)          


      
class LearnPage(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('LearnPage.html', section='content')
      
class P3Notes(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/P3_Notes.html', section='content')
      
class P4Notes(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/P4_Notes.html', section='content')
      
class P5Notes(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/P5_Notes.html', section='content')
      
class P6Notes(BaseHandler):
    def get(self, **kwargs):               
        return self.render_response('Notes/P6_Notes.html', section='content')
    
class P5WNFiguresToWords(BaseHandler):
    def get(self, **kwargs):
        VideoLink={}
        VideoID = "UjANe8EkGcc"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"            
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Write_Words",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Write_Words"})
        return self.render_response('Notes/Primary5/WholeNumbers/Figures-to-Words.html', **VideoLink)    

class P5WNWordsToFigures(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "6d_WhNYOqWM"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Write_Figures",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Write_Figures"})
        return self.render_response('Notes/Primary5/WholeNumbers/Words-to-Figures.html', **VideoLink)

class P5WNPlaceValue(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "f3R3_f_cDWw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"            
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Place_Values",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Place_Values"})
        return self.render_response('Notes/Primary5/WholeNumbers/Place-Value.html', **VideoLink)

class P5WNComparisonOrdering(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "A2h_BtmTi0M"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Comparing_Ordering",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Comparing_Ordering"})
        return self.render_response('Notes/Primary5/WholeNumbers/Comparison-Ordering-Pattern.html', **VideoLink)

class P5WNApproximationEstimation1(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "EyiC6cGjIhg"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Approximation_Estimation",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Approximation_Estimation"})
        return self.render_response('Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-1.html', **VideoLink)

class P5WNApproximationEstimation2(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "zOA1feq5e_M"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Approximation_Estimation",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Approximation_Estimation"})
        return self.render_response('Notes/Primary5/WholeNumbers/Approximation-Estimation-Part-2.html', **VideoLink)

class P5WNMultiply(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "gStP4sr0ASQ"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Multiplication_Division",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Multiplication_Division"})
        return self.render_response('Notes/Primary5/WholeNumbers/Multiply-by-10-100-1000.html', **VideoLink)

class P5WNDivide(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "eA2uhrp2gd0"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Multiplication_Division",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Multiplication_Division"})
        return self.render_response('Notes/Primary5/WholeNumbers/Divide-by-10-100-1000.html', **VideoLink)

class P5WNOperations(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "rh0gNtvyKy8"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Order_Operations",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Order_Operations"})
        return self.render_response('Notes/Primary5/WholeNumbers/Order-of-Operations.html', **VideoLink)

class P5WNWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Whole_Numbers_Word_Problems",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Whole_Numbers_Word_Problems"})
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems.html', **VideoLink)

class P5WNWordProblems1(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "YFCaivv2DgA"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems2(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "8pXRGKpOA4E"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems3(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "kXt8MDLM8Iw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems4(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "HTAX7pfRTZ8"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems5(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "md895QiA5Qw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems6(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "B1fdOXD7W9I"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems7(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "mgbyXs4yDkw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems8(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "aBb5YVWOo5U"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems9(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "uNMdYXnj6es"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems10(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "XNvBwS86uAM"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems11(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "SZSb55KccC4"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems12(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "Jgon2zzLXNw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems13(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "2B6uVbPdbCw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems14(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "N_u3FSaeYqA"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems15(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "UArFG4sEyCQ"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems16(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "nraJqwZ3q1I"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems17(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "9D8JMJ0D-ow"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems18(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "FESW-uqQlN4"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems19(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "Y-7EspSDgjM"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems20(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "AF2pO0co5qw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems21(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "e-bhW5zDJxY"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems22(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "P_TH8KLq9aM"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5WNWordProblems23(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "t0_xee2qMB4"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/WholeNumbers/Word-Problems-Video.html', **VideoLink)

class P5FRWhatIsFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "m9I-ER9j_Ac"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Fractions/What-Is-a-Fraction.html', **VideoLink)

class P5FRTypesFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "PKY8cbq-qoY"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Fractions/Types-of-Fractions.html', **VideoLink)

class P5FRImproperMixedFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "3vzMNQzUrw4"       
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Mixed_Numbers_Improper_Fractions",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Mixed_Numbers_Improper_Fractions"})
        return self.render_response('Notes/Primary5/Fractions/Improper-Mixed-Fractions.html', **VideoLink)

class P5FRSimplifyingFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "Td-o2lZFVHk"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Fractions_Simplifying",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Fractions_Simplifying"})
        return self.render_response('Notes/Primary5/Fractions/Simplifying-Fractions-GCF.html', **VideoLink)

class P5FRUnlikeFractions1(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "nFJ48n5R3Xc"       
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Fractions/Unlike-Fractions-LCM-Part-1.html', **VideoLink)

class P5FRUnlikeFractions2(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "TO9y_9T-5v0"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Fractions/Unlike-Fractions-LCM-Part-2.html', **VideoLink)

class P5FRAddProperFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "j6zai-_TbY8"        
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        #Both P4 & P5 using the same notes so can't give practice and worksheet URL
        '''VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Add_Like_Related_Fractions",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Fractions_Add_Like"})'''
        return self.render_response('Notes/Primary5/Fractions/Addition-Proper-Fractions.html', **VideoLink)

class P5FRSubProperFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "zoXhiHBMpi0"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        #Both P4 & P5 using the same notes so can't give practice and worksheet URL
        '''VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Subtract_Like_Related_Fractions",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Fractions_Subtract_Like"})'''
        return self.render_response('Notes/Primary5/Fractions/Subtraction-Proper-Fractions.html', **VideoLink)

class P5FRAddMixedFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "yChIwpyinuM"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Fractions/Addition-Mixed-Fractions.html', **VideoLink)

class P5FRSubMixedFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "KtCuEoeKzeQ"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Fractions/Subtraction-Mixed-Fractions.html', **VideoLink)

class P5FRMultFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "cbq-WP0mKeE"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Multiply_Proper_Improper_Fractions",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Fractions_Multiply_Proper_Improper"})
        return self.render_response('Notes/Primary5/Fractions/Multiplication-Fractions.html', **VideoLink)

class P5FRMultMixedFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "F6lIOxUDhFQ"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Multiply_Mixed_Fraction_Whole_Number",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Fractions_Multiply_Mixed"})
        return self.render_response('Notes/Primary5/Fractions/Multiplication-Mixed-Fractions.html', **VideoLink)

class P5FRDivisionFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "-YbjGLQ_K6c"       
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Divide_Proper_Fraction_Whole_Number",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Fractions_Divide"})
        return self.render_response('Notes/Primary5/Fractions/Division-Proper-Fraction.html', **VideoLink)

class P5FRFractionDivision(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "bbDRdQGJOLM"       
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Fractions/Fraction-as-Division.html', **VideoLink)

class P5FRFractionDecimal(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "9n2rytBo4Mk"       
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Fractions/Fractions-Decimals.html', **VideoLink)

class P5DCMultiply(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "Y65k3zdtCPg"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Decimals_Multiply_Divide",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Decimals_Multiply_Divide"})
        return self.render_response('Notes/Primary5/Decimal/multiplying-decimal-numbers-by-10s-100s-1000s.html', **VideoLink)

class P5DCDivide(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "wNyqCodFQUE"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Decimals_Multiply_Divide",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Decimals_Multiply_Divide"})
        return self.render_response('Notes/Primary5/Decimal/dividing-decimal-numbers-by-10s-100s-1000s.html', **VideoLink)

class P5DCRounding(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "-03HNiwS-yQ"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Decimals_Rounding_Off",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Decimals_Rounding_Off"})
        return self.render_response('Notes/Primary5/Decimal/rounding-off-decimal-numbers.html', **VideoLink)

class P5DCEstimation(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "CHoz1DyEiEs"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Decimal/estimation-in-calculations-with-decimal-numbers.html', **VideoLink)

class P5PRIntroduction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "x1w0c04c9uo"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Express_as_Percentage",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Percentage_Express_Percentage"})
        return self.render_response('Notes/Primary5/Percentage/introduction-to-percentage.html', **VideoLink)

class P5PRFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "lRYvtHyoDP0"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Express_as_Fraction",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Percentage_Express_Fraction"})
        return self.render_response('Notes/Primary5/Percentage/percentage-and-fraction.html', **VideoLink)

class P5PRDecimals(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "4M4i9iZYsaE"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Express_as_Decimal",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Percentage_Express_Decimal"})
        return self.render_response('Notes/Primary5/Percentage/percentage-and-decimals.html', **VideoLink)

class P5RTIntroduction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "nUAS2PN83LY"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Ratio/introduction-to-ratio.html', **VideoLink)

class P5RTEquivalent(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "0bg2AXuFsWc"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Ratio/equivalent-ratios.html', **VideoLink)

class P5RTSimplifying(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "raxlNU2BqQY"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Ratio/simplifying-ratios.html', **VideoLink)                   

class P5MTTriangleBH(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "yDODrzIg40A"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Measurement/triangle-base-height-measurement.html', **VideoLink)

class P5MTTriangleArea(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "etgKw81UQ50"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Measurement_Area_Triangle",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Measurement_Area_Triangle"})
        return self.render_response('Notes/Primary5/Measurement/finding-area-of-triangle.html', **VideoLink)

class P5MTVolume1(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "jnJbgatKSCQ"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Measurement_Volume_Cube_Cuboid",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Measurement_Volume_Cube_Cuboid"})
        return self.render_response('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-1.html', **VideoLink)

class P5MTVolume2(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "ZupVNUf_g8Y"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Measurement_Volume_Cube_Cuboid",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Measurement_Volume_Cube_Cuboid"})
        return self.render_response('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-2.html', **VideoLink)

class P5MTVolume3(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "kWkKGYWWGqQ"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Measurement_Volume_Cube_Cuboid",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Measurement_Volume_Cube_Cuboid"})
        return self.render_response('Notes/Primary5/Measurement/volume-of-cube-cuboid-part-3.html', **VideoLink)
            
class P5DAAverage(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "veBH8H9dWX4"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Data_Analysis_Find_Average",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Data_Analysis_Find_Average"})
        return self.render_response('Notes/Primary5/DataAnalysis/average.html', **VideoLink)
            
class P5GeometryWhatIsAngle(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "gshd5HjCQzs"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('NotesPage.html', **VideoLink)
            
class P5GeometryAngles(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "TZJ15IDFFwg"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Geometry_Find_Unknown_Angles",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Geometry_Angles"})
        return self.render_response('Notes/Primary5/Geometry/finding-unknown-angles.html', **VideoLink)
            
class P5GeometryTriangles(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "iFyFfdd1ZWE"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/types-of-triangles.html', **VideoLink)
            
class P5GeometryAngleSum(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "EwJ4dUgHOnw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/angle-sum-of-triangles.html', **VideoLink)

class P5GeometryTriangleAngle(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Triangles_Find_Unknown_Angles",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Geometry_Triangles"})
        return self.render_response('Notes/Primary5/Geometry/triangle-finding-unknown-angles.html', **VideoLink)
            
class P5GeometryDrawingTriangles1(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "KkByriIlrkE"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/drawing-triangles-using-geometrical-instruments-part-1.html', **VideoLink)
            
class P5GeometryDrawingTriangles2(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "9HMJnUop2xw"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/drawing-triangles-using-geometrical-instruments-part-2.html', **VideoLink)
            
class P5GeometryDrawingTriangles3(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "yD_Ciioumyk"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/drawing-triangles-using-geometrical-instruments-part-3.html', **VideoLink)

class P5GeometryFourSided(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/four-sided-figures-types-and-properties.html', **VideoLink)
            
class P5GeometryFourSidedAngles1(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "3S1vW58fF4M"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Find_Unknown_Angles_in_Four_Sided_Figures",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Geometry_Four_Sided_Figures"})
        return self.render_response('Notes/Primary5/Geometry/four-sided-figures-finding-unknown-angles-part-1.html', **VideoLink)
            
class P5GeometryFourSidedAngles2(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "wV10R_1U1_k"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Find_Unknown_Angles_in_Four_Sided_Figures",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Geometry_Four_Sided_Figures"})
        return self.render_response('Notes/Primary5/Geometry/four-sided-figures-finding-unknown-angles-part-2.html', **VideoLink)
            
class P5GeometryFourSidedAngles3(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "ok7PsUzWZlU"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_5_Math_Practice/Find_Unknown_Angles_in_Four_Sided_Figures",
                          'worksheet_url':"/Grade_5_Math_Worksheets/Geometry_Four_Sided_Figures"})
        return self.render_response('Notes/Primary5/Geometry/four-sided-figures-finding-unknown-angles-part-3.html', **VideoLink)
            
class P5GeometryFourSidedFigures1(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "FClYkrjtXHY"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/drawing-four-sided-figures-parallelogram.html', **VideoLink)
            
class P5GeometryFourSidedFigures2(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "QQfZMHxtqrc"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/drawing-four-sided-figures-rhombus.html', **VideoLink)
            
class P5GeometryFourSidedFigures3(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "siI2mMlTjnk"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary5/Geometry/drawing-four-sided-figures-trapezium.html', **VideoLink)

class P6WholeNumberProperFraction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Divide_Whole_Number_Proper_Fraction",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Fractions_Divide_Whole_Number"})
        return self.render_response('Notes/Primary6/Fractions/Dividing-Whole-Number-by-Proper-Fraction.html', **VideoLink)

class P6ProperFractionProperFraction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Divide_Proper_Fraction_by_Proper_Fraction",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Fractions_Divide_Proper"})
        return self.render_response('Notes/Primary6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction.html', **VideoLink)

class P6AlgebraWhatIsAlgebra(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions.html', **VideoLink)

class P6AlgebraSimplifying(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Algebra_Evaluate_Expressions",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Algebra_Evaluate_Expressions"})
        return self.render_response('Notes/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions.html', **VideoLink)

class P6PRFindWhole(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Percentage_Find_Whole_Given_Part",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Percentage_Find_Whole_Given_Part"})
        return self.render_response('Notes/Primary6/Percentage/Finding-Whole-Given-Part-and-Percentage.html', **VideoLink)

class P6PRIncDec(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Percentage_Increase_Decrease",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Percentage_Increase_Decrease"})
        return self.render_response('Notes/Primary6/Percentage/Finding-Percentage-Increase-Decrease.html', **VideoLink)

class P6PercentageWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Percentage_Word_Problems",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Percentage_Word_Problems"})
        return self.render_response('Notes/Primary6/Percentage/Percentage-Advanced-Word-Problems.html', **VideoLink)

class P6SpeedDistanceTime(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Speed_Distance_Time",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Speed_Distance_Time"})
        return self.render_response('Notes/Primary6/Speed/Distance-Time-Speed.html', **VideoLink)

class P6SpeedAverage(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary6/Speed/Average-Speed.html', **VideoLink)

class P6SpeedAdvancedWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Speed_Word_Problems",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Speed_Word_Problems"})
        return self.render_response('Notes/Primary6/Speed/Speed-Advanced-Word-Problems.html', **VideoLink)

class P6DataAnalysisPieChart(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "xO2HptuN5Wg"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary6/DataAnalysis/Pie-Charts.html', **VideoLink)

class P6DataAnalysisPieChartWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Data_Analysis_Pie_Chart",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Data_Analysis_Pie_Chart"})
        return self.render_response('Notes/Primary6/DataAnalysis/Pie-Charts-Word-Problems.html', **VideoLink)

class P6RatioWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Ratio_Word_Problems",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Ratio"})
        return self.render_response('Notes/Primary6/Ratio/Ratio-Word-Problems.html', **VideoLink)

class P6RatioFraction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary6/Ratio/Ratio-and-Fraction.html', **VideoLink)    

class P6RatioEquivalentFraction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary6/Ratio/Equivalent-Fraction-and-Ratio.html', **VideoLink)

class P6MeasurementWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Measurement_Volume_Cube_Cuboid",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Measurement_Volume_Cube_Cuboid"})
        return self.render_response('Notes/Primary6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems.html', **VideoLink)    

class P6MeasurementRadiusDiameter(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Measurement_Circle_Radius_Diameter",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Measurement_Circle_Radius_Diameter"})
        return self.render_response('Notes/Primary6/Measurement/Radius-and-Diameter-of-Circle.html', **VideoLink)    

class P6MeasurementCircleCircumference(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Measurement_Circle_Circumference",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Measurement_Circle_Circumference"})
        return self.render_response('Notes/Primary6/Measurement/Circumference-of-Circle.html', **VideoLink)    

class P6MeasurementCircleArea(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Measurement_Circle_Area",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Measurement_Circle_Area"})
        return self.render_response('Notes/Primary6/Measurement/Area-of-Circle.html', **VideoLink)    

class P6MeasurementComposite(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_6_Math_Practice/Area_Perimeter_of_Composite_Figures",
                          'worksheet_url':"/Grade_6_Math_Worksheets/Measurement_Composite_Figures"})
        return self.render_response('Notes/Primary6/Measurement/Area-and-Perimeter-of-Composite-Figures.html', **VideoLink)    

class P6GeometryAdvancedProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary6/Geometry/Finding-Unknown-Angles-Advanced-Problems.html', **VideoLink)

class P4DataAnalysisTablesBar(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Data_Analysis_Tables_Bar_Graphs",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Data_Analysis_Tables_Bar_Graphs"})
        return self.render_response('Notes/Primary4/DataAnalysis/Tables-and-Bar-Graphs.html', **VideoLink)

class P4DataAnalysisLineGraphs(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Data_Analysis_Line_Graphs",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Data_Analysis_Line_Graphs"})
        return self.render_response('Notes/Primary4/DataAnalysis/Line-Graphs.html', **VideoLink)

class P4GeometryParallelPerpendicular(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary4/Geometry/Perpendicular-and-Parallel-Lines.html', **VideoLink)

class P4GeometryUnderstandingAngles(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "gshd5HjCQzs"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary4/Geometry/Understanding-Angles.html', **VideoLink)

class P4GeometryWhatisanAngle(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = "gshd5HjCQzs"
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary4/Geometry/Understanding-Angles.html', **VideoLink)

class P4GeometryDrawingAngles(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary4/Geometry/Drawing-Angles.html', **VideoLink)

class P4GeometryAnglesTurnsDirections(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary4/Geometry/Angles-Turns-and-Directions.html', **VideoLink)

class P4GeometryQuadrilateral(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary4/Geometry/Quadrilaterals-Rectangles-and-Squares.html', **VideoLink)

class P4GeometrySymmetry(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary4/Geometry/Symmetric-Figures-Shapes-and-Patterns.html', **VideoLink)

class P4MeasurementRectangleSquare(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Perimeter_Rectangle_Squares",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Perimeter_Rectangle_Squares"})
        return self.render_response('Notes/Primary4/Measurement/Area-and-Perimeter-of-Rectangles-and-Squares.html', **VideoLink)

class P4MeasurementTime(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Measurement_24-Hour_Clock",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Measurement_24-Hour_Clock"})
        return self.render_response('Notes/Primary4/Measurement/Time-Seconds-24-Hour-Clock-Duration.html', **VideoLink)

class P4WNWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Whole_Numbers_Word_Problems",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Whole_Numbers_Word_Problems"})
        return self.render_response('Notes/Primary4/WholeNumbers/Whole_Numbers_Word_Problems.html', **VideoLink)

class P4WNFactorsMultiples(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Whole_Numbers_Factors_Multiples",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Whole_Numbers_Factors_Multiples"})
        return self.render_response('Notes/Primary4/WholeNumbers/Whole_Numbers_Factors_and_Multiples.html', **VideoLink)

class P4WNUpto100000(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Whole_Numbers_Place_Values",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Whole_Numbers_Place_Values"})
        return self.render_response('Notes/Primary4/WholeNumbers/Whole_Numbers_Upto_100000.html', **VideoLink)

class P4WNMultiplyDivide(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Whole_Numbers_Multiplication_Division",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Whole_Numbers_Multiplication_Division"})
        return self.render_response('Notes/Primary4/WholeNumbers/Whole-Numbers-Multiplication-and-Division-by-1-digit-and-2-digit-Numbers.html', **VideoLink)

class P4Decimal10s100s1000s(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Decimals_Thousandths",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Decimals_Thousandths"})
        return self.render_response('Notes/Primary4/Decimals/Decimals-Understanding-Tenths-Hundredths-Thousandths.html', **VideoLink)

class P4DecimalAddition(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Decimals_Addition_Subtraction",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Decimals_Addition_Subtraction"})
        return self.render_response('Notes/Primary4/Decimals/Decimals-Addition.html', **VideoLink)

class P4DecimalSubtraction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Decimals_Addition_Subtraction",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Decimals_Addition_Subtraction"})
        return self.render_response('Notes/Primary4/Decimals/Decimals-Subtraction.html', **VideoLink)

class P4DecimalMultiplication(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Decimals_Multiplication_Division",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Decimals_Multiplication_Division"})
        return self.render_response('Notes/Primary4/Decimals/Decimals-Multiplication.html', **VideoLink)

class P4DecimalDivision(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Decimals_Multiplication_Division",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Decimals_Multiplication_Division"})
        return self.render_response('Notes/Primary4/Decimals/Decimals-Division.html', **VideoLink)

class P4DecimalWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Decimals_Word_Problems",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Decimals_Word_Problems"})
        return self.render_response('Notes/Primary4/Decimals/Decimals-Word-Problems.html', **VideoLink)

class P4FractionsWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_4_Math_Practice/Fractions_Word_Problems",
                          'worksheet_url':"/Grade_4_Math_Worksheets/Fractions_Word_Problems"})
        return self.render_response('Notes/Primary4/Fractions/Fractions-Word-Problems-Grade-4.html', **VideoLink)

class P4FractionsOfSet(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary4/Fractions/Fraction-of-a-Set.html', **VideoLink)

'''
class P3WNUpto10000(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Number_Notation_Place_Values",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Number_Notation_Place_Values"})
        return self.render_response('Notes/Primary3/WholeNumbers/Whole_Numbers_Upto_10000.html', **VideoLink)

class P3WNFiguresToWordsUpto10000(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Figures_to_Words",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Figures_to_Words"})
        return self.render_response('Notes/Primary3/WholeNumbers/Figures_To_Words_Upto_10000.html', **VideoLink)

class P3WNWordsToFiguresUpto10000(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Words_to_Figures",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Words_to_Figures"})
        return self.render_response('Notes/Primary3/WholeNumbers/Words_To_Figures_Upto_10000.html', **VideoLink)

class P3WNNumberPatterns(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Patterns",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Patterns"})
        return self.render_response('Notes/Primary3/WholeNumbers/Number_Patterns.html', **VideoLink)

class P3WNTimesTables6789(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary3/WholeNumbers/Multiplication_Tables_Of_6_7_8_9.html', **VideoLink)                

class P3WNWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Word_Problems",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Word_Problems"})
        return self.render_response('Notes/Primary3/WholeNumbers/Whole_Numbers_Word_Problems.html', **VideoLink)

class P3WNComparingOrdering(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Comparing_Ordering",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Comparing_Ordering"})
        return self.render_response('Notes/Primary3/WholeNumbers/Comparing_Ordering.html', **VideoLink)

class P3WNAddition(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Addition",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Addition"})
        return self.render_response('Notes/Primary3/WholeNumbers/Addition_Of_Numbers_Within_10000.html', **VideoLink)

class P3WNSubtraction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Subtraction",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Subtraction"})
        return self.render_response('Notes/Primary3/WholeNumbers/Subtraction_Of_Numbers_Within_10000.html', **VideoLink)

class P3WNMultiplication(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Multiplication",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Multiplication"})
        return self.render_response('Notes/Primary3/WholeNumbers/Multiplication_Of_Numbers_Within_10000.html', **VideoLink)

class P3WNDivision(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Whole_Numbers_Division",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Whole_Numbers_Division"})
        return self.render_response('Notes/Primary3/WholeNumbers/Division_Of_Numbers_Within_1000.html', **VideoLink)
'''
   
class P3MOWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Money_Word_Problems",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Money_Word_Problems"})
        return self.render_response('Notes/Primary3/Money/Money_Word_Problems.html', **VideoLink)

class P3MOAddition(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Money_Addition",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Money_Addition"})
        return self.render_response('Notes/Primary3/Money/Addition_Of_Money.html', **VideoLink)

class P3MOSubtraction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Money_Subtraction",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Money_Subtraction"})
        return self.render_response('Notes/Primary3/Money/Subtraction_Of_Money.html', **VideoLink)

class P3TITellingTime(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Telling_Time",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Telling_Time"})
        return self.render_response('Notes/Primary3/Time/Telling_Time.html', **VideoLink)

class P3TITimeConversion(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Time_Conversion_Hours_Minutes",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Time_Conversion_Hours_Minutes"})
        return self.render_response('Notes/Primary3/Time/Hours_and_Minutes.html', **VideoLink)

class P3TITimeAddition(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Time_Addition",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Time_Addition"})
        return self.render_response('Notes/Primary3/Time/Time_Addition.html', **VideoLink)

class P3TITimeSubtraction(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Time_Subtraction",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Time_Subtraction"})
        return self.render_response('Notes/Primary3/Time/Time_Subtraction.html', **VideoLink)

class P3TITimeDuration(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Time_Finding_Duration_Start_Finish",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Time_Finding_Duration_Start_Finish"})
        return self.render_response('Notes/Primary3/Time/Time_Duration.html', **VideoLink)

class P3TITimeWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Time_Word_Problems",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Time_Word_Problems"})
        return self.render_response('Notes/Primary3/Time/Time_Word_Problems.html', **VideoLink)

class P3LMVMetresCentimetres(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Metres_Centimetres",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Metres_Centimetres"})
        return self.render_response('Notes/Primary3/LengthMassVolume/Metres_Centimetres.html', **VideoLink)

class P3LMVKiloMetresMetres(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Kilometres_Metres",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Kilometres_Metres"})
        return self.render_response('Notes/Primary3/LengthMassVolume/KiloMetres_Metres.html', **VideoLink)

class P3LMVKilogramsGrams(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Kilograms_Grams",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Kilograms_Grams"})
        return self.render_response('Notes/Primary3/LengthMassVolume/Kilograms_Grams.html', **VideoLink)

class P3LMVLitresMillilitres(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Litres_Millilitres",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Litres_Millilitres"})
        return self.render_response('Notes/Primary3/LengthMassVolume/Litres_Millilitres.html', **VideoLink)

class P3LMV1StepWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Length_Mass_Volume_1-Step_Word_Problems",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Length_Mass_Volume_1-Step_Word_Problems"})
        return self.render_response('Notes/Primary3/LengthMassVolume/1_Step_Story_Sums.html', **VideoLink)

class P3LMV2StepWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Length_Mass_Volume_2-Step_Word_Problems",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Length_Mass_Volume_2-Step_Word_Problems"})
        return self.render_response('Notes/Primary3/LengthMassVolume/2_Step_Story_Sums.html', **VideoLink)

class P3FREquivalentFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Equivalent-Fraction",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Equivalent-Fraction"})
        return self.render_response('Notes/Primary3/Fractions/Equivalent_Fractions.html', **VideoLink)

class P3FRSimplifyingFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Simplifying-Fractions",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Simplifying-Fractions"})
        return self.render_response('Notes/Primary3/Fractions/Simplifying_Fractions.html', **VideoLink)

class P3FRComparingOrderingFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Comparing-and-Ordering-Fractions",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Comparing-and-Ordering-Fractions"})
        return self.render_response('Notes/Primary3/Fractions/Comparing_Ordering_Fractions.html', **VideoLink)

class P3FRAddingFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Adding-Fractions",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Adding-Fractions"})
        return self.render_response('Notes/Primary3/Fractions/Addition_Fractions.html', **VideoLink)

class P3FRSubtractingFractions(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Subtracting-Fractions",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Subtracting-Fractions"})
        return self.render_response('Notes/Primary3/Fractions/Subtracting_Fractions.html', **VideoLink)

class P3APSquareUnits(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Area_in_Square_Units",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Area_in_Square_Units"})
        return self.render_response('Notes/Primary3/AreaPerimeter/Area_Square_Units.html', **VideoLink)

class P3APSquareCmM(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Area_in_Square_cm_Square_m",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Area_in_Square_cm_Square_m"})
        return self.render_response('Notes/Primary3/AreaPerimeter/Area_Square_CM_Square_M.html', **VideoLink)

class P3APArea(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Area_of_Squares_Rectangles",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Area_of_Squares_Rectangles"})
        return self.render_response('Notes/Primary3/AreaPerimeter/Area_Square_Rectangle.html', **VideoLink)

class P3APPerimeter(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Perimeter_of_Squares_Rectangles",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Perimeter_of_Squares_Rectangles"})
        return self.render_response('Notes/Primary3/AreaPerimeter/Perimeter_Square_Rectangle.html', **VideoLink)

class P3APWordProblems(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Area_Perimeter_Word_Problems",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Area_Perimeter_Word_Problems"})
        return self.render_response('Notes/Primary3/AreaPerimeter/Area_Perimeter_Word_Problems.html', **VideoLink)

class P3ANIdentifying(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Identifying_Angles_in_Figures",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Identifying_Angles_in_Figures"})
        return self.render_response('Notes/Primary3/Angles/Identifying_Angles.html', **VideoLink)

class P3ANRightAngles(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Right_Angles",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Right_Angles"})
        return self.render_response('Notes/Primary3/Angles/Right_Angles.html', **VideoLink)

class P3BGBarGraphs(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Bar_Graphs",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Bar_Graphs"})
        return self.render_response('Notes/Primary3/BarGraphs/Bar_Graphs.html', **VideoLink)

class P3PPPerpendicularParallel(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        VideoLink.update({'practice_url':"/Grade_3_Math_Practice/Identifying_Perpendicular_Parallel_Lines",
                          'worksheet_url':"/Grade_3_Math_Worksheets/Identifying_Perpendicular_Parallel_Lines"})
        return self.render_response('Notes/Primary3/PerpendicularParallel/Perpendicular_Parallel.html', **VideoLink)
                
class P2TimesTable(BaseHandler):
    def get(self, **kwargs):               
        VideoLink={}
        VideoID = ""
        VideoLink["VideoCall"]="PrepareVideo('"+VideoID+"');"
        return self.render_response('Notes/Primary2/WholeNumbers/Multiplication-Times-Tables-Tips.html', **VideoLink)

class CalculatorAPRS(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary4/Measurement/Calculator-Area-and-Perimeter-of-Rectangles-and-Squares.html')

class TimesChart2To15(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/WholeNumbers/Free-Printable-Times-Table-Chart-From-2-to-15.html')

class TimesChart16To30(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/WholeNumbers/Free-Printable-Times-Table-Chart-From-16-to-30.html')

class CalculatorTimesTable(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/WholeNumbers/Calculator-Times-Table-Multiplication-Chart-2-to-100.html')

class CalculatorRadius(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary6/Measurement/Calculator-Radius-of-Circle-Given-Diameter-Circumference-Area.html')

class CalculatorDiameter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary6/Measurement/Calculator-Diameter-of-Circle-for-Elementary-Grade-Math.html')

class CalculatorCircumference(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary6/Measurement/Calculator-Circumference-of-Circle-Given-Radius-Diameter-Area.html')

class CalculatorArea(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary6/Measurement/Calculator-Area-of-Circle-Given-Radius-Diameter-Circumference.html')

class MathCalculators(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Math-Calculators.html')

class TimeUnitsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Time-Units-Converter.html')

class HoursUnitConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-Converter.html')

class HoursToMinutesConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Minutes-Converter.html')

class HoursToSecondsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Seconds-Converter.html')

class HoursToMillisecondsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Milliseconds-Converter.html')

class HoursToDaysConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Days-Converter.html')

class HoursToWeeksConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Weeks-Converter.html')

class HoursToMonthsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Months-Converter.html')

class HoursToYearsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Years-Converter.html')

class HoursToDecadesConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Decades-Converter.html')

class HoursToCenturiesConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Centuries-Converter.html')

class HoursToMillenniumsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Millenniums-Converter.html')

class HoursToMicrosecondsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Microseconds-Converter.html')

class HoursToNanosecondsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Nanoseconds-Converter.html')

class HoursToPicosecondsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/TimeUnitsConverter/Hours-to-Picoseconds-Converter.html')

class CalculatorNumberComparison(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/WholeNumbers/Calculator-to-Compare-Two-Numbers.html')

class CalculatorTimeDuration(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/Time/Calculator-Time-Duration-Addition-Subtraction.html')

class LengthUnitsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Length-Units-Converter.html')

class MeterUnitConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-Converter.html')

class MeterToCentimeterConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-to-Centimeter-Converter.html')

class MeterToMillimeterConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-to-Millimeter-Converter.html')

class MeterToKilometreConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-to-Kilometre-Converter.html')

class MeterToInchesConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-to-Inches-Converter.html')

class MeterToFeetConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-to-Feet-Converter.html')

class MeterToFeetInchesConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-to-Feet-and-Inches-Conversion.html')

class MeterToMilesConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-to-Miles-Converter.html')

class MeterToYardsConverter(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/LengthUnitConverter/Meter-to-Yards-Converter.html')

class EquivalentFractionsCalculator(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/Fractions/Equivalent-Fractions-Generator.html')

class SimplifyingFractionsCalculator(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/Fractions/Simplifying-Fractions-Calculator.html')

class CompareFractionsCalculator(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/Fractions/Compare-Fractions-Calculator.html')

class AddFractionsCalculator(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/Fractions/Add-Fractions-Calculator.html')

class SubtractFractionsCalculator(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary3/Fractions/Subtract-Fractions-Calculator.html')

class WorksheetsPerimeterRectangles(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Perimeter-of-Rectangles.html')

class WorksheetsPerimeterSquares(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Perimeter-of-Squares.html')

class WorksheetsAreaRectangles(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Area-of-Rectangles.html')

class WorksheetsAreaSquares(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Area-of-Squares.html')

class WorksheetsCircumferenceCircle(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Circumference-of-Circle.html')

class WorksheetsDiameterRadiusCircle(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Diameter-Radius-of-Circle.html')

class WorksheetsNumbersUpTo10000(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Numbers-Up-To-10000.html')

class WorksheetsFiguresToWordsUpTo10000(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Figures-To-Words-Up-To-10000.html')

class WorksheetsWordsToFiguresUpTo10000(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Words-To-Figures-Up-To-10000.html')

class WorksheetsBasicNumberPatterns(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Basic-Number-Patterns.html')

class WorksheetsCompareOrder4Digits(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Compare-Order-Four-Digit-Numbers.html')

class WorksheetsAdditionUpTo10000(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Addition-of-Numbers-Up-To-10000.html')

class WorksheetsSubtractionUpTo10000(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Subtraction-of-Numbers-Up-To-10000.html')

class WorksheetsMultiplication3Digits(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Multiplication-of-3-Digits.html')

class WorksheetsDivision2Digits(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Long-Division-of-2-Digits.html')

class WorksheetsWholeNumbersWordProblems(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-2-Step-Word-Problems-Whole-Numbers.html')

class WorksheetsMoneyAddition(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Money-Addition.html')

class WorksheetsMoneySubtraction(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Money-Subtraction.html')

class WorksheetsMoneyWordProblems(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Money-Word-Problems-Story-Sum.html')

class WorksheetsTellingTime(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Reading-and-Telling-Time.html')

class WorksheetsHoursToMinutes(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Convert-Hours-to-Minutes.html')

class WorksheetsTimeAddition(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Time-Addition-Add-Hours-Minutes.html')

class WorksheetsTimeSubtraction(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Time-Subtraction-Subtract-Hours-Minutes.html')

class WorksheetsTimeDuration(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-Calculate-Time-Duration.html')

class WorksheetsTimeWordProblems(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/Free-Math-Worksheet-on-2-Step-Time-Duration-Word-Problems.html')

class WorksheetsConvertMetresCentimetres(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-on-how-to-convert-metres-to-centimeters.html')

class WorksheetsConvertKilometersMeters(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-on-how-to-convert-kilometers-to-meters.html')

class WorksheetsConvertKilogramsGrams(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-on-how-to-convert-kilograms-to-grams.html')

class WorksheetsConvertLitresMillilitres(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-on-how-to-convert-litres-to-millilitres.html')

class WorksheetsLMV1StepWP(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-solve-1-step-length-mass-volume.html')

class WorksheetsLMV2StepWP(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-solve-2-step-length-mass-volume.html')

class WorksheetsWhatIsAFraction(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-what-is-a-fraction.html')

class WorksheetsEquivalentFraction(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-what-are-equivalent-fraction.html')

class WorksheetsSimplifyingFraction(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-simplifying-fractions.html')

class WorksheetsCnOFraction(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-comparing-ordering-fractions.html')

class WorksheetsAddFractions(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-add-fractions.html')

class WorksheetsSubtractFractions(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-subtract-fractions.html')

class WorksheetsSquareUnits(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-area-in-square-units.html')

class WorksheetsSquareCmM(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-area-in-square-centimeters-meters.html')

class WorksheetsAreaSquare(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-how-to-calculate-area-of-a-square.html')

class WorksheetsIdentifyingAngles(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-identifying-angles.html')

class WorksheetsRightAngles(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-right-angles.html')

class WorksheetsBarGraphs(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Worksheets/free-math-worksheet-bar-graphs.html')

class PropertiesTriangle(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Primary5/Geometry/properties-of-triangles.html')

class MathWorksheets(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Math-Worksheets.html')

class MathGlossary(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Math-Glossary.html')

class Rectangle(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Glossary/Rectangle.html')

class Square(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('Notes/Glossary/Square.html')

       
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()