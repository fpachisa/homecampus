/*
 * The TopicalUI JS
 */
$(document).ready(function(){
	var viewport = {
		width  : $(window).width(),
		height : $(window).height()
	};
	
	if(viewport.width > 768){
		makeSidebarFixed();
	}
	
	/* SideBar Collapse Management */
	current = $(".topical-ui__links.active");
	$("body").on("click", ".topical-ui__links-trigger", function(evt){
		evt.preventDefault();
		var parent = $(this).parent();
		
		//slide up curent
		current.children("ul").hide();
		current.removeClass("active");
		
		//slide down new one
		parent.addClass("active");
		parent.children("ul").show();
		
		current = parent;
	});
	
});

function makeSidebarFixed(){
	var sidebar = $(".topical-ui__sidebar");
	
	//get the sidebar's offset
	var offsetTop = 55;//sidebar.position().top;
	
	$(window).on('scroll', function(){
		if($(this).scrollTop() >= offsetTop){
			if(!sidebar.hasClass("fixed"))
				sidebar.addClass("fixed");
		} else if ($(this).scrollTop() < offsetTop) {
			if(sidebar.hasClass("fixed"))
				sidebar.removeClass("fixed");
		}
	});
}