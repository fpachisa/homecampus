var canvasWidth = 300;
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

function DrawRandomTriangles(angle1,angle2)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (0 + Math.random()*(30-0))*(Math.PI/180);
	if (angle1>90)
	{
		rotateAngle = (-15 + Math.random()*(15-(-15)))*(Math.PI/180);
	}
	
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;

	context.strokeStyle="black";
	context.lineWidth = 2;
	context.beginPath();
	context.arc(x1-75,y1+50,15,0,2*Math.PI-Math.PI*angle1/180,true);
	context.stroke();
	context.beginPath();
	context.arc(x1-75+100/Math.tan(Math.PI*angle1/180),y1-50,15,Math.PI*angle2/180,Math.PI-Math.PI*angle1/180,false);
	context.stroke();
	context.beginPath();
	context.arc(x1+75,y1+50,15,Math.PI,Math.PI+Math.PI*angle2/180,false);
	
	context.moveTo(x1-75,y1+50);
	context.lineTo(x1-75+100/Math.tan(Math.PI*angle1/180),y1-50);
	context.lineTo(x1+75,y1+50);
	context.closePath();	
	context.stroke();
	context.beginPath();
	context.strokeStyle="green";
	context.font = "9pt Calibri";
	context.lineWidth = 1;
	context.strokeText("A",x1-90,y1+50);
	context.strokeText("B",x1-75+100/Math.tan(Math.PI*angle1/180),y1-60);
	context.strokeText("C",x1+80,y1+50);
	if (angle1 >=60 && angle1 < 90)
	{
		context.strokeText("x",x1-75+100/Math.tan(Math.PI*angle1/180),y1-20);
	}
	else if (angle1 < 60)
	{
		context.strokeText("x",x1-75+100/Math.tan(Math.PI*angle1/180)-10,y1-20);
	}
	else
	{
		context.strokeText("x",x1-75+100/Math.tan(Math.PI*angle1/180)+15,y1-25);
	}
	context.stroke();
	context.restore();
}

function DrawRightAngleTriangle(height,base,angle1,angle2)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-20 + Math.random()*(20-(-20)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;

	context.strokeStyle="black";
	context.lineWidth = 2;
	context.beginPath();
	context.strokeRect(x1-75,y1+60,15,15);
	context.stroke();
	context.beginPath();
	context.arc(x1-75+base,y1+75,15,Math.PI,Math.PI+Math.PI*angle2/180,false);
	context.stroke();
	context.beginPath();
	context.arc(x1-75,y1+75-height,15,Math.PI*angle2/180,Math.PI*angle2/180+Math.PI*(90-angle2)/180,false);
	
	context.moveTo(x1-75+base,y1+75);
	context.lineTo(x1-75,y1+75);
	context.lineTo(x1-75,y1+75-height);
	context.closePath();	
	context.stroke();
	context.beginPath();
	context.strokeStyle="green";
	context.font = "9pt Calibri";
	context.lineWidth = 1;
	context.strokeText("A",x1-90,y1+75);
	context.strokeText("B",x1-75,y1+75-height-10);
	context.strokeText("C",x1-75+base+10,y1+75);
	context.strokeText("x",x1-65,y1+75-height+30);
	context.stroke();
	context.restore();
}

function DrawParallelogram(angle1,type)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-20 + Math.random()*(20-(-20)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = -100;
	y1 = 40;
	var base = 75 + Math.random()*(100-75);
	var height = 50 + Math.random()*(75-50);
	
	context.strokeStyle="black";
	context.lineWidth = 2;
	context.beginPath();
	context.arc(x1,y1,15,0,2*Math.PI-Math.PI*angle1/180,true);
	context.stroke();
	context.beginPath();
	if (type==1)
	{
		context.arc(x1+height/Math.tan(angle1*Math.PI/180),y1-height,15,0,Math.PI*(180-angle1)/180,false);
	}
	else if (type==2)
	{
		context.arc(x1+height/Math.tan(angle1*Math.PI/180)+base,y1-height,15,Math.PI,Math.PI-Math.PI*(angle1)/180,true);
	}
	else
	{
		context.arc(x1+height/Math.tan(angle1*Math.PI/180)+base-height*Math.tan((90-angle1)*Math.PI/180),y1,15,Math.PI,Math.PI+Math.PI*(180-angle1)/180,false);
	}
	context.moveTo(x1,y1);
	context.lineTo(x1+height/Math.tan(angle1*Math.PI/180),y1-height);
	context.lineTo(x1+height/Math.tan(angle1*Math.PI/180)+base,y1-height);
	context.lineTo(x1+height/Math.tan(angle1*Math.PI/180)+base-height*Math.tan((90-angle1)*Math.PI/180),y1)
	context.closePath();	
	context.stroke();
	context.beginPath();
	context.strokeStyle="green";
	context.font = "9pt Calibri";
	context.lineWidth = 1;
	context.strokeText("A",x1+height/Math.tan(angle1*Math.PI/180)-10,y1-height-10);
	context.strokeText("B",x1-10,y1+10);
	context.strokeText("C",x1+height/Math.tan(angle1*Math.PI/180)+base-height*Math.tan((90-angle1)*Math.PI/180),y1+10);
	context.strokeText("D",x1+height/Math.tan(angle1*Math.PI/180)+base,y1-height-10);
	if (type==1)
	{
		context.strokeText("x",x1+height/Math.tan(angle1*Math.PI/180)+10,y1-height+25);
	}
	else if (type==2)
	{
		context.strokeText("x",x1+height/Math.tan(angle1*Math.PI/180)+base-30,y1-height+15);
	}
	else
	{
		context.strokeText("x",x1+height/Math.tan(angle1*Math.PI/180)+base-height*Math.tan((90-angle1)*Math.PI/180)-10,y1-20);
	}
	context.stroke();
	context.restore();
}

