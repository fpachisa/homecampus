var canvasWidth = 250;
var canvasHeight = 220;

// global variable
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

function P4DrawRectangleSquare1(l1,l2,l3,l4,d1,d2,d3,d4)
{
	WindowReady();
	var x1 = context.canvas.width/2;
	var y1 = context.canvas.height/2;
	context.save();
	context.translate(x1,y1);
	var rotateAngle = -Math.PI;
	//context.rotate(rotateAngle);
	x1 = 0;
	y1 = 0;

	context.beginPath();
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.lineTo(x1+l3,y1);
	context.lineTo(x1+l3,y1+l4);
	context.lineTo(x1-l1,y1+l4);
	context.lineTo(x1-l1,y1-l2);
	context.lineTo(x1,y1-l2);
	context.closePath();
	context.strokeStyle="black";
	context.stroke();
	context.fillStyle = get_colour();
	context.fill();
	
	context.beginPath();
	context.lineWidth = 1;
	
	context.moveTo(x1,y1-10);
	context.lineTo(x1+l3,y1-10);
	context.moveTo(x1+l3,y1-15);
	context.lineTo(x1+l3,y1-5);

	context.moveTo(x1+l3+5,y1);
	context.lineTo(x1+l3+15,y1);
	context.moveTo(x1+l3+10,y1);
	context.lineTo(x1+l3+10,y1+l4);
	context.moveTo(x1+l3+5,y1+l4);
	context.lineTo(x1+l3+15,y1+l4);	

	context.moveTo(x1-l1-5,y1);
	context.lineTo(x1-l1-15,y1);
	context.moveTo(x1-l1-10,y1);
	context.lineTo(x1-l1-10,y1-l2);
	context.moveTo(x1-l1-5,y1-l2);
	context.lineTo(x1-l1-15,y1-l2);

	context.moveTo(x1-l1,y1-l2-5);
	context.lineTo(x1-l1,y1-l2-15);
	context.moveTo(x1-l1,y1-l2-10);
	context.lineTo(x1,y1-l2-10);
	context.moveTo(x1,y1-l2-5);
	context.lineTo(x1,y1-l2-15);
	
	context.strokeStyle="black";
	context.stroke();	
    
	context.fillStyle = "black";    

	//displaying the easier numbers
	context.fillText(d3,x1+l3/2,y1-15);
    context.fillText(d4,x1+l3+13,y1+l4/2);
    context.fillText(d2,x1-l1-25,y1-l2/2);
    context.fillText(d1,x1-l1/2,y1-l2-13);
    
    context.fillText("A",x1-l1-10,y1-l2-5);
    context.fillText("B",x1+5,y1-l2);
    context.fillText("C",x1-10,y1);
    context.fillText("D",x1+l3+10,y1-5);
    context.fillText("E",x1+l3,y1+l4+15);
    context.fillText("F",x1-l1-10,y1+l4+15);
    
    context.restore();
}

