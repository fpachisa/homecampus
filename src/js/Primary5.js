$(document).ready(function() 
{	
	$("#P5MT_ConversionOfUnits").click(function() 
			{ 		
				clearStyle();
				$("#P5MT_ConversionOfUnits_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 011;
				var learnURL = "";
				var practiceURL = "/Grade_5_Math_Practice/Measurement_Unit_Conversion";
				var worksheetURL = "/Grade_5_Math_Worksheets/Measurement_Unit_Conversion";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P5MeasurementUnitConversion").show("fast");
			});
	
	$("#P5MT_AreaOfTriangle").click(function() 
			{ 		
				clearStyle();
				$("#P5MT_AreaOfTriangle_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-5/Measurement/Area-of-Triangle";
				var practiceURL = "/Grade_5_Math_Practice/Measurement_Area_Triangle";
				var worksheetURL = "/Grade_5_Math_Worksheets/Measurement_Area_Triangle";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P5MeasurementAreaOfTriangle").show("fast");
			});
	
	$("#P5MT_VolumeCubesCuboids3").click(function() 
			{ 		
				clearStyle();
				$("#P5MT_VolumeCubesCuboids3_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-5/Measurement/Introduction-to-volume-of-cube-cuboid-part-3";
				var practiceURL = "/Grade_5_Math_Practice/Measurement_Volume_Cube_Cuboid";
				var worksheetURL = "/Grade_5_Math_Worksheets/Measurement_Volume_Cube_Cuboid";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P5MeasurementVolume").show("fast");
			});
	
	$("#P5MT_WordProblems").click(function() 
			{ 		
				clearStyle();
				$("#P5MT_WordProblems_DIV").css({"background-color":"#F5857B"});
				$("#ActionButtons").html("");
				var buttonRequired = 011;
				var learnURL = "";
				var practiceURL = "/Grade_5_Math_Practice/Measurement_Word_Problems";
				var worksheetURL = "/Grade_5_Math_Worksheets/Measurement_Word_Problems";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P5MeasurementWordProblems").show("fast");
			});
	
	$("#P5RT_SimplifyingRatios").click(function() 
			{ 		
				clearStyle();
				$("#P5RT_SimplifyingRatios_DIV").css({"background-color":"#FAA756"});
				$("#ActionButtons").html("");
				var buttonRequired = 111;
				var learnURL = "/Learn/Primary-Grade-5/Ratio/Simplifying";
				var practiceURL = "/Grade_5_Math_Practice/Ratio_Simplest_Form";
				var worksheetURL = "/Grade_5_Math_Worksheets/Ratio_Simplest_Form";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P5RatioSimplestForm").show("fast");
			});
	
	$("#P5RT_FindingMissingNumber").click(function() 
			{ 		
				clearStyle();
				$("#P5RT_FindingMissingNumber_DIV").css({"background-color":"#FAA756"});
				$("#ActionButtons").html("");
				var buttonRequired = 011;
				var learnURL = "";
				var practiceURL = "/Grade_5_Math_Practice/Ratio_Missing_Number";
				var worksheetURL = "/Grade_5_Math_Worksheets/Ratio_Missing_Number";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P5RatioMissingNumber").show("fast");
			});
	
	$("#P5RT_WordProblems").click(function() 
			{ 		
				clearStyle();
				$("#P5RT_WordProblems_DIV").css({"background-color":"#FAA756"});
				$("#ActionButtons").html("");
				var buttonRequired = 011;
				var learnURL = "";
				var practiceURL = "/Grade_5_Math_Practice/Ratio_Word_Problems";
				var worksheetURL = "/Grade_5_Math_Worksheets/Ratio_Word_Problems";
				$("#ActionButtons").html("");
				$("#ActionButtons").html(generateActionButtons(buttonRequired,learnURL,practiceURL,worksheetURL));
				$("#P5RatioWordProblems").show("fast");
			});

});

