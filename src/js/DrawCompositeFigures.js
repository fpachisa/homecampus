var canvasWidth = 250;
var canvasHeight = 220;


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

function DrawCircleSquare1(diameter,unit)
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
	context.lineWidth = 2;
	context.strokeRect(x1-radius,y1-radius,2*radius,2*radius);	
	context.strokeStyle="black";
	context.stroke();
	context.arc(x1,y1,radius,0,2*Math.PI,true);

	context.fillStyle = get_random_color();
	context.fill();
	if (unit ==1)
    	{
    		unit = "cm";
    	}
    else
    	{
    		unit = "m";
    	}
    context.font = "10pt Calibri";
    context.moveTo(x1-radius,y1-radius-3);
    context.lineTo(x1-radius,y1-radius-9);
    context.moveTo(x1-radius,y1-radius-6);
    context.lineTo(x1+radius,y1-radius-6);
    context.moveTo(x1+radius,y1-radius-3);
    context.lineTo(x1+radius,y1-radius-9);
    context.stroke();
    context.closePath();
    context.beginPath();
    context.fillStyle = "black";    
    context.fillText(diameter+" "+unit,x1-10,y1-radius-9);

    context.restore();
}
function DrawCircleSquare2(diameter,unit)
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
	context.lineWidth = 3;
	context.strokeRect(x1-radius,y1-radius,2*radius,2*radius);	
	context.strokeStyle="black";	
	context.arc(x1,y1,radius,0,2*Math.PI,true);
	context.stroke();	
	context.fillStyle = get_random_color();
	context.fill();
    context.restore();
}
function DrawThreeFourthCircle(radius,unit)
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

	context.lineWidth = 3;
	context.strokeStyle="black";
	context.arc(x1,y1,drawRadius,0,Math.PI,true);
	context.closePath();
	context.moveTo(x1,y1);
	var startAngle = (0.6 + Math.random()*(0.8-0.6)) * Math.PI
	context.arc(x1,y1,drawRadius,startAngle,startAngle-Math.PI/2,true);
	context.closePath();
	context.stroke();
	context.fillStyle = get_random_color();
	context.fill();
	context.restore();
}
function DrawQuadrants1(radius,unit,flag)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (0 + Math.random()*(180-0))*(Math.PI/180);
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

	context.lineWidth = 3;
	context.strokeStyle="black";
	if (flag == 2)
		{
			context.moveTo(x1,y1-drawRadius);
			context.arc(x1,y1-drawRadius,drawRadius,0,Math.PI/2,false);
			context.closePath();
			context.moveTo(x1,y1+drawRadius);
			context.arc(x1,y1+drawRadius,drawRadius,Math.PI,-Math.PI/2,false);
			context.closePath();
		}
	else if (flag == 3)
		{
			context.moveTo(x1,y1-drawRadius);
			context.arc(x1,y1-drawRadius,drawRadius,0,Math.PI/2,false);
			context.closePath();
			context.moveTo(x1-drawRadius,y1);
			context.arc(x1-drawRadius,y1,drawRadius,-Math.PI/2,0,false);
			context.closePath();		
			context.moveTo(x1,y1+drawRadius);
			context.arc(x1,y1+drawRadius,drawRadius,Math.PI,-Math.PI/2,false);
			context.closePath();
		}
	else if (flag == 4)
	{
		context.moveTo(x1,y1-drawRadius);
		context.arc(x1,y1-drawRadius,drawRadius,0,Math.PI/2,false);
		context.closePath();
		context.moveTo(x1-drawRadius,y1);
		context.arc(x1-drawRadius,y1,drawRadius,-Math.PI/2,0,false);
		context.closePath();		
		context.moveTo(x1,y1+drawRadius);
		context.arc(x1,y1+drawRadius,drawRadius,Math.PI,-Math.PI/2,false);
		context.closePath();
		context.moveTo(x1+drawRadius,y1);
		context.arc(x1+drawRadius,y1,drawRadius,Math.PI/2,Math.PI,false);
		context.closePath();		
	}
	context.stroke();
	context.fillStyle = get_random_color();
	context.fill();
	context.restore();
}
function DrawRectangleSemiCircles1(radius1,radius2,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height*1.2/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-40 + Math.random()*(40-(-40)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (unit == 1)
		{
			unit = "cm";
		}
	else 
	{
		unit = "m";
	}
	if (radius2<5)
		{
			var drawRadius1 = 30;
			var drawRadius2 = 50;
		}
	else if (radius2<10)
		{
			var drawRadius1 = 40;
			var drawRadius2 = 60;
		}
	else
		{
			var drawRadius1 = 50;
			var drawRadius2 = 70;
		}
	context.beginPath();

	context.lineWidth = 3;
	context.strokeStyle="black";

	context.arc(x1,y1-drawRadius1,drawRadius2,0,Math.PI,true);
	context.arc(x1+drawRadius2,y1,drawRadius1,-Math.PI/2,Math.PI/2,false);
	context.closePath();
	var color = get_random_color();
	context.fillStyle = color;
	context.strokeRect(x1-drawRadius2,y1-drawRadius1,2*drawRadius2,2*drawRadius1);
	context.fillRect(x1-drawRadius2,y1-drawRadius1,2*drawRadius2,2*drawRadius1);
	context.stroke();
	context.fillStyle = color;
	context.fill();
	context.lineWidth = 1;
	context.moveTo(x1-drawRadius2-13,y1-drawRadius1);
	context.lineTo(x1-drawRadius2-5,y1-drawRadius1);
	context.moveTo(x1-drawRadius2-9,y1-drawRadius1);
	context.lineTo(x1-drawRadius2-9,y1+drawRadius1);
	context.moveTo(x1-drawRadius2-13,y1+drawRadius1);
	context.lineTo(x1-drawRadius2-5,y1+drawRadius1);
	context.strokeText(2*radius1+" "+unit,x1-drawRadius2-40,y1);

	context.moveTo(x1-drawRadius2,y1+drawRadius1+13);
	context.lineTo(x1-drawRadius2,y1+drawRadius1+5);
	context.moveTo(x1-drawRadius2,y1+drawRadius1+9);
	context.lineTo(x1+drawRadius2,y1+drawRadius1+9);
	context.moveTo(x1+drawRadius2,y1+drawRadius1+13);
	context.lineTo(x1+drawRadius2,y1+drawRadius1+5);
	context.strokeText(2*radius2+" "+unit,x1,y1+drawRadius1+20);
	
	context.stroke();

	context.restore();
}
function DrawTriangleSemiCircles1(radius1,radius2,unit)
{
	WindowReady();
	var x1 = context.canvas.width*1.3/2;
	var y1 = context.canvas.height*1.3/3;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (0 + Math.random()*(30-(0)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (unit == 1)
		{
			unit = "cm";
		}
	else 
	{
		unit = "m";
	}
	if (radius2<5)
		{
			var drawRadius1 = 30;
			var drawRadius2 = 40;
		}
	else if (radius2<10)
		{
			var drawRadius1 = 40;
			var drawRadius2 = 50;
		}
	else
		{
			var drawRadius1 = 50;
			var drawRadius2 = 60;
		}
	context.beginPath();

	context.lineWidth = 3;
	context.strokeStyle="black";
	var color = get_random_color();	
	context.moveTo(x1+drawRadius2,y1+drawRadius1);
	context.lineTo(x1-drawRadius2,y1+drawRadius1);
	context.lineTo(x1-drawRadius2,y1-drawRadius1);
	context.closePath();

	context.fillStyle = color;
	context.fill();
	context.arc(x1-drawRadius2,y1,drawRadius1,-Math.PI/2,Math.PI/2,true);
	context.arc(x1,y1+drawRadius1,drawRadius2,Math.PI,0,true);

	context.fillStyle = color;
	context.stroke();
	context.fill();
	context.lineWidth = 1;
	context.moveTo(x1-drawRadius2-13,y1-drawRadius1);
	context.lineTo(x1-drawRadius2-5,y1-drawRadius1);
	context.moveTo(x1-drawRadius2-9,y1-drawRadius1);
	context.lineTo(x1-drawRadius2-9,y1+drawRadius1);
	context.moveTo(x1-drawRadius2-13,y1+drawRadius1);
	context.lineTo(x1-drawRadius2-5,y1+drawRadius1);
	context.strokeText(2*radius1+" "+unit,x1-drawRadius2-40,y1);

	context.moveTo(x1-drawRadius2,y1+drawRadius1+13);
	context.lineTo(x1-drawRadius2,y1+drawRadius1+5);
	context.moveTo(x1-drawRadius2,y1+drawRadius1+9);
	context.lineTo(x1+drawRadius2,y1+drawRadius1+9);
	context.moveTo(x1+drawRadius2,y1+drawRadius1+13);
	context.lineTo(x1+drawRadius2,y1+drawRadius1+5);
	context.strokeText(2*radius2+" "+unit,x1,y1+drawRadius1+20);
	
	context.stroke();

	context.restore();
}
function DrawTwoSemiCircles1(radius1,radius2,diff,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-40 + Math.random()*(40-(-40)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (unit == 1)
		{
			unit = "cm";
		}
	else 
	{
		unit = "m";
	}
	var drawRadius1 = 30 + 2*radius1;
	if (diff == 0)
		{
			diff = 0;
		}
	else
		{
			diff = 10 + 2*diff;
		}
	var drawRadius2 = drawRadius1 + diff + 10;
	context.beginPath();

	context.lineWidth = 3;
	context.strokeStyle="black";
	var color = get_random_color();	
	context.arc(x1+diff,y1,drawRadius2,0,Math.PI,true);
	context.fillStyle = color;
	context.stroke();
	context.fill();

	context.beginPath();
	/* coloring the second semi-circle with the canvas color. So that it remains invsible. 
	If ever the canvas color is changed this color also will have to be changed */
	context.fillStyle = "#EEFFFE";
	context.arc(x1,y1,drawRadius1,0,Math.PI,true);	
	context.stroke();
	context.fill();
	context.lineWidth = 1;
	context.font = "10pt Calibri";
	
	// just closing the edge of the semicircles
	context.moveTo(x1+diff-drawRadius2,y1);
	context.lineTo(x1-drawRadius1,y1);
	context.moveTo(x1+diff+drawRadius2,y1);
	context.lineTo(x1+drawRadius1,y1);
	
	context.moveTo(x1-drawRadius1,y1+5);
	context.lineTo(x1-drawRadius1,y1+13);
	context.moveTo(x1-drawRadius1,y1+9);
	context.lineTo(x1+drawRadius1,y1+9);
	context.moveTo(x1+drawRadius1,y1+5);
	context.lineTo(x1+drawRadius1,y1+13);
	context.strokeText(2*radius1+" "+unit,x1,y1+20);

	context.moveTo(x1+diff-drawRadius2,y1+18);
	context.lineTo(x1+diff-drawRadius2,y1+26);
	context.moveTo(x1+diff-drawRadius2,y1+22);
	context.lineTo(x1+diff+drawRadius2,y1+22);
	context.moveTo(x1+diff+drawRadius2,y1+18);
	context.lineTo(x1+diff+drawRadius2,y1+26);
	context.strokeText(2*radius2+" "+unit,x1+diff,y1+33);
	
	context.stroke();

	context.restore();
}
function DrawTwoSemiCircles2(radius1,radius2,diff,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-40 + Math.random()*(40-(-40)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (unit == 1)
		{
			unit = "cm";
		}
	else 
	{
		unit = "m";
	}
	var drawRadius1 = 4*radius1;
	var drawDiff = 4*diff;
	var drawRadius2 = 4*radius2;
	context.beginPath();

	context.lineWidth = 3;
	context.strokeStyle="black";
	var color = get_random_color();	
	context.arc(x1+drawDiff,y1,drawRadius2,0,Math.PI,true);
	context.fillStyle = color;
	context.stroke();
	context.fill();
	context.beginPath();
	context.arc(x1,y1,drawRadius1,0,Math.PI,true);
	context.fillStyle = "#EEFFFE";
	context.stroke();
	context.fill();
	
	context.lineWidth = 1;
	context.font = "9pt Calibri";
	var bigDiff = drawRadius2 + drawDiff - drawRadius1;
	var smallDiff = drawRadius2 - drawDiff - drawRadius1;
	context.moveTo(x1+drawRadius1+bigDiff/2-3,y1+5);
	context.lineTo(x1+drawRadius1+bigDiff/2-3,y1+18);
	context.moveTo(x1+drawRadius1+bigDiff/2-3,y1+5);
	context.lineTo(x1+drawRadius1+bigDiff/2-5,y1+8);
	context.moveTo(x1+drawRadius1+bigDiff/2-3,y1+5);
	context.lineTo(x1+drawRadius1+bigDiff/2-1,y1+8);
	var displayBigDiff = radius2 + diff - radius1;
	context.strokeText(displayBigDiff+" "+unit,x1+drawRadius1+bigDiff/2+2,y1+30);

	context.moveTo(x1-drawRadius1-smallDiff/2-3,y1+5);
	context.lineTo(x1-drawRadius1-smallDiff/2-3,y1+18);
	context.moveTo(x1-drawRadius1-smallDiff/2-3,y1+5);
	context.lineTo(x1-drawRadius1-smallDiff/2-5,y1+8);
	context.moveTo(x1-drawRadius1-smallDiff/2-3,y1+5);
	context.lineTo(x1-drawRadius1-smallDiff/2-1,y1+8);
	var displaySmallDiff = radius2 - diff - radius1;
	context.strokeText(displaySmallDiff+" "+unit,x1-drawRadius1-smallDiff/2+2,y1+30);

	context.moveTo(x1-drawRadius1,y1+5);
	context.lineTo(x1-drawRadius1,y1+13);
	context.moveTo(x1-drawRadius1,y1+9);
	context.lineTo(x1+drawRadius1,y1+9);
	context.moveTo(x1+drawRadius1,y1+5);
	context.lineTo(x1+drawRadius1,y1+13);
	context.strokeText(2*radius1+" "+unit,x1,y1+20);
	
	context.moveTo(x1+drawRadius1,y1);
	context.lineTo(x1+drawRadius1+bigDiff,y1);
	context.moveTo(x1-drawRadius1,y1);
	context.lineTo(x1-drawRadius1-smallDiff,y1);
	context.stroke();

	context.restore();
}
function DrawTwoSemiCirclesSquare1(radius1,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-40 + Math.random()*(40-(-40)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (unit == 1)
		{
			unit = "cm";
		}
	else 
	{
		unit = "m";
	}
	var drawRadius1 = 4*radius1;

	context.beginPath();
	context.lineWidth = 3;
	context.strokeStyle="black";
	var color = get_random_color();	
	context.arc(x1+drawRadius1,y1-drawRadius1,drawRadius1,Math.PI,Math.PI/2,true);
	context.arc(x1-drawRadius1,y1+drawRadius1,drawRadius1,-Math.PI/2,0,false);
	context.strokeRect(x1-drawRadius1,y1-drawRadius1,2*drawRadius1,2*drawRadius1);
	context.closePath();
	context.fillStyle = color;
	context.stroke();
	context.fill();
	context.lineWidth = 1;
	context.font = "9pt Calibri";
	context.moveTo(x1-drawRadius1-5,y1-drawRadius1);
	context.lineTo(x1-drawRadius1-13,y1-drawRadius1);
	context.moveTo(x1-drawRadius1-9,y1-drawRadius1);
	context.lineTo(x1-drawRadius1-9,y1);
	context.moveTo(x1-drawRadius1-5,y1);
	context.lineTo(x1-drawRadius1-13,y1);
	context.strokeText(radius1,x1-drawRadius1-35,y1-drawRadius1/2);

	context.moveTo(x1-drawRadius1-5,y1+drawRadius1);
	context.lineTo(x1-drawRadius1-13,y1+drawRadius1);
	context.moveTo(x1-drawRadius1-9,y1+drawRadius1);
	context.lineTo(x1-drawRadius1-9,y1);
	context.moveTo(x1-drawRadius1-5,y1);
	context.lineTo(x1-drawRadius1-13,y1);
	context.strokeText(radius1,x1-drawRadius1-35,y1+drawRadius1/2);

	context.moveTo(x1-drawRadius1,y1-drawRadius1-5);
	context.lineTo(x1-drawRadius1,y1-drawRadius1-13);
	context.moveTo(x1-drawRadius1,y1-drawRadius1-9);
	context.lineTo(x1+drawRadius1,y1-drawRadius1-9);
	context.moveTo(x1+drawRadius1,y1-drawRadius1-5);
	context.lineTo(x1+drawRadius1,y1-drawRadius1-13);
	context.strokeText(2*radius1+" "+unit,x1,y1-drawRadius1-20);
	
	context.stroke();

	context.restore();
}
function DrawTwoSemiCirclesSquare2(radius1,unit)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-40 + Math.random()*(40-(-40)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;
	var unit = unit;
	if (unit == 1)
		{
			unit = "cm";
		}
	else 
	{
		unit = "m";
	}
	var drawRadius1 = 4*radius1;

	context.beginPath();
	context.lineWidth = 3;
	context.strokeStyle="black";
	var color = get_random_color();	
	context.arc(x1+drawRadius1,y1-drawRadius1,2*drawRadius1,Math.PI,Math.PI/2,true);
	context.arc(x1-drawRadius1,y1+drawRadius1,2*drawRadius1,-Math.PI/2,0,false);
	context.strokeRect(x1-drawRadius1,y1-drawRadius1,2*drawRadius1,2*drawRadius1);
	context.fillStyle = color;
	context.stroke();
	context.fill();
	context.lineWidth = 1;
	context.font = "9pt Calibri";

	context.moveTo(x1-drawRadius1,y1-drawRadius1-5);
	context.lineTo(x1-drawRadius1,y1-drawRadius1-13);
	context.moveTo(x1-drawRadius1,y1-drawRadius1-9);
	context.lineTo(x1+drawRadius1,y1-drawRadius1-9);
	context.moveTo(x1+drawRadius1,y1-drawRadius1-5);
	context.lineTo(x1+drawRadius1,y1-drawRadius1-13);
	context.strokeText(2*radius1+" "+unit,x1,y1-drawRadius1-20);
	
	context.stroke();

	context.restore();
}


function get_random_color() 
{
	var colour_code = Math.floor(Math.random()*56);
	var colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"];
	return colours[colour_code];
}