function P4DrawRectangleSquare2(l1,l2,l3,l4,d1,d2,d3,d4)
{
	WindowReady();

	x1 = 20;
	y1 = 30;

	context.beginPath();
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.lineTo(x1+l1,y1);
	context.lineTo(x1+l1,y1+l2);
	context.lineTo(x1+l1-l3,y1+l2);
	context.lineTo(x1+l1-l3,y1+l2-l4);
	context.lineTo(x1,y1+l2-l4);
	context.closePath();
	context.strokeStyle="black";
	context.stroke();
	context.fillStyle = get_colour();
	context.fill();

	context.beginPath();
	context.lineWidth = 1;
	
	context.moveTo(x1,y1-5);
	context.lineTo(x1,y1-15);
	context.moveTo(x1,y1-10);
	context.lineTo(x1+l1,y1-10);
	context.moveTo(x1+l1,y1-15);
	context.lineTo(x1+l1,y1-5);	
	
	context.moveTo(x1+l1+5,y1);
	context.lineTo(x1+l1+15,y1);
	context.moveTo(x1+l1+10,y1);
	context.lineTo(x1+l1+10,y1+l2);
	context.moveTo(x1+l1+5,y1+l2);
	context.lineTo(x1+l1+15,y1+l2);	

	context.moveTo(x1+l1,y1+l2+5);
	context.lineTo(x1+l1,y1+l2+15);
	context.moveTo(x1+l1,y1+l2+10);
	context.lineTo(x1+l1-l3,y1+l2+10);
	context.moveTo(x1+l1-l3,y1+l2+15);
	context.lineTo(x1+l1-l3,y1+l2+5);

	context.moveTo(x1+l1-l3-5,y1+l2);
	context.lineTo(x1+l1-l3-15,y1+l2);
	context.moveTo(x1+l1-l3-10,y1+l2);
	context.lineTo(x1+l1-l3-10,y1+l2-l4);
	
	context.strokeStyle="black";
	context.stroke();	    
	context.fillStyle = "black";

	//displaying the easier numbers
	context.fillText(d1,x1+l1/2,y1-15);
    context.fillText(d2,x1+l1+15,y1+l2/2);
    context.fillText(d3,x1+l1-l3/2,y1+l2+20);
    context.fillText(d4,x1+l1-l3-25,y1+l2-l4/2);
    
    context.fillText("A",x1,y1-15);
    context.fillText("B",x1+l1+5,y1-15);
    context.fillText("C",x1+l1+5,y1+l2+15);
    context.fillText("D",x1+l1-l3-10,y1+l2+15);
    context.fillText("E",x1+l1-l3+5,y1+l2-l4);
    context.fillText("F",x1-5,y1+l2-l4+10);	
}

function P4DrawRectangleSquare3(l1,l2,l3,l4,l5,d1,d2,d3,d4,d5)
{
	WindowReady();

	x1 = 30;
	y1 = 30;

	context.beginPath();
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.lineTo(x1+l1,y1);
	context.lineTo(x1+l1,y1+l2);
	context.lineTo(x1+l1-l3,y1+l2);
	context.lineTo(x1+l1-l3,y1+l2+l4);
	context.lineTo(x1+l1-l3-l5,y1+l2+l4);
	context.lineTo(x1+l1-l3-l5,y1+l2);
	context.lineTo(x1,y1+l2);
	context.closePath();
	context.strokeStyle="black";
	context.stroke();
	context.fillStyle = get_colour();
	context.fill();

	context.beginPath();
	context.lineWidth = 1;
	
	context.moveTo(x1,y1-5);
	context.lineTo(x1,y1-15);
	context.moveTo(x1,y1-10);
	context.lineTo(x1+l1,y1-10);
	context.moveTo(x1+l1,y1-5);
	context.lineTo(x1+l1,y1-15);

	context.moveTo(x1+l1+5,y1);
	context.lineTo(x1+l1+15,y1);
	context.moveTo(x1+l1+10,y1);
	context.lineTo(x1+l1+10,y1+l2);
	context.moveTo(x1+l1+5,y1+l2);
	context.lineTo(x1+l1+15,y1+l2);

	context.moveTo(x1+l1,y1+l2+5);
	context.lineTo(x1+l1,y1+l2+15);
	context.moveTo(x1+l1,y1+l2+10);
	context.lineTo(x1+l1-l3,y1+l2+10);
	
	if (l1-l3-l5>l5)
	{
		context.moveTo(x1,y1+l2+10);
		context.lineTo(x1,y1+l2+20);
		context.moveTo(x1,y1+l2+15);
		context.lineTo(x1+(l1-l3-l5),y1+l2+15);
		context.fillStyle = "black";
		context.fillText(d1-d3-d5,x1+(l1-l3-l5)/2-5,y1+l2+30);
	}
	else
	{
		context.moveTo(x1+(l1-l3-l5),y1+l2+l4+5);
		context.lineTo(x1+(l1-l3-l5),y1+l2+l4+15);
		context.moveTo(x1+(l1-l3-l5),y1+l2+l4+10);
		context.lineTo(x1+(l1-l3),y1+l2+l4+10);
		context.moveTo(x1+(l1-l3),y1+l2+l4+15);
		context.lineTo(x1+(l1-l3),y1+l2+l4+5);
		context.fillStyle = "black";
		context.fillText(d5,x1+l1-l3-l5/2,y1+l2+l4+20);
	}
	
	context.moveTo(x1-5,y1);
	context.lineTo(x1-15,y1);
	context.moveTo(x1-10,y1);
	context.lineTo(x1-10,y1+l2+l4);
	context.moveTo(x1-5,y1+l2+l4);
	context.lineTo(x1-15,y1+l2+l4);	
	
	context.strokeStyle="black";
	context.stroke();	    
	context.fillStyle = "black";

	//displaying the easier numbers
	context.fillText(d1,x1+l1/2,y1-15);
    context.fillText(d2,x1+l1+15,y1+l2/2);
    context.fillText(d3,x1+l1-l3/2,y1+l2+20);
    context.fillText(d2+d4,x1-25,y1+(l2+l4)/2);
    
    context.fillText("A",x1-15,y1-5);
    context.fillText("B",x1+l1+5,y1-5);
    context.fillText("C",x1+l1+5,y1+l2+10);
    context.fillText("D",x1+l1-l3,y1+l2-5);
    context.fillText("E",x1+l1-l3+5,y1+l2+l4+5);
    context.fillText("F",x1+l1-l3-l5-10,y1+l2+l4+5);
    context.fillText("G",x1+l1-l3-l5-10,y1+l2-5);
    context.fillText("H",x1-5,y1+l2+10);
}

