/*
 * Creates a popup modal window for signin and register
 * 
 * 11-07-2016
 */

$(document).ready(function(){
	
	var viewport  = {
		width: $(window).width(),
		height:$(window).height()
	};
	
	var _fallback = /Mobi/i.test(navigator.userAgent);	//test for a mobile UA
	
	var modal = init();		//returns an object containg modal and its associated objects
	
	//attach a listener
	$("#signin-button").on('click', function(evt){
		if(viewport.width > 767 && !_fallback){
			evt.preventDefault();
			signin(modal);
		}
	});
	
	$("#register-button").on('click', function(evt){
		if(viewport.width > 767 && !_fallback){
			evt.preventDefault();
			register(modal);
		}		
	});
	
	//specific areas that require signin!
	$("body").on('click', ".sign-in-required", function(evt){
		if( (!_user.i ) && (viewport.width > 767 && !_fallback) ){
			evt.preventDefault();
			signin(modal);
		}
	});
	
	//form submit handle
	$("body").on('click', '#embed-sign-in', function(evt){
		evt.preventDefault();
		console.log("Signing In");
		signin_handler($("#sign-in-form"), $(this));
	});
	
	$("body").on('click', '#embed-register', function(evt){
		evt.preventDefault();
		console.log("Registering");
		register_handler($("#register-form"), $(this));
	});
	
	
	//Social Login Handlers
	$("body").on('click', "#sign-in--fb", function(evt){
		evt.preventDefault();
		FacebookLoginHandler(location.href);
	});
	
	
	//shortcut links
	$("body").on('click', '#trigger', function(evt){
		evt.preventDefault();
		var callback = $(this).attr("data-callback");
		if(callback == "register")
			modal.short({ callback: register, args: modal});
		else if(callback == "signin")
			modal.short({ callback: signin, args: modal});
		else if(callback == "forgotPassword")
			window.location.href= "/ForgotPassword";
		else
			console.log("Invalid callback property!");
			
	});
	
	//LoginAsChild Handles
	$(".LoginAsChild").on('click', function(evt){
		evt.preventDefault();
		LoginAsChild( $(this).attr("data-username") );
	});
	
	
});



//init
//create a modal and embed to the DOM
function init(){
	
	var obj = { };
	
	//creating the modal
	var modal_overlay = $("<div />", {'class': "account-modal-overlay"});
	var modal = $("<div />", {'class': "account-modal"});
	
	//accessories
	var modal_title = $("<div />", {'class': 'account-modal-title'});
	var modal_close = $("<div class='account-modal-close'><a>&times;</a></div>");
	var modal_content = $("<div />", {'class':'account-modal-cnt'});
	
	//add the components to DOM
	modal_title.appendTo(modal);	//title
	modal_close.appendTo(modal);	//close button
	modal_content.appendTo(modal);	//content
	
	modal.appendTo(modal_overlay);	//the modal
	modal_overlay.appendTo( $("body") );
	
	
	/* Modal call interface */
	
	// 1> Display the Modal
	obj.show = function(){
		modal_overlay.css({'display': 'block'});
		
		$.Velocity
			.animate(modal_overlay, {"opacity": 1}, 300)
			.then(function(){
				var offset = ($(window).height() - modal.height()) / 2;
				return $.Velocity.animate(modal, {"marginTop": offset}, 450);
			});
		
		return this;
	}
	
	// 2> Close the Modal
	obj.hide = function(){
		$.Velocity
			.animate(modal, {"marginTop": "-500px"}, 300)
			.then(function(){ return $.Velocity.animate(modal_overlay, {"opacity": 0}, 200); })
			.then(function(){ return modal_overlay.css({"display": "none"}); });
		
		return this;	//facilitate chaining
	}
	
	//Generic Close Gestures!
	modal_overlay.on('click', function(evt){
		evt.preventDefault();
		if(evt.target == modal_overlay[0]){
			obj.hide();
		}
	});
	
	modal_close.children("a").on('click', function(evt){
		evt.preventDefault();
		obj.hide();
	});
	
	
	//shorthand function
	obj.setTitle = function(txt) {
		modal_title.empty();
		modal_title.html("<h3 style='text-align:center'>" + txt + "</h3>");
		return this;	//facilitate chaining
	}
	
	obj.setContent = function(txt) {
		modal_content.empty();
		modal_content.html(txt);
		return this;	//facilitate chaining
	}
	
	
	//Shortcut facilitator
	obj.short = function(params){
		modal.animate({"marginTop": "-500px"}, 300, function(){
			params.callback( params.args );
		});
	}
	
	
	return obj;
}


