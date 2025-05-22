$(document).ready(function() 
{ 
	$("#P1WNAddition").click(function() 
    	{            
            HideUnhideDiv();
			var HtmlText = 'Primary 1-->Whole Numbers-->Addition';
            var URLText = '/P1/Whole_Numbers/Rayan/Addition';
            return AJAXCall(HtmlText,URLText);
    	});
			
});

function AJAXCall(HtmlText,URLText)
{        
		return $.ajax(
		{
			type: "POST",
			url: URLText,
			data: "",
			beforeSend: function(){
				$(".problem__overlay").css("display", "block");
			},
			complete: function(){
				$(".problem__overlay").css("display", "none");
			},
			success: function(responseText)
			{                   
                HtmlText = responseText
                $(".practice-container").html(HtmlText);
                $("#answer").focus();
			}
		});    
}



function MainFuntion(ChildFunction){
    return this[ChildFunction]();
}

function P3WNPlaceValues()
{
	var HtmlText = 'Primary 3-->Whole Numbers-->Place Values';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Number_Notation_Place_Values';
    return AJAXCall(HtmlText,URLText);		
}

function P3WNFiguresToWords() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Figures to Words';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Figures_to_Words';
    return AJAXCall(HtmlText,URLText);
}

function P3WNWordsToFigures() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Words to Figures';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Words_to_Figures';
    return AJAXCall(HtmlText,URLText);
}

function P3WNComparingOrdering() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Comparing and Ordering';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Comparing_Ordering';
    return AJAXCall(HtmlText,URLText);
}

function P3WNNumberPatterns() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Number Patterns';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Patterns';
    return AJAXCall(HtmlText,URLText);
}

function P3WNAddition() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Addition';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Addition';
    return AJAXCall(HtmlText,URLText);
}

function P3WNSubtraction() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Subtraction';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Subtraction';
    return AJAXCall(HtmlText,URLText);
}

function P3WNMultiplication() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Multiplication';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Multiplication';
    return AJAXCall(HtmlText,URLText);
}

function P3WNDivision() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Division';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Division';
    return AJAXCall(HtmlText,URLText);
}