function DrawRhombus(angle1,type)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	if (Math.random()>0.5)
	{
		var rotateAngle = (30 + Math.random()*(45-30))*(Math.PI/180);
	}
	else
	{
		var rotateAngle = (-30 + Math.random()*(-45-(-30)))*(Math.PI/180);
	}
	rotateAngle = 30*Math.PI/180;
	context.rotate(rotateAngle);
	x1 = -100;
	y1 = 40;
	var base = 50 + Math.random()*(75-50);
	var height = base * Math.sin(Math.PI*angle1/180);
	
	context.strokeStyle="black";
	context.lineWidth = 2;
	context.beginPath();
	context.arc(x1,y1,15,0,2*Math.PI-Math.PI*angle1/180,true);
	context.stroke();
	context.beginPath();
	if (type==1)
	{
		context.arc(x1+height/Math.tan(angle1*Math.PI/180),y1-height,10,0,Math.PI*(180-angle1)/180,false);
	}
	else if (type==2)
	{
		context.arc(x1+height/Math.tan(angle1*Math.PI/180)+base,y1-height,10,Math.PI,Math.PI-Math.PI*(angle1)/180,true);
	}
	else
	{
		context.arc(x1+height/Math.tan(angle1*Math.PI/180)+base-height*Math.tan((90-angle1)*Math.PI/180),y1,10,Math.PI,Math.PI+Math.PI*(180-angle1)/180,false);
	}
	context.moveTo(x1,y1);
	context.lineTo(x1+height/Math.tan(angle1*Math.PI/180),y1-height);
	context.lineTo(x1+height/Math.tan(angle1*Math.PI/180)+base,y1-height);
	context.lineTo(x1+height/Math.tan(angle1*Math.PI/180)+base-height*Math.tan((90-angle1)*Math.PI/180),y1)
	context.closePath();	
	context.stroke();
	context.beginPath();
	context.strokeStyle="green";
	context.font = "9pt Calibri";
	context.lineWidth = 1;
	context.strokeText("A",x1+height/Math.tan(angle1*Math.PI/180)-10,y1-height-10);
	context.strokeText("B",x1-10,y1+10);
	context.strokeText("C",x1+height/Math.tan(angle1*Math.PI/180)+base-height*Math.tan((90-angle1)*Math.PI/180),y1+10);
	context.strokeText("D",x1+height/Math.tan(angle1*Math.PI/180)+base,y1-height-10);
	if (type==1)
	{
		context.strokeText("x",x1+height/Math.tan(angle1*Math.PI/180)+10,y1-height+25);
	}
	else if (type==2)
	{
		context.strokeText("x",x1+height/Math.tan(angle1*Math.PI/180)+base-30,y1-height+15);
	}
	else
	{
		context.strokeText("x",x1+height/Math.tan(angle1*Math.PI/180)+base-height*Math.tan((90-angle1)*Math.PI/180)-10,y1-20);
	}
	context.stroke();
	context.restore();
}

function DrawTrapezium(angle1)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = (-20 + Math.random()*(20-(-20)))*(Math.PI/180);
	context.rotate(rotateAngle);
	x1 = -100;
	y1 = 40;
	
	var base = 75 + Math.random()*(120-75);
	var base1 = (0.4 + Math.random()*(0.6-0.4)) * base;
	var height = 50 + Math.random()*(75-50);

	context.strokeStyle="black";
	context.lineWidth = 2;
	context.beginPath();
	context.arc(x1,y1,15,0,2*Math.PI-Math.PI*angle1/180,true);
	context.stroke();
	context.beginPath();
	context.arc(x1+height/Math.tan(angle1*Math.PI/180),y1-height,10,0,Math.PI*(180-angle1)/180,false);
	
	context.moveTo(x1,y1);
	context.lineTo(x1+height/Math.tan(angle1*Math.PI/180),y1-height);
	context.lineTo(x1+height/Math.tan(angle1*Math.PI/180)+base1,y1-height);
	context.lineTo(x1+base,y1)
	context.closePath();	
	context.stroke();
	context.beginPath();
	context.strokeStyle="green";
	context.font = "9pt Calibri";
	context.lineWidth = 1;
	context.strokeText("A",x1+height/Math.tan(angle1*Math.PI/180)-10,y1-height-5);
	context.strokeText("B",x1-10,y1+10);
	context.strokeText("C",x1+base+5,y1+10);
	context.strokeText("D",x1+height/Math.tan(angle1*Math.PI/180)+base1+5,y1-height-5);
	context.strokeText("x",x1+height/Math.tan(angle1*Math.PI/180)+10,y1-height+25);
	context.stroke();
	context.restore();
}

function get_random_color_draw_shapes() 
{
	var colour_code = Math.floor(Math.random()*56);
	var colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"];
	return colours[colour_code];
}