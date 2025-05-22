$(document).ready(function(){
	console.log("navigation.js ready")
	
	//side scroll menu for mobile devices
	var _mob_menu = $(".mobile-menu");
	var body = $("body");
	var overlay = getOverlay(body[0], overlayClickListener);
	
	
	$("body").on("click", "#menu-opener", function(evt){
		evt.preventDefault();
		overlay.open();
		_mob_menu.addClass("open");
		body.css({overflow: "hidden"}); //to prevent scroll while menu is open
	});
	
	$("body").on("click", ".menu-closer", function(evt){
		evt.preventDefault();
		overlay.close();
		_mob_menu.removeClass("open");
		body.css({overflow: "auto"});
	});
	
	
	function overlayClickListener(){
		overlay.close();
		_mob_menu.removeClass("open");
		body.css({overflow: "auto"});
	}
});

function getOverlay(body, onClick){
	var _o = document.createElement("div");
	var _s  = _o.style;
	
	//adding styles
	_s.position = "fixed";
	_s.top = 0;
	_s.left = 0;
	_s.zIndex = 998;
	_s.backgroundColor = "rgba(0,0,0,0.5)";
	_s.width = "100%";
	_s.height = "100%";
	
	var _int = {};
	
	//open
	_int.open = function(){
		body.appendChild(_o);
	}
	
	//close
	_int.close = function(){
		body.removeChild(_o);
	}
	
	//click
	$(_o).on('click', function(){
		onClick();
	});
	
	
	return _int;
}