function P4DrawRectangleSquare4(l1,l2,l3,l4,l5,d1,d2,d3,d4,d5)
{
	WindowReady();

	x1 = 30;
	y1 = 30+l2+l3;

	context.beginPath();
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.lineTo(x1+l1,y1);
	context.lineTo(x1+l1,y1-l2);
	context.lineTo(x1+l1-l3,y1-l2);
	context.lineTo(x1+l1-l3,y1-l2-l4);
	context.lineTo(x1+l1-l3-l5,y1-l2-l4);
	context.lineTo(x1+l1-l3-l5,y1-l2);
	context.lineTo(x1,y1-l2);
	context.closePath();
	context.strokeStyle="black";
	context.stroke();
	context.fillStyle = get_colour();
	context.fill();

	context.beginPath();
	context.lineWidth = 1;
	
	context.moveTo(x1,y1+5);
	context.lineTo(x1,y1+15);
	context.moveTo(x1,y1+10);
	context.lineTo(x1+l1,y1+10);
	context.moveTo(x1+l1,y1+5);
	context.lineTo(x1+l1,y1+15);

	context.moveTo(x1+l1+5,y1);
	context.lineTo(x1+l1+15,y1);
	context.moveTo(x1+l1+10,y1);
	context.lineTo(x1+l1+10,y1-l2);
	context.moveTo(x1+l1+5,y1-l2);
	context.lineTo(x1+l1+15,y1-l2);

	context.moveTo(x1+l1,y1-l2-5);
	context.lineTo(x1+l1,y1-l2-15);
	context.moveTo(x1+l1,y1-l2-10);
	context.lineTo(x1+l1-l3,y1-l2-10);
	
	if (l1-l3-l5>l5)
	{
		context.moveTo(x1,y1-l2-10);
		context.lineTo(x1,y1-l2-20);
		context.moveTo(x1,y1-l2-15);
		context.lineTo(x1+(l1-l3-l5),y1-l2-15);
		
		context.moveTo(x1-5,y1);
		context.lineTo(x1-15,y1);
		context.moveTo(x1-10,y1);
		context.lineTo(x1-10,y1-l2-l4);
		context.moveTo(x1-5,y1-l2-l4);
		context.lineTo(x1-15,y1-l2-l4);
		context.fillStyle = "black";
		context.fillText(d2+d4,x1-25,y1-(l2+l4)/2);	
		context.fillText(d1-d3-d5,x1+(l1-l3-l5)/2-5,y1-l2-30);
	}
	else
	{
		context.moveTo(x1+(l1-l3-l5),y1-l2-l4-5);
		context.lineTo(x1+(l1-l3-l5),y1-l2-l4-15);
		context.moveTo(x1+(l1-l3-l5),y1-l2-l4-10);
		context.lineTo(x1+(l1-l3),y1-l2-l4-10);
		context.moveTo(x1+(l1-l3),y1-l2-l4-15);
		context.lineTo(x1+(l1-l3),y1-l2-l4-5);

		context.moveTo(x1+l1-l3-10,y1-l2-l4);
		context.lineTo(x1+l1-l3-10,y1-l2);
		context.moveTo(x1+l1-l3-5,y1-l2);
		context.lineTo(x1+l1-l3-15,y1-l2);		
		
		context.fillStyle = "black";
		context.fillText(d5,x1+l1-l3-l5/2,y1-l2-l4-20);
		context.fillText(d4,x1+l1-l3-25,y1-l2-l4/2);
	}		
	
	context.strokeStyle="black";
	context.stroke();	    
	context.fillStyle = "black";

	//displaying the easier numbers
	context.fillText(d1,x1+l1/2,y1+25);
    context.fillText(d2,x1+l1+15,y1-l2/2);
    context.fillText(d3,x1+l1-l3/2,y1-l2-15);
    
    
    context.fillText("A",x1-15,y1+15);
    context.fillText("B",x1+l1+5,y1+15);
    context.fillText("C",x1+l1+5,y1-l2-5);
    context.fillText("D",x1+l1-l3,y1-l2+15-5);
    context.fillText("E",x1+l1-l3+5,y1-l2-l4);
    context.fillText("F",x1+l1-l3-l5-10,y1-l2-l4);
    context.fillText("G",x1+l1-l3-l5-10,y1-l2+15-5);
    context.fillText("H",x1-5,y1-l2);
}

