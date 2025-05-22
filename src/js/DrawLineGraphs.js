var canvasWidth = 500;
var canvasHeight = 370;


//global variable
var context;
window.DivID = '0';

function SetDivID(DivID)
{
	window.DivID = DivID;
}

function WindowReady()
{
	//var context = document.getElementById('canvasComplex').getContext("2d"); // Can't do this with IE
	// To account for IE all this must be done
	//This DivID code is written so that all figures are displayed at their respective positions in test report.
	DivID = window.DivID;
	if (DivID == '0')
	{
		var foo = document.getElementById("canvasCrossBrowserDiv");
	}
	else
	{
		var foo = document.getElementById(DivID); 
	}
	//setting the canvas width and height so is not over-written by other js which are also accessing the same variables.
	canvasWidth = 500;
	canvasHeight = 410;
	var canvas = document.createElement('canvas');
	canvas.setAttribute("width", canvasWidth);
	canvas.setAttribute("height", canvasHeight);
	canvas.setAttribute("id", "canvasCrossBrowser");
	foo.appendChild(canvas);
	if (typeof G_vmlCanvasManager != 'undefined') {
		canvas = G_vmlCanvasManager.initElement(canvas);
	}	
	context = canvas.getContext("2d");
	CanvasRenderingContext2D.prototype.dashedLine = 
	function(x1, y1, x2, y2, dashLen) {
	    if (dashLen == undefined) dashLen = 2;
	    
	    var dX = x2 - x1;
	    var dY = y2 - y1;
	    var dashes = Math.floor(Math.sqrt(dX * dX + dY * dY) / dashLen);
	    var dashX = dX / dashes;
	    var dashY = dY / dashes;
	    
	    var q = 0;
	    while (q++ < dashes) {
	     x1 += dashX;
	     y1 += dashY;
	     this[q % 2 == 0 ? 'moveTo' : 'lineTo'](x1, y1);
	    }
	    this[q % 2 == 0 ? 'moveTo' : 'lineTo'](x2, y2);
	};	
}

function P4DrawLineChart1(XAxisMaxNumber,YAxisMaxNumber,XAxisInterval,YAxisInterval,XAxisLabel,YAxisLabel,ChartName,DataPoints)
{
	WindowReady();
	var ChartHeight = 300;
	var ChartWidth = 410;

	var x1 = 50;
	var y1 = 50;
	context.beginPath();
	context.lineWidth = 1;

	// drawing horizontal lines
	var TotalHorizontalLines = 2 * YAxisMaxNumber / YAxisInterval;
	var YAxisDrawInterval = (ChartHeight - y1) / TotalHorizontalLines;

	for (var i=0; i<TotalHorizontalLines+1; i++)
	{
		if (i%2==0)
		{
			context.moveTo(x1-8,y1+i*YAxisDrawInterval);
			if ((YAxisMaxNumber-i*YAxisInterval/2)<10)
			{
				context.fillText(YAxisMaxNumber-i*YAxisInterval/2,x1-20,y1+i*YAxisDrawInterval+5);
			}
			else if (YAxisMaxNumber-i*YAxisInterval/2<100)
			{
				context.fillText(YAxisMaxNumber-i*YAxisInterval/2,x1-25,y1+i*YAxisDrawInterval+5);
			}			
			else
			{
				context.fillText(YAxisMaxNumber-i*YAxisInterval/2,x1-30,y1+i*YAxisDrawInterval+5);
			}
		}
		else
		{
			context.moveTo(x1-5,y1+i*YAxisDrawInterval);
		}
		context.lineTo(ChartWidth,y1+i*YAxisDrawInterval);
	}
	
	// drawing vertical lines
	var TotalVerticalLines = 2 * XAxisMaxNumber / XAxisInterval;
	var XAxisDrawInterval = (ChartWidth - x1) / TotalVerticalLines;

	for (var i=0; i<TotalVerticalLines+1; i++)
	{
		context.moveTo(x1+i*XAxisDrawInterval,y1);
		if(i%2==0)
		{
			context.lineTo(x1+i*XAxisDrawInterval,ChartHeight+7);
			if (i*XAxisInterval/2<10)
			{
				context.fillText(0+i*XAxisInterval/2,x1+i*XAxisDrawInterval-3,ChartHeight+20);
			}
			else
			{
				context.fillText(0+i*XAxisInterval/2,x1+i*XAxisDrawInterval-7,ChartHeight+20);
			}
			
		}		
		else
		{
			context.lineTo(x1+i*XAxisDrawInterval,ChartHeight);
		}
	}
	
	context.strokeStyle="grey";
	context.stroke();
	
	//drawing and connecting dots 
	
	context.beginPath();
	for (i=0;i<DataPoints.length;i++)
	{
		context.arc(x1+DataPoints[i][0]*XAxisDrawInterval/XAxisInterval*2,y1+(YAxisMaxNumber-DataPoints[i][1])*2*YAxisDrawInterval/YAxisInterval,2,0,2*Math.PI,true);
	}
	
	context.strokeStyle="red";
	context.stroke();
	
	// Labeling the graph
	context.beginPath();
	context.font = "bold 9pt Courier";
	context.fillText(ChartName,x1+100,y1-20);
	
	context.font = "9pt Courier";
	context.fillText(XAxisLabel,x1+150,y1+ChartHeight);
	
	//Y-axis label (writing it vertical)
	var x1 = 50;
	var y1 = 20;
	context.save();
	context.translate(x1, y1+ChartHeight/2);  
	context.rotate(-Math.PI/2);  
	context.textAlign = "center";  
	context.fillText(YAxisLabel, 0, -40);  
	context.restore(); 
	
	
	//context.fillText(YAxisLabel,x1-90,y1+ChartHeight/2);
}