function P3WNWordProblems() 
{            
	var HtmlText = 'Primary 3-->Whole Numbers-->Word Problems';
    var URLText = '/Grade_3_Math_Practice/Whole_Numbers_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P3MOAddition() 
{            
	var HtmlText = 'Primary 3-->Money-->Addition';
    var URLText = '/Grade_3_Math_Practice/Money_Addition';
    return AJAXCall(HtmlText,URLText);
}

function P3MOSubtraction() 
{            
	var HtmlText = 'Primary 3-->Money-->Subtraction';
    var URLText = '/Grade_3_Math_Practice/Money_Subtraction';
    return AJAXCall(HtmlText,URLText);
}

function P3MOWordProblems() 
{            
	var HtmlText = 'Primary 3-->Money-->Word Problems';
    var URLText = '/Grade_3_Math_Practice/Money_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P3TITellingTime() 
{            
	var HtmlText = 'Primary 3-->Time-->Telling Time';
    var URLText = '/Grade_3_Math_Practice/Telling_Time';
    return AJAXCall(HtmlText,URLText);
}

function P3TIConversionTime() 
{            
	var HtmlText = 'Primary 3-->Time-->Conversion of Time';
    var URLText = '/Grade_3_Math_Practice/Time_Conversion_Hours_Minutes';
    return AJAXCall(HtmlText,URLText);
}

function P3TIAddition() 
{            
	var HtmlText = 'Primary 3-->Time-->Addition';
    var URLText = '/Grade_3_Math_Practice/Time_Addition';
    return AJAXCall(HtmlText,URLText);
}

function P3TISubtraction() 
{            
	var HtmlText = 'Primary 3-->Time-->Subtraction';
    var URLText = '/Grade_3_Math_Practice/Time_Subtraction';
    return AJAXCall(HtmlText,URLText);
}

function P3TIDuration() 
{            
	var HtmlText = 'Primary 3-->Time-->Start and Finish Time';
    var URLText = '/Grade_3_Math_Practice/Time_Finding_Duration_Start_Finish';
    return AJAXCall(HtmlText,URLText);
}

function P3TIWordProblems() 
{            
	var HtmlText = 'Primary 3-->Time-->Word Problems';
    var URLText = '/Grade_3_Math_Practice/Time_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}
	
function P3LMMetreCentiMetre() 
{            
	var HtmlText = 'Primary 3-->Length, Mass and Volume-->Metres/Centimetres';
    var URLText = '/Grade_3_Math_Practice/Metres_Centimetres';
    return AJAXCall(HtmlText,URLText);
}
	
function P3LMKiloMetre() 
{            
	var HtmlText = 'Primary 3-->Length, Mass and Volume-->Kilometres/Metres';
    var URLText = '/Grade_3_Math_Practice/Kilometres_Metres';
    return AJAXCall(HtmlText,URLText);
}
	
function P3LMKiloGram() 
{            
	var HtmlText = 'Primary 3-->Length, Mass and Volume-->Kilograms/Grams';
    var URLText = '/Grade_3_Math_Practice/Kilograms_Grams';
    return AJAXCall(HtmlText,URLText);
}
	
function P3LMLitresMilli() 
{            
	var HtmlText = 'Primary 3-->Length, Mass and Volume-->Litres/Millitres';
    var URLText = '/Grade_3_Math_Practice/Litres_Millilitres';
    return AJAXCall(HtmlText,URLText);
}
	
function P3LMWordProblems() 
{            
	var HtmlText = 'Primary 3-->Length, Mass and Volume-->Word Problems';
    var URLText = '/Grade_3_Math_Practice/Length_Mass_Volume_1-Step_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}
	
function P3LMWordProblems_2Steps() 
{            
	var HtmlText = 'Primary 3-->Length, Mass and Volume-->2-Steps Word Problems';
    var URLText = '/Grade_3_Math_Practice/Length_Mass_Volume_2-Step_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

	
function P3ANIdentifying() 
{            
	var HtmlText = 'Primary 3-->Angles-->Identifying Angles';
    var URLText = '/Grade_3_Math_Practice/Identifying_Angles_in_Figures';
    return AJAXCall(HtmlText,URLText);
}
	
function P3ANRightAngle() 
{            
	var HtmlText = 'Primary 3-->Angles-->Right Angles';
    var URLText = '/Grade_3_Math_Practice/Right_Angles';
    return AJAXCall(HtmlText,URLText);
}

function P3BGBarGraphs() 
{            
	var HtmlText = 'Primary 3-->Bar Graphs-->Interpreting Graphs';
    var URLText = '/Grade_3_Math_Practice/Bar_Graphs';
    return AJAXCall(HtmlText,URLText);
}

function P3APSquareUnits() 
{            
	var HtmlText = 'Primary 3-->Area and Perimeter-->Area in Square Units';
    var URLText = '/Grade_3_Math_Practice/Area_in_Square_Units';
    return AJAXCall(HtmlText,URLText);
}

function P3APSquareCmM() 
{            
	var HtmlText = 'Primary 3-->Area and Perimeter-->Area in Square cm / Square m';
    var URLText = '/Grade_3_Math_Practice/Area_in_Square_cm_Square_m';
    return AJAXCall(HtmlText,URLText);
}

function P3APPerimeter() 
{            
	var HtmlText = 'Primary 3-->Area and Perimeter-->Perimeter of Squares/Rectangles';
    var URLText = '/Grade_3_Math_Practice/Perimeter_of_Squares_Rectangles';
    return AJAXCall(HtmlText,URLText);
}

function P3APArea() 
{            
	var HtmlText = 'Primary 3-->Area and Perimeter-->Area of Squares/Rectangles';
    var URLText = '/Grade_3_Math_Practice/Area_of_Squares_Rectangles';
    return AJAXCall(HtmlText,URLText);
}

function P3APWordProblems() 
{            
	var HtmlText = 'Primary 3-->Area and Perimeter-->Word Problems';
    var URLText = '/Grade_3_Math_Practice/Area_Perimeter_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P3FRWhatIsFractions() 
{            
	var HtmlText = 'Primary 3-->Fractions-->What is a Fraction?';
    var URLText = '/Grade_3_Math_Practice/What_is_a_Fraction';
    return AJAXCall(HtmlText,URLText);
}

function P3FREquivalentFractions() 
{            
	var HtmlText = 'Primary 3-->Fractions-->Equivalent Fractions';
    var URLText = '/Grade_3_Math_Practice/Equivalent-Fraction';
    return AJAXCall(HtmlText,URLText);
}

function P3FRSimplifyingFractions() 
{            
	var HtmlText = 'Primary 3-->Fractions-->Simplifying Fractions';
    var URLText = '/Grade_3_Math_Practice/Simplifying-Fractions';
    return AJAXCall(HtmlText,URLText);
}

function P3FRComparingOrdering() 
{            
	var HtmlText = 'Primary 3-->Fractions-->Comparing and Ordering Fractions';
    var URLText = '/Grade_3_Math_Practice/Comparing-and-Ordering-Fractions';
    return AJAXCall(HtmlText,URLText);
}

function P3FRAddition() 
{            
	var HtmlText = 'Primary 3-->Fractions-->Adding Fractions';
    var URLText = '/Grade_3_Math_Practice/Adding-Fractions';
    return AJAXCall(HtmlText,URLText);
}

function P3FRSubtraction() 
{            
	var HtmlText = 'Primary 3-->Fractions-->Subtracting Fractions';
    var URLText = '/Grade_3_Math_Practice/Subtracting-Fractions';
    return AJAXCall(HtmlText,URLText);
}

function P3PPPerpendicularParallel() 
{            
	var HtmlText = 'Primary 3-->Identifying Perpendicular and Parallel Lines';
    var URLText = '/Grade_3_Math_Practice/Identifying_Perpendicular_Parallel_Lines';
    return AJAXCall(HtmlText,URLText);
}

function P4WholeNumbersPlaceValues() 
{                                  
	var HtmlText = 'Primary 4-->Whole Numbers-->Number Notation and Place Values';
    var URLText = '/Grade_4_Math_Practice/Whole_Numbers_Place_Values';
    return AJAXCall(HtmlText,URLText);
}

function P4WholeNumbersWriteInWords() 
{                                  
	var HtmlText = 'Primary 4-->Whole Numbers-->Write in Words';
    var URLText = '/Grade_4_Math_Practice/Whole_Numbers_Write_Words';
    return AJAXCall(HtmlText,URLText);
}
	
function P4WholeNumbersWriteInFigures() 
{            
	var HtmlText = 'Primary 4-->Whole Numbers-->Write in Figures';
    var URLText = '/Grade_4_Math_Practice/Whole_Numbers_Write_Figures';
    return AJAXCall(HtmlText,URLText);
}
	
function P4WholeNumbersComparingOrdering() 
{                                  
	var HtmlText = 'Primary 4-->Whole Numbers-->Comparing and Ordering';
    var URLText = '/Grade_4_Math_Practice/Whole_Numbers_Comparing_Ordering';
    return AJAXCall(HtmlText,URLText);
}
	
function P4WholeNumbersRoundingOff() 
{                                  
	var HtmlText = 'Primary 4-->Whole Numbers-->Rounding Off';
    var URLText = '/Grade_4_Math_Practice/Whole_Numbers_Rounding_Off';
    return AJAXCall(HtmlText,URLText);
}
	
function P4WholeNumbersFactorMultiple() 
{                                  
	var HtmlText = 'Primary 4-->Whole Numbers-->Factors and Multiples';
    var URLText = '/Grade_4_Math_Practice/Whole_Numbers_Factors_Multiples';
    return AJAXCall(HtmlText,URLText);
}

function P4WholeNumbersMutliplyDivide() 
{                                 
	var HtmlText = 'Primary 4-->Whole Numbers-->Multiplication and Division';
    var URLText = '/Grade_4_Math_Practice/Whole_Numbers_Multiplication_Division';
    return AJAXCall(HtmlText,URLText);
}

function P4WNWordProblems() 
{            
	var HtmlText = 'Primary 4-->Whole Numbers-->Word Problems';
    var URLText = '/Grade_4_Math_Practice/Whole_Numbers_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P4FractionsMixedImproper() 
{                                  
	var HtmlText = 'Primary 4-->Fractions-->Mixed Numbers and Improper Fractions';
    var URLText = '/Grade_4_Math_Practice/Mixed_Numbers_Improper_Fractions';
    return AJAXCall(HtmlText,URLText);
}
	
function P4FractionsSimplifying() 
{                                    
	var HtmlText = 'Primary 4-->Fractions-->Simplifying Fractions';
    var URLText = '/Grade_4_Math_Practice/Fractions_Simplifying';
    return AJAXCall(HtmlText,URLText);
}

	
function P4FractionsAdd() 
{                                 
	var HtmlText = 'Primary 4-->Fractions-->Add Like Fractions';
    var URLText = '/Grade_4_Math_Practice/Add_Like_Related_Fractions';
    return AJAXCall(HtmlText,URLText);
}
	
function P4FractionsSubtract() 
{                                   
	var HtmlText = 'Primary 4-->Fractions-->Subtract Like Fractions';
    var URLText = '/Grade_4_Math_Practice/Subtract_Like_Related_Fractions';
    return AJAXCall(HtmlText,URLText);
}

function P4FractionsMultiplication() 
{                                  
	var HtmlText = 'Primary 4-->Fractions-->Multiply Fractions and Whole Number';
    var URLText = '/Grade_4_Math_Practice/Multiplication_Fractions_Whole_Numbers';
    return AJAXCall(HtmlText,URLText);
}

function P4FRWordProblems() 
{                                   
	var HtmlText = 'Primary 4-->Fractions-->Word Problems';
	var URLText = '/Grade_4_Math_Practice/Fractions_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P4DATablesBarGraphs() 
{                                   
	var HtmlText = 'Primary 4-->Data Analysis-->Tables and Bar Graphs';
    var URLText = '/Grade_4_Math_Practice/Data_Analysis_Tables_Bar_Graphs';
    return AJAXCall(HtmlText,URLText);
}

function P4DALineGraphs() 
{                                   
	var HtmlText = 'Primary 4-->Data Analysis-->Line Graphs';
    var URLText = '/Grade_4_Math_Practice/Data_Analysis_Line_Graphs';
    return AJAXCall(HtmlText,URLText);
}

function P4DecimalsTenths() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Notation and Place Values - Tenths';
    var URLText = '/Grade_4_Math_Practice/Decimals_Tenths';
    return AJAXCall(HtmlText,URLText);
}
	
function P4DecimalsHundredths() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Notation and Place Values - Hundredths';
    var URLText = '/Grade_4_Math_Practice/Decimals_Hundredths';
    return AJAXCall(HtmlText,URLText);
}

function P4DecimalsThousandths() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Notation and Place Values - Thousandths';
    var URLText = '/Grade_4_Math_Practice/Decimals_Thousandths';
    return AJAXCall(HtmlText,URLText);
}
	
function P4DecimalsComparingOrdering() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Comparing and Ordering';
    var URLText = '/Grade_4_Math_Practice/Decimals_Comparing_Ordering';
    return AJAXCall(HtmlText,URLText);
}

function P4DecimalsRoundingOff() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Rounding Off';
    var URLText = '/Grade_4_Math_Practice/Decimals_Rounding_Off';
    return AJAXCall(HtmlText,URLText);
}
	
function P4DecimalsFractions() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Fractions';
    var URLText = '/Grade_4_Math_Practice/Decimals_Fractions';
    return AJAXCall(HtmlText,URLText);
}
	
function P4DecimalsAddSub() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Addition/Subtaction';
    var URLText = '/Grade_4_Math_Practice/Decimals_Addition_Subtraction';
    return AJAXCall(HtmlText,URLText);
}
	
function P4DecimalsMultiplyDivide() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Multiplication/Division';
    var URLText = '/Grade_4_Math_Practice/Decimals_Multiplication_Division';
    return AJAXCall(HtmlText,URLText);
}

