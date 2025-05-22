$(document).ready(function(){
	
	// STATE
	//------
	var parent = $(".scr-1 .screen__body");
	var state = parent.html();		//backing up initial-state
	var body = $("body");
	var practice_call = $(".homepage-practice-call"); 
	
	
	//HOMEPAGE LEARN BUTTON
	//---------------------
	body.on('click', "#homepage-learn-btn", function(evt){
		evt.preventDefault();
		var _scr_2_offset = $(".scr-2").position().top;
		body.animate({scrollTop: _scr_2_offset}, 750, "swing");
	});
	
	//HOMEPAGE PRACTICE BUTTON
	//------------------------
	if(_user == undefined || _user.i == false) {
		uc1({parent: parent, state: state, body: body});
	} else {
		uc2({body: body, practice_call: practice_call});
	}
	
	
	//extending jQuery for flip animation
	$.fn.extend({
		flipOut: function(){
			var _def = $.Deferred();
			var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
			var x = $(this).addClass("animated flipOutY").one(animationEnd, function(){
				$(this).css("visibility", "hidden").removeClass("animated flipOutY");
				_def.resolve();
			});
			
			return _def.promise();
		},
		
		flipIn: function(){
			var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
			$(this).css("visibility", "visible").addClass("animated flipInY").one(animationEnd, function(){
				$(this).removeClass("animated flipInY");
			});
		}
	});
	
});


// USE CASE I
//-----------
function uc1(p) {
	// Get the forms
	var form = getFormBoiler();
	
	// Getting the objects here
	var body = p.body;
	var parent = p.parent;
	var state = p.state;
	
	
	//HOMEPAGE PRACTICE BUTTON
	//------------------------
	body.on('click',"#homepage-practice-btn", function(evt){
		evt.preventDefault();
		
		//move the parent out of scope
		parent.flipOut().done(function(){
			//when animation is complete
			parent.empty();					//clearing parent
			parent.css({marginTop: 0});
			parent.append(form.registerForm);
			
			//get back to user's scope
			parent.flipIn();
		});
	});

	// Sign In Now!
	//-------------
	body.on('click', '.signin-trigger', function(evt){
		evt.preventDefault();
		//move the parent out of scope
		parent.flipOut().done(function(){
			//when animation is complete
			parent.empty();					//clearing parent
			parent.css({marginTop: 0});
			parent.append(form.signInForm);
			//get back to user's scope
			parent.flipIn();
		});
	});
	
	// Why Join?
	//-----------------
	body.on("click", ".benefits-trigger", function(evt){
		evt.preventDefault();
		var _scr_3_offset = $(".scr-3").position().top;
		body.animate({scrollTop: _scr_3_offset}, 750, "swing");
	});
	
	//Go Back?
	//--------
	body.on("click", ".reset-state", function(evt){
		evt.preventDefault();
		parent.empty();
		
		//see homepage.less @LINE - 94
		parent.css({marginTop: "8%"});
		parent.html(state);
	});
}

// USE CASE II
//------------
function uc2(p){
	var showing = false;
	p.body.on('click',"#homepage-practice-btn", function(evt){
		evt.preventDefault();
		if(!showing){
			p.practice_call.show();
			showing = true;
		} else {
			p.practice_call.hide();
			showing = false;
		}
	});
}



// Utility
//--------
function getFormBoiler() {
	// Register Form Boilerplate
	//-------------------------
	var registerHtml = '<div class="social-login"><button class="btn-facebook btn-icon" id="sign-in--fb"><i class="fa fa-facebook"></i></button> <button class="btn-google btn-icon" id="sign-in--gp"><i class="fa fa-google-plus"></i></button></div> <div class="or-separator no-pop"><span>or</span></div><form class="register-form" id="register-form"><div><input name="parent_first_name" id="parent_first_name" type="text" placeholder="Enter Firstname"/></div><div><input name="parent_last_name" id="parent_last_name" type="text" placeholder="Enter Lastname"></div><div><input name="email" id="email" type="email" size=25 placeholder="Enter Email"></div><div><input name="parent_password" id="parent_password" type="password"  placeholder="Enter Password"></div><div class="register-form__ctrl"><button type="submit" id="embed-register" class="btn-screen__blue-shadow">Sign Up</button> <div>Already a member? <a href="javascript:void(0)" class="signin-trigger">Sign In now</a></div> <div> <a href="javascript:void(0)" class="benefits-trigger">Why Join?</a></div> <div><a href="javascript:void(0);" class="reset-state">Go Back</a></div></div></form>';
	var regTitle = $("<div />", {'class': 'form-arena__title', 'html': '<h2>Join Now</h2>'});
	var registerForm = $("<div />", {'class': 'form-arena', 'html': registerHtml});
	registerForm.prepend(regTitle);
	
	
	// Sign In Form Boilerplate
	//------------------------
	var signinHtml = '<div class="social-login"><button class="btn-facebook" id="sign-in--fb"><i class="fa fa-facebook"></i></button> <button class="btn-google" id="sign-in--gp"><i class="fa fa-google-plus"></i></button></div> <div class="or-separator no-pop"><span>or</span></div> <form class="sign-in-form" id="sign-in-form"><div><input name="username" id="username" type="text" placeholder="Enter username" /></div><div><input name="password" id="password" type="password" placeholder="Enter password"></div><div class="sign-in-form__ctrl" style="text-align:center;"><button type="submit" class="btn-screen__blue-shadow" id="embed-sign-in">Sign In</button></div>  <div><a href="javascript:void(0);" class="reset-state">Go Back</a></div></form>';
	var signInTitle = $("<div />", {'class': 'form-arena__title', 'html': '<h2>Sign In</h2>'}); 
	var signInForm = $("<div />", {'class': 'form-arena', 'html': signinHtml});
	signInForm.prepend(signInTitle);
	
	return {
		registerForm: registerForm,
		signInForm: signInForm
	};
}
