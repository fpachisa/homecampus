$(document).ready(function() 
{
	$("#P6AG").click(function() 
		{ 		
			hideTopics();
			clearStyle();
			$("#topics").css({"margin-top":"0px"});
			$("#P6AGTopics").show("fast");
		});

	$("#P6FR").click(function() 
			{ 		
				hideTopics();
				clearStyle();
				$("#topics").css({"margin-top":"60px"});
				$("#P6FRTopics").show("fast");
			});

	$("#P6SP").click(function() 
			{ 		
				hideTopics();
				clearStyle();
				$("#topics").css({"margin-top":"125px"});
				$("#P6SPTopics").show("fast");
			});

	$("#P6RT").click(function() 
			{ 		
				hideTopics();
				clearStyle();
				$("#topics").css({"margin-top":"190px"});
				$("#P6RTTopics").show("fast");
			});

	$("#P6MT").click(function() 
			{ 		
				hideTopics();
				clearStyle();
				$("#topics").css({"margin-top":"220px"});
				$("#P6MTTopics").show("fast");
			});

	$("#P6DA").click(function() 
			{ 		
				hideTopics();
				clearStyle();
				$("#topics").css({"margin-top":"320px"});
				$("#P6DATopics").show("fast");
			});

	$("#P6PR").click(function() 
			{ 		
				hideTopics();
				clearStyle();
				$("#topics").css({"margin-top":"405px"});
				$("#P6PRTopics").show("fast");
			});

	$("#P6GT").click(function() 
			{ 		
				hideTopics();
				clearStyle();
				$("#topics").css({"margin-top":"475px"});
				$("#P6GTTopics").show("fast");
			});

	
	$("#P6AG_SimplifyingAlgebraicExpressions").click(function() 
			{ 		
				clearStyle();
				$("#P6AG_SimplifyingAlgebraicExpressions_DIV").css({"background-color":"#F6EB68"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions";
				var practiceURL = "/Grade_6_Math_Practice/Algebra_Simplify_Expressions";
				var worksheetURL = "/Grade_6_Math_Worksheets/Algebra_Simplify_Expressions";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6AGSimplifyingExpression").show("fast");
			});
	
	$("#P6AG_EvaluatingAlgebraicExpressions").click(function() 
			{ 		
				clearStyle();
				$("#P6AG_EvaluatingAlgebraicExpressions_DIV").css({"background-color":"#F6EB68"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions";
				var practiceURL = "/Grade_6_Math_Practice/Algebra_Evaluate_Expressions";
				var worksheetURL = "/Grade_6_Math_Worksheets/Algebra_Evaluate_Expressions";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6AGEvaluationExpression").show("fast");
			});
	
	$("#P6AG_WordProblems").click(function() 
			{ 		
				clearStyle();
				$("#P6AG_WordProblems_DIV").css({"background-color":"#F6EB68"});
				$("#ActionButtons").html("");
				var buttonRequired = 011;
				var learnURL = "";
				var practiceURL = "/Grade_6_Math_Practice/Algebra_Word_Problems";
				var worksheetURL = "/Grade_6_Math_Worksheets/Algebra_Word_Problems";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6AGWordProblems").show("fast");
			});
	
	$("#P6FR_DividingWholeNumberByProperFraction").click(function() 
			{ 		
				clearStyle();
				$("#P6FR_DividingWholeNumberByProperFraction_DIV").css({"background-color":"#E4B3EC"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Fractions/Dividing-Whole-Number-by-Proper-Fraction";
				var practiceURL = "/Grade_6_Math_Practice/Divide_Whole_Number_Proper_Fraction";
				var worksheetURL = "/Grade_6_Math_Worksheets/Fractions_Divide_Whole_Number";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6FRDivideWholeNumber").show("fast");
			});
	
	$("#P6FR_DividingProperFractionByProperFraction").click(function() 
			{ 		
				clearStyle();
				$("#P6FR_DividingProperFractionByProperFraction_DIV").css({"background-color":"#E4B3EC"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Fractions/Dividing-Proper-Fraction-by-Proper-Fraction";
				var practiceURL = "/Grade_6_Math_Practice/Divide_Proper_Fraction_by_Proper_Fraction";
				var worksheetURL = "/Grade_6_Math_Worksheets/Fractions_Divide_Proper";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6FRDivideProperFraction").show("fast");
			});
	
	$("#P6FR_WordProblems").click(function() 
			{ 		
				clearStyle();
				$("#P6FR_WordProblems_DIV").css({"background-color":"#E4B3EC"});
				$("#ActionButtons").html("");
				var buttonRequired = 011;
				var learnURL = "";
				var practiceURL = "/Grade_6_Math_Practice/Fractions_Word_Problems";
				var worksheetURL = "/Grade_6_Math_Worksheets/Fractions_Word_Problems";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6FRWordProblems").show("fast");
			});
	
	$("#P6SP_FindingDistanceTimeSpeed").click(function() 
			{ 		
				clearStyle();
				$("#P6SP_FindingDistanceTimeSpeed_DIV").css({"background-color":"#3ED6CE"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Speed/Distance-Time-Speed";
				var practiceURL = "/Grade_6_Math_Practice/Speed_Distance_Time";
				var worksheetURL = "/Grade_6_Math_Worksheets/Speed_Distance_Time";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6SPDTS").show("fast");
			});
	
	$("#P6SP_WordProblems").click(function() 
			{ 		
				clearStyle();
				$("#P6SP_WordProblems_DIV").css({"background-color":"#3ED6CE"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Speed/Advanced-Word-Problems";
				var practiceURL = "/Grade_6_Math_Practice/Speed_Word_Problems";
				var worksheetURL = "/Grade_6_Math_Worksheets/Speed_Word_Problems";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6SPWordProblems").show("fast");
			});
	
	$("#P6RT_WordProblems").click(function() 
			{ 		
				clearStyle();
				$("#P6RT_WordProblems_DIV").css({"background-color":"#FAA756"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Ratio/Word-Problems";
				var practiceURL = "/Grade_6_Math_Practice/Ratio_Word_Problems";
				var worksheetURL = "/Grade_6_Math_Worksheets/Ratio";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6RTWordProblems").show("fast");
			});
	
	$("#P6MT_RadiusDiameterCircles").click(function() 
			{ 		
				clearStyle();
				$("#P6MT_RadiusDiameterCircles_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Measurement/Radius-and-Diameter-of-Circle";
				var practiceURL = "/Grade_6_Math_Practice/Measurement_Circle_Radius_Diameter";
				var worksheetURL = "/Grade_6_Math_Worksheets/Measurement_Circle_Radius_Diameter";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6MTRadius").show("fast");
			});
	
	$("#P6MT_CircumferenceCircles").click(function() 
			{ 		
				clearStyle();
				$("#P6MT_CircumferenceCircles_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Measurement/Circumference-of-Circle";
				var practiceURL = "/Grade_6_Math_Practice/Measurement_Circle_Circumference";
				var worksheetURL = "/Grade_6_Math_Worksheets/Measurement_Circle_Circumference";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6MTCircumference").show("fast");
			});
	
	$("#P6MT_AreaCircles").click(function() 
			{ 		
				clearStyle();
				$("#P6MT_AreaCircles_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Measurement/Area-of-Circle";
				var practiceURL = "/Grade_6_Math_Practice/Measurement_Circle_Area";
				var worksheetURL = "/Grade_6_Math_Worksheets/Measurement_Circle_Area";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6MTArea").show("fast");
			});
	
	$("#P6MT_PerimeterSemicirclesQuadrants").click(function() 
			{ 		
				clearStyle();
				$("#P6MT_PerimeterSemicirclesQuadrants_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 011;
				var learnURL = "";
				var practiceURL = "/Grade_6_Math_Practice/Measurement_Semi_Circle_Quadrant_Perimeter";
				var worksheetURL = "/Grade_6_Math_Worksheets/Measurement_Semi_Circle_Quadrant_Perimeter";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6MTSemiPerimeter").show("fast");
			});
	
	$("#P6MT_AreaSemicirclesQuadrants").click(function() 
			{ 		
				clearStyle();
				$("#P6MT_AreaSemicirclesQuadrants_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 011;
				var learnURL = "";
				var practiceURL = "/Grade_6_Math_Practice/Measurement_Semi_Circle_Quadrant_Area";
				var worksheetURL = "/Grade_6_Math_Worksheets/Measurement_Semi_Circle_Quadrant_Area";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6MTSemiArea").show("fast");
			});
	
	$("#P6MT_AreaPerimeterCompositeFigures").click(function() 
			{ 		
				clearStyle();
				$("#P6MT_AreaPerimeterCompositeFigures_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Area-and-Perimeter-of-Composite-Figures";
				var practiceURL = "/Grade_6_Math_Practice/Area_Perimeter_of_Composite_Figures";
				var worksheetURL = "/Grade_6_Math_Worksheets/Measurement_Composite_Figures";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6MTComposite").show("fast");
			});
	
	$("#P6MT_VolumeCubesCuboids").click(function() 
			{ 		
				clearStyle();
				$("#P6MT_VolumeCubesCuboids_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Measurement/Volume-Cube-Cuboid-Advanced-Word-Problems";
				var practiceURL = "/Grade_6_Math_Practice/Measurement_Volume_Cube_Cuboid";
				var worksheetURL = "/Grade_6_Math_Worksheets/Measurement_Volume_Cube_Cuboid";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6MTVolume").show("fast");
			});
	
	$("#P6DA_PieChartsWordProblems").click(function() 
			{ 		
				clearStyle();
				$("#P6DA_PieChartsWordProblems_DIV").css({"background-color":"#E884B3"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Data-Analysis/Pie-Chart-Word-Problems";
				var practiceURL = "/Grade_6_Math_Practice/Data_Analysis_Pie_Chart";
				var worksheetURL = "/Grade_6_Math_Worksheets/Data_Analysis_Pie_Chart";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6DAWordProblems").show("fast");
			});
	
	$("#P6PR_FindingWhole").click(function() 
			{ 		
				clearStyle();
				$("#P6PR_FindingWhole_DIV").css({"background-color":"#F58BCA"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Percentage/Finding-Whole-Given-Part-and-Percentage";
				var practiceURL = "/Grade_6_Math_Practice/Percentage_Find_Whole_Given_Part";
				var worksheetURL = "/Grade_6_Math_Worksheets/Percentage_Find_Whole_Given_Part";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6PRFindWhole").show("fast");
			});
	
	$("#P6PR_FindingPercentageIncreaseDecrease").click(function() 
			{ 		
				clearStyle();
				$("#P6PR_FindingPercentageIncreaseDecrease_DIV").css({"background-color":"#F58BCA"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Percentage/Finding-Percentage-Increase-Decrease";
				var practiceURL = "/Grade_6_Math_Practice/Percentage_Increase_Decrease";
				var worksheetURL = "/Grade_6_Math_Worksheets/Percentage_Increase_Decrease";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6PRIncDec").show("fast");
			});
	
	$("#P6PR_WordProblems").click(function() 
			{ 		
				clearStyle();
				$("#P6PR_WordProblems_DIV").css({"background-color":"#F58BCA"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-6/Percentage/Advanced-Word-Problems";
				var practiceURL = "/Grade_6_Math_Practice/Percentage_Word_Problems";
				var worksheetURL = "/Grade_6_Math_Worksheets/Percentage_Word_Problems";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P6PRWordProblems").show("fast");
			});

});

function clearStyle()
{
	$("#P6AG_SimplifyingAlgebraicExpressions_DIV").css({"background-color":"white"});
	$("#P6AG_EvaluatingAlgebraicExpressions_DIV").css({"background-color":"white"});
	$("#P6AG_WordProblems_DIV").css({"background-color":"white"});
	$("#P6FR_DividingWholeNumberByProperFraction_DIV").css({"background-color":"white"});
	$("#P6FR_DividingProperFractionByProperFraction_DIV").css({"background-color":"white"});
	$("#P6FR_WordProblems_DIV").css({"background-color":"white"});
	$("#P6SP_FindingDistanceTimeSpeed_DIV").css({"background-color":"white"});
	$("#P6SP_WordProblems_DIV").css({"background-color":"white"});
	$("#P6RT_WordProblems_DIV").css({"background-color":"white"});
	$("#P6MT_RadiusDiameterCircles_DIV").css({"background-color":"white"});
	$("#P6MT_CircumferenceCircles_DIV").css({"background-color":"white"});
	$("#P6MT_AreaCircles_DIV").css({"background-color":"white"});
	$("#P6MT_PerimeterSemicirclesQuadrants_DIV").css({"background-color":"white"});
	$("#P6MT_AreaSemicirclesQuadrants_DIV").css({"background-color":"white"});
	$("#P6MT_AreaPerimeterCompositeFigures_DIV").css({"background-color":"white"});
	$("#P6MT_VolumeCubesCuboids_DIV").css({"background-color":"white"});
	$("#P6DA_PieChartsWordProblems_DIV").css({"background-color":"white"});
	$("#P6PR_FindingWhole_DIV").css({"background-color":"white"});
	$("#P6PR_FindingPercentageIncreaseDecrease_DIV").css({"background-color":"white"});
	$("#P6PR_WordProblems_DIV").css({"background-color":"white"});
	
	$("#ActionButtons").html("");
	
	$("#P6AGSimplifyingExpression").hide("fast");
	$("#P6AGEvaluationExpression").hide("fast");
	$("#P6AGWordProblems").hide("fast");
	$("#P6DAWordProblems").hide("fast");
	$("#P6FRDivideProperFraction").hide("fast");
	$("#P6FRDivideWholeNumber").hide("fast");
	$("#P6FRWordProblems").hide("fast");
	$("#P6MTCircumference").hide("fast");
	$("#P6MTRadius").hide("fast");
	$("#P6MTArea").hide("fast");
	$("#P6MTSemiPerimeter").hide("fast");
	$("#P6MTSemiArea").hide("fast");
	$("#P6MTComposite").hide("fast");
	$("#P6MTVolume").hide("fast");
	$("#P6PRFindWhole").hide("fast");
	$("#P6PRIncDec").hide("fast");
	$("#P6PRWordProblems").hide("fast");
	$("#P6RTWordProblems").hide("fast");
	$("#P6SPDTS").hide("fast");
	$("#P6SPWordProblems").hide("fast");
}

function generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL)
{
	var html = "";
	if (buttonRequired==111)
	{
		html = '<a href="'+learnURL+'"><img src="/images/site/learn_button.png"></a><br><br>';
		html = html + '<a href="'+practiceURL+'"><img src="/images/site/practice_button.png"></a><br><br>';
		html = html + '<a href="'+worksheetURL+'"><img src="/images/site/worksheet_button.png"></a><br><br>';

	}
	else if (buttonRequired==011)
	{
		html = html + '<a href="'+practiceURL+'"><img src="/images/site/practice_button.png"></a><br><br>';
		html = html + '<a href="'+worksheetURL+'"><img src="/images/site/worksheet_button.png"></a><br><br>';		
	}
	return html;
}

function hideTopics()
{
	$("#P6AGTopics").hide("fast");
	$("#P6FRTopics").hide("fast");
	$("#P6SPTopics").hide("fast");
	$("#P6RTTopics").hide("fast");
	$("#P6MTTopics").hide("fast");
	$("#P6DATopics").hide("fast");
	$("#P6PRTopics").hide("fast");
	$("#P6GTTopics").hide("fast");
}

