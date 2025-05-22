var WIDTH = "100%";
var HEIGHT = 400;

$(document).ready(function() 
 	{ 		  	
		$("body").on('click', "#GenerateReport", function() 
	    	{
				$(this).attr("disabled", true);
				var username = $("#username").val();
				var grade = $("#grade").val();
				var URL = "/Progress/Generate_Dashboard_Report";
				AJAXCall(URL,username,grade);	            				
	    	});
	}
);

function AJAXCall(URL,username,grade)
{            	
	$("#ReportContent").html('<img style="margin-left:400px;margin-top:80px;" alt="Generating Report" src="/images/site/InProgress.gif">');
	var URLText = URL
	var data = {username:username,grade:grade};
	$.ajax(
	{
		type: "POST",
		url: URLText,
		data: data,
		success: function(responseText)
		{                   
			$("#GenerateReport").attr("disabled", false);
			$("#ReportContent").html('');
			$("#ReportContent").html(responseText);
		}
	});    
}

function AJAXCall1(URL,username,reportname,grade)
{            	
	$("#ReportContent").html('<img style="margin-left:400px;margin-top:80px;" alt="Generating Report" src="/images/site/InProgress.gif">');
	var URLText = URL
	var data = {username:username,reportname:reportname,grade:grade};
	$.ajax(
	{
		type: "POST",
		url: URLText,
		data: data,
		success: function(responseText)
		{                   
			$("#GenerateReport").attr("disabled", false);
			$("#ReportContent").html(responseText);
		}
	});    
}

function AJAXCall2(URL,username,reportname,grade,topic,TopicName)
{            	
	$("#ReportContent").html('<img style="margin-left:400px;margin-top:80px;" alt="Generating Report" src="/images/site/InProgress.gif">');
	var URLText = URL
	var data = {username:username,reportname:reportname,grade:grade,topic:topic,TopicName:TopicName};
	$.ajax(
	{
		type: "POST",
		url: URLText,
		data: data,
		success: function(responseText)
		{                   
			$("#GenerateReport").attr("disabled", false);
			$("#ReportContent").html(responseText);
		}
	});    
}


// Google Charts Object

/*
 * Firstly, collect all the data from the backend using the same routines
 * Then, iterate through the :charts: object and call :draw: on each object -- :draw: must be present in each sub-object of charts
 * 
 * Why all this? This will help save the data and re-draw charts on window resize, making them responsive
 */
var charts = {};

// Library loaded?
charts.ready = false;

// Google Charts onLoad Handler
charts.onLoadComplete = function(){
	charts.ready = true;
	charts.drawAll();
};


// (Re)draw all the charts
charts.drawAll = function(){
	if(!charts.ready)
		return;
		
	for(key in charts){
		if(charts[key].hasOwnProperty("draw")){			
			charts[key].draw();
		}
	}
}

// Adding a Listener for window.onresize
$(window).on("resize", function(evt){
	charts.drawAll();
});

//Column Chart
charts.columnChart = {
	data: [],
	title: "",
	draw: function(params){
		var _d = new google.visualization.arrayToDataTable(this.data);	//Data Table
	    
		// Charts Options
		var defaults = {'title': this.title,
                'width': WIDTH,
                'height': HEIGHT,
                //'backgroundColor':'#E9FCFA',
                'hAxis': {title: 'Topic'},
                'colors':['#3367d6','green'],
                'vAxis': {minValue:10,format:'#'}
                };

		params = params || {};
	    var options = $.extend({}, defaults, params);

	    // Instantiate and draw our chart, passing in some options.
	    var chart = new google.visualization.ColumnChart(document.getElementById('columnbar'));
	    chart.draw(_d, options);
	}
};

// Bar Charts
charts.barCharts = {
	data: [],
	title: "",
	draw: function(params){
		var _d = new google.visualization.DataTable();
		_d.addColumn('string', 'Topics');
		_d.addColumn('number', 'Average % Scored');
		_d.addRows(this.data);
		
		// Set chart options
		var defaults = {
				'title': this.title,
				'width': WIDTH,
				'height': HEIGHT,
				'tooltip':{text:'percentage'},
				'hAxis':{minValue:0,maxValue:100},
				'colors':['orange']
				};
		
		params = params || {};
	    var options = $.extend({}, defaults, params);

		// Instantiate and draw our chart, passing in some options.
		var chart = new google.visualization.BarChart(document.getElementById('barChart'));
		chart.draw(_d, options);
	}
};

