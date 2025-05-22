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

function DrawTriangle1(base,Height,displayBase,displayHeight)
{
	var x1 = 20+(Math.random()*(40-10));
	var y1 = 20+(Math.random()*(40-10));
	var angle = Math.random()*90;
	
	var YOffset = 0;
	
	WindowReady();
	
	var XDisplace = Height * Math.cos(Math.PI*angle/180)
	var YDisplace = Height * Math.sin(Math.PI*angle/180)
	
	var x2 = x1 + XDisplace
	var y2 = y1 + YDisplace
		
	var angle1 = 90-angle
	var XDisplace = base * Math.cos(Math.PI*angle1/180)
	var YDisplace = base * Math.sin(Math.PI*angle1/180)

	//boundary conditions
	if (y2-YDisplace<0)
	{
		YOffset = YDisplace - y2 + 30
	}
	var x3 = x2 + XDisplace	
	var y3 = y2 - YDisplace
	
	y1 = y1 + YOffset
	y2 = y2 + YOffset
	y3 = y3 + YOffset	
	
	//creating a small square to denote a right angle
	var SqX1 = x2 + 10*Math.cos(Math.PI*angle1/180)
	var SqY1 = y2 - 10*Math.sin(Math.PI*angle1/180)
	
	var SqX2 = x2 - 10*Math.cos(Math.PI*angle/180)
	var SqY2 = y2 - 10*Math.sin(Math.PI*angle/180)

	var SqX3 = x2 + Math.sqrt(10*10+10*10)*Math.cos(Math.PI*(angle1+45)/180)
	var SqY3 = y2 - Math.sqrt(10*10+10*10)*Math.sin(Math.PI*(angle1+45)/180)
	
	context.beginPath();
	context.moveTo(x1,y1);
	context.lineTo(x2,y2);
	context.lineTo(x3,y3);

	context.fillStyle="yellow";
	context.fill();	
	context.closePath();
    	
	context.beginPath();
	
	context.moveTo(SqX1,SqY1);
	context.dashedLine(SqX1,SqY1,x2,y2);
	context.dashedLine(x2,y2,SqX2,SqY2);
	context.dashedLine(SqX2,SqY2,SqX3,SqY3);
	context.dashedLine(SqX3,SqY3,SqX1,SqY1);
	
	context.strokeStyle="black";
	context.stroke();

	context.strokeText("A",x1-5,y1-5);	
	if (y3-15<0)
	{
		context.strokeText("B",x3+10,y3+10);
	}
	else
	{
		context.strokeText("B",x3-5,y3-5);
	}
	context.strokeText("C",x2-5,y2+10);

	context.strokeText(displayBase,(x1+x2)/2-15,(y1+y2)/2+15);
	context.strokeText(displayHeight,(x2+x3)/2+10,(y2+y3)/2+15);
}