function P4DCWordProblems() 
{            
	var HtmlText = 'Primary 4-->Decimals-->Word Problems';
    var URLText = '/Grade_4_Math_Practice/Decimals_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P4MTTime24Hrs() 
{                                 
	var HtmlText = 'Primary 4-->Measurement-->24-Hour Clock';
    var URLText = '/Grade_4_Math_Practice/Measurement_24-Hour_Clock';
    return AJAXCall(HtmlText,URLText);
}

function P4MTTimeDuration() 
{            
	var HtmlText = 'Primary 4-->Measurement-->Time Duration';
    var URLText = '/Grade_4_Math_Practice/Measurement_Time_Duration';
    return AJAXCall(HtmlText,URLText);
}

function P4MTPerimeter() 
{            
	var HtmlText = 'Primary 4-->Measurement-->Perimeter';
    var URLText = '/Grade_4_Math_Practice/Perimeter_Rectangle_Squares';
    return AJAXCall(HtmlText,URLText);
}

function P4MTArea() 
{            
	var HtmlText = 'Primary 4-->Measurement-->Area';
    var URLText = '/Grade_4_Math_Practice/Area_Rectangle_Squares';
    return AJAXCall(HtmlText,URLText);
}
	
function P4MTCompositeFigures() 
{            
	var HtmlText = 'Primary 4-->Measurement-->Composite Figures';
    var URLText = '/Grade_4_Math_Practice/Measurement_Composite_Figures';
    return AJAXCall(HtmlText,URLText);
}

function P5WholeNumbersWriteInWords() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Write in words';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Write_Words';
    return AJAXCall(HtmlText,URLText);
}
	
