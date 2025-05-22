import Problems.Primary5.WholeNumbers.WriteInFigures
import Problems.Primary5.WholeNumbers.WriteInWords
import Problems.Primary5.WholeNumbers.ApproximationEstimation
import Problems.Primary5.WholeNumbers.ComparingAndOrdering
import Problems.Primary5.WholeNumbers.FindPattern
import Problems.Primary5.WholeNumbers.MultiplyDivide
import Problems.Primary5.WholeNumbers.OrderOfOperation
import Problems.Primary5.WholeNumbers.PlaceValue
import Problems.Primary5.WholeNumbers.WordProblems
import Problems.Primary5.Fractions.AddSubMixedFractions
import Problems.Primary5.Fractions.AddSubProperFractions
import Problems.Primary5.Fractions.DivideProperFractions
import Problems.Primary5.Fractions.MultMixedFractions
import Problems.Primary5.Fractions.MultProperImproperFractions
import Problems.Primary5.Fractions.WordProblems
import Problems.Primary5.Decimals.MultiplyDivide
import Problems.Primary5.Decimals.Rounding
import Problems.Primary5.Decimals.WordProblems
import Problems.Primary5.Percentage.ExpressAsPercent
import Problems.Primary5.Percentage.ExpressAsDecimal
import Problems.Primary5.Percentage.ExpressAsFraction
import Problems.Primary5.Percentage.WordProblems
import Problems.Primary5.Ratio.SimplestForm
import Problems.Primary5.Ratio.MissingNumber
import Problems.Primary5.Ratio.WordProblems
import Problems.Primary5.Measurement.UnitConversion
import Problems.Primary5.Measurement.AreaOfTriangle
import Problems.Primary5.Measurement.Volume
import Problems.Primary5.Measurement.WordProblems
import Problems.Primary5.Geometry.Angles
import Problems.Primary5.Geometry.Triangles
import Problems.Primary5.Geometry.FourSidedFigures
import Problems.Primary5.DataAnalysis.FindAverage
import Problems.Primary5.DataAnalysis.FindTotal
import Problems.Primary5.DataAnalysis.WordProblems
import Config