function P4DrawLineChart2(XAxisMaxNumber,YAxisMaxNumber,XAxisInterval,YAxisInterval,XAxisLabel,YAxisLabel,ChartName,DataPoints,DayNames)
{
	WindowReady();
	var ChartHeight = 300;
	var ChartWidth = 410;

	var x1 = 50;
	var y1 = 50;
	context.beginPath();
	context.lineWidth = 1;

	// drawing horizontal lines
	var TotalHorizontalLines = 2 * YAxisMaxNumber / YAxisInterval;
	var YAxisDrawInterval = (ChartHeight - y1) / TotalHorizontalLines;

	for (var i=0; i<TotalHorizontalLines+1; i++)
	{
		if (i%2==0)
		{
			context.moveTo(x1-8,y1+i*YAxisDrawInterval);
			if ((YAxisMaxNumber-i*YAxisInterval/2)<10)
			{
				context.fillText(YAxisMaxNumber-i*YAxisInterval/2,x1-20,y1+i*YAxisDrawInterval+5);
			}
			else if (YAxisMaxNumber-i*YAxisInterval/2<100)
			{
				context.fillText(YAxisMaxNumber-i*YAxisInterval/2,x1-25,y1+i*YAxisDrawInterval+5);
			}			
			else
			{
				context.fillText(YAxisMaxNumber-i*YAxisInterval/2,x1-30,y1+i*YAxisDrawInterval+5);
			}
		}
		else
		{
			context.moveTo(x1-5,y1+i*YAxisDrawInterval);
		}
		context.lineTo(ChartWidth,y1+i*YAxisDrawInterval);
	}
	
	// drawing vertical lines
	var TotalVerticalLines = XAxisMaxNumber / XAxisInterval;
	var XAxisDrawInterval = (ChartWidth - x1) / TotalVerticalLines;

	for (var i=0; i<TotalVerticalLines+1; i++)
	{
		context.moveTo(x1+i*XAxisDrawInterval,y1);
		context.lineTo(x1+i*XAxisDrawInterval,ChartHeight+7);
		context.fillText(DayNames[i],x1+i*XAxisDrawInterval-3,ChartHeight+20);
	}
	
	context.strokeStyle="grey";
	context.stroke();
	
	//drawing and connecting dots 
	
	context.beginPath();
	for (i=0;i<DataPoints.length;i++)
	{
		context.arc(x1+DataPoints[i][0]*XAxisDrawInterval/XAxisInterval,y1+(YAxisMaxNumber-DataPoints[i][1])*2*YAxisDrawInterval/YAxisInterval,2,0,2*Math.PI,true);
	}
	
	context.strokeStyle="red";
	context.stroke();
	
	// Labeling the graph
	context.beginPath();
	context.font = "bold 9pt Courier";
	context.fillText(ChartName,x1+100,y1-20);
	
	context.font = "9pt Courier";
	context.fillText(XAxisLabel,x1+150,y1+ChartHeight);

	//Y-axis label (writing it vertical)
	var x1 = 50;
	var y1 = 20;
	context.save();
	context.translate(x1, y1+ChartHeight/2);  
	context.rotate(-Math.PI/2);  
	context.textAlign = "center";  
	context.fillText(YAxisLabel, 0, -40);  
	context.restore(); 
	
	//context.fillText(YAxisLabel,x1-90,y1+ChartHeight/2);
}

var colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"];

function getRandomArrayElements(arr, count)
{     
	var randoms = [], clone = arr.slice(0);     
	for (var i = 0, index; i < count; ++i) 
	{         
		index = Math.floor(Math.random() * clone.length);         
		randoms.push(clone[index]);         
		clone[index] = clone.pop();     
	}     
	return randoms; 
}

function get_colour()
{
	var colour_code = Math.floor(Math.random()*colours.length);
	return colours[colour_code];
}