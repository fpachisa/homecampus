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

function DrawAngles1(angle1)
{
	WindowReady();
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
	var cp2 = y1;
	
	context.font = "bold 12px sans-serif";
	//first line
	context.moveTo(cp1,cp2);
	var angle1 = angle1
	y2 = 0;
	x2 = cp1+(y1-y2)/Math.tan(Math.PI*angle1/180);
	context.lineTo(x2,y2);

	//right arc	
	context.moveTo(cp1,cp2);
	context.arc(cp1,cp2,15,0,(2*Math.PI-Math.PI*(angle1)/180),true);

	//left arc
	context.moveTo(cp1,cp2);
	context.arc(cp1,cp2,18,Math.PI,Math.PI+Math.PI*(180-angle1)/180,false);
	context.closePath();
		
	context.strokeStyle="black";
	context.stroke();
	
	context.beginPath();
	var Angle1Text = String(Math.round(angle1));
	context.fillText(Angle1Text,cp1+20,cp2-5);
	
	context.fillText("X",cp1-25,cp2-5);
	context.closePath();	
}

function DrawAngles2(angle1,angle2)
{
	WindowReady();
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
	var cp2 = y1;

	//first line
	context.moveTo(cp1,cp2);
	var angle1 = angle1;
	y2 = 0;
	x2 = cp1+(y1-y2)/Math.tan(Math.PI*angle1/180);
	context.lineTo(x2,y2);
	
	context.font = "bold 12px sans-serif";
	//right arc	
	context.moveTo(cp1,cp2);
	context.arc(cp1,cp2,15,0,(2*Math.PI-Math.PI*(angle1)/180),true);
	var Angle1Text = String(Math.round(angle1));
	context.fillText(Angle1Text,cp1+20,cp2-5);
	
	//second line
	context.moveTo(cp1,cp2);
	var angle2 = angle2;	
	y2 = 0;
	x2 = cp1-(y1-y2)/Math.tan(Math.PI*angle2/180);
	context.lineTo(x2,y2);
	
	//left arc
	context.moveTo(cp1,cp2);
	context.arc(cp1,cp2,15,Math.PI,Math.PI+Math.PI*angle2/180,false);
	var Angle1Text = String(Math.round(angle2));
	context.fillText(Angle1Text,cp1-35,cp2-5);
	
	//middle arc
	context.moveTo(cp1,cp2);
	context.arc(cp1,cp2,20,Math.PI+Math.PI*angle2/180,2*Math.PI-Math.PI*(angle1)/180,false);
	context.fillText("X",cp1-5,cp2-25);
			
	context.strokeStyle="black";
	context.stroke();
}

function DrawAngles3(angle1)
{
	 WindowReady();
	 var x1 = 0;
	 var y1 = 100;
	 var x2 = 0;
	 var y2 = y1;
	 context.beginPath();
	 //base line
	 context.moveTo(x1,y1);
	 x2 = 150;
	 context.lineTo(x2,y2);
	 //common point
	 var cp1 = x2-80;
	 var cp2 = y2;
	
	 context.moveTo(cp1,cp2);
	 var angle1 = angle1;
	 y3 = 0;
	 x3 = cp1+y2/Math.tan(Math.PI*angle1/180);
	 context.lineTo(x3,y3);
	 
	 context.moveTo(cp1,cp2);
	 y4 = y1+100;
	 x4 = cp1-y2/Math.tan(Math.PI*angle1/180);
	 context.lineTo(x4,y4); 
	 
	 context.font = "bold 12px sans-serif";
	 //right arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,15,0,(2*Math.PI-Math.PI*angle1/180),true);
	 var Angle1Text = String(Math.round(angle1));
	 context.fillText(Angle1Text,cp1+20,cp2-5);
	
	 //bottom right arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,18,0,(Math.PI-Math.PI*angle1/180),false);
	 context.fillText("X",cp1+20,cp2+20);
	    
	 context.strokeStyle="black";
	 context.stroke();
}

function DrawAngles4(angle1)
{
	 WindowReady();
	 var x1 = 0;
	 var y1 = 100;
	 var x2 = 0;
	 var y2 = y1;
	 context.beginPath();
	 //base line
	 context.moveTo(x1,y1);
	 x2 = 150;
	 context.lineTo(x2,y2);
	 //common point
	 var cp1 = x2-80;
	 var cp2 = y2;
	
	 context.moveTo(cp1,cp2);
	 var angle1 = angle1;
	 y3 = 0;
	 x3 = cp1+y2/Math.tan(Math.PI*angle1/180);
	 context.lineTo(x3,y3);
	 
	 context.moveTo(cp1,cp2);
	 y4 = y1+100;
	 x4 = cp1-y2/Math.tan(Math.PI*angle1/180);
	 context.lineTo(x4,y4); 
	
	context.font = "bold 12px sans-serif";
	 //right arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,15,0,(2*Math.PI-Math.PI*(angle1)/180),true);
	 var Angle1Text = String(angle1);
	 context.fillText(Angle1Text,cp1+20,cp2-5);
	
	 //left arc
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,15,Math.PI,Math.PI-Math.PI*angle1/180,true);
	 context.fillText("X",cp1-35,cp2+15);
	   
	 context.strokeStyle="black";
	 context.stroke();
}