function P4DrawRectangleSquare5(l1,l2,l3,l4,l5,d1,d2,d3,d4,d5)
{
	WindowReady();

	x1 = 30;
	y1 = 30;

	context.beginPath();
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.lineTo(x1+l1,y1);
	context.lineTo(x1+l1,y1+l2);
	context.lineTo(x1+l1+l3,y1+l2);
	context.lineTo(x1+l1+l3,y1+l2+l4);
	context.lineTo(x1+l1+l3-l5,y1+l2+l4);
	context.lineTo(x1+l1+l3-l5,y1+l2);
	context.lineTo(x1,y1+l2);
	context.closePath();
	context.strokeStyle="black";
	context.stroke();
	context.fillStyle = get_colour();
	context.fill();

	context.beginPath();
	context.lineWidth = 1;
	
	context.moveTo(x1,y1-5);
	context.lineTo(x1,y1-15);
	context.moveTo(x1,y1-10);
	context.lineTo(x1+l1,y1-10);
	context.moveTo(x1+l1,y1-5);
	context.lineTo(x1+l1,y1-15);

	context.moveTo(x1+l1+5,y1);
	context.lineTo(x1+l1+15,y1);
	context.moveTo(x1+l1+10,y1);
	context.lineTo(x1+l1+10,y1+l2);

	context.moveTo(x1+l1,y1+l2+5);
	context.lineTo(x1+l1,y1+l2+15);
	context.moveTo(x1+l1,y1+l2+10);
	context.lineTo(x1+l1+l3,y1+l2+10);

	context.moveTo(x1,y1+l2+5);
	context.lineTo(x1,y1+l2+15);
	context.moveTo(x1,y1+l2+10);
	context.lineTo(x1+(l1+l3-l5),y1+l2+10);
	
	context.moveTo(x1-5,y1);
	context.lineTo(x1-15,y1);
	context.moveTo(x1-10,y1);
	context.lineTo(x1-10,y1+l2+l4);
	context.moveTo(x1-5,y1+l2+l4);
	context.lineTo(x1-15,y1+l2+l4);
	
	context.strokeStyle="black";
	context.stroke();	    
	context.fillStyle = "black";

	//displaying the easier numbers
	context.fillText(d1,x1+l1/2,y1-15);
    context.fillText(d2,x1+l1+13,y1+l2/2);
    context.fillText(d3,x1+l1+l3/2,y1+l2+25);
    context.fillText(d1+d3-d5,x1+(l1+l3-l5)/2,y1+l2+25);
    context.fillText(d2+d4,x1-25,y1+(l2+l4)/2);
    
    context.fillText("A",x1-15,y1-10);
    context.fillText("B",x1+l1+5,y1-10);
    context.fillText("C",x1+l1+15,y1+l2-5);
    context.fillText("D",x1+l1+l3+5,y1+l2);
    context.fillText("E",x1+l1+l3+5,y1+l2+l4);
    context.fillText("F",x1+l1+l3-l5-10,y1+l2+l4+5);
    context.fillText("G",x1+l1+l3-l5-15,y1+l2-5);
    context.fillText("H",x1-25,y1+l2+5);
}

