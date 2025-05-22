$(document).ready(function() 
{ 
	if (window.location.hash)
	    {   
			hash_page_name = location.hash;
	    	//removing the hash and loading the appropriate page on page refresh
	    	page_name = hash_page_name.substring(2,hash_page_name.length);

			Grade7BookPageLoadByName(page_name);
			$("#Grade7PageContainer").fadeIn();
			//$("#grade7TOCLink").fadeIn();
	    }
	    
	    else //show the cover page
	    {
			$("#Grade7PageContainer").fadeOut();
			$("#grade7TOCLink").fadeOut();				
			$("#grade7BTOCLink").fadeOut();
			$("#grade7CTOCLink").fadeOut();
	    	//$("#Grade7CoverPageDesktop").fadeIn();   	
	    	$("#Grade7BookShelf").fadeIn();
	    } 
	
	/*
	 * Not using this as the page is loading twice when left or right button is clicked and also the Topical test is not working  
	//to make the back button of the browser work
	$(function(){
	         // Bind the event.
	 	$(window).bind('hashchange', function() { 
	 	}).trigger('hashchange');
      });
	*/
	
	$("#Grade7aCoverPageDesktop").click(
		function(){
			//$("#Grade7CoverPageDesktop").fadeOut();
			$("#Grade7BookShelf").fadeOut();
			Grade7BookPageLoadByNumber(0,1,"7A");
			$("#Grade7PageContainer").fadeIn();
			$("#grade7TOCLink").fadeIn();
			$('html,body').animate({
		        scrollTop: $("#grade7aTopics").offset().top},
		        'slow');
			//window.scroll(200,300);
	  	});
	$("#Grade7bCoverPageDesktop").click(
		function(){
			//$("#Grade7CoverPageDesktop").fadeOut();
			$("#Grade7BookShelf").fadeOut();
			Grade7BookPageLoadByNumber(0,1,"7B");
			$("#Grade7PageContainer").fadeIn();
			$("#grade7BTOCLink").fadeIn();
			$('html,body').animate({
		        scrollTop: $("#grade7aTopics").offset().top},
		        'slow');
			//window.scroll(200,300);
	  	});	
	$("#Grade7cCoverPageDesktop").click(
			function(){
				//$("#Grade7CoverPageDesktop").fadeOut();
				$("#Grade7BookShelf").fadeOut();
				Grade7BookPageLoadByNumber(0,1,"7C");
				$("#Grade7PageContainer").fadeIn();
				$("#grade7CTOCLink").fadeIn();
				$('html,body').animate({
			        scrollTop: $("#grade7cTopics").offset().top},
			        'slow');
				//window.scroll(200,300);
		  	});	

});

function Grade7BookPageLoadByNumber(leftPage,rightPage,book_code)
{
	var data = {leftPage:leftPage,rightPage:rightPage,book_code:book_code};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Book-Page-Load",
		data: data,
		success: function(responseText)
		{
			$("#leftPageArrow").show();
			$("#rightPageArrow").show();
			$("#leftPage").html(responseText.split("PAGEBREAK")[0]);
			$("#leftPageArrow").html(responseText.split("PAGEBREAK")[1]);
			$("#rightPage").html(responseText.split("PAGEBREAK")[2]);
			$("#rightPageArrow").html(responseText.split("PAGEBREAK")[3]);
			pageName = responseText.split("PAGEBREAK")[4];
			location.hash = "!"+responseText.split("PAGEBREAK")[4];
			$('html,body').animate({
		        scrollTop: $("#leftPage").offset().top},
		        'slow');
			document.title = pageName+" | Grade-7-Mathematics";
		}
	});
}

