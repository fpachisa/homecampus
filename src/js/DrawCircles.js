var canvasWidth = 250;
var canvasHeight = 200;


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

function DrawCircle1(diameter,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (0 + Math.random()*(90-20))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (diameter<10)
		{
			var radius = 50;
		}
	else if (diameter<20)
		{
			var radius = 60;
		}
	else
		{
			var radius = 70;
		}
	context.beginPath();
	context.moveTo(x1-radius,y1);
	context.lineTo(x1+radius,y1);
	context.lineWidth = 2;
	context.arc(x1,y1,radius,0,2*Math.PI,true);
	
	context.strokeStyle="black";
	context.stroke();
	
	context.closePath();
	context.fillStyle = "blue";
    if (unit ==1)
    	{
    		unit = "cm";
    	}
    else
    	{
    		unit = "m";
    	}
    context.font = "10pt Calibri";
	context.fillText(diameter+" "+unit,x1-10,y1-5);
	context.restore();
}

function DrawCircle2(radius,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (0 + Math.random()*(90-20))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (radius<10)
		{
			var drawRadius = 50;
		}
	else if (radius<20)
		{
			var drawRadius = 60;
		}
	else
		{
			var drawRadius = 70;
		}
	context.beginPath();
	context.moveTo(x1,y1);
	context.lineTo(x1+drawRadius,y1);
	context.lineWidth = 2;
	context.arc(x1,y1,drawRadius,0,2*Math.PI,true);
	context.strokeStyle="black";
	context.stroke();
	context.closePath();

	context.beginPath();
	context.fillStyle = "blue";
    if (unit ==1)
    	{
    		unit = "cm";
    	}
    else
    	{
    		unit = "m";
    	}
    context.font = "10pt Calibri";
    context.arc(x1,y1,3,0,2*Math.PI,true);
    context.fill();
	context.fillText(radius+" "+unit,x1+drawRadius/3,y1-5);
	context.restore();
}

function DrawSemiCircle1(diameter,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (0 + Math.random()*(90-20))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (diameter<10)
		{
			var radius = 50;
		}
	else if (diameter<20)
		{
			var radius = 60;
		}
	else
		{
			var radius = 70;
		}
	context.beginPath();
	context.moveTo(x1-radius,y1);
	context.lineTo(x1+radius,y1);
	context.lineWidth = 2;
	context.arc(x1,y1,radius,0,Math.PI,true);
	
	context.strokeStyle="black";
	context.stroke();
	
	context.closePath();
	context.fillStyle = get_random_color();
    if (unit ==1)
    	{
    		unit = "cm";
    	}
    else
    	{
    		unit = "m";
    	}
    context.font = "9pt Calibri";
    context.arc(x1,y1,1,0,2*Math.PI,true);
    context.moveTo(x1-radius,y1+5);
    context.lineTo(x1-radius,y1+11);
    context.moveTo(x1-radius,y1+8);
    context.lineTo(x1+radius,y1+8);
    context.moveTo(x1+radius,y1+5);
    context.lineTo(x1+radius,y1+11);
    context.fill();
    context.stroke();
    context.closePath();
    context.beginPath();
    context.fillStyle = "black";
    context.fillText(diameter+" "+unit,x1-10,y1+25);
    context.restore();
}

function DrawSemiCircle2(radius,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (0 + Math.random()*(90-20))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (radius<10)
		{
			var drawRadius = 50;
		}
	else if (radius<20)
		{
			var drawRadius = 60;
		}
	else
		{
			var drawRadius = 70;
		}
	context.beginPath();
	context.moveTo(x1,y1);
	context.lineTo(x1+drawRadius,y1);
	context.lineWidth = 2;
	context.arc(x1,y1,drawRadius,0,Math.PI,true);
	
	context.strokeStyle="black";
	context.stroke();
	
	context.closePath();
	context.fillStyle = get_random_color();
    if (unit ==1)
    	{
    		unit = "cm";
    	}
    else
    	{
    		unit = "m";
    	}
    context.font = "9pt Calibri";
    context.arc(x1,y1,1,0,2*Math.PI,true);
    context.moveTo(x1,y1+5);
    context.lineTo(x1,y1+11);
    context.moveTo(x1,y1+8);
    context.lineTo(x1+drawRadius,y1+8);
    context.moveTo(x1+drawRadius,y1+5);
    context.lineTo(x1+drawRadius,y1+11);
    context.fill();
    context.stroke();
    context.closePath();
    context.beginPath();
    context.fillStyle = "black";
    context.fillText(radius+" "+unit,x1+drawRadius/3,y1+25);
    context.restore();
}

function DrawQuarterCircle1(radius,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-90 + Math.random()*(90-20))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (radius<10)
		{
			var drawRadius = 50;
		}
	else if (radius<20)
		{
			var drawRadius = 60;
		}
	else
		{
			var drawRadius = 70;
		}
	context.beginPath();
	context.moveTo(x1,y1);
	context.lineWidth = 2;
	context.arc(x1,y1,drawRadius,3*Math.PI/2,0,false);
	
	context.strokeStyle="black";
	context.stroke();
	
	context.closePath();
	context.fillStyle = get_random_color();
    if (unit ==1)
    	{
    		unit = "cm";
    	}
    else
    	{
    		unit = "m";
    	}
    context.font = "9pt Calibri";
    context.arc(x1,y1,1,0,2*Math.PI,true);
    context.moveTo(x1,y1+5);
    context.lineTo(x1,y1+11);
    context.moveTo(x1,y1+8);
    context.lineTo(x1+drawRadius,y1+8);
    context.moveTo(x1+drawRadius,y1+5);
    context.lineTo(x1+drawRadius,y1+11);
    context.fill();
    context.stroke();
    context.closePath();
    context.beginPath();
    context.fillStyle = "black";
    context.fillText(radius+" "+unit,x1+drawRadius/3,y1+25);
    context.restore();
}
function get_random_color() 
{
	var colour_code = Math.floor(Math.random()*56);
	var colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"];
	return colours[colour_code];
}