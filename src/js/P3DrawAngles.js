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

function P3ANDrawAngleQ1a(angle1)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	var r1 = 250;
	var r2 = 50;
	context.save();
	context.translate(r1,r2);
	var rotateAngle = (60 + Math.random()*100)*(Math.PI/180);
	context.rotate(rotateAngle);
	
	var x1 = 0;
	var y1 = 0;
	context.beginPath();
	//base line
	context.moveTo(x1,y1);
	x2 = x1 + 200;
	context.lineTo(x2,y1);
	//first line
	context.moveTo(x1,y1);

	var angle1 = angle1
	x3 = x2;
	y3 = (x2-x1)*Math.tan(Math.PI*angle1/180);
	context.lineTo(x3,y3);
	context.closePath();
	context.strokeStyle="black";
	context.stroke();
	context.restore();
}
function P3ANDrawAngleQ1b(angle1)
{
	WindowReady();
	canvas.setAttribute("height", 200);
	var x1 = 0;
	var y1 = 100;
	var x2 = 0;
	var y2 = 0;
	context.beginPath();
	//base line
	context.moveTo(x1,y1);
	x2 = 150;
	context.lineTo(x2,y1);
	//common point
	var cp1 = x2-80;
	var cp2 = y1+80;

	//first line
	context.moveTo(cp1,cp2);
	var angle1 = angle1
	y2 = 0;
	x2 = cp1+(y1-y2)/Math.tan(Math.PI*angle1/180);
	context.lineTo(x2,y2);
		
	context.strokeStyle="black";
	context.stroke();
}

