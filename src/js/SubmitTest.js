	//defined a global variable which will be used in explain function
$(document).ready(function() 
{ 		   	
	$("body").on('click', "#tryNext", function() {
			$(this).attr("disabled", true);
			var TestId = $("#TestId").val();
			var counter = $("#counter").val();
    		var answer = $("#answer").val();
    		var next = "Y"
			if (answer == undefined) {
				//if its a MCQ question it will go in this if loop
				answer = $("input:radio[name=answer]:checked").val();
			}
			var data = {TestId:TestId,counter:counter,answer_submitted:answer,next:next};
			console.log(data);
			$.ajax(
			{
				type: "POST",
				url: "/Tests/GetProblems",
				data: data,
				success: function(responseText)
				{                   
					$("#TestPage").html(responseText);
				}				
			});
    	});
	
	$("body").on('click', "#tryPrevious", function() {
		$(this).attr("disabled", true );
		var TestId = $("#TestId").val();
		var counter = $("#counter").val();
		var answer = $("#answer").val();
		var next = "N";
		if (answer == undefined) {
			//if its a MCQ question it will go in this if loop
			answer = $("input:radio[name=answer]:checked").val();
		}
		
		var data = {TestId:TestId,counter:counter,answer_submitted:answer,next:next};
		
		$.ajax({
			type: "POST",
			url: "/Tests/GetProblems",
			data: data,
			success: function(responseText) {                   
				$("#TestPage").html(responseText);
				}
			});
	   });	
	
	$("body").on('click', "#submitTest", function() {
		var TestId = $("#TestId").val();
		var counter = $("#counter").val();
		var answer = $("#answer").val();
		
		if (answer == undefined) {
			//if its a MCQ question it will go in this if loop
			answer = $("input:radio[name=answer]:checked").val();
			}
		
		$("#TestPage").html('<img style="margin-left:auto;margin-right:auto;"alt="Generating Report" src="/images/site/InProgress.gif">');
		
		var data = {TestId:TestId,counter:counter,answer_submitted:answer};
		$.ajax({
			type: "POST",
			url: "/Tests/GenerateTestReport",
			data: data,
			success: function(responseText) {						
				$("#TestPage").html(responseText);
				}				
			});
		});	
});

function GetClickedProblem(counter)
{
	var TestId = $("#TestId").val();
	var current_counter = $("#counter").val();
	var clicked_counter = counter
	var answer = $("#answer").val();
	if (answer == undefined)
	{
		//if its a MCQ question it will go in this if loop
		answer = $("input:radio[name=answer]:checked").val();
	}
	var data = {TestId:TestId,current_counter:current_counter,clicked_counter:clicked_counter,answer_submitted:answer};
	$.ajax(
	{
		type: "POST",
		url: "/Tests/GetClickedProblem",
		data: data,
		success: function(responseText)
		{                   
			$("#TestPage").html(responseText);
		}				
	});
}