function P4DrawRectangleSquare6(l1,l2,l3,l4,l5,l6,d1,d2,d3,d4,d5,d6)
{
	WindowReady();

	x1 = 30;
	y1 = 30;

	context.beginPath();
	context.lineWidth = 2;
	context.moveTo(x1,y1);
	context.lineTo(x1+l1,y1);
	context.lineTo(x1+l1,y1+l2);
	context.lineTo(x1+l1+l3,y1+l2);
	context.lineTo(x1+l1+l3,y1+l2+l4);
	context.lineTo(x1+l1+l3-l5,y1+l2+l4);
	context.lineTo(x1+l1+l3-l5,y1+l2+l4-l6);
	context.lineTo(x1+l1,y1+l2+l4-l6);
	context.lineTo(x1+l1,y1+l2+l4);
	context.lineTo(x1,y1+l2+l4);
	context.closePath();
	context.strokeStyle="black";
	context.stroke();
	context.fillStyle = get_colour();
	context.fill();

	context.beginPath();
	context.lineWidth = 1;
	
	context.moveTo(x1,y1-5);
	context.lineTo(x1,y1-15);
	context.moveTo(x1,y1-10);
	context.lineTo(x1+l1,y1-10);
	context.moveTo(x1+l1,y1-5);
	context.lineTo(x1+l1,y1-15);

	context.moveTo(x1+l1-10,y1);
	context.lineTo(x1+l1-10,y1+l2);
	context.moveTo(x1+l1-5,y1+l2);
	context.lineTo(x1+l1-15,y1+l2)
	
	context.moveTo(x1+l1,y1+l2-15);
	context.lineTo(x1+l1+l3,y1+l2-15);
	context.moveTo(x1+l1+l3,y1+l2-20);
	context.lineTo(x1+l1+l3,y1+l2-10);
	
	context.moveTo(x1+l1+l3-l5,y1+l2);
	context.dashedLine(x1+l1+l3-l5,y1+l2,x1+l1+l3-l5,y1+l2+l4-l6);
	
	context.moveTo(x1+l1+l3+5,y1+l2);
	context.lineTo(x1+l1+l3+15,y1+l2);
	context.moveTo(x1+l1+l3+10,y1+l2);
	context.lineTo(x1+l1+l3+10,y1+l2+l4);
	context.lineTo(x1+l1+l3+5,y1+l2+l4);
	context.lineTo(x1+l1+l3+15,y1+l2+l4);
	
	context.moveTo(x1+l1+l3,y1+l2+l4+5);
	context.lineTo(x1+l1+l3,y1+l2+l4+15);
	context.moveTo(x1+l1+l3,y1+l2+l4+10);
	context.lineTo(x1+l1+l3-l5,y1+l2+l4+10);
	context.moveTo(x1+l1+l3-l5,y1+l2+l4+15);
	context.lineTo(x1+l1+l3-l5,y1+l2+l4+5);
	
	context.moveTo(x1+l1-5,y1+l2+l4-l6);
	context.lineTo(x1+l1-15,y1+l2+l4-l6);
	context.moveTo(x1+l1-10,y1+l2+l4-l6);
	context.lineTo(x1+l1-10,y1+l2+l4);
	
	context.strokeStyle="black";
	context.stroke();	    
	context.fillStyle = "black";

	//displaying the easier numbers
	context.fillText(d1,x1+l1/2,y1-15);
    context.fillText(d2,x1+l1-25,y1+l2/2);
    context.fillText(d3,x1+l1+l3/2,y1+l2-25);
    context.fillText(d4,x1+l1+l3+15,y1+l2+l4/2);
    context.fillText(d5,x1+l1+l3-l5/2,y1+l2+l4+25);
    context.fillText(d6,x1+l1-25,y1+l2+l4-l6/2);
    
    context.fillText("A",x1-15,y1-10);
    context.fillText("B",x1+l1+5,y1-10);
    context.fillText("C",x1+l1+5,y1+l2-5);
    context.fillText("D",x1+l1+l3-l5-10,y1+l2-5);
    context.fillText("E",x1+l1+l3+5,y1+l2-5);
    context.fillText("F",x1+l1+l3+5,y1+l2+l4+15);
    context.fillText("G",x1+l1+l3-l5-15,y1+l2+l4+15);
    context.fillText("H",x1+l1+l3-l5-10,y1+l2+l4-l6+15);
    context.fillText("I",x1+l1+5,y1+l2+l4-l6+15);
    context.fillText("J",x1+l1,y1+l2+l4+15);
    context.fillText("K",x1,y1+l2+l4+15);
}

