import Problems.Primary3.WholeNumbers.P3WNPlaceValue
import Problems.Primary3.WholeNumbers.P3WNFiguresToWords
import Problems.Primary3.WholeNumbers.P3WNWordsToFigures
import Problems.Primary3.WholeNumbers.P3WNComparingOrdering
import Problems.Primary3.WholeNumbers.P3WNNumberPatterns
import Problems.Primary3.WholeNumbers.P3WNAddition
import Problems.Primary3.WholeNumbers.P3WNSubtraction
import Problems.Primary3.WholeNumbers.P3WNMultiplication
import Problems.Primary3.WholeNumbers.P3WNDivision
import Problems.Primary3.WholeNumbers.P3WNWordProblems
import Problems.Primary3.Money.P3MOAddition
import Problems.Primary3.Money.P3MOSubtraction
import Problems.Primary3.Money.P3MOWordProblems
import Problems.Primary3.LengthMassVolume.P3LMKiloGram
import Problems.Primary3.LengthMassVolume.P3LMKiloMetre
import Problems.Primary3.LengthMassVolume.P3LMLitresMilli
import Problems.Primary3.LengthMassVolume.P3LMMetreCentiMetre
import Problems.Primary3.LengthMassVolume.P3LMWordProblems_2Steps
import Problems.Primary3.LengthMassVolume.P3LMWordProblems
import Problems.Primary3.Time.P3TIAddition
import Problems.Primary3.Time.P3TIConversionTime
import Problems.Primary3.Time.P3TISubtraction
import Problems.Primary3.Time.P3TIDuration
import Problems.Primary3.Time.P3TITellingTime
import Problems.Primary3.Time.P3TIWordProblems
import Problems.Primary3.Angles.P3ANIdentifying
import Problems.Primary3.Angles.P3ANRightAngle
import Problems.Primary3.BarGraphs.P3BGBarGraphs
import Problems.Primary3.AreaPerimeter.P3APSquareUnits
import Problems.Primary3.AreaPerimeter.P3APSquareCmM
import Problems.Primary3.AreaPerimeter.P3APArea
import Problems.Primary3.AreaPerimeter.P3APPerimeter
import Problems.Primary3.AreaPerimeter.P3APWordProblems
import Problems.Primary3.Fractions.P3FRWhatIsFractions
import Problems.Primary3.Fractions.P3FREquivalentFractions
import Problems.Primary3.Fractions.P3FRSimplifyingFractions
import Problems.Primary3.Fractions.P3FRComparingOrdering
import Problems.Primary3.Fractions.P3FRAddition
import Problems.Primary3.Fractions.P3FRSubtraction
import Problems.Primary3.PerpendicularParallel.P3PPPerpendicularParallel

import Config

