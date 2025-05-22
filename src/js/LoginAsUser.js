
function LoginAsChild(item)
{
	var username = $(item).attr("id");
	var data = {username:username};
	$.ajax(
	{
		type: "POST",
		url: "/MyProfile/LoginAsChild",
		data: data,
		success: function(responseText)
		{
			var URL = "/";
			if (responseText == "P3")
			{
				URL = "/Primary_Grade_3_Mathematics";
			}
			else if (responseText == "P4")
			{
				URL = "/Primary_Grade_4_Mathematics";
			}
			else if (responseText == "P5")
			{
				URL = "/Primary_Grade_5_Mathematics";
			}
			else if (responseText == "P6")
			{
				URL = "/Primary_Grade_6_Mathematics";
			}			
			parent.location=URL;
		}
	});
}

function LoginAsChildAccount(username)
{
	var data = {username:username};
	$.ajax(
	{
		type: "POST",
		url: "/MyProfile/LoginAsChild",
		data: data,
		success: function(responseText)
		{
			var URL = "/";
			if (responseText == "P3")
			{
				URL = "/Primary_Grade_3_Mathematics";
			}
			else if (responseText == "P4")
			{
				URL = "/Primary_Grade_4_Mathematics";
			}
			else if (responseText == "P5")
			{
				URL = "/Primary_Grade_5_Mathematics";
			}
			else if (responseText == "P6")
			{
				URL = "/Primary_Grade_6_Mathematics";
			}			
			parent.location=URL;
		}
	});
}

function FacebookLoginHandler(URL)
{
	    FB.login(function(response) {

	        if (response.authResponse) {
	            console.log('Welcome!  Fetching your information.... ');
	            console.log(URL);
	            //console.log(response); // dump complete info
	            access_token = response.authResponse.accessToken; //get access token
	            user_id = response.authResponse.userID; //get FB UID

	            FB.api('/me', function(response) {
	            	var username = response.email;
	            	var first_name = response.first_name;
	            	var last_name = response.last_name;
	                var data = {username:username,first_name:first_name,last_name:last_name,source:'Facebook'};
	                if (!username)
	                {
	                	alert("Facebook didn't provide your email. Please use Google or Home Campus id to Login");
	                }
	                else
	                {
	                	callLoginAJAX(data,URL);
	                }
	                           
	            });

	        } else {
	            //user hit cancel button
	            console.log('User cancelled login or did not fully authorize.');

	        }
	    }, {
	        scope: 'email'
	    });	
   /* FB.api('/me', function(response)
    {
    	var username = response.email;
    	var first_name = response.first_name;
    	var last_name = response.last_name;
        var data = {username:username,first_name:first_name,last_name:last_name,source:'Facebook'};
        callLoginAJAX(data,URL);
	});*/
    

}

function callLoginAJAX(data,URL)
{
	$.ajax(
	    	{
	    		type: "POST",
	    		url: URL,
	    		data: data,
	    		success: function(responseText)
	    		{	
	    			if (responseText=="Facebook" || responseText=="Google+")
	    			{
	    				parent.location = "/MyProfile"
	    			}
	    			else
	    			{
	    				parent.location=URL;
	    			}   			
	    		}
	    	}); 
}