function P4DrawRectangleSquare7(l1,l2,l3,d1,d2,d3)
{
	WindowReady();

	x1 = 30;
	y1 = 30;
	
	context.fillStyle = get_colour();
	context.fillRect(x1,y1,l1,l1);
	context.closePath();
	
	x2 = x1+15 + Math.random()*((x1+l1-l2-15)-(x1+15));
	y2 = y1+15 + Math.random()*((y1+l1-l3-15)-(y1+15));
	context.fillStyle = "#EEFFFE";
	context.fillRect(x2,y2,l2,l3);
	
	context.beginPath();
	context.lineWidth = 1;
	
	context.moveTo(x1,y1-5);
	context.lineTo(x1,y1-15);
	context.moveTo(x1,y1-10);
	context.lineTo(x1+l1,y1-10);
	context.moveTo(x1+l1,y1-5);
	context.lineTo(x1+l1,y1-15);
	
	context.moveTo(x1+l1+5,y1);
	context.lineTo(x1+l1+15,y1);
	context.moveTo(x1+l1+10,y1);
	context.lineTo(x1+l1+10,y1+l1);
	context.moveTo(x1+l1+5,y1+l1);
	context.lineTo(x1+l1+15,y1+l1);
	
	if (x2-x1>30)
		{
			context.moveTo(x2-5,y2);
			context.lineTo(x2-15,y2);
			context.moveTo(x2-10,y2);
			context.lineTo(x2-10,y2+l3);
			context.moveTo(x2-15,y2+l3);
			context.lineTo(x2-5,y2+l3);
			context.fillStyle = "black";
			context.fillText(d3,x2-25,y2+l3/2);
		}
	else
		{
			context.moveTo(x2+l2+5,y2);
			context.lineTo(x2+l2+15,y2);
			context.moveTo(x2+l2+10,y2);
			context.lineTo(x2+l2+10,y2+l3);
			context.moveTo(x2+l2+15,y2+l3);
			context.lineTo(x2+l2+5,y2+l3);
			context.fillStyle = "black";
			context.fillText(d3,x2+l2+15,y2+l3/2);
		}
	if (y2-y1>30)
	{
		context.moveTo(x2,y2-5);
		context.lineTo(x2,y2-15);
		context.moveTo(x2,y2-10);
		context.lineTo(x2+l2,y2-10);
		context.moveTo(x2+l2,y2-15);
		context.lineTo(x2+l2,y2-5);
		context.fillStyle = "black";
		context.fillText(d2,x2+l2/2,y2-15);		
	}
	else
	{
		context.moveTo(x2,y2+l3+5);
		context.lineTo(x2,y2+l3+15);
		context.moveTo(x2,y2+l3+10);
		context.lineTo(x2+l2,y2+l3+10);
		context.moveTo(x2+l2,y2+l3+15);
		context.lineTo(x2+l2,y2+l3+5);
		context.fillStyle = "black";
		context.fillText(d2,x2+l2/2,y2+l3+25);
	}
	
	context.strokeStyle="black";
	context.stroke();
	context.fillStyle = "black";
	//displaying the easier numbers
	context.fillText(d1,x1+l1/2,y1-15);
	context.fillText(d1,x1+l1+15,y1+l1/2);

}