//** Sign-in Section **
//==========================================================================================================
function signin(modalWindow) {
	//var html =  '<div class="social-login"><button class="btn-facebook" id="sign-in--fb"><i class="fa fa-facebook"></i></button> <button class="btn-google" id="sign-in--gp"><i class="fa fa-google-plus"></i></button></div> <div class="or-separator"><span>or</span></div> <form class="sign-in-form" id="sign-in-form"><div><input name="username" id="username" type="text" placeholder="Enter username" /><span class="error-hint">Invalid Username</span></div><div><input name="password" id="password" type="password" placeholder="Enter password"><span class="error-hint">Invalid Password</span></div><div class="sign-in-form__ctrl"><button type="submit" class="btn-primary" id="embed-sign-in" style="display:block;margin:0">Sign In</button><a class="sign-in-form__ctrl--a" href="javascript:void(0)" id="trigger" data-callback="register">Not a member?</a><a class="sign-in-form__ctrl--a right" href="javascript:void(0)" id="trigger" data-callback="forgotPassword">Forgot Password?</a></div></form>';
	var html =  '<form class="sign-in-form" id="sign-in-form"><div><input name="username" id="username" type="text" placeholder="Enter username" /><span class="error-hint">Invalid Username</span></div><div><input name="password" id="password" type="password" placeholder="Enter password"><span class="error-hint">Invalid Password</span></div><div class="sign-in-form__ctrl"><button type="submit" class="btn-primary" id="embed-sign-in" style="display:block;margin:0">Sign In</button><a class="sign-in-form__ctrl--a" href="javascript:void(0)" id="trigger" data-callback="register">Not a member?</a><a class="sign-in-form__ctrl--a right" href="javascript:void(0)" id="trigger" data-callback="forgotPassword">Forgot Password?</a></div></form>';
	modalWindow.setTitle("LOGIN TO HOMECAMPUS").setContent(html).show();
}

//** Sign-in form submit handle **
//================================
function signin_handler(form, sign_button){
	//get the data and sanitize (simply check for presence)
	var obj = {};
	form.serializeArray().map(function(x){ obj[x.name] = x.value; });
	var err = false;
	
	//Checking input
	if( obj.username === "" ) {
		console.log("Empty Username");
		has_error($("#username"));
		err = true;
	}
	
	if( obj.password === "" ) {
		console.log("Empty Password");
		has_error($("#password"));
		err = true;
	}
	if( err )return;
	
	//form validated
	//disabling signin button to indicate progress
	sign_button.prop("disabled", true).addClass("wait");
	
	//now serialize and send data to server
	var url = "/SignIn?continue=" +  encodeURIComponent(location.pathname) + "&async";
	var data = form.serialize();
	
	doLogin(data, url, sign_button);
}


//** Register Section **
//==========================================================================================================
function register(modalWindow) {
	//var html = '<div class="social-login"><button class="btn-facebook btn-icon" id="sign-in--fb"><i class="fa fa-facebook"></i></button> <button class="btn-google btn-icon" id="sign-in--gp"><i class="fa fa-google-plus"></i></button></div> <div class="or-separator"><span>or</span></div><form class="register-form" id="register-form"><div><input name="parent_first_name" id="parent_first_name" type="text" placeholder="Enter Firstname"/><span class="error-hint">Invalid Firstname</span></div><div><input name="parent_last_name" id="parent_last_name" type="text" placeholder="Enter Lastname"><span class="error-hint">Invalid Lastname</span></div><div><input name="email" id="email" type="email" size=25 placeholder="Enter Email"><span class="error-hint">Invalid Email</span></div><div><input name="parent_password" id="parent_password" type="password"  placeholder="Enter Password"><span class="error-hint">Invalid Password</span></div><div class="register-form__ctrl"><button type="submit" id="embed-register" class="btn-primary btn-block">Sign Up</button> <div class="register-form__ctrl-a">Already a member? <a href="javascript:void(0)" id="trigger" data-callback="signin">Sign In now</a></div></div></form>';
	var html = '<form class="register-form" id="register-form"><div><input name="parent_first_name" id="parent_first_name" type="text" placeholder="Enter Firstname"/><span class="error-hint">Invalid Firstname</span></div><div><input name="parent_last_name" id="parent_last_name" type="text" placeholder="Enter Lastname"><span class="error-hint">Invalid Lastname</span></div><div><input name="email" id="email" type="email" size=25 placeholder="Enter Email"><span class="error-hint">Invalid Email</span></div><div><input name="parent_password" id="parent_password" type="password"  placeholder="Enter Password"><span class="error-hint">Invalid Password</span></div><div class="register-form__ctrl"><button type="submit" id="embed-register" class="btn-primary btn-block">Sign Up</button> <div class="register-form__ctrl-a">Already a member? <a href="javascript:void(0)" id="trigger" data-callback="signin">Sign In now</a></div></div></form>';
	modalWindow.setTitle("Register with HomeCampus").setContent(html).show();
}

