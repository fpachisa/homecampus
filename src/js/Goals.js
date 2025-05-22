$(document).ready(function() 
 	{ 		  	
		$("#ViewGoals").click(function() 
	    	{
				$("#InProgress").html('<img style="margin-left:600px;margin-top:-50px;" alt="Generating Report" src="/images/site/InProgress.gif">');
				var username = $("#child").val();
				var grade = $("#grade").val();
				var topic = $("#concept").val();
				if (topic == 'P4DC')
				{
					window.location.replace("/Goals/Grade_4_Decimal_Goals?username="+username);
				}
				else if (topic == 'P4FR')
				{
					window.location.replace("/Goals/Grade_4_Fractions_Goals?username="+username);
				}				
				else if (topic == 'P4MT')
				{
					window.location.replace("/Goals/Grade_4_Measurement_Goals?username="+username);
				}		            				
				else if (topic == 'P4DA')
				{
					window.location.replace("/Goals/Grade_4_Data_Analysis_Goals?username="+username);
				}		            				
				else if (topic == 'P4WN')
				{
					window.location.replace("/Goals/Grade_4_Whole_Numbers_Goals?username="+username);
				}		            				
				else if (topic == 'P5DA')
				{
					window.location.replace("/Goals/Grade_5_Data_Analysis_Goals?username="+username);
				}		            				
				else if (topic == 'P5DC')
				{
					window.location.replace("/Goals/Grade_5_Decimal_Goals?username="+username);
				}
				else if (topic == 'P5FR')
				{
					window.location.replace("/Goals/Grade_5_Fractions_Goals?username="+username);
				}				
				else if (topic == 'P5GT')
				{
					window.location.replace("/Goals/Grade_5_Geometry_Goals?username="+username);
				}		            				
				else if (topic == 'P5MT')
				{
					window.location.replace("/Goals/Grade_5_Measurement_Goals?username="+username);
				}		            				
				else if (topic == 'P5PR')
				{
					window.location.replace("/Goals/Grade_5_Percentage_Goals?username="+username);
				}		            				
				else if (topic == 'P5RT')
				{
					window.location.replace("/Goals/Grade_5_Ratio_Goals?username="+username);
				}		            				
				else if (topic == 'P5WN')
				{
					window.location.replace("/Goals/Grade_5_Whole_Numbers_Goals?username="+username);
				}		            				
				else if (topic == 'P6AG')
				{
					window.location.replace("/Goals/Grade_6_Algebra_Goals?username="+username);
				}		            				
				else if (topic == 'P6DA')
				{
					window.location.replace("/Goals/Grade_6_Data_Analysis_Goals?username="+username);
				}		            				
				else if (topic == 'P6FR')
				{
					window.location.replace("/Goals/Grade_6_Fractions_Goals?username="+username);
				}					            				
				else if (topic == 'P6MT')
				{
					window.location.replace("/Goals/Grade_6_Measurement_Goals?username="+username);
				}		            				
				else if (topic == 'P6PR')
				{
					window.location.replace("/Goals/Grade_6_Percentage_Goals?username="+username);
				}		            				
				else if (topic == 'P6RT')
				{
					window.location.replace("/Goals/Grade_6_Ratio_Goals?username="+username);
				}		            				
				else if (topic == 'P6SP')
				{
					window.location.replace("/Goals/Grade_6_Speed_Goals?username="+username);
				}
	    	});

		$("#SaveGoals").click(function() 
		    	{
					$("#SaveGoals").button( "option", "disabled", true );
					var username = $("#child").val();
					var grade = $("#grade").val();
					var topic = $("#concept").val();
					var URL = "/Goals/Save_Goals";
					var json_DataArray = JSON.stringify(DataArray);
					AJAXCall(URL,username,grade,topic,json_DataArray);		            				
		    	});
	}
);

function AJAXCall(URL,username,grade,topic,DataArray)
{            	
	var URLText = URL
	var data = {username:username,grade:grade,topic:topic,DataArray:DataArray};
	$.ajax(
	{
		type: "POST",
		url: URLText,
		data: data,
		success: function(responseText)
		{                   
			$("#ViewGoals").click();
		}
	});    
}