function DrawTriangle2(base,Height,displayBase,displayHeight)
{
	var x1 = 20+(Math.random()*(40-10));
	var y1 = 20+(Math.random()*(40-10));
	//var base = 60+(Math.random()*(110-60));
	//var Height = 60+(Math.random()*(100-60));
	var angle = Math.random()*90;
	
	var YOffset = 0;
	
	WindowReady();
	
	var XDisplace = Height * Math.cos(Math.PI*angle/180)
	var YDisplace = Height * Math.sin(Math.PI*angle/180)
	
	var x2 = x1 + XDisplace
	var y2 = y1 + YDisplace
		
	var angle1 = 90-angle
	var XDisplace = base * Math.cos(Math.PI*angle1/180)
	var YDisplace = base * Math.sin(Math.PI*angle1/180)

	//boundary conditions
	if (y2-YDisplace<0)
	{
		YOffset = YDisplace - y2 + 30
	}
	var x3 = x2 + XDisplace	
	var y3 = y2 - YDisplace
	
	y1 = y1 + YOffset
	y2 = y2 + YOffset
	y3 = y3 + YOffset	
	
	//creating a small square to denote a right angle
	var SqX1 = x2 + 10*Math.cos(Math.PI*angle1/180)
	var SqY1 = y2 - 10*Math.sin(Math.PI*angle1/180)
	
	var SqX2 = x2 - 10*Math.cos(Math.PI*angle/180)
	var SqY2 = y2 - 10*Math.sin(Math.PI*angle/180)

	var SqX3 = x2 + Math.sqrt(10*10+10*10)*Math.cos(Math.PI*(angle1+45)/180)
	var SqY3 = y2 - Math.sqrt(10*10+10*10)*Math.sin(Math.PI*(angle1+45)/180)
	
	var y4 = y1 + 30 + Math.random()*(100-30);
	var x4 = x1 + (x2-x1)*(y4-y1)/(y2-y1);
	
	if (x4>300)
	{
		x4 = 300;
		y4 = y1 + (y2-y1)*(x4-x1)/(x2-x1);
	}

	while(Math.sqrt((x2-x4)*(x2-x4)+(y2-y4)*(y2-y4))<30)
	{
		y4 = y1 + 30 + Math.random()*(100-30);
		x4 = x1 + (x2-x1)*(y4-y1)/(y2-y1);
		
		if (x4>300)
		{
			x4 = 300;
			y4 = y1 + (y2-y1)*(x4-x1)/(x2-x1);			
		}		
		
	}	
	context.beginPath();
	context.moveTo(x1,y1);
	context.lineTo(x4,y4);
	context.lineTo(x3,y3);
	context.closePath();

	context.fillStyle="yellow";
	context.fill();
	context.closePath();

	context.beginPath();
	
	context.moveTo(x1,y1);
	context.dashedLine(x1,y1,x2,y2);
	context.dashedLine(x2,y2,x3,y3);
	context.moveTo(x4,y4);
	context.lineTo(x1,y1);

	context.strokeStyle="black";
	context.stroke();
		
	context.moveTo(SqX1,SqY1);
	context.dashedLine(SqX1,SqY1,x2,y2);
	context.dashedLine(x2,y2,SqX2,SqY2);
	context.dashedLine(SqX2,SqY2,SqX3,SqY3);
	context.dashedLine(SqX3,SqY3,SqX1,SqY1);
	
	context.strokeStyle="#333";
	context.stroke();
    
    context.beginPath();
	context.strokeText("A",x1-5,y1-5);	
	if (y3-15<0)
	{
		context.strokeText("B",x3+10,y3+10);
	}
	else
	{
		context.strokeText("B",x3-5,y3-5);
	}
	context.strokeText("C",x4-10,y4+10);
	context.strokeText("D",x2-5,y2+10);

	context.strokeText(displayBase,(x1+x4)/2-15,(y1+y4)/2+15);
	context.strokeText(displayHeight,(x2+x3)/2+10,(y2+y3)/2+15);
}

function DrawTriangle3(x,y,length,breadth,displayBase,displayHeight,xA,yA,xB,yB,xC,yC)
{
	WindowReady();
	
	context.beginPath();
	context.strokeRect(x,y,length,breadth);
	
	context.strokeStyle="#333";
	context.stroke();
	
	context.beginPath();
	context.moveTo(xA,yA);
	context.lineTo(xB,yB);
	context.lineTo(xC,yC);
	
	context.fillStyle="yellow";
	context.fill();
	context.closePath();
	
	context.beginPath();
	if (yB>y)
	{
		context.strokeText(displayHeight,(xB+xC)/2,yB+15);
		context.strokeText("B",xB,yB+10);
	}
	else
	{
		context.strokeText(displayHeight,(xB+xC)/2,yB-15);
		context.strokeText("B",xB,yB-10);
	}
	if (xA>x)
	{
		context.strokeText(displayBase,xA+15,(yA+yC)/2);
		context.strokeText("A",xA+10,yA);
		context.strokeText("C",xC+10,yC);
	}
	else
	{
		context.strokeText(displayBase,xA-15,(yA+yC)/2);
		context.strokeText("A",xA-10,yA);
		context.strokeText("C",xC-10,yC);
	}
}