function Grade7BookPageLoadByName(pageName)
{
	var data = {pageName:pageName};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Book-Page-Load-By-Name",
		data: data,
		success: function(responseText)
		{
			$("#leftPageArrow").show();
			$("#rightPageArrow").show();
			$("#leftPage").html(responseText.split("PAGEBREAK")[0]);
			$("#leftPageArrow").html(responseText.split("PAGEBREAK")[1]);
			$("#rightPage").html(responseText.split("PAGEBREAK")[2]);
			$("#rightPageArrow").html(responseText.split("PAGEBREAK")[3]);
			pageName = responseText.split("PAGEBREAK")[4];
			location.hash = "!"+responseText.split("PAGEBREAK")[4];
			book_code = responseText.split("PAGEBREAK")[5];
			if (book_code == "7A")
			{
				$("#grade7TOCLink").fadeIn();
			}
			else if (book_code == "7B")
			{
				$("#grade7BTOCLink").fadeIn();
			}
			else if (book_code == "7C")
			{
				$("#grade7CTOCLink").fadeIn();
			}
			if (pageName=='Table-Of-Contents')
			{
				//$(document).scrollTo('#grade7aTopics');
				window.scroll(600,600);
			}
			document.title = pageName+" | Grade-7-Mathematics";
		}
	});
}


function rightTurnArrowClick(pageNumber)
{
    var params = $(pageNumber).attr("id");
    book_code = params.substr(0, 2);
    nextPageNumber = parseInt(params.substr(2, params.length));

	if (book_code=="7A" && nextPageNumber==316)
	{
		$("#Grade7PageContainer").fadeOut();
		$("#grade7TOCLink").fadeOut();
		//$("#Grade7CoverPageDesktop").fadeIn();
		$("#Grade7BookShelf").fadeIn();
		location.hash = "";		
	}
	else if (book_code=="7B" && nextPageNumber==160)
	{
		$("#Grade7PageContainer").fadeOut();
		$("#grade7BTOCLink").fadeOut();
		//$("#Grade7CoverPageDesktop").fadeIn();
		$("#Grade7BookShelf").fadeIn();
		location.hash = "";		
	}	
	else
	{
		Grade7BookPageLoadByNumber(nextPageNumber,nextPageNumber+1,book_code);
	}

}

function leftTurnArrowClick(pageNumber)
{
    var params = $(pageNumber).attr("id");
    book_code = params.substr(0, 2);
    prevPageNumber = parseInt(params.substr(2, params.length));

    if (book_code=="7A" && prevPageNumber==-1)
	{
		$("#Grade7PageContainer").fadeOut();
		$("#grade7TOCLink").fadeOut();
		//$("#Grade7CoverPageDesktop").fadeIn();		
		$("#Grade7BookShelf").fadeIn();
	}
    else if (book_code=="7B" && prevPageNumber==-1)
	{
		$("#Grade7PageContainer").fadeOut();
		$("#grade7BTOCLink").fadeOut();
		//$("#Grade7CoverPageDesktop").fadeIn();		
		$("#Grade7BookShelf").fadeIn();
	}    
	else
	{
		Grade7BookPageLoadByNumber(prevPageNumber-1,prevPageNumber,book_code);
	}
}

function Grade7TopicalTestLoadByName(student_id,leftPage,rightPage,testTopic,attempt,testStart,testPageName,total_marks)
{	
	var data = {student_id:student_id,leftPage:leftPage,rightPage:rightPage,test_topic:testTopic,attempt:attempt,test_start:testStart,total_marks:total_marks};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Topical-Test-By-Name",
		data: data,
		success: function(responseText)
		{
			$("#leftPageArrow").hide();
			$("#rightPageArrow").hide();
			$("#leftPage").html(responseText.split("PAGEBREAK")[0]);
			$("#rightPage").html(responseText.split("PAGEBREAK")[1]);
			location.hash = "!"+testPageName;
		}
	});
}

function Grade7SaveAndLoadTest(test_id,student_id,leftPage,rightPage,total_elapsed_time,answer_ids)
{	
	var data = {test_id:test_id,student_id:student_id,leftPage:leftPage,rightPage:rightPage,total_elapsed_time:total_elapsed_time,answer_ids:answer_ids};
	$.ajax(
	{
		type: "POST",
		url: "/Grade-7-Topical-Test-Save-And-Load",
		data: data,
		success: function(responseText)
		{
			$("#leftPageArrow").hide();
			$("#rightPageArrow").hide();
			$("#leftPage").html(responseText.split("PAGEBREAK")[0]);
			$("#rightPage").html(responseText.split("PAGEBREAK")[1]);
			location.hash = "!"+testPageName;
		}
	});
}
