import Problems.Primary4.WholeNumbers.WriteInFigures
import Problems.Primary4.WholeNumbers.WriteInWords
import Problems.Primary4.WholeNumbers.PlaceValue
import Problems.Primary4.WholeNumbers.ComparingAndOrdering
import Problems.Primary4.WholeNumbers.RoundingOff
import Problems.Primary4.WholeNumbers.FactorMultiple
import Problems.Primary4.WholeNumbers.MultiplicationDivision
import Problems.Primary4.Fractions.MixedNumbersImproperFractions
import Problems.Primary4.Fractions.SimplifyingFractions
import Problems.Primary4.Fractions.AddLikeRelatedFractions
import Problems.Primary4.Fractions.SubtractLikeRelatedFractions
import Problems.Primary4.Fractions.MultiplyProperImproperFractions
import Problems.Primary4.Decimals.DecimalsTenths
import Problems.Primary4.Decimals.DecimalsHundredths
import Problems.Primary4.Decimals.DecimalsThousandths
import Problems.Primary4.Decimals.DecimalsComparingOrdering
import Problems.Primary4.Decimals.DecimalsRoundingOff
import Problems.Primary4.Decimals.DecimalsFractions
import Problems.Primary4.Decimals.DecimalsAddSub
import Problems.Primary4.Decimals.DecimalsMultiplyDivide
import Problems.Primary4.Decimals.P4DCWordProblems
import Problems.Primary4.Measurement.MTTime24Hrs
import Problems.Primary4.Measurement.MTTimeDuration
import Problems.Primary4.Measurement.MTPerimeter
import Problems.Primary4.Measurement.MTArea
import Problems.Primary4.Measurement.MTCompositeFigures
import Problems.Primary4.DataAnalysis.P4DALineGraphs
import Problems.Primary4.DataAnalysis.P4DATablesBarGraphs
import Problems.Primary4.WholeNumbers.P4WNWordProblems
import Problems.Primary4.Fractions.P4FRWordProblems
import Config