//Pie Charts
charts.pieChart = {
	data: [],
	title: "",
	draw: function(params){
		var _d = new google.visualization.DataTable();	//Data Table
	    _d.addColumn('string', 'Topics');
	    _d.addColumn('number', 'Slices');
	    _d.addRows( this.data );

	    // Set chart options
	    var defaults = {'title': this.title,
	                   'width':WIDTH,
	                   'height':HEIGHT,
	                   'tooltip':{text:'percentage'}
	                   };
	    
	    params = params || {};
	    var options = $.extend({}, defaults, params);
	    
	    // Instantiate and draw our chart, passing in the options
	    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
	    chart.draw( _d, options);
	}
};



// TestReport Pie Chart
charts.testPieChart = {
	data: [],
	title: "",
	draw: function(params){
		var _d = new google.visualization.DataTable();
	    _d.addColumn('string', 'Topics');
	    _d.addColumn('number', 'Slices');
	    _d.addRows( this.data );

	    // Set chart options
	    var defaults = {
	    		'title':this.title,
	    		'width': WIDTH,
	    		'height': HEIGHT
	    		};
	    
	    params = params || {};
	    var options = $.extend({}, defaults, params);
	    
	    // Instantiate and draw our chart, passing in some options.
	    var chart = new google.visualization.PieChart(document.getElementById('piechart'));
	    chart.draw(_d, options);
	}
};

// ----- Data Accumulator Routines -----
// Using same names here to maintain compatibility

function drawGooglePieChart(Data, Title) {
	// Accumulator for PieChart
	charts.pieChart.data = Data;
	charts.pieChart.title = Title;
	charts.drawAll();
}

function drawGoogleColumnChart(Data, Title) {
	// Accumulator for ColumnChart
	charts.columnChart.data = Data;
	charts.columnChart.title = Title;
	charts.drawAll();
}

function drawGoogleBarChart(Data, Title) {
	charts.barCharts.data = Data;
	charts.barCharts.title = Title;
	charts.drawAll();
}

function drawGoogleTestReportPieChart(Data, Title) {
	charts.testPieChart.data = Data;
	charts.testPieChart.title = Title;
	charts.drawAll();
}

// ----- END of Data Accumulators -----
// ------------------------------------


function DetailTestReport(item)
{
	$("#ReportContent").html('<img style="margin-left:400px;margin-top:80px;" alt="Generating Report" src="/images/site/InProgress.gif">');
	var TestId = $(item).attr("id"); 
	GenerateTestReport(TestId);
}

function GenerateTestReport(TestId)
{
	var data = {TestId:TestId};
	$.ajax(
	{
		type: "POST",
		url: "/Progress/Generate_Test_Report",
		data: data,
		success: function(responseText)
		{
			$("#ReportContent").show("fast");
			$("#ReportContent").html(responseText);
		}				
	});
}

function DetailConceptReport(item)
{
	$("#ReportContent").html('<img style="margin-left:400px;margin-top:80px;" alt="Generating Report" src="/images/site/InProgress.gif">');
	var parameters = $(item).attr("id"); 
	var URL = "/Progress/Generate_Detail_Report";
	var parameters = parameters.split(",");
	var topic = parameters[0]
	var grade = 'P'+parameters[1]
	var username = parameters[2]
	var topicName = parameters[3]
	var reportname = "DetailReport"
	AJAXCall2(URL,username,reportname,grade,topic,topicName);
}

function ProblemReport(item)
{
	$("#ReportContent").html('<img style="margin-left:400px;margin-top:80px;" alt="Generating Report" src="/images/site/InProgress.gif">');
	var parameters = $(item).attr("id"); 
	var URL = "/Progress/Generate_Problem_Report";
	var parameters = parameters.split(",");
	var topic = parameters[0]
	var grade = 'P'+parameters[1]
	var username = parameters[2]
	var topicName = parameters[3]
	var reportname = "ProblemReport"
	AJAXCall2(URL,username,reportname,grade,topic,topicName);
}

function StudentReport(item)
{
	$("#ReportContent").html('<img style="margin-left:400px;margin-top:80px;" alt="Generating Report" src="/images/site/InProgress.gif">');
	var student_username = $(item).attr("id") ; 
	var URL = "/Progress/Generate_Student_Report";
	var data = {student_username:student_username}
	$.ajax(
			{
				type: "POST",
				url: URL,
				data: data,
				success: function(responseText)
				{
					$("#ReportContent").show("fast");
					$("#ReportContent").html(responseText);
				}				
			});
}

