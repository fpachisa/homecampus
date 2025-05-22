$(document).ready(function() 
 	{ 		
    	
		$("#GenerateTestReport").click(function() 
    	    	{
    				var TestId = $("#tests").val();
    				var URL = "/Tests/GenerateTestReport";
        	        AJAXCall2(URL,TestId);    				
    	    	});
	}
);

function AJAXCall(URL,StudentId)
{            	
	$("#ReportListPractice").hide("fast");
	$("#ReportListTests").hide("fast");
	$("#NoTestsCompleted").hide("fast");
	var URLText = URL
	var data = {StudentId:StudentId};
	$.ajax(
	{
		type: "POST",
		url: URLText,
		data: data,
		success: function(responseText)
		{                   
			$("#ReportContent").html(responseText);
		}
	});    
}

function AJAXCall2(URL,TestId)
{            	
	$("#ReportListPractice").hide("fast");
	$("#ReportListTests").hide("fast");
	$("#NoTestsCompleted").hide("fast");
	var URLText = URL
	var data = {TestId:TestId};
	$.ajax(
	{
		type: "POST",
		url: URLText,
		data: data,
		success: function(responseText)
		{                   
			$("#ReportContent").html(responseText);
		}
	});    
}

function ChildPracticeConceptReport(item)
{
	var StudentId = $(item).attr("id"); 
	var URL = "/Progress/Report_by_Concept";
    AJAXCall(URL,StudentId);    				
}

function ChildPracticeHCRankReport(item)
{
	var StudentId = $(item).attr("id"); 
	var URL = "/Progress/Report_by_HCRank";
    AJAXCall(URL,StudentId);    				
}