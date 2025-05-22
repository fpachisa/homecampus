import Problems.Primary6.Algebra.SimplifyingAlgebra
import Problems.Primary6.Algebra.EvaluationAlgebra
import Problems.Primary6.Fractions.DivideWholeNumber
import Problems.Primary6.Fractions.DivideProperFraction
import Problems.Primary6.Percentage.WholePart
import Problems.Primary6.Percentage.PercentIncDec
import Problems.Primary6.Speed.DistanceTimeSpeed
import Problems.Primary6.Measurement.CircleCircumference
import Problems.Primary6.Measurement.CircleRadiusDiameter
import Problems.Primary6.Measurement.CircleArea
import Problems.Primary6.Measurement.SemiCirclePerimeter
import Problems.Primary6.Measurement.SemiCircleArea
import Problems.Primary6.Measurement.CompositeFigures
import Problems.Primary6.Measurement.VolumeOfCubeCuboid
import Problems.Primary6.Ratio.P6RTWordProblems
import Problems.Primary6.DataAnalysis.P6DAWordProblems
import Problems.Primary6.Algebra.P6AGWordProblems
import Problems.Primary6.Fractions.P6FRWordProblems
import Problems.Primary6.Speed.P6SPWordProblems
import Problems.Primary6.Percentage.P6PRWordProblems
import Config

def GenerateP6TestProblems(concept,problem_type):
    if concept == "P6AGEvaluationExpression":
        Config.test_values = Problems.Primary6.Algebra.EvaluationAlgebra.EvaluationAlgebra().GenerateTestProblem(problem_type)                
    elif concept == "P6AGSimplifyingExpression":
        Config.test_values = Problems.Primary6.Algebra.SimplifyingAlgebra.SimplifyingAlgebra().GenerateTestProblem(problem_type)                
    elif concept == "P6AGWordProblems":
        Config.test_values = Problems.Primary6.Algebra.P6AGWordProblems.P6AGWordProblems().GenerateTestProblem(problem_type)                
    elif concept == "P6DAWordProblems":
        Config.test_values = Problems.Primary6.DataAnalysis.P6DAWordProblems.P6DAWordProblems().GenerateTestProblem(problem_type)                
    elif concept == "P6FRDivideProperFraction":
        Config.test_values = Problems.Primary6.Fractions.DivideProperFraction.DivideProperFraction().GenerateTestProblem(problem_type)
    elif concept == "P6FRDivideWholeNumber":
        Config.test_values = Problems.Primary6.Fractions.DivideWholeNumber.DivideWholeNumber().GenerateTestProblem(problem_type)
    elif concept == "P6FRWordProblems":
        Config.test_values = Problems.Primary6.Fractions.P6FRWordProblems.P6FRWordProblems().GenerateTestProblem(problem_type)
    elif concept == "P6MTArea":
        Config.test_values = Problems.Primary6.Measurement.CircleArea.CircleArea().GenerateTestProblem(problem_type)
    elif concept == "P6MTCircumference":
        Config.test_values = Problems.Primary6.Measurement.CircleCircumference.CircleCircumference().GenerateTestProblem(problem_type)
    elif concept == "P6MTRadius":
        Config.test_values = Problems.Primary6.Measurement.CircleRadiusDiameter.CircleRadiusDiameter().GenerateTestProblem(problem_type)
    elif concept == "P6MTComposite":
        Config.test_values = Problems.Primary6.Measurement.CompositeFigures.CompositeFigures().GenerateTestProblem(problem_type)
    elif concept == "P6MTSemiArea":
        Config.test_values = Problems.Primary6.Measurement.SemiCircleArea.SemiCircleArea().GenerateTestProblem(problem_type)
    elif concept == "P6MTSemiPerimeter":
        Config.test_values = Problems.Primary6.Measurement.SemiCirclePerimeter.SemiCirclePerimeter().GenerateTestProblem(problem_type)
    elif concept == "P6MTVolume":
        Config.test_values = Problems.Primary6.Measurement.VolumeOfCubeCuboid.VolumeOfCubeCuboid().GenerateTestProblem(problem_type)
    elif concept == "P6PRWordProblems":
        Config.test_values = Problems.Primary6.Percentage.P6PRWordProblems.P6PRWordProblems().GenerateTestProblem(problem_type)
    elif concept == "P6PRIncDec":
        Config.test_values = Problems.Primary6.Percentage.PercentIncDec.PercentIncDec().GenerateTestProblem(problem_type)
    elif concept == "P6PRFindWhole":
        Config.test_values = Problems.Primary6.Percentage.WholePart.WholePart().GenerateTestProblem(problem_type)
    elif concept == "P6RTWordProblems":
        Config.test_values = Problems.Primary6.Ratio.P6RTWordProblems.P6RTWordProblems().GenerateTestProblem(problem_type)
    elif concept == "P6SPWordProblems":
        Config.test_values = Problems.Primary6.Speed.P6SPWordProblems.P6SPWordProblems().GenerateTestProblem(problem_type)
    elif concept == "P6SPDTS":
        Config.test_values = Problems.Primary6.Speed.DistanceTimeSpeed.DistanceTimeSpeed().GenerateTestProblem(problem_type)
                                    
    Config.test_values["concept"] = concept

    return Config.test_values