def GenerateP3TestProblems(concept,problem_type):
    if (concept=="P3WNPlaceValues"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNPlaceValue.P3WNPlaceValue().GenerateTestProblem(problem_type)
    elif (concept=="P3WNFiguresToWords"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNFiguresToWords.P3WNFiguresToWords().GenerateTestProblem(problem_type)
    elif (concept=="P3WNWordsToFigures"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNWordsToFigures.P3WNWordsToFigures().GenerateTestProblem(problem_type)
    elif (concept=="P3WNComparingOrdering"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNComparingOrdering.P3WNComparingOrdering().GenerateTestProblem(problem_type)
    elif (concept=="P3WNNumberPatterns"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNNumberPatterns.P3WNNumberPatterns().GenerateTestProblem(problem_type)
    elif (concept=="P3WNAddition"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNAddition.P3WNAddition().GenerateTestProblem(problem_type)
    elif (concept=="P3WNSubtraction"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNSubtraction.P3WNSubtraction().GenerateTestProblem(problem_type)
    elif (concept=="P3WNMultiplication"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNMultiplication.P3WNMultiplication().GenerateTestProblem(problem_type)
    elif (concept=="P3WNDivision"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNDivision.P3WNDivision().GenerateTestProblem(problem_type)
    elif (concept=="P3WNWordProblems"):
        Config.test_values = Problems.Primary3.WholeNumbers.P3WNWordProblems.P3WNWordProblems().GenerateTestProblem(problem_type)
    elif (concept=="P3MOAddition"):
        Config.test_values = Problems.Primary3.Money.P3MOAddition.P3MOAddition().GenerateTestProblem(problem_type)
    elif (concept=="P3MOSubtraction"):
        Config.test_values = Problems.Primary3.Money.P3MOSubtraction.P3MOSubtraction().GenerateTestProblem(problem_type)
    elif (concept=="P3MOWordProblems"):
        Config.test_values = Problems.Primary3.Money.P3MOWordProblems.P3MOWordProblems().GenerateTestProblem(problem_type)
    elif (concept=="P3LMKiloGram"):
        Config.test_values = Problems.Primary3.LengthMassVolume.P3LMKiloGram.P3LMKiloGram().GenerateTestProblem(problem_type)
    elif (concept=="P3LMKiloMetre"):
        Config.test_values = Problems.Primary3.LengthMassVolume.P3LMKiloMetre.P3LMKiloMetre().GenerateTestProblem(problem_type)
    elif (concept=="P3LMLitresMilli"):
        Config.test_values = Problems.Primary3.LengthMassVolume.P3LMLitresMilli.P3LMLitresMilli().GenerateTestProblem(problem_type)
    elif (concept=="P3LMMetreCentiMetre"):
        Config.test_values = Problems.Primary3.LengthMassVolume.P3LMMetreCentiMetre.P3LMMetreCentiMetre().GenerateTestProblem(problem_type)
    elif (concept=="P3LMWordProblems_2Steps"):
        Config.test_values = Problems.Primary3.LengthMassVolume.P3LMWordProblems_2Steps.P3LMWordProblems_2Steps().GenerateTestProblem(problem_type)
    elif (concept=="P3LMWordProblems"):
        Config.test_values = Problems.Primary3.LengthMassVolume.P3LMWordProblems.P3LMWordProblems().GenerateTestProblem(problem_type)
    elif (concept=="P3TIAddition"):
        Config.test_values = Problems.Primary3.Time.P3TIAddition.P3TIAddition().GenerateTestProblem(problem_type)
    elif (concept=="P3TIConversionTime"):
        Config.test_values = Problems.Primary3.Time.P3TIConversionTime.P3TIConversionTime().GenerateTestProblem(problem_type)
    elif (concept=="P3TISubtraction"):
        Config.test_values = Problems.Primary3.Time.P3TISubtraction.P3TISubtraction().GenerateTestProblem(problem_type)
    elif (concept=="P3TIDuration"):
        Config.test_values = Problems.Primary3.Time.P3TIDuration.P3TIDuration().GenerateTestProblem(problem_type)
    elif (concept=="P3TITellingTime"):
        Config.test_values = Problems.Primary3.Time.P3TITellingTime.P3TITellingTime().GenerateTestProblem(problem_type)
    elif (concept=="P3TIWordProblems"):
        Config.test_values = Problems.Primary3.Time.P3TIWordProblems.P3TIWordProblems().GenerateTestProblem(problem_type)
    elif (concept=="P3ANIdentifying"):
        Config.test_values = Problems.Primary3.Angles.P3ANIdentifying.P3ANIdentifying().GenerateTestProblem(problem_type)
    elif (concept=="P3ANRightAngle"):
        Config.test_values = Problems.Primary3.Angles.P3ANRightAngle.P3ANRightAngle().GenerateTestProblem(problem_type)
    elif (concept=="P3BGBarGraphs"):
        Config.test_values = Problems.Primary3.BarGraphs.P3BGBarGraphs.P3BGBarGraphs().GenerateTestProblem(problem_type)
    elif (concept=="P3APSquareUnits"):
        Config.test_values = Problems.Primary3.AreaPerimeter.P3APSquareUnits.P3APSquareUnits().GenerateTestProblem(problem_type)
    elif (concept=="P3APSquareCmM"):
        Config.test_values = Problems.Primary3.AreaPerimeter.P3APSquareCmM.P3APSquareCmM().GenerateTestProblem(problem_type)
    elif (concept=="P3APArea"):
        Config.test_values = Problems.Primary3.AreaPerimeter.P3APArea.P3APArea().GenerateTestProblem(problem_type)
    elif (concept=="P3APPerimeter"):
        Config.test_values = Problems.Primary3.AreaPerimeter.P3APPerimeter.P3APPerimeter().GenerateTestProblem(problem_type)
    elif (concept=="P3APWordProblems"):
        Config.test_values = Problems.Primary3.AreaPerimeter.P3APWordProblems.P3APWordProblems().GenerateTestProblem(problem_type)
    elif (concept=="P3FRWhatIsFractions"):
        Config.test_values = Problems.Primary3.Fractions.P3FRWhatIsFractions.P3FRWhatIsFractions().GenerateTestProblem(problem_type)
    elif (concept=="P3FREquivalentFractions"):
        Config.test_values = Problems.Primary3.Fractions.P3FREquivalentFractions.P3FREquivalentFractions().GenerateTestProblem(problem_type)
    elif (concept=="P3FRSimplifyingFractions"):
        Config.test_values = Problems.Primary3.Fractions.P3FRSimplifyingFractions.P3FRSimplifyingFractions().GenerateTestProblem(problem_type)
    elif (concept=="P3FRComparingOrdering"):
        Config.test_values = Problems.Primary3.Fractions.P3FRComparingOrdering.P3FRComparingOrdering().GenerateTestProblem(problem_type)
    elif (concept=="P3FRAddition"):
        Config.test_values = Problems.Primary3.Fractions.P3FRAddition.P3FRAddition().GenerateTestProblem(problem_type)
    elif (concept=="P3FRSubtraction"):
        Config.test_values = Problems.Primary3.Fractions.P3FRSubtraction.P3FRSubtraction().GenerateTestProblem(problem_type)
    elif (concept=="P3PPPerpendicularParallel"):
        Config.test_values = Problems.Primary3.PerpendicularParallel.P3PPPerpendicularParallel.P3PPPerpendicularParallel().GenerateTestProblem(problem_type)
    
    Config.test_values["concept"] = concept

    return Config.test_values