function DrawAngles5(angle1,angle2,angle3,angle4)
{
	 WindowReady();
	 //common point
	 var cp1 = 80;
	 var cp2 = 80;
	
	 //first line
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 var angle1 = angle1;
	 y1 = 0;
	 x1 = cp1+cp2/Math.tan(Math.PI*angle1/180);
	 context.lineTo(x1,y1);
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke();
	 
	 //second line
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 var angle2 = angle2;
	 y2 = 0;
	 x2 = cp1-cp2/Math.tan(Math.PI*angle2/180);
	 context.lineTo(x2,y2);
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke(); 
	 
	 //third line
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 var angle3 = angle3;
	 y3 = 160;
	 x3 = cp1+cp2/Math.tan(Math.PI*angle3/180);
	 context.lineTo(x3,y3);
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke(); 
	 
	 //fourth line
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 var angle4 = angle4;
	 y4 = 160;
	 x4 = cp1-cp2/Math.tan(Math.PI*angle4/180);
	 context.lineTo(x4,y4);
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke(); 
	 
	 context.font = "bold 12px sans-serif";
	 //first arc 
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,15,Math.PI*angle3/180,-Math.PI*angle1/180,true);
	 var Angle1Text = String(Math.round(angle1+angle3));
	 context.fillText(Angle1Text,cp1+20,cp2+5);
	 
	 //second arc
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,20,Math.PI+Math.PI*angle2/180,-Math.PI*angle1/180,false);
	 var Angle2Text = String(Math.round(180-angle1-angle2));
	 context.fillText(Angle2Text,cp1,cp2-20);
	
	 //third arc
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,15,Math.PI-Math.PI*angle4/180,Math.PI+Math.PI*angle2/180,false);
	 var Angle3Text = String(Math.round(angle2+angle4));
	 context.fillText(Angle3Text,cp1-35,cp2+10);
	
	 //fourth arc
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,20,Math.PI*angle3/180,Math.PI-Math.PI*angle4/180,false);
	 //var Angle4Text = String(Math.round(180-angle3-angle4));
	 context.fillText("X",cp1-10,cp2+30);
	    
	 context.strokeStyle="black";
	 context.stroke();    
}

function DrawAngles6(angle1,angle2)
{
	 WindowReady();
	 //common point
	 var cp1 = 80;
	 var cp2 = 80;
	
	 //first line
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 var angle1 = angle1;
	 y1 = 0;
	 x1 = cp1+cp2/Math.tan(Math.PI*angle1/180);
	 context.lineTo(x1,y1);
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke();
	 
	 //second line
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 var angle2 = angle2;
	 y2 = 0;
	 x2 = cp1-cp2/Math.tan(Math.PI*angle2/180);
	 context.lineTo(x2,y2);
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke(); 
	 
	 context.font = "bold 12px sans-serif";
	 //second arc
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,20,Math.PI+Math.PI*angle2/180,-Math.PI*angle1/180,false);
	 var Angle2Text = String(Math.round(180-angle1-angle2));
	 context.fillText(Angle2Text,cp1-5,cp2-25);
	
	 //third arc
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,15,-Math.PI*angle1/180,Math.PI+Math.PI*angle2/180,false);
	 //var Angle3Text = String(Math.round(angle2+angle4));
	 context.fillText("X",cp1-5,cp2+30);
	    
	 context.strokeStyle="black";
	 context.stroke();    
}