function P5WholeNumbersWriteInFigures() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Write in figures';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Write_Figures';
    return AJAXCall(HtmlText,URLText);
}
	
function P5WholeNumbersPlaceValue() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Place Value';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Place_Values';
    return AJAXCall(HtmlText,URLText);
}
	
function P5WholeNumbersComparingAndOrdering() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Comparing and ordering';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Comparing_Ordering';
    return AJAXCall(HtmlText,URLText);
}
	
function P5WholeNumbersFindPattern() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Find pattern';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Find_Pattern';
    return AJAXCall(HtmlText,URLText);
}

function P5WholeNumbersApproximationEstimation() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Approximation/Estimation';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Approximation_Estimation';
    return AJAXCall(HtmlText,URLText);
}
	
function P5WholeNumbersMultiplyDivide() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Multiply/Divide by 10s, 100s and 1000s';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Multiplication_Division';
    return AJAXCall(HtmlText,URLText);
}

function P5WholeNumbersOrderOfOperation() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Order of operation';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Order_Operations';
    return AJAXCall(HtmlText,URLText);
}
	
function P5WholeNumbersWordProblems() 
{            
	var HtmlText = 'Primary 5-->Whole Numbers-->Word problems';
    var URLText = '/Grade_5_Math_Practice/Whole_Numbers_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P5FractionsAddSubProperFractions() 
{            
	var HtmlText = 'Primary 5-->Fractions-->Add/Subtract proper fractions';
    var URLText = '/Grade_5_Math_Practice/Add_Subtract_Proper_Fractions';
    return AJAXCall(HtmlText,URLText);
}
	
function P5FractionsAddSubMixedFractions() 
{            
	var HtmlText = 'Primary 5-->Fractions-->Add/Subtract mixed fractions';
    var URLText = '/Grade_5_Math_Practice/Add_Subtract_Mixed_Fractions';
    return AJAXCall(HtmlText,URLText);
}
	
function P5FractionsMultProperImproperFractions() 
{                       
	var HtmlText = 'Primary 5-->Fractions-->Multiply proper/improper fractions';
    var URLText = '/Grade_5_Math_Practice/Multiply_Proper_Improper_Fractions';
    return AJAXCall(HtmlText,URLText);
}

function P5FractionsMultMixedFractions() 
{            
	var HtmlText = 'Primary 5-->Fractions-->Multiply mixed fractions';
    var URLText = '/Grade_5_Math_Practice/Multiply_Mixed_Fraction_Whole_Number';
    return AJAXCall(HtmlText,URLText);
}

function P5FractionsDivideProperFractions() 
{            
	var HtmlText = 'Primary 5-->Fractions-->Divide proper fractions';
    var URLText = '/Grade_5_Math_Practice/Divide_Proper_Fraction_Whole_Number';
    return AJAXCall(HtmlText,URLText);
}

function P5FractionsWordProblems() 
{            
	var HtmlText = 'Primary 5-->Fractions-->Word Problems';
    var URLText = '/Grade_5_Math_Practice/Fractions_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P5DecimalsMultiplyDivide() 
{            
	var HtmlText = 'Primary 5-->Decimal-->Multiply/Divide by 10,100,1000';
    var URLText = '/Grade_5_Math_Practice/Decimals_Multiply_Divide';
    return AJAXCall(HtmlText,URLText);
}
	
function P5DecimalsRounding() 
{            
	var HtmlText = 'Primary 5-->Decimal-->Rounding off';
    var URLText = '/Grade_5_Math_Practice/Decimals_Rounding_Off';
    return AJAXCall(HtmlText,URLText);
}
    	    	
function P5DecimalsWordProblems() 
{            
	var HtmlText = 'Primary 5-->Decimal-->Word Problems';
    var URLText = '/Grade_5_Math_Practice/Decimals_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P5PercentageExpressAsPercent() 
{            
	var HtmlText = 'Primary 5-->Percentage-->Express as percent';
    var URLText = '/Grade_5_Math_Practice/Express_as_Percentage';
    return AJAXCall(HtmlText,URLText);
}
	
function P5PercentageExpressAsDecimal() 
{            
	var HtmlText = 'Primary 5-->Percentage-->Express as decimal';
    var URLText = '/Grade_5_Math_Practice/Express_as_Decimal';
    return AJAXCall(HtmlText,URLText);
}
	
function P5PercentageExpressAsFraction() 
{            
	var HtmlText = 'Primary 5-->Percentage-->Express as fraction';
    var URLText = '/Grade_5_Math_Practice/Express_as_Fraction';
    return AJAXCall(HtmlText,URLText);
}
    	    	
function P5PercentageWordProblems() 
{            
	var HtmlText = 'Primary 5-->Percentage-->Word Problems';
    var URLText = '/Grade_5_Math_Practice/Percentage_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P5RatioSimplestForm() 
{            
	var HtmlText = 'Primary 5-->Ratio-->Ratio in simplest form';
    var URLText = '/Grade_5_Math_Practice/Ratio_Simplest_Form';
    return AJAXCall(HtmlText,URLText);
}
	
function P5RatioMissingNumber() 
{            
	var HtmlText = 'Primary 5-->Ratio-->Find the missing number';
    var URLText = '/Grade_5_Math_Practice/Ratio_Missing_Number';
    return AJAXCall(HtmlText,URLText);
}

function P5RatioWordProblems() 
{            
	var HtmlText = 'Primary 5-->Ratio-->Word Problems';
    var URLText = '/Grade_5_Math_Practice/Ratio_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P5MeasurementUnitConversion() 
{            
	var HtmlText = 'Primary 5-->Measurement-->Unit conversion';
    var URLText = '/Grade_5_Math_Practice/Measurement_Unit_Conversion';
    return AJAXCall(HtmlText,URLText);
}
    	    	
function P5MeasurementAreaOfTriangle() 
{            
	var HtmlText = 'Primary 5-->Measurement-->Area of triangle';
    var URLText = '/Grade_5_Math_Practice/Measurement_Area_Triangle';
    return AJAXCall(HtmlText,URLText);
}
	
function P5MeasurementVolume() 
{            
	var HtmlText = 'Primary 5-->Measurement-->Volume of cube/cuboid';
    var URLText = '/Grade_5_Math_Practice/Measurement_Volume_Cube_Cuboid';
    return AJAXCall(HtmlText,URLText);
}                            	

function P5MeasurementWordProblems() 
{            
	var HtmlText = 'Primary 5-->Measurement-->Word Problems';
    var URLText = '/Grade_5_Math_Practice/Measurement_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}                            	

function P5GeometryAngles() 
{            
	var HtmlText = 'Primary 5-->Geometry-->Angles';
    var URLText = '/Grade_5_Math_Practice/Geometry_Find_Unknown_Angles';
    return AJAXCall(HtmlText,URLText);
}

function P5GeometryTriangles() 
{            
	var HtmlText = 'Primary 5-->Geometry-->Triangles';
    var URLText = '/Grade_5_Math_Practice/Triangles_Find_Unknown_Angles';
    return AJAXCall(HtmlText,URLText);
}

function P5GeometryFourSided() 
{            
	var HtmlText = 'Primary 5-->Geometry-->Four sided figures';
    var URLText = '/Grade_5_Math_Practice/Find_Unknown_Angles_in_Four_Sided_Figures';
    return AJAXCall(HtmlText,URLText);
}

function P5DataAnalysisAverage() 
{            
	var HtmlText = 'Primary 5-->Data Analysis-->Find Average';
    var URLText = '/Grade_5_Math_Practice/Data_Analysis_Find_Average';
    return AJAXCall(HtmlText,URLText);
}

function P5DataAnalysisTotal() 
{            
	var HtmlText = 'Primary 5-->Data Analysis-->Find Total';
    var URLText = '/Grade_5_Math_Practice/Data_Analysis_Find_Total';
    return AJAXCall(HtmlText,URLText);
}

function P5DataAnalysisWordProblems() 
{            
	var HtmlText = 'Primary 5-->Data Analysis-->Word Problems';
    var URLText = '/Grade_5_Math_Practice/Data_Analysis_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P6AGSimplifyingExpression() 
{            
	var HtmlText = 'Primary 6-->Algebra-->Simplifying Algebraic Expression';
    var URLText = '/Grade_6_Math_Practice/Algebra_Simplify_Expressions';
    return AJAXCall(HtmlText,URLText);
}

function P6AGEvaluationExpression() 
{            
	var HtmlText = 'Primary 6-->Algebra-->Evaluating Algebraic Expression';
    var URLText = '/Grade_6_Math_Practice/Algebra_Evaluate_Expressions';
    return AJAXCall(HtmlText,URLText);
}

function P6AGWordProblems() 
{            
	var HtmlText = 'Primary 6-->Algebra-->Word Problems';
    var URLText = '/Grade_6_Math_Practice/Algebra_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P6FRDivideWholeNumber() 
{            
	var HtmlText = 'Primary 6-->Fractions-->Divide whole number by proper fraction';
    var URLText = '/Grade_6_Math_Practice/Divide_Whole_Number_Proper_Fraction';
    return AJAXCall(HtmlText,URLText);
}

function P6FRDivideProperFraction() 
{            
	var HtmlText = 'Primary 6-->Fractions-->Divide proper fraction by proper fraction';
    var URLText = '/Grade_6_Math_Practice/Divide_Proper_Fraction_by_Proper_Fraction';
    return AJAXCall(HtmlText,URLText);
}	

function P6FRWordProblems() 
{            
	var HtmlText = 'Primary 6-->Fractions-->Word Problems';
    var URLText = '/Grade_6_Math_Practice/Fractions_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P6SPDTS() 
{            
	var HtmlText = 'Primary 6-->Speed-->Distance, Time and Speed';
    var URLText = '/Grade_6_Math_Practice/Speed_Distance_Time';
    return AJAXCall(HtmlText,URLText);
}

function P6SPWordProblems() 
{            
	var HtmlText = 'Primary 6-->Speed-->Word Problems';
    var URLText = '/Grade_6_Math_Practice/Speed_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P6RTWordProblems() 
{            
	var HtmlText = 'Primary 6-->Ratio-->Word Problems';
    var URLText = '/Grade_6_Math_Practice/Ratio_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P6PRFindWhole() 
{            
	var HtmlText = 'Primary 6-->Percentage-->Finding whole given part and percentage';
    var URLText = '/Grade_6_Math_Practice/Percentage_Find_Whole_Given_Part';
    return AJAXCall(HtmlText,URLText);
}

function P6PRIncDec() 
{            
	var HtmlText = 'Primary 6-->Percentage-->Finding percentage increase/decrease';
    var URLText = '/Grade_6_Math_Practice/Percentage_Increase_Decrease';
    return AJAXCall(HtmlText,URLText);
}
	
function P6PRWordProblems() 
{            
	var HtmlText = 'Primary 6-->Percentage-->Word Problems';
    var URLText = '/Grade_6_Math_Practice/Percentage_Word_Problems';
    return AJAXCall(HtmlText,URLText);
}

function P6DAWordProblems() 
{            
	var HtmlText = 'Primary 6-->Data Analysis-->Word Problems';
    var URLText = '/Grade_6_Math_Practice/Data_Analysis_Pie_Chart';
    return AJAXCall(HtmlText,URLText);
}

function P6MTRadius() 
{            
	var HtmlText = 'Primary 6-->Measurement-->Radius/diameter of a circle';
    var URLText = '/Grade_6_Math_Practice/Measurement_Circle_Radius_Diameter';
    return AJAXCall(HtmlText,URLText);
}

function P6MTCircumference() 
{            
	var HtmlText = 'Primary 6-->Measurement-->Circumference of a circle';
    var URLText = '/Grade_6_Math_Practice/Measurement_Circle_Circumference';
    return AJAXCall(HtmlText,URLText);
}

function P6MTArea() 
{            
	var HtmlText = 'Primary 6-->Measurement-->Area of a circle';
    var URLText = '/Grade_6_Math_Practice/Measurement_Circle_Area';
    return AJAXCall(HtmlText,URLText);
}

function P6MTSemiPerimeter() 
{            
	var HtmlText = 'Primary 6-->Measurement-->Perimeter of a semicircle/quadrant';
    var URLText = '/Grade_6_Math_Practice/Measurement_Semi_Circle_Quadrant_Perimeter';
    return AJAXCall(HtmlText,URLText);
}

function P6MTSemiArea() 
{            
	var HtmlText = 'Primary 6-->Measurement-->Area of a semicircle/quadrant';
    var URLText = '/Grade_6_Math_Practice/Measurement_Semi_Circle_Quadrant_Area';
    return AJAXCall(HtmlText,URLText);
}

function P6MTComposite() 
{            
	var HtmlText = 'Primary 6-->Measurement-->Area/perimeter of a composite figure';
    var URLText = '/Grade_6_Math_Practice/Area_Perimeter_of_Composite_Figures';
    return AJAXCall(HtmlText,URLText);
}

function P6MTVolume() 
{            
	var HtmlText = 'Primary 6-->Measurement-->Volume of a cube/cuboid';
    var URLText = '/Grade_6_Math_Practice/Measurement_Volume_Cube_Cuboid';
    return AJAXCall(HtmlText,URLText);
}
