/*
 * [TODO]
 * Add State Change animations to the Reports and enable back-btn navigation
 */
var ExplainDialog = popie({
	addCloseButton: true,
	title: "<h4>Explanation</h4>",
	defineHeightAsCss: true,
	modalClass: "ExplainDialog",	//hc-basic
	buttons: { "Ok": {'class': 'btn-modal', 'handle': function(){ ExplainDialog.hide(); } } },
	buttonGroupClass: "btn-group"
});
$(document).ready(function(){
	
	//listen for click on .btn-exp
	$("body").on("click", ".btn-exp", function(evt){
		explainContent = $( "#" + $(this).attr("data-explain-tag") ).html();
		
		ExplainDialog
			.setContent(explainContent)
			.show();
	});	
});