def GenerateP4TestProblems(concept,problem_type):
    if concept == "P4DecimalsAddSub":
        Config.test_values = Problems.Primary4.Decimals.DecimalsAddSub.DecimalsAddSub().GenerateTestProblem(problem_type)                
    elif concept == "P4DecimalsComparingOrdering":
        Config.test_values = Problems.Primary4.Decimals.DecimalsComparingOrdering.DecimalsComparingOrdering().GenerateTestProblem(problem_type)                
    elif concept == "P4DecimalsFractions":
        Config.test_values = Problems.Primary4.Decimals.DecimalsFractions.DecimalsFractions().GenerateTestProblem(problem_type)                
    elif concept == "P4DecimalsHundredths":
        Config.test_values = Problems.Primary4.Decimals.DecimalsHundredths.DecimalsHundredths().GenerateTestProblem(problem_type)                
    elif concept == "P4DecimalsMultiplyDivide":
        Config.test_values = Problems.Primary4.Decimals.DecimalsMultiplyDivide.DecimalsMultiplyDivide().GenerateTestProblem(problem_type)                
    elif concept == "P4DecimalsRoundingOff":
        Config.test_values = Problems.Primary4.Decimals.DecimalsRoundingOff.DecimalsRoundingOff().GenerateTestProblem(problem_type)                
    elif concept == "P4DecimalsTenths":
        Config.test_values = Problems.Primary4.Decimals.DecimalsTenths.DecimalsTenths().GenerateTestProblem(problem_type)                
    elif concept == "P4DecimalsThousandths":
        Config.test_values = Problems.Primary4.Decimals.DecimalsThousandths.DecimalsThousandths().GenerateTestProblem(problem_type)                
    elif concept == "P4DCWordProblems":
        Config.test_values = Problems.Primary4.Decimals.P4DCWordProblems.P4DCWordProblems().GenerateTestProblem(problem_type)                
    elif concept == "P4FractionsAdd":
        Config.test_values = Problems.Primary4.Fractions.AddLikeRelatedFractions.AddLikeRelatedFractions().GenerateTestProblem(problem_type)                
    elif concept == "P4FractionsMixedImproper":
        Config.test_values = Problems.Primary4.Fractions.MixedNumbersImproperFractions.MixedNumbersImproperFractions().GenerateTestProblem(problem_type)                
    elif concept == "P4FractionsMultiplication":
        Config.test_values = Problems.Primary4.Fractions.MultiplyProperImproperFractions.MultiplyProperImproperFractions().GenerateTestProblem(problem_type)                
    elif concept == "P4FractionsSimplifying":
        Config.test_values = Problems.Primary4.Fractions.SimplifyingFractions.SimplifyingFractions().GenerateTestProblem(problem_type)                
    elif concept == "P4FractionsSubtract":
        Config.test_values = Problems.Primary4.Fractions.SubtractLikeRelatedFractions.SubtractLikeRelatedFractions().GenerateTestProblem(problem_type)                
    elif concept == "P4MTArea":
        Config.test_values = Problems.Primary4.Measurement.MTArea.MTArea().GenerateTestProblem(problem_type)                
    elif concept == "P4MTCompositeFigures":
        Config.test_values = Problems.Primary4.Measurement.MTCompositeFigures.MTCompositeFigures().GenerateTestProblem(problem_type)                
    elif concept == "P4MTPerimeter":
        Config.test_values = Problems.Primary4.Measurement.MTPerimeter.MTPerimeter().GenerateTestProblem(problem_type)                
    elif concept == "P4MTTime24Hrs":
        Config.test_values = Problems.Primary4.Measurement.MTTime24Hrs.MTTime24Hrs().GenerateTestProblem(problem_type)                
    elif concept == "P4MTTimeDuration":
        Config.test_values = Problems.Primary4.Measurement.MTTimeDuration.MTTimeDuration().GenerateTestProblem(problem_type)                
    elif concept == "P4WholeNumbersComparingOrdering":
        Config.test_values = Problems.Primary4.WholeNumbers.ComparingAndOrdering.ComparingAndOrdering().GenerateTestProblem(problem_type)                
    elif concept == "P4WholeNumbersFactorMultiple":
        Config.test_values = Problems.Primary4.WholeNumbers.FactorMultiple.FactorMultiple().GenerateTestProblem(problem_type)                
    elif concept == "P4WholeNumbersMutliplyDivide":
        Config.test_values = Problems.Primary4.WholeNumbers.MultiplicationDivision.MultiplicationDivision().GenerateTestProblem(problem_type)                
    elif concept == "P4WholeNumbersPlaceValues":
        Config.test_values = Problems.Primary4.WholeNumbers.PlaceValue.PlaceValue().GenerateTestProblem(problem_type)                
    elif concept == "P4WholeNumbersRoundingOff":
        Config.test_values = Problems.Primary4.WholeNumbers.RoundingOff.RoundingOff().GenerateTestProblem(problem_type)                
    elif concept == "P4WholeNumbersWriteInFigures":
        Config.test_values = Problems.Primary4.WholeNumbers.WriteInFigures.WriteInFigures().GenerateTestProblem(problem_type)                
    elif concept == "P4WholeNumbersWriteInWords":
        Config.test_values = Problems.Primary4.WholeNumbers.WriteInWords.WriteInWords().GenerateTestProblem(problem_type)                
    elif concept == "P4DALineGraphs":
        Config.test_values = Problems.Primary4.DataAnalysis.P4DALineGraphs.P4DALineGraphs().GenerateTestProblem(problem_type)                
    elif concept == "P4DATablesBarGraphs":
        Config.test_values = Problems.Primary4.DataAnalysis.P4DATablesBarGraphs.P4DATablesBarGraphs().GenerateTestProblem(problem_type)                
    elif concept == "P4WNWordProblems":
        Config.test_values = Problems.Primary4.WholeNumbers.P4WNWordProblems.P4WNWordProblems().GenerateTestProblem(problem_type)                
    elif concept == "P4FRWordProblems":
        Config.test_values = Problems.Primary4.Fractions.P4FRWordProblems.P4FRWordProblems().GenerateTestProblem(problem_type)                
    
    Config.test_values["concept"] = concept

    return Config.test_values