function P3ANDrawLinesQ1()
{
	WindowReady();
	canvas.setAttribute("height", 200);
	var r1 = 250;
	var r2 = 50;
	context.save();
	context.translate(r1,r2);
	var rotateAngle = (60 + Math.random()*100)*(Math.PI/180);
	context.rotate(rotateAngle);
	
	var x1 = 0;
	var y1 = 0;
	context.beginPath();
	//base line
	context.moveTo(x1,y1);
	x2 = x1 + 200;
	y2 = y1;
	context.lineTo(x2,y2);
	//first line
	x3 = x1 + (-30 + Math.random()*60);
	y3 = y1 + (30 + Math.random()*30);
	
	x4 = x2 + (-30 + Math.random()*60);
	y4 = y2 + (30 + Math.random()*30);
	context.moveTo(x3,y3);
	context.lineTo(x4,y4);
	context.strokeStyle="black";
	context.stroke();
	context.restore();
}
//Problem 2
function P3ANDrawAngleQ2(angle1,colours)
{
	WindowReady();
	canvas.setAttribute("height", 220);
	var x1 = 20;
	var y1 = 20;
	context.beginPath();
	context.rect(10, 10, 388, 208);
	context.moveTo(190,10);
	context.lineTo(190,218);
    context.lineWidth = 2;
    context.strokeStyle = 'black';
    context.stroke();
    context.closePath();
    
    context.beginPath();
	//base line
	context.moveTo(x1,y1);
	x2 = x1 + 150;
	y2 = y1;
	context.lineTo(x2,y2);
	//first line
	context.moveTo(x1,y1);

	var angle1 = angle1;
	x3 = x2;
	y3 = (x2-x1)*Math.tan(Math.PI*angle1/180);
	if (y3>200)
	{
		y3 = 200;
	}
	context.lineTo(x3,y3);
	context.closePath();
	context.lineWidth = 4;
	context.strokeStyle=eval(colours)[0];
	context.stroke();
	
	context.beginPath();
	//base line
	x1 = 220;
	y1 = 50;
	context.moveTo(x1,y1);
	x2 = x1 + 150;
	y2 = y1;
	context.lineTo(x2,y2);
	//first line
	x3 = x1 + (-30 + Math.random()*60);
	y3 = y1 + (30 + Math.random()*30);
	
	x4 = x2 + (-30 + Math.random()*60);
	y4 = y2 + (30 + Math.random()*30);
	context.moveTo(x3,y3);
	context.lineTo(x4,y4);
	context.closePath();
	context.lineWidth = 4;
	context.strokeStyle=eval(colours)[1];
	context.stroke();
}
//Problem 3
function P3ANDrawAngleQ3a(angle1,angle2,angle3,colours)
{
	WindowReady();
	context.beginPath();
	//drawing a rectangle and cutting it into half
	context.rect(10, 10, 488, 288);
	context.moveTo(249,10);
	context.lineTo(249,298);
    context.lineWidth = 2;
    context.strokeStyle = 'black';
    context.stroke();
    context.closePath();
    
    //drawing first angle
    
    context.beginPath();
	x1 = 20;
	y1 = 200;
    context.moveTo(x1,y1);
	x2 = x1 + 150;
	y2 = y1;
	context.lineTo(x2,y2);
	context.moveTo(x1,y1);

	var angle1 = angle1;
	x3 = x2;
	y3 = y1 - (x2-x1)*Math.tan(Math.PI*angle1/180);
	if (y3<20)
	{
		y3 = 20;
	}
	context.lineTo(x3,y3);
	context.closePath();
	newAngle1 = Math.atan((y1-y3)/(x3-x1));
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,0,-newAngle1,true);

	context.strokeStyle=eval(colours)[0];
	context.stroke();
	
    //drawing second angle
    
    context.beginPath();
	x1 = 350;
	y1 = 150;
    context.moveTo(x1,y1);
	var angle2 = angle2;
    x2 = x1 + 100;
	y2 = y1 - (x2-x1)*Math.tan(Math.PI*angle2/180);;
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	newAngle2 = Math.atan((y1-y2)/(x2-x1));
	context.moveTo(x1,y1);

	var angle3 = angle3;
	x3 = x1 - 80;
	y3 = y1 - (x1-x3)*Math.tan(Math.PI*(180-angle3-angle2)/180);
	if (y3<20)
	{
		y3 = 20;
	}
	context.lineTo(x3,y3);
	context.closePath();
	newAngle23 = Math.atan((y1-y3)/(x1-x3));
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI+newAngle23,-newAngle2,false);
	context.strokeStyle=eval(colours)[1];
	context.stroke();	
}
//Problem 3
function P3ANDrawAngleQ3b(angle1,angle2,angle3,angle4,colours)
{
	WindowReady();
	context.beginPath();
	//drawing a rectangle and cutting it into half
	context.rect(10, 10, 488, 288);
	context.moveTo(249,10);
	context.lineTo(249,298);
    context.lineWidth = 2;
    context.strokeStyle = 'black';
    context.stroke();
    context.closePath();
    
    //drawing first angle
    
    context.beginPath();
	x1 = 120;
	y1 = 60;
	context.moveTo(x1,y1);
	x2 = 20;
	y2 =  y1 + (x1-x2)*Math.tan(Math.PI*angle2/180);;
	if (y2>250)
	{
		y2 = 250;
	}
	context.lineTo(x2,y2);
	newAngle2 = Math.atan((y2-y1)/(x1-x2));
	context.moveTo(x1,y1);

	x3 = x1+100;
	y3 = y1 + (x3-x1)*Math.tan(Math.PI*(180-angle3-angle2)/180);
	if (y3>250)
	{
		y3 = 250;
	}
	context.lineTo(x3,y3);
	context.closePath();
	newAngle23 = Math.atan((y3-y1)/(x3-x1));
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,newAngle23,Math.PI-newAngle2,false);
	context.strokeStyle=eval(colours)[0];
	context.stroke();
	
    //drawing second angle
    
    context.beginPath();
	x1 = 350;
	y1 = 150;
    context.moveTo(x1,y1);
    x2 = x1 + 100;
	y2 = y1 - (x2-x1)*Math.tan(Math.PI*angle1/180);
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	newAngle2 = Math.atan((y1-y2)/(x2-x1));
	context.moveTo(x1,y1);

	x3 = x1 - 100;
	y3 = y1 - (x1-x3)*Math.tan(Math.PI*(180-angle1-angle4)/180);
	if (y3<20)
	{
		y3 = 20;
	}
	context.lineTo(x3,y3);
	context.closePath();
	newAngle12 = Math.atan((y1-y3)/(x1-x3));
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,-newAngle2,Math.PI+newAngle12,true);
	context.strokeStyle=eval(colours)[1];
	context.stroke();	
}
//Problem 4
function P3ANDrawAngleQ4a(angle1,angle2,angle3,angle4,colours,labels)
{
	WindowReady();
	context.beginPath();
	//drawing a rectangle and cutting it into half
	context.rect(10, 10, 488, 288);
	context.moveTo(249,10);
	context.lineTo(249,298);
    context.lineWidth = 2;
    context.strokeStyle = 'black';
    context.stroke();
    context.closePath();
    
    //drawing first angle
    
    context.beginPath();
	x1 = 20;
	y1 = 170;
    context.moveTo(x1,y1);
	y2 = y1 + 70;
	x2 = x1 + (y2-y1)*Math.tan(Math.PI*angle1/180);
	if (x2>230)
	{
		x2 = 230;
	}	
	context.lineTo(x2,y2);
	//if you cut x2 at 230 the angle1 will change
	var newAngle1 = Math.atan((x2-x1)/(y2-y1));
	context.moveTo(x1,y1);

	y3 = 20
	x3 = x1 + (y1-y3)*Math.tan(Math.PI*(180-angle1-angle2)/180);
	if (x3>230)
	{
		x3 = 230;
	}
	context.lineTo(x3,y3);
	//if you cut x3 at 230 the angle1 will change
	var newAngle12 = Math.atan((x3-x1)/(y1-y3));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI/2-newAngle1,3*Math.PI/2+newAngle12,true);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x1+35,y1);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[0];
	context.stroke();
	
    //drawing second angle
    
    context.beginPath();
	x1 = 350;
	y1 = 150;
    context.moveTo(x1,y1);
    x2 = x1 + 100;
	y2 = y1 - (x2-x1)*Math.tan(Math.PI*angle3/180);;
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	context.moveTo(x1,y1);
	//if you cut y2 at 20 the angle3 will change
	var newAngle3 = Math.atan((y1-y2)/(x2-x1));
	context.moveTo(x1,y1);
	
	x3 = x1 - 80;
	y3 = y1 + (x3-x1)*Math.tan(Math.PI*(180-angle4-angle3)/180);
	if (y3<20)
	{
		y3 = 20;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 20 the angle34 will change
	var newAngle34 = Math.atan((y1-y3)/(x1-x3));	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,-newAngle3,Math.PI+newAngle34,true);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1,y1-35);	
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[1];
	context.stroke();	
}
//Problem 4
function P3ANDrawAngleQ4b(angle1,angle2,angle3,angle4,colours,labels)
{
	WindowReady();
	context.beginPath();
	//drawing a rectangle and cutting it into half
	context.rect(10, 10, 488, 288);
	context.moveTo(249,10);
	context.lineTo(249,298);
    context.lineWidth = 2;
    context.strokeStyle = 'black';
    context.stroke();
    context.closePath();
    
    //drawing first angle
    
    context.beginPath();
	x1 = 120;
	y1 = 120;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1 + (x2-x1)*Math.tan(Math.PI*angle1/180);
	if (y2-y1>60)
	{
		y2 = y1 + 60;
	}	
	context.lineTo(x2,y2);
	//if you cut y2 at 60 the angle1 will change
	var newAngle1 = Math.atan((y2-y1)/(x2-x1));
	context.moveTo(x1,y1);

	x3 = 20
	y3 = y1 + (x1-x3)*Math.tan(Math.PI*(180-angle1-angle2)/180);
	if (y3-y1>60)
	{
		y3 = y1 + 60;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle12 = Math.atan((y3-y1)/(x1-x3));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,newAngle1,Math.PI-newAngle12,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x1,y1+45);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[0];
	context.stroke();
	
    //drawing second angle
    
    context.beginPath();
	x1 = 350;
	y1 = 150;
    context.moveTo(x1,y1);
    x2 = x1 + 100;
	y2 = y1 - (x2-x1)*Math.tan(Math.PI*angle3/180);;
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	context.moveTo(x1,y1);
	//if you cut y2 at 20 the angle3 will change
	var newAngle3 = Math.atan((y1-y2)/(x2-x1));
	context.moveTo(x1,y1);
	
	x3 = x1 - 80;
	y3 = y1 + (x3-x1)*Math.tan(Math.PI*(180-angle4-angle3)/180);
	if (y3<20)
	{
		y3 = 20;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 20 the angle34 will change
	var newAngle34 = Math.atan((y1-y3)/(x1-x3));	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,-newAngle3,Math.PI+newAngle34,true);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1,y1-35);	
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[1];
	context.stroke();	
}