def GenerateP5TestProblems(concept,problem_type):
    if concept == "P5DataAnalysisAverage":
        Config.test_values = Problems.Primary5.DataAnalysis.FindAverage.FindAverage().GenerateTestProblem(problem_type)                
    elif concept == "P5DataAnalysisTotal":
        Config.test_values = Problems.Primary5.DataAnalysis.FindTotal.FindTotal().GenerateTestProblem(problem_type)                
    elif concept == "P5DataAnalysisWordProblems":
        Config.test_values = Problems.Primary5.DataAnalysis.WordProblems.WordProblems().GenerateTestProblem(problem_type)
    elif concept == "P5DecimalsMultiplyDivide":
        Config.test_values = Problems.Primary5.Decimals.MultiplyDivide.MultiplyDivide().GenerateTestProblem(problem_type)
    elif concept == "P5DecimalsRounding":
        Config.test_values = Problems.Primary5.Decimals.Rounding.Rounding().GenerateTestProblem(problem_type)
    elif concept == "P5DecimalsWordProblems":
        Config.test_values = Problems.Primary5.Decimals.WordProblems.WordProblems().GenerateTestProblem(problem_type)
    elif concept == "P5FractionsAddSubMixedFractions":
        Config.test_values = Problems.Primary5.Fractions.AddSubMixedFractions.AddSubMixedFractions().GenerateTestProblem(problem_type)
    elif concept == "P5FractionsAddSubProperFractions":
        Config.test_values = Problems.Primary5.Fractions.AddSubProperFractions.AddSubProperFractions().GenerateTestProblem(problem_type)
    elif concept == "P5FractionsMultProperImproperFractions":
        Config.test_values = Problems.Primary5.Fractions.MultProperImproperFractions.MultProperImproperFractions().GenerateTestProblem(problem_type)
    elif concept == "P5FractionsMultMixedFractions":
        Config.test_values = Problems.Primary5.Fractions.MultMixedFractions.MultMixedFractions().GenerateTestProblem(problem_type)
    elif concept == "P5FractionsDivideProperFractions":
        Config.test_values = Problems.Primary5.Fractions.DivideProperFractions.DivideProperFractions().GenerateTestProblem(problem_type)
    elif concept == "P5FractionsWordProblems":
        Config.test_values = Problems.Primary5.Fractions.WordProblems.WordProblems().GenerateTestProblem(problem_type)
    elif concept == "P5GeometryAngles":
        Config.test_values = Problems.Primary5.Geometry.Angles.Angles().GenerateTestProblem(problem_type)
    elif concept == "P5GeometryTriangles":
        Config.test_values = Problems.Primary5.Geometry.Triangles.Triangles().GenerateTestProblem(problem_type)
    elif concept == "P5GeometryFourSided":
        Config.test_values = Problems.Primary5.Geometry.FourSidedFigures.FourSidedFigures().GenerateTestProblem(problem_type)
    elif concept == "P5GeometryFourSided":
        Config.test_values = Problems.Primary5.Geometry.FourSidedFigures.FourSidedFigures().GenerateTestProblem(problem_type)
    elif concept == "P5MeasurementAreaOfTriangle":
        Config.test_values = Problems.Primary5.Measurement.AreaOfTriangle.AreaOfTriangle().GenerateTestProblem(problem_type)
    elif concept == "P5MeasurementUnitConversion":
        Config.test_values = Problems.Primary5.Measurement.UnitConversion.UnitConversion().GenerateTestProblem(problem_type)
    elif concept == "P5MeasurementVolume":
        Config.test_values = Problems.Primary5.Measurement.Volume.Volume().GenerateTestProblem(problem_type)
    elif concept == "P5MeasurementWordProblems":
        Config.test_values = Problems.Primary5.Measurement.WordProblems.WordProblems().GenerateTestProblem(problem_type)
    elif concept == "P5PercentageExpressAsDecimal":
        Config.test_values = Problems.Primary5.Percentage.ExpressAsDecimal.ExpressAsDecimal().GenerateTestProblem(problem_type)
    elif concept == "P5PercentageExpressAsFraction":
        Config.test_values = Problems.Primary5.Percentage.ExpressAsFraction.ExpressAsFraction().GenerateTestProblem(problem_type)
    elif concept == "P5PercentageExpressAsPercent":
        Config.test_values = Problems.Primary5.Percentage.ExpressAsPercent.ExpressAsPercent().GenerateTestProblem(problem_type)
    elif concept == "P5PercentageWordProblems":
        Config.test_values = Problems.Primary5.Percentage.WordProblems.WordProblems().GenerateTestProblem(problem_type)
    elif concept == "P5RatioMissingNumber":
        Config.test_values = Problems.Primary5.Ratio.MissingNumber.MissingNumber().GenerateTestProblem(problem_type)
    elif concept == "P5RatioSimplestForm":
        Config.test_values = Problems.Primary5.Ratio.SimplestForm.SimplestForm().GenerateTestProblem(problem_type)
    elif concept == "P5RatioWordProblems":
        Config.test_values = Problems.Primary5.Ratio.WordProblems.WordProblems().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersApproximationEstimation":
        Config.test_values = Problems.Primary5.WholeNumbers.ApproximationEstimation.ApproximationEstimation().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersComparingAndOrdering":
        Config.test_values = Problems.Primary5.WholeNumbers.ComparingAndOrdering.ComparingAndOrdering().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersFindPattern":
        Config.test_values = Problems.Primary5.WholeNumbers.FindPattern.FindPattern().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersMultiplyDivide":
        Config.test_values = Problems.Primary5.WholeNumbers.MultiplyDivide.MultiplyDivide().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersOrderOfOperation":
        Config.test_values = Problems.Primary5.WholeNumbers.OrderOfOperation.OrderOfOperation().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersPlaceValue":
        Config.test_values = Problems.Primary5.WholeNumbers.PlaceValue.PlaceValue().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersWriteInFigures":
        Config.test_values = Problems.Primary5.WholeNumbers.WriteInFigures.WriteInFigures().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersWriteInWords":
        Config.test_values = Problems.Primary5.WholeNumbers.WriteInWords.WriteInWords().GenerateTestProblem(problem_type)
    elif concept == "P5WholeNumbersWordProblems":
        Config.test_values = Problems.Primary5.WholeNumbers.WordProblems.WordProblems().GenerateTestProblem(problem_type)
                            
    Config.test_values["concept"] = concept

    return Config.test_values