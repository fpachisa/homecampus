function Grade7SaveAnswer(question_id,question_type,answer_id,entered_answer,student_id)
{
	var data = {question_id:question_id,question_type:question_type,answer_id:answer_id,entered_answer:entered_answer,student_id:student_id};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Book-Save-Answer",
		data: data,
		success: function(responseText)
		{
		}
	});
}

function Grade7SubmitAnswer(student_id,question_type,answers)
{
	var data = {student_id:student_id,question_type:question_type,answers:answers};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Book-Submit-Answer",
		data: data,
		success: function(responseText)
		{
			location.reload();
		}
	});
}

function Grade7ClearAnswer(student_id,answer_ids)
{
	var data = {student_id:student_id,answer_ids:answer_ids};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Book-Clear-Answer",
		data: data,
		success: function(responseText)
		{
			location.reload();
		}
	});
}

function Grade7SaveTestTime(test_id,total_seconds_elapsed,student_id,loadPage)
{
	var data = {test_id:test_id,total_seconds_elapsed:total_seconds_elapsed,student_id:student_id};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Topical-Test-Save-Time",
		data: data,
		success: function(responseText)
		{
			location.reload();
		}
	});
}

function Grade7SaveTestAnswer(test_id,question_id,answer_id,entered_answer,student_id,question_marks,elapsed_time)
{
	var data = {test_id:test_id,question_id:question_id,answer_id:answer_id,entered_answer:entered_answer,student_id:student_id,question_marks:question_marks,elapsed_time:elapsed_time};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Topical-Test-Save-Answer",
		data: data,
		success: function(responseText)
		{
		}
	});
}

function Grade7SubmitTest(test_id,student_id,total_seconds_elapsed,answer_ids)
{
	var data = {test_id:test_id,student_id:student_id,total_seconds_elapsed:total_seconds_elapsed,answer_ids:answer_ids};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Topical-Test-Submit",
		data: data,
		success: function(responseText)
		{
			location.reload();
		}
	});
}