//Problem 5
function P3ANDrawAngleQ5a(angle1,angle2,angle3,angle4,angle5,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 500);
	context.beginPath();
	x1 = 100;
	y1 = 150;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1;	
	context.lineTo(x2,y2);
	y3 = 20;
	x3 = x2 - (y2-y3)/(Math.tan(Math.PI*angle1/180));
    context.moveTo(x2,y2);
	context.lineTo(x3,y3);
	
	context.moveTo(x2,y2);
	context.arc(x2,y2,25,Math.PI,Math.PI+(Math.PI*angle1/180),false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x2-35,y2-20);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.closePath();	
	
	context.beginPath();
	//drawing a rectangle and cutting it into half
	context.rect(10, 200, 488, 288);
	context.moveTo(249,200);
	context.lineTo(249,488);
    context.lineWidth = 2;
    context.strokeStyle = 'black';
    context.stroke();
    context.closePath();
    
    //angle 1
    context.beginPath();
	x1 = 120;
	y1 = 320;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1 + (x2-x1)*Math.tan(Math.PI*angle2/180);
	if (y2-y1>60)
	{
		y2 = y1 + 60;
	}	
	context.lineTo(x2,y2);
	//if you cut y2 at 60 the angle1 will change
	var newAngle1 = Math.atan((y2-y1)/(x2-x1));
	context.moveTo(x1,y1);

	x3 = 20
	y3 = y1 + (x1-x3)*Math.tan(Math.PI*(180-angle2-angle3)/180);
	if (y3-y1>60)
	{
		y3 = y1 + 60;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle23 = Math.atan((y3-y1)/(x1-x3));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,newAngle1,Math.PI-newAngle23,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1,y1+45);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[1];
	context.stroke();

	//angle 2
    context.beginPath();
	x1 = 370;
	y1 = 380;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1 - (x2-x1)*Math.tan(Math.PI*angle4/180);
	if (y2<220)
	{
		y2 = 220;
	}	
	context.lineTo(x2,y2);
	//if you cut y2 at 60 the angle1 will change
	var newAngle4 = Math.atan((y1-y2)/(x2-x1));
	context.moveTo(x1,y1);

	x3 = x1-100;
	y3 = y1 - (x1-x3)*Math.tan(Math.PI*(180-angle4-angle5)/180);
	if (y3<220)
	{
		y3 = 220;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle45 = Math.atan((y1-y3)/(x1-x3));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI+newAngle45,-newAngle4,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[2],x1-5,y1-35);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[2];
	context.stroke();
    
}
//Problem 5
function P3ANDrawAngleQ5b(angle1,angle2,angle3,angle4,angle5,colours,labels)
{
	WindowReady();
	canvas.setAttribute("height", 500);
	context.beginPath();
	x1 = 300;
	y1 = 150;
    context.moveTo(x1,y1);
	x2 = x1 - 100;
	y2 = y1;	
	context.lineTo(x2,y2);
	y3 = 20;
	x3 = x2 + (y2-y3)/(Math.tan(Math.PI*angle1/180));
    context.moveTo(x2,y2);
	context.lineTo(x3,y3);
	
	context.moveTo(x2,y2);
	context.arc(x2,y2,25,0,-(Math.PI*angle1/180),true);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[0],x2+30,y2-10);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[0];
    context.stroke();
    context.closePath();	
	
	context.beginPath();
	//drawing a rectangle and cutting it into half
	context.rect(10, 200, 488, 288);
	context.moveTo(249,200);
	context.lineTo(249,488);
    context.lineWidth = 2;
    context.strokeStyle = 'black';
    context.stroke();
    context.closePath();
    
    //angle 1
    context.beginPath();
	x1 = 120;
	y1 = 280;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1 + (x2-x1)*Math.tan(Math.PI*angle2/180);
	if (y2-y1>120)
	{
		y2 = y1 + 120;
	}	
	context.lineTo(x2,y2);
	//if you cut y2 at 60 the angle1 will change
	var newAngle1 = Math.atan((y2-y1)/(x2-x1));
	context.moveTo(x1,y1);

	x3 = x1-100;
	y3 = y1 + (x1-x3)*Math.tan(Math.PI*(180-angle2-angle3)/180);
	if (y3-y1>120)
	{
		y3 = y1 + 120;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle23 = Math.atan((y3-y1)/(x1-x3));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,newAngle1,Math.PI-newAngle23,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1,y1+45);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[1];
	context.stroke();

	//angle 2
    context.beginPath();
	x1 = 370;
	y1 = 380;
    context.moveTo(x1,y1);
	x2 = x1 + 100;
	y2 = y1 - (x2-x1)*Math.tan(Math.PI*angle4/180);
	if (y2<220)
	{
		y2 = 220;
	}	
	context.lineTo(x2,y2);
	//if you cut y2 at 60 the angle1 will change
	var newAngle4 = Math.atan((y1-y2)/(x2-x1));
	context.moveTo(x1,y1);

	x3 = x1-100;
	y3 = y1 - (x1-x3)*Math.tan(Math.PI*(180-angle4-angle5)/180);
	if (y3<220)
	{
		y3 = 220;
	}
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle45 = Math.atan((y1-y3)/(x1-x3));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI+newAngle45,-newAngle4,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[2],x1-5,y1-35);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[2];
	context.stroke();
    
}
//Problem 6
function P3ANDrawAngleQ6a(angle1,angle2,angle3,angle4,angle5,colours,labels)
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
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI+newAngle34,-newAngle3,false);
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
//Problem 6
function P3ANDrawAngleQ6b(angle1,angle2,angle3,angle4,angle5,colours,labels)
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
	context.fillText(eval(labels)[0],x1+20,y1+40);		
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
    if (x2<350)
    {
    	x2 = 350;
    }
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle45 = Math.atan((x1-x3)/(y3-y1));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI/2+newAngle45,3*Math.PI/2-newAngle4,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[2],x1-40,y1);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[2];
	context.stroke();
}
//Problem 7
function P3ANDrawAngleQ7a(angle1,angle2,angle3,angle4,angle5,angle6,colours,labels)
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
	x1 = 280;
	y1 = 80;
    context.moveTo(x1,y1);
	x2 = 170;
	y2 = y1 - (x1-x2)/(Math.tan(Math.PI*angle3/180));
	if (y2<20)
	{
		y2 = 20;
	}
	context.lineTo(x2,y2);
	var newAngle3 = Math.atan((x1-x2)/(y1-y2));

	context.moveTo(x1,y1);
	x3 = 170;
	y3 = y1 + (x1-x3)/(Math.tan(Math.PI*(180-angle3-angle4)/180));
	if (y3>180)
	{
		y3 = 180;
	}		
	context.lineTo(x3,y3);
	var newAngle34 = Math.atan((x1-x3)/(y3-y1));
	
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,Math.PI/2+newAngle34,3*Math.PI/2-newAngle3,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[1],x1-50,y1+5);		
    context.lineWidth = 2;
    context.strokeStyle = eval(colours)[1];
    context.stroke();
    context.closePath();	

	//angle 3
    context.beginPath();
	x1 = 310;
	y1 = 100;
    context.moveTo(x1,y1);
	y2 = 20;
    x2 = x1 + (y1-y2)*Math.tan(Math.PI*angle5/180);
    if (x2>450)
    {
    	x2 = 450;
    }
	context.lineTo(x2,y2);
	var newAngle5 = Math.atan((x2-x1)/(y1-y2));	
	
	context.moveTo(x1,y1);
	y3 = y1 + 100;
	x3 = x1 + (y3-y1)*Math.tan(Math.PI*(180-angle5-angle6)/180);
    if (x2>450)
    {
    	x2 = 450;
    }
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle56 = Math.atan((x3-x1)/(y3-y1));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,3*Math.PI/2+newAngle5,Math.PI/2-newAngle56,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[2],x1+40,y1);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[2];
	context.stroke();
}
//Problem 7
function P3ANDrawAngleQ7b(angle1,angle2,angle3,angle4,angle5,angle6,colours,labels)
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
	context.fillText(eval(labels)[0],x1-10,y1+100);		
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

	//angle 3
    context.beginPath();
	x1 = 310;
	y1 = 100;
    context.moveTo(x1,y1);
	y2 = 20;
    x2 = x1 + (y1-y2)*Math.tan(Math.PI*angle5/180);
    if (x2>450)
    {
    	x2 = 450;
    }
	context.lineTo(x2,y2);
	var newAngle5 = Math.atan((x2-x1)/(y1-y2));	
	
	context.moveTo(x1,y1);
	y3 = y1 + 100;
	x3 = x1 + (y3-y1)*Math.tan(Math.PI*(180-angle5-angle6)/180);
    if (x2>450)
    {
    	x2 = 450;
    }
	context.lineTo(x3,y3);
	//if you cut y3 at 60 the angle1 will change
	var newAngle56 = Math.atan((x3-x1)/(y3-y1));
	
	context.closePath();
	context.moveTo(x1,y1);
	context.arc(x1,y1,25,3*Math.PI/2+newAngle5,Math.PI/2-newAngle56,false);
	context.font = '12pt Verdana';
	context.fillText(eval(labels)[2],x1+40,y1);
	context.lineWidth = 2;
	context.strokeStyle=eval(colours)[2];
	context.stroke();
}
