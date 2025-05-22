$(document).ready(function(){
	var _this_script = $("script[src='/js/unified_grade_index.js']");
	var grade = _this_script.attr("data-grade");
	var intent = _this_script.attr("data-intent");

	//get user intent
	var learnIntent = (intent == "lrn")?true:false;
	var practiceIntent = (intent == "prc")?true:false;
	
	var pathToMap = "/js/Primary" + grade + "_urlmap.json";
	
	//ignore all the clicks that are made before the urlmap is loaded (may arise due to slower network connections or something like that)
	$(".chapter__topic").on("click.pending-urlmap", function(evt){
		evt.preventDefault();
	});
	
	//load the urlmap
	$.get(pathToMap, function(resp){
		//boot(learnIntent, practiceIntent, JSON.parse(resp));
		boot(learnIntent, practiceIntent, resp);
	});
});

//sets up controls after the urlmap is downloaded
function boot(learnIntent, practiceIntent, url){
	MODAL = extend_popie();
	$(".chapter__topic").off("click.pending-urlmap");	//remove listener
	$(".chapter__topic").on("click", function(evt){
		tag = $(this).attr("data-tag");
		u = url[tag];
		if(!u)return true;	//to continue loading href
		
		if(learnIntent)return true;	//continue with default action
		if(practiceIntent){location.href = u[1];return false}	//load practice url by default
		
		MODAL.setRankTable(tag).setURL(u[0], u[1], u[2]).show();
		return false;	//to prevent loading href
	});
}

//extends the default popie object to add custom elements to  the content section ad make interfacing to htem easier
function extend_popie(){
	var _o = popie();
	
	//add xternal objects to popie
	var ranktable = document.createElement("div");
	
	var buttonSet = document.createElement("div");
		buttonSet.className = "btn-group";
		
	var learnButton = document.createElement("a");
		learnButton.className = "btn-learn";
		learnButton.innerHTML = "Learn";
	
	var practiceButton = document.createElement("a");
		practiceButton.className = "btn-practice sign-in-required";
		practiceButton.innerHTML = "Practice";
	
	var worksheetButton = document.createElement("a");
		worksheetButton.className = "btn-worksheet sign-in-required";
		worksheetButton.innerHTML = "Worksheet";
	
	//add objects to DOM
	buttonSet.appendChild(learnButton);
	buttonSet.appendChild(practiceButton);
	buttonSet.appendChild(worksheetButton);
	
	/*var _all = document.createElement("div");	//just a helper
		//_all.appendChild(ranktable);
		_all.appendChild(buttonSet);*/	
	
	_o.append( buttonSet );	//add the external elements to the content section ofthe popie dialog
	
	//interface
	_o.setRankTable = function(selector){
		var element = document.getElementById(selector);
		var y = (element != null)? element.innerHTML : "<h2 style='text-align:center;'>What would you like to do?</h2>";
		_o.setContent(y);
		return this;
	};
	
	_o.setURL = function(learnURL, practiceURL, worksheetURL){
		learnButton.style.display = "table-cell";	//reset
		if(learnURL != "")
			learnButton.href = learnURL;
		else
			learnButton.style.display = "none";	//do not dislay the learn button at all if there is no learn link!
		
		practiceButton.href = practiceURL;
		worksheetButton.href = worksheetURL;
		return this;
	};
	
	return _o;
}