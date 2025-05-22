$(document).ready(function() 
{ 
    $("#Learning").click(function() 
    	{
            HideAll();
    		$("#LearningFAQs").toggle("slow");

    	});

    $("#Practice").click(function() 
    	{
    		HideAll();
    		$("#PracticeFAQs").toggle("slow");

    	});    	
    $("#Progress").click(function() 
    	{
    		HideAll();
    		$("#ProgressFAQs").toggle("slow");

    	});    	
    $("#Membership").click(function() 
    	{
    		HideAll();
    		$("#MembershipFAQs").toggle("slow");

    	});    	
    $("#Technical").click(function() 
    	{
    		HideAll();
    		$("#TechnicalFAQs").toggle("slow");

    	});    	
    $("#Others").click(function() 
    	{
    		HideAll();
    		$("#OthersFAQs").toggle("slow");

    	});    	
});

function HideAll()
{
	$("#LearningFAQs").hide("fast");
	$("#PracticeFAQs").hide("fast");
	$("#ProgressFAQs").hide("fast");
	$("#MembershipFAQs").hide("fast");
	$("#TechnicalFAQs").hide("fast");
	$("#OthersFAQs").hide("fast");
}