function DrawAngles7(angle1,angle2,angle3)
{
	 WindowReady();
	 var cp1 = 80;
	 var cp2 = 80;
	  
	 //line 1 
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 //angle1 = 30 + Math.random()*(70-30);
	 var y1 = 0;
	 var x1 = cp1+cp2/Math.tan(Math.PI*angle1/180);
	
	 context.lineTo(x1,y1);
	  
	 context.moveTo(cp1,cp2);
	 var y2 = 160;
	 var x2 = cp1-cp2/Math.tan(Math.PI*angle1/180);
	 context.lineTo(x2,y2);
	 
	 context.font = "bold 12px sans-serif";
	 context.fillText("A",x1+5,y1+10);
	 if (x2+15<15)
	 {
	  context.fillText("B",15,y2);
	 }
	 else
	 {
	  context.fillText("B",x2+15,y2);
	 }
	 context.closePath();
	  
	 context.strokeStyle="black";
	 context.stroke(); 
	 // line 2 
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 //angle2 = 30 + Math.random()*(50-30);
	
	 y3 = 0;
	 x3 = cp1-cp2/Math.tan(Math.PI*angle2/180);
	 context.lineTo(x3,y3);
	  
	 context.moveTo(cp1,cp2);
	 y4 = 160;
	 x4 = cp1+cp2/Math.tan(Math.PI*angle2/180);
	 context.lineTo(x4,y4);
	 if (x3+15<15)
	 {
	  context.fillText("C",15,y3+30);
	 }
	 else
	 {
	  context.fillText("C",x3+15,y3+30);
	 }
	 context.fillText("D",x4+15,y4);
	
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke();
	  
	 // line 3 
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 //angle3 = angle2 * 1.5 + 20;
	 //angle3 = angle2 + 20 + Math.random()*(160-angle1-angle2);
	
	 y5 = 0;
	 x5 = cp1-cp2/Math.tan(Math.PI*angle3/180);
	 context.lineTo(x5,y5);
	 context.fillText("E",x5+5,y5+10);
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke();
	 
	 //bottom arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,15,Math.PI-Math.PI*angle1/180,Math.PI*angle2/180,true);
	 var AngleText1 = String(Math.round(180-angle1-angle2));
	 context.fillText(AngleText1,cp1-10,cp2+25);
	 
	 //middle arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,10,Math.PI+Math.PI*angle2/180,Math.PI+Math.PI*angle3/180,false);
	 var AngleText2 = String(Math.round(angle3-angle2));
	 context.fillText(AngleText2,cp1-10,cp2-20);
	 
	 //left arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,18,Math.PI-Math.PI*angle1/180,Math.PI+Math.PI*angle2/180,false);
	 context.fillText("X",cp1-30,cp2+5);
	 
	 context.fillText("O",cp1+8,cp2+5);
	 	    
	 context.strokeStyle="black";
	 context.stroke();
}

function DrawAngles8(angle1,angle2,angle3)
{
	 WindowReady();
	 var cp1 = 80;
	 var cp2 = 80;
	  
	 //line 1 
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 //angle1 = 30 + Math.random()*(70-30);
	 var y1 = 0;
	 var x1 = cp1+cp2/Math.tan(Math.PI*angle1/180);
	
	 context.lineTo(x1,y1);
	  
	 context.moveTo(cp1,cp2);
	 var y2 = 160;
	 var x2 = cp1-cp2/Math.tan(Math.PI*angle1/180);
	 context.lineTo(x2,y2);
	 
	 context.font = "bold 12px sans-serif";
	 context.fillText("A",x1+5,y1+10);
	 if (x2+15<15)
	 {
	  context.fillText("B",15,y2);
	 }
	 else
	 {
	  context.fillText("B",x2+15,y2);
	
	
	 }
	 context.closePath();
	  
	 context.strokeStyle="black";
	 context.stroke(); 
	 // line 2 
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 //angle2 = 30 + Math.random()*(50-30);
	
	 y3 = 0;
	 x3 = cp1-cp2/Math.tan(Math.PI*angle2/180);
	 context.lineTo(x3,y3);
	  
	 context.moveTo(cp1,cp2);
	 y4 = 160;
	 x4 = cp1+cp2/Math.tan(Math.PI*angle2/180);
	 context.lineTo(x4,y4);
	 if (x3+15<15)
	 {
	  context.fillText("C",15,y3+30);
	 }
	 else
	 {
	  context.fillText("C",x3+15,y3+30);
	 }
	 context.fillText("D",x4+15,y4);
	
	 context.closePath();
	
	 context.strokeStyle="black";
	 context.stroke();
	  
	 // line 3 
	 context.beginPath();
	 context.moveTo(cp1,cp2);
	 //angle3 = angle2 * 1.5 + 20;
	 //angle3 = angle2 + 20 + Math.random()*(160-angle1-angle2);
	
	 y5 = 0;
	 x5 = cp1-cp2/Math.tan(Math.PI*angle3/180);
	 context.lineTo(x5,y5);
	 context.fillText("E",x5+5,y5+10);
	 context.closePath();
	 context.strokeStyle="black";
	 context.stroke();
	 
	 //bottom arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,15,Math.PI-Math.PI*angle1/180,Math.PI*angle2/180,true);
	 var AngleText1 = String(Math.round(180-angle1-angle2));
	 context.fillText(AngleText1,cp1,cp2+25);
	 
	 //middle arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,10,Math.PI+Math.PI*angle2/180,Math.PI+Math.PI*angle3/180,false);
	 var AngleText2 = String(Math.round(angle3-angle2));
	 context.fillText(AngleText2,cp1-20,cp2-20);
	 //left arc 
	 context.moveTo(cp1,cp2);
	 context.arc(cp1,cp2,18,Math.PI+Math.PI*angle3/180,-Math.PI*angle1/180,false);
	 context.fillText("X",cp1,cp2-25);
	 
	 context.fillText("O",cp1+8,cp2+5);
	 	     
	context.strokeStyle="black";
	context.stroke();
}
