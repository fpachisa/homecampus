var canvasWidth = 500;
var canvasHeight = 300;


//global variable
var context;
var canvas;
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
	canvasWidth = 500;
	canvasHeight = 300;
	canvas = document.createElement('canvas');
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

//Problem 1 acute angle
function P3ANRightAngleQ1a(angle1,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
    //drawing first angle
    
    context.beginPath();
	x1 = 50;
	y1 = 150;
    context.moveTo(x1,y1);
	y2 = y1;
	x2 = x1 + 130;	
	context.lineTo(x2,y2);

	y3 = 20
	x3 = x2 - (y2-y3)/Math.tan(Math.PI*(angle1)/180);
	if (x3<50)
	{
		x3 = 50;
	}
	context.lineTo(x3,y3);
	//if you cut x3 at 230 the angle1 will change
	var newAngle1 = Math.atan((y2-y3)/(x2-x3));

	context.moveTo(x2,y2);
	context.arc(x2,y2,25,Math.PI,Math.PI+newAngle1,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x2-45,y2-10);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[0];
	context.stroke();	
}
//Problem 1 Right Angle
function P3ANRightAngleQ1b(angle1,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
    //drawing first angle
    
    context.beginPath();
	x1 = 50;
	y1 = 150;
    context.moveTo(x1,y1);
	y2 = y1;
	x2 = x1 + 130;	
	context.lineTo(x2,y2);

	y3 = 20
	x3 = x2;
	context.lineTo(x3,y3);
	context.moveTo(x2,y2);
	context.arc(x2,y2,25,Math.PI,Math.PI+Math.PI/2,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x2-35,y2-20);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[0];
	context.stroke();	
}
//Problem 1 obtuse angle
function P3ANRightAngleQ1c(angle1,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
    //drawing first angle
    
    context.beginPath();
	x1 = 50;
	y1 = 150;
    context.moveTo(x1,y1);
	y2 = y1;
	x2 = x1 + 130;	
	context.lineTo(x2,y2);

	y3 = 20
	x3 = x2 + (y2-y3)/Math.tan(Math.PI*(180-angle1)/180);
	if (x3>300)
	{
		x3 = 300;
	}
	context.lineTo(x3,y3);
	//if you cut x3 at 230 the angle1 will change
	var newAngle1 = Math.atan((y2-y3)/(x3-x2));

	context.moveTo(x2,y2);
	context.arc(x2,y2,25,Math.PI,-newAngle1,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x2-15,y2-30);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[0];
	context.stroke();	
}
//Problem 2
function P3ANRightAngleQ2a(angle1,angle2,angle3,angle4,angle5,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	x1 = 150;
	y1 = 90;
    context.moveTo(x1,y1);
	x2 = x1 - 130;
	y2 = y1 - (x1-x2)/(Math.tan(Math.PI*angle1/180));
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	var newAngle1 = Math.atan((x1-x2)/(y1-y2));
	context.moveTo(x1,y1);
	x3 = x2;
	y3 = y1 + (x1-x3)/(Math.tan(Math.PI*(180-angle1-angle2)/180));
	if (y3>150)
	{
		y3 = 150;
	}	
	var newAngle12 = Math.atan((x1-x3)/(y3-y1));
	context.lineTo(x3,y3);
	
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI/2+newAngle12,3*Math.PI/2-newAngle1,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x1-50,y1+7);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.closePath();	
    
    //angle 2
    context.beginPath();
	x1 = 250;
	y1 = 150;
    context.moveTo(x1,y1);
	x2 = x1 + 75;
	y2 = y1 - (x2-x1)*Math.tan(Math.PI*angle3/180);
	if (y2<20)
	{
		y2 = 20;
	}	
	context.lineTo(x2,y2);
	//if you cut y2 at 60 the angle1 will change
	var newAngle3 = Math.atan((y1-y2)/(x2-x1));
	context.moveTo(x1,y1);

	x3 = x1-75;
	y3 = y1 - (x1-x3)*Math.tan(Math.PI*(180-angle3-angle4)/180);
	if (y3<20)
	{
		y3 = 20;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle34 = Math.atan((y1-y3)/(x1-x3));
	
	context.closePath();
	//creating a square for right angle
	squareSide = 20;
	rx1 = x1 + squareSide*Math.cos(newAngle3);
	ry1 = y1 - squareSide*Math.sin(newAngle3);
	context.moveTo(rx1,ry1);
	squareDiagnol = Math.sqrt(2*squareSide*squareSide);
	rx2 = x1 + squareDiagnol*Math.cos(Math.PI/4+newAngle3);
	ry2 = y1 - squareDiagnol*Math.sin(Math.PI/4+newAngle3);
	context.lineTo(rx2,ry2);
	rx3 = x1 - squareSide*Math.cos(newAngle34);
	ry3 = y1 - squareSide*Math.sin(newAngle34);
	context.lineTo(rx3,ry3);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1-5,y1-30);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[1];
	context.stroke();

	//angle 3
    context.beginPath();
	x1 = 400;
	y1 = 40;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1
	context.lineTo(x2,y2);
	context.moveTo(x1,y1);

	y3 = y1 + 100;
	x3 = x1 - (y3-y1)/Math.tan(Math.PI*(180-angle5)/180);
	if (x1-x3>90)
	{
		x3 = x1 - 90;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle45 = Math.atan((y3-y1)/(x1-x3));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,0,Math.PI-newAngle45,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[2],x1+10,y1+40);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[2];
	context.stroke();
}
//Problem 2
function P3ANRightAngleQ2b(angle1,angle2,angle3,angle4,angle5,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	x1 = 20;
	y1 = 20;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1
	context.lineTo(x2,y2);
	context.moveTo(x1,y1);
	y3 = 150;
	x3 = x1 + (y3-y1)/(Math.tan(Math.PI*angle1/180));
	if (x3>120)
	{
		x3 = 120;
	}	
	var newAngle1 = Math.atan((y3-y1)/(x3-x1));
	context.lineTo(x3,y3);
	
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,0,newAngle1,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x1+30,y1+25);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.closePath();	
    
    //angle 2
    context.beginPath();
	x1 = 230;
	y1 = 30;
    context.moveTo(x1,y1);
	y2 = 150;
	x2 = x1 + (y3-y1)/(Math.tan(Math.PI*angle2/180));
	if (x2>330)
	{
		x2 = 330;
	}	
	var newAngle2 = Math.atan((y2-y1)/(x2-x1));
	context.lineTo(x2,y2);
	
	//angle 3
    context.moveTo(x1,y1);
	y3 = 170;
	x3 = x1 - (y3-y1)/(Math.tan(Math.PI*(180-angle2-angle3)/180));
	if (x3>130)
	{
		x3 = 130;
	}	
	var newAngle23 = Math.atan((y3-y1)/(x1-x3));
	context.lineTo(x3,y3);
	context.closePath();

	context.moveTo(x1,y1);
	context.arc(x1,y1,25,newAngle2,Math.PI-newAngle23,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1-15,y1+40);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[1];
	context.stroke();

	//angle 3
    context.beginPath();
	x1 = 470;
	y1 = 100;
    context.moveTo(x1,y1);
	y2 = 20;
    x2 = x1 - (y1-y2)*Math.tan(Math.PI*angle4/180);
    if (x2<350)
    {
    	x2 = 350;
    }
	context.lineTo(x2,y2);
	var newAngle4 = Math.atan((x1-x2)/(y1-y2));	
	
	context.moveTo(x1,y1);
	y3 = y1 + 100;
	x3 = x1 - (y3-y1)*Math.tan(Math.PI*(180-angle4-angle5)/180);
   /* if (x3<400)
    {
    	x3 = 400;
    }*/
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle45 = Math.atan((x1-x3)/(y3-y1));
	
	context.closePath();
	//creating a square for right angle
	squareSide = 20;
	rx1 = x1 - squareSide*Math.sin(newAngle4);
	ry1 = y1 - squareSide*Math.cos(newAngle4);
	context.moveTo(rx1,ry1);
	squareDiagnol = Math.sqrt(2*squareSide*squareSide);
	rx2 = x1 - squareDiagnol*Math.sin(Math.PI/4+newAngle4);
	ry2 = y1 - squareDiagnol*Math.cos(Math.PI/4+newAngle4);
	context.lineTo(rx2,ry2);
	rx3 = x1 - squareSide*Math.sin(newAngle45);
	ry3 = y1 + squareSide*Math.cos(newAngle45);
	context.lineTo(rx3,ry3);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[2],x1-45,y1);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[2];
	context.stroke();
}
//Problem 4
function P3ANRightAngleQ4a(angle1,angle2,angle3,angle4,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	x1 = 135;
	y1 = 80;
    context.moveTo(x1,y1);
	x2 = 20;
	y2 = y1 - (x1-x2)/(Math.tan(Math.PI*angle1/180));
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	var newAngle1 = Math.atan((x1-x2)/(y1-y2));

	context.moveTo(x1,y1);
	x3 = 20;
	y3 = y1 + (x1-x3)/(Math.tan(Math.PI*(180-angle1-angle2)/180));
	if (y3>180)
	{
		y3 = 180;
	}		
	context.lineTo(x3,y3);
	var newAngle12 = Math.atan((x1-x3)/(y3-y1));
	
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI/2+newAngle12,3*Math.PI/2-newAngle1,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x1-40,y1+10);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.closePath();	

	//angle 2
    context.beginPath();
	x1 = 310;
	y1 = 100;
    context.moveTo(x1,y1);
	y2 = 20;
    x2 = x1 + (y1-y2)*Math.tan(Math.PI*angle3/180);
    if (x2>450)
    {
    	x2 = 450;
    }
	context.lineTo(x2,y2);
	var newAngle3 = Math.atan((x2-x1)/(y1-y2));	
	
	context.moveTo(x1,y1);
	y3 = y1 + 100;
	x3 = x1 + (y3-y1)*Math.tan(Math.PI*(180-angle3-angle4)/180);
    if (x2>450)
    {
    	x2 = 450;
    }
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle34 = Math.atan((x3-x1)/(y3-y1));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,3*Math.PI/2+newAngle3,Math.PI/2-newAngle34,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1+40,y1);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[1];
	context.stroke();
}
//Problem 4
function P3ANRightAngleQ4b(angle1,angle2,angle3,angle4,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	x1 = 75;
	y1 = 30;
    context.moveTo(x1,y1);
	y2 = 180;
	x2 = x1 + (y2-y1)/(Math.tan(Math.PI*angle1/180));
	if (x2>140)
	{
		x2 = 140;
	}
	context.lineTo(x2,y2);
	var newAngle1 = Math.atan((y2-y1)/(x2-x1));

	context.moveTo(x1,y1);
	y3 = 180;
	x3 = x1 - (y3-y1)/(Math.tan(Math.PI*(180-angle1-angle2)/180));
	if (x3<20)
	{
		x3 = 20;
	}
	context.lineTo(x3,y3);
	var newAngle12 = Math.atan((y3-y1)/(x1-x3));
	
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,newAngle1,Math.PI-newAngle12,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x1,y1+50);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.closePath();	
    
    //angle 2
	context.beginPath();
	x1 = 225;
	y1 = 30;
    context.moveTo(x1,y1);
	x2 = 280;
    y2 = y1 + (x2-x1)*Math.tan(Math.PI*angle3/180);
	if (y2>180)
	{
		y2 = 180;
	}
	context.lineTo(x2,y2);
	var newAngle3 = Math.atan((y2-y1)/(x2-x1));

	context.moveTo(x1,y1);
	x3 = 170;
    y3 = y1 + (x1-x3)*Math.tan(Math.PI*(180-angle3-angle4)/180);
	if (y3>180)
	{
		y3 = 180;
	}
	context.lineTo(x3,y3);
	var newAngle34 = Math.atan((y3-y1)/(x1-x3));
	
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,newAngle3,Math.PI-newAngle34,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1-10,y1+40);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[1];
    context.stroke();
    context.closePath();	
}
//problem 4
function P3ANRightAngleQ4c(angle1,angle2,angle3,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	x1 = 150;
	y1 = 90;
    context.moveTo(x1,y1);
	x2 = x1 - 130;
	y2 = y1 - (x1-x2)/(Math.tan(Math.PI*angle1/180));
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	var newAngle1 = Math.atan((x1-x2)/(y1-y2));
	context.moveTo(x1,y1);
	x3 = x2;
	y3 = y1 + (x1-x3)/(Math.tan(Math.PI*(180-angle1-angle2)/180));
	if (y3>150)
	{
		y3 = 150;
	}	
	var newAngle12 = Math.atan((x1-x3)/(y3-y1));
	context.lineTo(x3,y3);
	
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI/2+newAngle12,3*Math.PI/2-newAngle1,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x1-50,y1+7);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.closePath();	

	//angle 3
    context.beginPath();
	x1 = 400;
	y1 = 40;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1
	context.lineTo(x2,y2);
	context.moveTo(x1,y1);

	y3 = y1 + 100;
	x3 = x1 - (y3-y1)/Math.tan(Math.PI*(180-angle3)/180);
	if (x1-x3>90)
	{
		x3 = x1 - 90;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle3 = Math.atan((y3-y1)/(x1-x3));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,0,Math.PI-newAngle3,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1+10,y1+40);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[1];
	context.stroke();
}
//problem 7
function P3ANRightAngleQ7a(colours,angle)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.save();
	context.translate(250,100);
	context.rotate(Math.PI*angle/180);
	context.beginPath();
	x1 = 30-200;
	y1 = 20-20;
    context.moveTo(x1,y1);
	x2 = x1;
	y2 = y1 + 100; 
	context.lineTo(x2,y2);
	x3 = x2+100;
	y3 = y2;
	context.lineTo(x3,y3);
	x4 = x3;
	y4 = y3 - 100;
	context.lineTo(x4,y4);
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.restore();
}
//problem 7
function P3ANRightAngleQ7b(colours,angle)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.save();
	context.translate(250,100);
	context.rotate(Math.PI*angle/180);
	context.beginPath();
	x1 = 30-200;
	y1 = 20-20;
    context.moveTo(x1,y1);
	x2 = x1;
	y2 = y1 + 100; 
	context.lineTo(x2,y2);
	x3 = x2+100;
	y3 = y2;
	context.lineTo(x3,y3);
	x4 = x3;
	y4 = y3 - 100;
	context.lineTo(x4,y4);
	context.closePath();
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.restore();
}
//problem 7
function P3ANRightAngleQ7c(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	context.font = '12pt Verdana';
	x1 = 30;
	y1 = 20;
    context.moveTo(x1,y1);
    context.fillText(eval(labels)[0],x1-15,y1);	
	x2 = x1;
	y2 = y1 + 100; 
	context.lineTo(x2,y2);
	context.fillText(eval(labels)[1],x2-15,y2);
	x3 = x2+100;
	y3 = y2;
	context.lineTo(x3,y3);
	context.fillText(eval(labels)[2],x3+5,y3);
	x4 = x3;
	y4 = y3 - 100;
	context.lineTo(x4,y4);
	context.fillText(eval(labels)[3],x4,y4-5);
	x5 = x4 + 100;
	y5 = y4;
	context.lineTo(x5,y5);
	context.fillText(eval(labels)[4],x5-5,y5-5);
	x6 = x5;
	y6 = y5 + 100;
	context.lineTo(x6,y6);
	context.fillText(eval(labels)[5],x6-15,y6);
	x7 = x6 + 100;
	y7 = y6;
	context.lineTo(x7,y7);
	context.fillText(eval(labels)[6],x7+5,y7);
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
}
//problem 7
function P3ANRightAngleQ7d(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	context.font = '12pt Verdana';
	x1 = 30;
	y1 = 20;
    context.moveTo(x1,y1);
    context.fillText(eval(labels)[0],x1-15,y1);	
	x2 = x1;
	y2 = y1 + 100; 
	context.lineTo(x2,y2);
	context.fillText(eval(labels)[1],x2-15,y2);
	x3 = x2+100;
	y3 = y2;
	context.lineTo(x3,y3);
	context.fillText(eval(labels)[2],x3+5,y3);
	x4 = x3;
	y4 = y3 - 100;
	context.lineTo(x4,y4);
	context.fillText(eval(labels)[3],x4,y4-5);
	x5 = x4 + 100;
	y5 = y4;
	context.lineTo(x5,y5);
	context.fillText(eval(labels)[4],x5-5,y5-5);
	x6 = x5;
	y6 = y5 + 100;
	context.lineTo(x6,y6);
	context.fillText(eval(labels)[5],x6-15,y6);
	x7 = x6 + 100;
	y7 = y6;
	context.lineTo(x7,y7);
	context.fillText(eval(labels)[6],x7+5,y7);
	x8 = x7;
	y8 = y7 + 100;
	context.lineTo(x8,y8);
	context.fillText(eval(labels)[7],x8+5,y8-20);
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
}
//problem 7
function P3ANRightAngleQ7e(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	context.font = '12pt Verdana';
	x1 = 30;
	y1 = 20;
    context.moveTo(x1,y1);
    context.fillText(eval(labels)[0],x1-15,y1);	
	x2 = x1;
	y2 = y1 + 100; 
	context.lineTo(x2,y2);
	context.fillText(eval(labels)[1],x2-15,y2);
	x3 = x2+100;
	y3 = y2;
	context.lineTo(x3,y3);
	context.fillText(eval(labels)[2],x3+5,y3);
	x4 = x3;
	y4 = y3 - 100;
	context.lineTo(x4,y4);
	context.fillText(eval(labels)[3],x4,y4-5);
	x5 = x4 + 100;
	y5 = y4;
	context.lineTo(x5,y5);
	context.fillText(eval(labels)[4],x5-5,y5-5);
	x6 = x5;
	y6 = y5 + 100;
	context.lineTo(x6,y6);
	context.fillText(eval(labels)[5],x6-15,y6);
	x7 = x6 + 100;
	y7 = y6;
	context.lineTo(x7,y7);
	context.fillText(eval(labels)[6],x7-10,y7-5);
	x8 = x7;
	y8 = y7 + 50;
	context.lineTo(x8,y8);
	context.fillText(eval(labels)[7],x8-15,y8);
	x9 = x8 + 50;
	y9 = y8;
	context.lineTo(x9,y9);
	context.fillText(eval(labels)[8],x9+5,y9);    
	context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
}
//problem 7
function P3ANRightAngleQ7f(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.beginPath();
	context.font = '12pt Verdana';
	x1 = 30;
	y1 = 20;
    context.moveTo(x1,y1);
    context.fillText(eval(labels)[0],x1-15,y1);	
	x2 = x1;
	y2 = y1 + 100; 
	context.lineTo(x2,y2);
	context.fillText(eval(labels)[1],x2-15,y2);
	x3 = x2+100;
	y3 = y2;
	context.lineTo(x3,y3);
	context.fillText(eval(labels)[2],x3+5,y3);
	x4 = x3;
	y4 = y3 - 100;
	context.lineTo(x4,y4);
	context.fillText(eval(labels)[3],x4,y4-5);
	x5 = x4 + 100;
	y5 = y4;
	context.lineTo(x5,y5);
	context.fillText(eval(labels)[4],x5-5,y5-5);
	x6 = x5;
	y6 = y5 + 100;
	context.lineTo(x6,y6);
	context.fillText(eval(labels)[5],x6-15,y6);
	x7 = x6 + 100;
	y7 = y6;
	context.lineTo(x7,y7);
	context.fillText(eval(labels)[6],x7-10,y7-5);
	x8 = x7;
	y8 = y7 + 50;
	context.lineTo(x8,y8);
	context.fillText(eval(labels)[7],x8-15,y8);
	x9 = x8 + 50;
	y9 = y8;
	context.lineTo(x9,y9);
	context.fillText(eval(labels)[8],x9+5,y9);    
	x10 = x9;
	y10 = y9 - 100;
	context.lineTo(x10,y10);
	context.fillText(eval(labels)[9],x10+5,y10);
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
}
//problem 7
function P3ANRightAngleQ7g(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.font = '12pt Verdana';
	x1 = 30;
	y1 = 20;
    context.moveTo(x1,y1);
    context.fillText(eval(labels)[0],x1-15,y1);	
	x2 = x1;
	y2 = y1 + 100; 
	context.lineTo(x2,y2);
	context.fillText(eval(labels)[1],x2-15,y2);
	x3 = x2+100;
	y3 = y2;
	context.lineTo(x3,y3);
	context.fillText(eval(labels)[2],x3+5,y3);
	x4 = x3;
	y4 = y3 - 100;
	context.lineTo(x4,y4);
	context.fillText(eval(labels)[3],x4,y4-5);
	x5 = x4 + 100;
	y5 = y4;
	context.lineTo(x5,y5);
	context.fillText(eval(labels)[4],x5-5,y5-5);
	x6 = x5;
	y6 = y5 + 100;
	context.lineTo(x6,y6);
	context.fillText(eval(labels)[5],x6-15,y6);
	x7 = x6 + 100;
	y7 = y6;
	context.lineTo(x7,y7);
	context.fillText(eval(labels)[6],x7-10,y7-5);
	x8 = x7;
	y8 = y7 + 50;
	context.lineTo(x8,y8);
	context.fillText(eval(labels)[7],x8-15,y8);
	x9 = x8 + 50;
	y9 = y8;
	context.lineTo(x9,y9);
	context.fillText(eval(labels)[8],x9+5,y9);    
	x10 = x9;
	y10 = y9 - 100;
	context.lineTo(x10,y10);
	context.fillText(eval(labels)[9],x10,y10-5);
 	x11 = x10 + 50;
	y11 = y10;
	context.lineTo(x11,y11);
	context.fillText(eval(labels)[10],x11,y11-5);
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
}
//problem 8
function P3ANRightAngleQ8a(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.font = '12pt Verdana';
	//point one
	x1 = 30;
	y1 = 20;
	context.moveTo(x1,y1);
    context.arc(x1,y1,5,0,2*Math.PI,false);
    context.fillStyle = eval(colours)[0];
    context.fill(); 
	// point 2
    context.beginPath();
    x2 = 30;
	y2 = 100;
	context.moveTo(x2,y2);
    context.arc(x2,y2,5,0,2*Math.PI,false);
    //context.fillStyle = eval(colours)[1];
    context.fill();
	// point 2
    context.beginPath();
    x3 = 130;
	y3 = 100;
	context.moveTo(x3,y3);
    context.arc(x3,y3,5,0,2*Math.PI,false);
    //context.fillStyle = eval(colours)[2];
    context.fill();
	
    context.beginPath();
    context.fillStyle = "black";
    context.fillText(eval(labels)[0],x1,y1-8);
    context.fillText(eval(labels)[1],x2,y2+20);	
    context.fillText(eval(labels)[2],x3,y3+20);    
    context.fill();
}
//problem 8
function P3ANRightAngleQ8b(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.font = '12pt Verdana';
	//point one
	x1 = 30;
	y1 = 20;
	context.moveTo(x1,y1);
    context.arc(x1,y1,5,0,2*Math.PI,false);
    context.fillStyle = eval(colours)[0];
    context.fill(); 
	// point 2
    context.beginPath();
    x2 = 130;
	y2 = 20;
	context.moveTo(x2,y2);
    context.arc(x2,y2,5,0,2*Math.PI,false);
    //context.fillStyle = eval(colours)[1];
    context.fill();
	// point 2
    context.beginPath();
    x3 = 130;
	y3 = 100;
	context.moveTo(x3,y3);
    context.arc(x3,y3,5,0,2*Math.PI,false);
    //context.fillStyle = eval(colours)[2];
    context.fill();
	
    context.beginPath();
    context.fillStyle = "black";
    context.fillText(eval(labels)[0],x1,y1-8);
    context.fillText(eval(labels)[1],x2,y2-8);	
    context.fillText(eval(labels)[2],x3,y3+20);    
    context.fill();
}
//problem 8
function P3ANRightAngleQ8c(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.font = '12pt Verdana';
	//point one
	x1 = 130;
	y1 = 20;
	context.moveTo(x1,y1);
    context.arc(x1,y1,5,0,2*Math.PI,false);
    context.fillStyle = eval(colours)[0];
    context.fill(); 
	// point 2
    context.beginPath();
    x2 = 20;
	y2 = 100;
	context.moveTo(x2,y2);
    context.arc(x2,y2,5,0,2*Math.PI,false);
    //context.fillStyle = eval(colours)[1];
    context.fill();
	// point 2
    context.beginPath();
    x3 = 130;
	y3 = 100;
	context.moveTo(x3,y3);
    context.arc(x3,y3,5,0,2*Math.PI,false);
    //context.fillStyle = eval(colours)[2];
    context.fill();
	
    context.beginPath();
    context.fillStyle = "black";
    context.fillText(eval(labels)[0],x1,y1-8);
    context.fillText(eval(labels)[1],x2,y2+20);	
    context.fillText(eval(labels)[2],x3,y3+20);    
    context.fill();
}
//problem 8
function P3ANRightAngleQ8d(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.font = '12pt Verdana';
	//point one
	x1 = 20;
	y1 = 20;
	context.moveTo(x1,y1);
    context.arc(x1,y1,5,0,2*Math.PI,false);
    context.fillStyle = eval(colours)[0];
    context.fill(); 
	// point 2
    context.beginPath();
    x2 = 130;
	y2 = 20;
	context.moveTo(x2,y2);
    context.arc(x2,y2,5,0,2*Math.PI,false);
    //context.fillStyle = eval(colours)[1];
    context.fill();
	// point 2
    context.beginPath();
    x3 = 20;
	y3 = 100;
	context.moveTo(x3,y3);
    context.arc(x3,y3,5,0,2*Math.PI,false);
    //context.fillStyle = eval(colours)[2];
    context.fill();
	
    context.beginPath();
    context.fillStyle = "black";
    context.fillText(eval(labels)[0],x1,y1-8);
    context.fillText(eval(labels)[1],x2,y2-8);	
    context.fillText(eval(labels)[2],x3,y3+20);    
    context.fill();
}
//problem 9
function P3ANRightAngleQ9a(angle1,angle2,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.font = '12pt Verdana';
	//angle 1
	x1 = 200;
	y1 = 180;
	context.moveTo(x1,y1);
	x2 = 20;
	y2 = y1 - (x1-x2)*Math.tan(Math.PI*angle1/180);
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	newAngle1 = Math.atan((y1-y2)/(x1-x2));
	// angle 2
	context.moveTo(x1,y1);
	x3 = 380;
	y3 = y1 - (x3-x1)*Math.tan(Math.PI*(180-angle2)/180-newAngle1);
	if (y3<20)
	{
		y3 = 20;
	}
	context.lineTo(x3,y3);
	context.lineTo(x2,y2);
	context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.beginPath();
	context.fillText(eval(labels)[0],x1,y1+20);
    context.fillText(eval(labels)[1],x2,y2-8);	
    context.fillText(eval(labels)[2],x3,y3-8);
    context.fillStyle = "black";
    context.fill();

}
//problem 9
function P3ANRightAngleQ9b(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.font = '12pt Verdana';
	context.rect(30,30,300,150);
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.beginPath();
	context.fillText(eval(labels)[0],30,22);
    context.fillText(eval(labels)[1],330,22);	
    context.fillText(eval(labels)[2],30,200);
    context.fillText(eval(labels)[3],330,200);
    context.fillStyle = "black";
    context.fill();
}
//problem 9
function P3ANRightAngleQ9c(colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	context.font = '12pt Verdana';
	x1 = 30;
	y1 = 30;
	context.moveTo(x1,y1);
	x2 = 30;
	y2 = 150;
	context.lineTo(x2,y2);
	context.moveTo(x1,y1);
	x3 = 300;
	y3 = 30;
	context.lineTo(x3,y3);
	x4 = x3;
	y4 = y3 + 30 + Math.random()*(70);
	context.lineTo(x4,y4);
	context.lineTo(x2,y2);
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.beginPath();
	context.fillText(eval(labels)[0],x1,y1-8);
    context.fillText(eval(labels)[1],x2,y2+20);	
    context.fillText(eval(labels)[2],x3,y3-8);
    context.fillText(eval(labels)[3],x4,y4+20);
    context.fillStyle = "black";
    context.fill();
}