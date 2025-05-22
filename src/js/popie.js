/*
 * Popie.js - A small javascript plugin to ease-out the process of creating and manipulating modals / dialogs
 *
 * @dependency - jQuery > 1.5
 * 
 * @todo - 	-- Remove jQuery Dependency by creating an alternative animation handler
 * 			-- Provide customisation options via params
 * 			-- Add css to its own stylesheet (not so important)
 */
(function( $, window ){
	
	var BASIC_HEIGHT_REQUIRED = 350;
	
	window.popie = function(params){
		
		//additional customizations
		var defaults = {
			addCloseButton: false,		// to add a close button on top-right
			addTitle: false,			// need to remove this
			closeOnESC: true,			// close the modal on ESC 
			sticky: false,				// sticky modal, if set the modal wont go on clicking outside/on the overlay area or pressing ESC
			onClose: function() { },	// fired when the dialog closes
			title: "",					// default title
			modalClass: "",				// additional custom modal class to add to the main modal container, useful for customising specific modals
			buttons: undefined,			// buttons to be appended to the modal
			// The buttons will be appended to a group-container that in turn will be apended to the modal body
			// any specific class for the group-container may go in here
			buttonGroupClass: "",
			defineHeightAsCss: false
		};
		
		/*
		 * Buttons must be added as
		 * buttons: {
		 * 	'name': {
		 * 		'class': "cssClass",
		 * 		'handle': function(evt){ ... },
		 * 		'focus': true/false [DEFAULT assumed to be false]
		 * 	},
		 * 	...
		 * }
		 */
		
		var settings = extend({}, defaults, params);
		
		// STEP 1 : Creating the containers
		// using native elements here to speed up things
		
		//Overlay
		var _overlay = document.createElement("div");
			_overlay.className = "modal-overlay";
			
		// Main Modal Area
		var _modal = document.createElement("div");
			_modal.className = "modal " + settings.modalClass;
			_modal.tabIndex = 0;	//to enable focus()
			
		// Content Holder; anything to display go in here!
		var _content = document.createElement("div");
			_content.className = "modal-content";
		
		// Extra Content, such as Buttons or any custom component go in here
		var _xtra = document.createElement("div");
			_xtra.className = "modal-xtra";
		
		
		// STEP 2: Add elements to DOM
		_modal.appendChild(_content);			//content arena
		_modal.appendChild(_xtra);				//extra elements arena
		_overlay.appendChild(_modal);			//the modal
		document.body.appendChild(_overlay);	//the overlay
		
		
		//caching jQuery objects
		var _o = $(_overlay);
		var _m = $(_modal);
		
		var obj = { };	// Interface methods object
				
		// 1> Display the Modal
		obj.show = function(){			
			_o.css({'display': 'block'});
			_o.animate({"opacity": 1}, 300).promise()
			  .pipe(function(){ if(settings.defineHeightAsCss == true){return _m.css("height",(_m.height()>BASIC_HEIGHT_REQUIRED)?_m.height():'auto').promise();}else{ var _ = $.Deferred(); _.resolve(); return _.promise();}})
			  .pipe(function(){var offset = ($(window).height() - _m.height()) / 2; return _m.animate({"marginTop": offset}, 450).promise(); })
			  .pipe(function(){ _m.focus(); })
			return this;	// Chaining
		}
		
		// 2> Close the Modal
		obj.hide = function(){
			//fire onClose
			settings.onClose();
			
			//start animation
			_m.animate({"marginTop": "-500px"}, 300).promise()
			  .pipe(function(){ return _o.animate({"opacity": 0}, 200).promise(); })
			  .pipe(function(){ return _o.css({"display": "none"}).promise(); })
			  .pipe(function(){ document.body.style.overflow = "auto";});
			
			return this;	//facilitate chaining
		}
		
		// 3> Setting the content of the modal
		obj.setContent = function(txt){
			_content.innerHTML = txt;
			return this;
		}
		
		// 4> To extend the Modal itself
		obj.append = function(x){
			_xtra.appendChild(x);
			return this;
		}
		
		/* Close Gesture  -- only if sticky is false */
		if( settings.sticky == false ){
			// close on overlay click
			_o.on("click", function(evt){
				if(evt.target == _overlay){	//target must be the overlay and not its children
					obj.hide();
					return false;
					}
				});
			
			// Close on ESC
			if( settings.closeOnESC == true){
				_m.on('keyup', function(evt){
					if(evt.which == 27){	// 27 => ESC
						obj.hide();
					}
				});
			}
		}
	
		/* Buttons */
		if( settings.buttons != undefined ){
			var container = document.createElement("div");
				container.className = settings.buttonGroupClass + " modal-push-btn-to-right";
			
			var focus = -1;
			var elem = null;
			//foreach button
			for(name in settings.buttons) {
				var btnSettings = settings.buttons[name];
				var x = $("<button />", {"class": btnSettings['class'], "html": name});
					x.on('click', btnSettings['handle']);
				
				if(focus === -1){
					// First Button gets the default focus
					elem = x;
					focus++;
				}
				
				if('focus' in btnSettings && btnSettings['focus'] == true){
					if(focus < 1){
						elem = x;
						focus++;	//only a single button can get focus
					} else {
						// throw or remain silent -- I chose to throw!!
						throw "Multiple buttons cannot receive focus!";
					}
				}
				container.appendChild(x[0]);	//send native dom element here!
			}
			
			if(elem != null){
				_m.on('keyup', function(evt){
					if(evt.which == 13){	// 13 for enter
						$(elem).trigger('click');
					}
				});
			}
			
			obj.append(container);
		}
		
	/* Additional */
		//do we need title?
		var _title = null;
		if( settings.title.length > 0 ){	//yes, we need it
			_title = document.createElement("div");
			_title.className = "modal-title";
			_title.innerHTML = settings.title;
			
			//add to dom, appending to _modal as its first child
			_modal.insertBefore(_title, _content);
			
			//add interface method
			obj.setTitle = function(txt){ 
				_title.innerHTML = txt;
				return this;
			}
		}

		//close button??
		if(settings.addCloseButton === true && settings.sticky == false){	//yess
			var _close = document.createElement("div");	//close button holder
				_close.className = "modal-close";
			var _close_button = document.createElement("a");	//close button
				_close_button.innerHTML = "&times;";
			_close.appendChild(_close_button);
			
			
			if(_title != null){
				_title.appendChild(_close);
			} else {
				_modal.appendChild(_close);	//add to modal
			}
			
			// close handler
			// using jQuery for now, need to remove dependency
			$(_close_button).on("click", function(evt){
				evt.preventDefault();
				obj.hide();
			});
		}		
		
		return obj;
	}
	
	
	//Re-creation of jQuery.extend to remove un-necessary dependency
	//taken from http://youmightnotneedjquery.com/#extend
	function extend(out){
		var out = out || {};
		
		for(var i=1; i<arguments.length; i++){
			var obj = arguments[i];
			
			if(!obj)continue;
			
			for(var key in obj){
				if(obj.hasOwnProperty(key))
					out[key] = obj[key];
			}
		}
		
		return out;
	}
	
}(jQuery, window));