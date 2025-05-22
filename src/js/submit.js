var IsParent = popie({
	addCloseButton: true, addTitle: true,
	buttons: { "Ok": {'class': 'btn-modal', 'handle':function(){ IsParent.hide(); } } },
	buttonGroupClass: "btn-group",
	title: "<h3>Dear Parent</h3>",
});

var ErrorDialog = popie({
	addCloseButton: true, addTitle: true,
	buttons: { "Ok": {'class': 'btn-modal', 'handle': function(){ location.reload(true); } } },
	buttonGroupClass: "btn-group",
	title: "<h3>Oops!!!</h3>",
	sticky: true,
	onClose: function(){ location.reload(true); }
});

var WrongDialog = popie({
	addCloseButton: true, addTitle: true,
	modalClass: "ExplainDialog",
	buttons: { 
		"Ok": {'focus':true, 'class': 'btn-modal', 'handle': function(){ WrongDialog.hide();$("#answer").val('');$("input[name=answer]:radio").attr("checked",false);MainFuntion(actualConcept).done(function(){timer.start(1000, "showTime");}); } },
		"Explanation": {'class': 'btn-modal', 'handle':function(){ WrongDialog.hide();ExplainDialog.setContent(explanation).show();	/*explanation will be global when initialized*/ } }
		},
	buttonGroupClass: "btn-group",
	title: "<h3>Incorrect</h3>",
	sticky: true,
	addCloseButton: false
});

var ExplainDialog = popie({
	addCloseButton: true, addTitle: true,
	title: "<h4>Explanation</h4>",
	defineHeightAsCss: true,
	modalClass: "ExplainDialog",	//hc-basic
	buttons: { "Ok": {'class': 'btn-modal', 'handle': function(){ ExplainDialog.hide(); } } },
	buttonGroupClass: "btn-group",
	onClose: function() { $("#answer").val('');$("input[name=answer]:radio").attr("checked",false);MainFuntion(actualConcept).done(function(){timer.start(1000, "showTime");}); }
});

// -------------------------------------  ------------------------------------------  ------------------------------------
//--------------------------------------  ------------------------------------------  ------------------------------------

//====== TIMER =====
var timer = {
	__timer: null,		//main function, private!!
	_elapsed: 0,
	start: function(interval, elementID){
		var x = document.getElementById(elementID);
		this.element = x;
		var y = 0;
		if(!x) console.log("No Element with ID: " + elementID+ " found!!");
		this.__timer = setInterval(function(){
			y += 1;
			if(x) x.innerHTML = y;
			this._elapsed += 1;
		}, interval);
	},
	stop: function(){
		clearInterval(this.__timer);
		return this._elapsed;
	},
	restart: function(interval, elementID){
		var temp = this.stop();
		this.start(interval, elementID);
		return temp;
	},
	stats: function(){
		return this._elapsed;
	}
}


$(document).ready(function() {
	
	//creating a timer to record time take for each problem
	timer.start(1000, "showTime");
	
	//get the form data as an Object
	var _data = {};
	$("#_data").serializeArray().map(function(x){ _data[x.name] = x.value; });
	
	actualConcept = _data['ConceptID'];		//keeping it global so its accessibe by the dialogs above w/out un-necessary boiler plate
	var concept = "#" + _data['ConceptID'];
	
	//Skip  >> Try Next button
	$("body").on('click', "#close", function() {
		$("#answer").val('');$("input[name=answer]:radio").attr("checked",false);$(concept).click();
		$("#submit").attr("disabled", true );
		$("#close").attr("disabled", true );
	});
    
	
	//submit the answer
	$("body").on("click", "#submit", function() {
		var IsParent = _data["IsParent"];
		var problems_attempted = $("attempted").val();
    	
    	$("#submit").attr("disabled", true );
    	$("#close").attr("disabled", true );
    	
    	var elapsed_seconds = timer.stop();
    	 	
    	var answer = $("#answer").val();
		if (answer == undefined) {
			//MCQs come here!
			answer = $("input:radio[name=answer]:checked").val();
		}
		
		var student_id = _data["student_id"];
		var complexity_level = _data["complexity_level"];		
		if (complexity_level == "")
			complexity_level = "medium";
		
		
		var HCScore = _data["HCScore"];
		if (HCScore == "")
			HCScore = 5; //Default score is 5
			
		var grade = _data["grade"];
		//for Primary 5 grade is still not defined so hard coding here
		if (grade == "")
			grade = 5;
		
		var data = {
				answer:answer,
				student_id:student_id,
				grade:grade,
				time_taken:elapsed_seconds,
				complexity_level:complexity_level,
				HCScore:HCScore,
				concept:actualConcept
			};
		
		$.ajax({
			type: "POST", 
			url: "/submit", 
			data: data,
			beforeSend: function() {
				console.log(data);
				$("#problem-loader").css("display", "inline-block");
			},
			error: function() {
				$("#problem-loader").css("display", "none");
				ErrorDialog.setContent("Some unknown error ocurred! Please try again later");
				ErrorDialog.show();	//this dialog will reload the page when closed, @see: line #12
			},
			success: resultCheck	//defined @137
		});
		
		
		//putting it in this closure so that the vars are accessible, though it's not a good idea
		function resultCheck( responseText ){
			$("#problem-loader").css("display", "none");
			
			//if answer is wrong the ajax request gets the explanation and if answer is correct only concept id is returned.				
			FullExplanation = responseText;
			
			if (FullExplanation=="Show error message"){
				ErrorDialog.setContent("You have either taken too long to answer or are logged in from more than 1 computer.");
				ErrorDialog.show();	//this dialog will reload the page when closed, @see: line @36
				
			} else {
				var IsParentText = 
					"<br><br>Note: You are logged in with Parent id.<br><br> \
					The problem you submit will not be reflected in the Progress Report as it shows the progress of the child only."
				
				
				correct = FullExplanation.split("ANSWERSEPARATOR")[0];
				ConceptID = FullExplanation.split("ANSWERSEPARATOR")[1];
				AnswerText = FullExplanation.split("ANSWERSEPARATOR")[2];
				explanation = FullExplanation.split("ANSWERSEPARATOR")[3];
				
				if (correct=="InCorrect") {
					if (IsParent=="True" && problems_attempted % 5 == 0)
						AnswerText = AnswerText + IsParentText;
					
					WrongDialog.setContent(AnswerText).show();
					
				} else {
					if (IsParent=="True" && problems_attempted % 5 == 0) {
						IsParent.setContent("Note: You are logged in with Parent id.<br><br>The problem you submit will not be reflected in the Progress Report as it shows the progress of the child only.").show();						
					}
					
					$("#problem-correct").css("display", "inline");
					
					//move onto next question
					setTimeout(function() {
						$("#problem-correct").css("display", "none");
						
						setTimeout(function() {
							$("#answer").val('');
							$("input[name=answer]:radio").attr("checked",false);
							
							MainFuntion(actualConcept)	//@riyaz: defined in practice.js
							.done(function(){
								//restarting timer!, when new question finishes loading.....
								timer.start(1000, "showTime");
							});
						},500);
					},2000);
				}
			}
		}	//end of resultCheck
		
   	});		//end of submit handler
	
});


function showSubscribe(title, content, link){
	sd = extendPopie({
		buttons: {
			"Subscribe": function(){ location.href="/Subscribe"; },
			"No, thanks": function(){ location.href= link; }
		},
		sticky: true,
		title: title,
		onClose: function(){ location.href = link}
	});
	
	sd.setContent(content).show();
}