function register_handler(form, button){
	//get the data and sanitize (simply check for presence)
	var obj = {};
	form.serializeArray().map(function(x){ obj[x.name] = x.value; });
	var err = false;
	
	//Checking input
	if( obj.parent_first_name === "" ) {
		console.log("Empty FirstName");
		has_error($("#parent_first_name"));
		err = true;
	}
	
	if( obj.parent_last_name === "" ) {
		console.log("Empty LastName");
		has_error($("#parent_last_name"));
		err = true;
	}

	if( obj.email === "" ) {
		console.log("Empty Password");
		has_error($("#email"));
		err = true;
	}

	if( obj.parent_password === "" ) {
		console.log("Empty Password");
		has_error($("#parent_password"));
		err = true;
	}
	
	if( err )return;
	
	//now serialize and send data to server
	var url = "/Register?continue=" +  encodeURIComponent(location.pathname) + "&async";
	var data = form.serialize();
	
	doLogin(data, url, button);
}


//** Social Login Handlers **
//==========================================================================================================

//** Google **
//------------

function googleAPIDoneLoading(){
	/* Executed when the APIs finish loading */
	
	// Additional params including the callback, the rest of the params will
	//come from the page-level configuration.
	var additionalParams = {
		'callback': GoogleLoginHandler
		};
	
	// Attach a click listener to a button to trigger the flow.
	$("body").on('click', "#sign-in--gp", function(evt) {
		evt.preventDefault();
		gapi.auth.signIn(additionalParams); // Will use page level configuration + additionalParams
	});
}

function GoogleLoginHandler(authResult)
{
	if (authResult['status']['signed_in']) {
		gapi.client.load('plus','v1',function(){  
			var request = gapi.client.plus.people.get( {'userId' : 'me'} );
			request.execute( function(profile) {
				var URL = "/SignIn?continue=" + encodeURIComponent(location.href) + "&async";
				var username = profile.emails[0].value;
				var last_name = profile.names['familyName'];
				var first_name = profile.names['givenName'];
				var data = {username:username,first_name:first_name,last_name:last_name,source:'Google+'};
				
				doLogin(data,URL, $("#sign-in--gp"));
				});
			});
		}
}

//** FaceBook **
//--------------

function FacebookLoginHandler()
{
	FB.login(function(response) {
		if (response.authResponse) {
			console.log('Welcome!  Fetching your information.... ');
			
			access_token = response.authResponse.accessToken; //get access token
			user_id = response.authResponse.userID; //get FB UID
			
			FB.api('/me', function(response) {
				console.log(response);
				var URL = "/SignIn?continue=" + encodeURIComponent(location.href) + "&async";
				var username = response.email;
				var first_name = response.first_name;
				var last_name = response.last_name;
				
				var data = {username:username,first_name:first_name,last_name:last_name,source:'Facebook'};
				if (!username) {
					alert("Facebook didn't provide your email. Please use Google or Home Campus id to Login");
					
				} else {
					doLogin(data,URL, $("#sign-in--fb"));
				}
			});
			
		} else {
			//user hit cancel button
			console.log('User cancelled login or did not fully authorize.');
			}
		}, 
		{ scope: 'email'}
	);	
}

//** LoginAsChild **
//** taken from original source **
// modified how the function is triggred! --see line 
//=========================================================================================================
function LoginAsChild(username)
{
	var data = {username:username};
	$.ajax(
	{
		type: "POST",
		url: "/MyProfile/LoginAsChild",
		data: data,
		error: function(){
			notify("Some error ocurred! Please try again.");
		},
		success: function(data) {
			data = JSON.parse(data);
			if(data.success == true){
				var URL = "/";
				switch( data.skill ){
				case "P3": URL = "/Primary_Grade_3_Mathematics";break;
				case "P4": URL = "/Primary_Grade_4_Mathematics";break;
				case "P5": URL = "/Primary_Grade_5_Mathematics";break;
				case "P6": URL = "/Primary_Grade_6_Mathematics";break;
				}
				
				window.location = URL;
			} else {
				location.reload(true);
			}
		}
	});
}


//** Utility **
//==========================================================================================================

//** Generic Login Call routine **
//================================
function doLogin(data, url, button){
	//return a promise
	return $.ajax({
		url: url,
		data: data,
		method:  "POST",
		cache:false,
		beforeSend: function(){
			//disable button and add cosmetic markup
			button.prop("disabled", true).addClass("wait");
		},
		complete: function(){
			//enable button and remove cosmetic markups
			button.prop("disabled", false).removeClass("wait");
		},
		
		error: function(){
			notify("Some error ocurred! Please try again later");
		},
		success: function(data, status, jqXHR){
			data = JSON.parse(data);
			if(data.success === true){
				//logged in here
				//if continue url is provided go there
				if(data.continue_url != undefined)
					location.href = data.continue_url;
				else
					location.reload(true);	//hard reload
			} else {
				//login failed!
				if(data.error != undefined) login_failed(data.error);
			}
		}
	});
}

function login_failed(error){
	notify(error, {backgroundColor: "#ef5350"});
	
	//cleanup --only for signin forms!
	has_error( $("#username").val("") );
	has_error( $("#password").val("") );
}

function has_error(field){
	var p = field.parent();
	p.addClass('has-error');
	field.one('change', function(){
		p.removeClass('has-error');
	});
}