function DrawTriangle4(x,y,length,breadth,displayBase,displayBase1,displayBase2,displayHeight,xA,yA,xB,yB,xC,yC)
{
	WindowReady();
	
	context.beginPath();
	context.strokeRect(x,y,length,breadth);
	
	context.strokeStyle="black";
	context.stroke();
	
	context.beginPath();
	context.moveTo(xA,yA);
	context.lineTo(xB,yB);
	context.lineTo(xC,yC);
	
	context.fillStyle="yellow";
	context.fill();
	context.closePath();
		
	context.strokeText("A",x-10,y);
	context.strokeText("B",x+length+5,y);
	context.strokeText("C",x+length+5,y+breadth+5);
	context.strokeText("D",x-10,y+breadth+5);
	if(yA>y)
	{
		context.strokeText("F",xB,yB-5);
		context.strokeText("E",xC,yC-5);
		
		context.strokeText(displayBase,x+length/2,y+breadth+10);
		context.strokeText(displayHeight,x+length+5,y+breadth/2);
		context.strokeText(displayBase1,(x+(xB-x)/2),(y-15));
		context.strokeText(displayBase2,(xC+(x+length-xC)/2),(y-15));		
	}
	else
	{
		context.strokeText("F",xB,yB+10);
		context.strokeText("E",xC,yC+10);
		
		context.strokeText(displayBase,x+length/2,y-5);
		context.strokeText(displayHeight,x+length+5,y+breadth/2);
		context.strokeText(displayBase1,(x+(xB-x)/2),(y+breadth+20));
		context.strokeText(displayBase2,(xC+(x+length-xC)/2),(y+breadth+20));	
	}
}

function DrawTriangle5(x,y,length,breadth,displayBase,displayBase1,displayBase2,displayHeight,displayHeight1,xA,yA,xB,yB,xC,yC)
{
	WindowReady();
	
	context.beginPath();
	context.strokeRect(x,y,length,breadth);
	
	context.strokeStyle="black";
	context.stroke();
	
	context.beginPath();
	context.moveTo(xA,yA);
	context.lineTo(xB,yB);
	context.lineTo(xC,yC);

	context.fillStyle="yellow";
	context.fill();
	context.closePath();
		
	context.beginPath();
	context.moveTo(xA,yA);
	context.dashedLine(xA,yA,x,yA);

	context.strokeStyle="black";
	context.stroke();	
		
	context.strokeText("A",x-10,y);
	context.strokeText("B",x+length+5,y);
	context.strokeText("C",x+length+5,y+breadth+5);
	context.strokeText("D",x-10,y+breadth+5);
	context.strokeText("E",x-10,yA);
	
	if(yB>y)
	{
		context.strokeText("F",xB,yB+10);
		context.strokeText("G",xC,yC+10);
		
		context.strokeText(displayBase,x+length/2,y-5);
		context.strokeText(displayHeight,x+length+5,y+breadth/2);
		context.strokeText(displayBase1,(x+(xB-x)/2),(y+breadth+20));
		context.strokeText(displayBase2,(xC+(x+length-xC)/2),(y+breadth+20));
		context.strokeText(displayHeight1,x-15,(y+yA)/2);	
	}
	else
	{
		context.strokeText("F",xB,yB-5);
		context.strokeText("G",xC,yC-5);
		
		context.strokeText(displayBase,x+length/2,y+breadth+10);
		context.strokeText(displayHeight,x+length+5,y+breadth/2);
		context.strokeText(displayBase1,(x+(xB-x)/2),(y-15));
		context.strokeText(displayBase2,(xC+(x+length-xC)/2),(y-15));
		context.strokeText(displayHeight1,x-15,yA+(y+breadth-yA)/2);
	}
}