function P4DrawRectangleSquare8(l1,d1)
{
	WindowReady();

	x1 = 30;
	y1 = 30;	

	context.beginPath();
	context.lineWidth = 2;
	context.moveTo(x1+2*l1,y1);
	context.lineTo(x1+3*l1,y1);
	context.lineTo(x1+3*l1,y1+3*l1);
	context.lineTo(x1,y1+3*l1);
	context.lineTo(x1,y1+2*l1);
	context.lineTo(x1+l1,y1+2*l1);
	context.lineTo(x1+l1,y1+l1);
	context.lineTo(x1+2*l1,y1+l1);	
	context.closePath();
	context.strokeStyle="black";
	context.stroke();	
	context.fillStyle = get_colour();
	context.fill();
	
	context.beginPath();
	context.lineWidth = 1;
	
	context.moveTo(x1+2*l1,y1-5);
	context.lineTo(x1+2*l1,y1-15);
	context.moveTo(x1+2*l1,y1-10);
	context.lineTo(x1+3*l1,y1-10);
	context.moveTo(x1+3*l1,y1-15);
	context.lineTo(x1+3*l1,y1-5);
	
	context.moveTo(x1+l1,y1+l1-5);
	context.lineTo(x1+l1,y1+l1-15);
	context.moveTo(x1+l1,y1+l1-10);
	context.lineTo(x1+2*l1,y1+l1-10);

	context.moveTo(x1+l1-15,y1+l1);
	context.lineTo(x1+l1-5,y1+l1);
	context.moveTo(x1+l1-10,y1+l1);
	context.lineTo(x1+l1-10,y1+2*l1);

	context.moveTo(x1-15,y1+2*l1);
	context.lineTo(x1-5,y1+2*l1);
	context.moveTo(x1-10,y1+2*l1);
	context.lineTo(x1-10,y1+3*l1);
	context.moveTo(x1-5,y1+3*l1);
	context.lineTo(x1-15,y1+3*l1);

	context.moveTo(x1+3*l1+5,y1);
	context.lineTo(x1+3*l1+15,y1);
	context.moveTo(x1+3*l1+10,y1);
	context.lineTo(x1+3*l1+10,y1+3*l1);
	context.moveTo(x1+3*l1+15,y1+3*l1);
	context.lineTo(x1+3*l1+5,y1+3*l1);

	context.moveTo(x1,y1+3*l1+5);
	context.lineTo(x1,y1+3*l1+15);
	context.moveTo(x1,y1+3*l1+10);
	context.lineTo(x1+3*l1,y1+3*l1+10);
	context.moveTo(x1+3*l1,y1+3*l1+5);
	context.lineTo(x1+3*l1,y1+3*l1+15);

	context.moveTo(x1+2*l1,y1+l1);
	context.dashedLine(x1+2*l1,y1+l1,x1+2*l1,y1+3*l1);

	context.moveTo(x1+l1,y1+2*l1);
	context.dashedLine(x1+l1,y1+2*l1,x1+l1,y1+3*l1);
	
	context.strokeStyle="black";
	context.stroke();
	context.fillStyle = "black";
	//displaying the easier numbers
	context.fillText(d1,x1+2*l1+l1/2,y1-15);
	context.fillText(d1,x1+l1+l1/2,y1+l1-15);
	context.fillText(d1,x1+l1-25,y1+l1+l1/2);
	context.fillText(d1,x1-25,y1+2*l1+l1/2);
	context.fillText(3*d1,x1+3*l1+15,y1+3*l1/2);
	context.fillText(3*d1,x1+3*l1/2,y1+3*l1+25);
}

function get_colour()
{
	var colour_code = Math.floor(Math.random()*56);
	var colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"];
	return colours[colour_code];
}