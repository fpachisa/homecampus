$(document).ready(function(){ 		
	
	$("#CreateTest").on('click', function(){
		$("#CreateTest").attr("disabled", true );
		var create_user = $("#create_user").val()
    	var username = $("#child").val()
		var grade = $("#grade").val()
		var concept = $("#concept").val()
		var sub_concept = $("#SubTopics").val()
		var display_concept = $("#display_concept").val()
		var class_name = $("#class_name").val()
    	var data = {create_user:create_user,username:username,grade:grade,concept:concept,display_concept:display_concept,class_name:class_name,sub_concept:sub_concept};
    	
		$.ajax({
			type: "POST",
			url: "/Worksheets/GenerateWorksheets",
			data: data,
			success: function(responseText){
				window.location.reload();
				}
			});
	});
});

function TestClick(item)
{
	var TestId = $(item).attr("id"); 
	AJAXCall(TestId);
}

function CompletedTestClick(item,page)
{
	var parameters = $(item).attr("id");
	var parameters = parameters.split(",");
	var TestId = parameters[0];
	var page = parameters[1];
	GenerateReport(TestId,page);
}

function AJAXCall(TestId)
{            	
	//$("#TestPage").hide("fast");
	//$("#TestContent").show("fast");
	var URLText = "/Tests/GetTest"
	var data = {TestId:TestId};
	$.ajax(
	{
		type: "POST",
		url: URLText,
		data: data,
		success: function(responseText)
		{                   
			$("#TestPage").css({"border":"0px"});
			$("#TestPage").html(responseText);
		}
	});    
}

function GenerateReport(TestId,page)
{
	$("#"+page).html('<img style="margin-left:400px;margin-top:80px;" alt="Generating Report" src="/images/site/InProgress.gif">');
	var data = {TestId:TestId};
	$.ajax(
	{
		type: "POST",
		url: "/Tests/GenerateTestReport",
		data: data,
		success: function(responseText)
		{
			$("#"+page).css({"border":"0px"});
			$("#"+page).html(responseText);
		}				
	});
}
