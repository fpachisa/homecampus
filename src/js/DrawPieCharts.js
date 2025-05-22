var canvasWidth = 270;
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

function DrawPieChart1(data,stalls)
{
	WindowReady();
	
	var colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"];	
	// based on Fisher-Yates algo
	colourShuffle = function(o){
		for(var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
		return o;
	};
	colourShuffle(colours);

	function getTotal()
	{
		var total = 0;
		for (var j = 0; j < data.length; j++) {
		total += (typeof data[j] == 'number') ? data[j] : 0;
		}
		return total;
	}

	function plotData() 
	{
		//var rotate = Math.random()*Math.PI*2;
		var lastend = 0;
		var total = getTotal();
		context.lineWidth = 2;
	
		for (var i = 0; i < data.length; i++) 
		{
			context.fillStyle = colours[i];
			context.beginPath();
			context.moveTo(125,110);			
			context.arc(125,110,90,lastend,lastend+(Math.PI*2*(data[i]/total)),false);
			context.lineTo(125,110);
			context.strokeStyle="black";
			context.stroke();				
			context.fill();
			lastend += Math.PI*2*(data[i]/total);
		}
		x1 = 125;
		y1 = 110;
		
		/*context.translate(x1,y1);
		context.rotate(rotate);*/
		context.beginPath();
		context.lineWidth = 1;
		//context.strokeRect(x1,y1,10,10);
		context.moveTo(x1+10,y1);
		context.lineTo(x1+10,y1+10);
		context.lineTo(x1,y1+10);
		context.strokeStyle="black";
		context.stroke();
		
		context.fillStyle = "black";
		//context.fillText(stalls[0],x1+30,y1+50);
		context.fillText(stalls[0],x1+90*Math.cos(Math.PI*(data[0]/total))-38,y1+90*Math.sin(Math.PI*(data[0]/total))-10);
		//context.fillText(stalls[1],x1-50,y1+50);
		context.fillText(stalls[1],x1+90*Math.cos(Math.PI*(data[1]+2*data[0])/total),y1+90*Math.sin(Math.PI*(data[1]+2*data[0])/total)-10);
		//context.fillText(stalls[2],x1-70,y1-20);
		//context.fillText("$"+data[2],x1-70,y1-10);
		context.fillText(stalls[2],x1+90*Math.cos(Math.PI*(data[2]+2*data[1]+2*data[0])/total)+10,y1+90*Math.sin(Math.PI*(data[2]+2*data[1]+2*data[0])/total)+20);
		context.fillText("$"+data[2],x1+90*Math.cos(Math.PI*(data[2]+2*data[1]+2*data[0])/total)+10,y1+90*Math.sin(Math.PI*(data[2]+2*data[1]+2*data[0])/total)+30);
		//context.fillText(stalls[3],x1+30,y1-40);
		//context.fillText("$"+data[3],x1+30,y1-30);
		context.fillText(stalls[3],x1+90*Math.cos(Math.PI*(data[3]+2*data[2]+2*data[1]+2*data[0])/total)-35,y1+90*Math.sin(Math.PI*(data[3]+2*data[2]+2*data[1]+2*data[0])/total)+20);
		context.fillText("$"+data[3],x1+90*Math.cos(Math.PI*(data[3]+2*data[2]+2*data[1]+2*data[0])/total)-35,y1+90*Math.sin(Math.PI*(data[3]+2*data[2]+2*data[1]+2*data[0])/total)+30);
	}		

	plotData();
}
function DrawPieChart2(data,clothes,num1,den1,num2,den2)
{
	WindowReady();
	
	var colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"];	
	// based on Fisher-Yates algo
	colourShuffle = function(o){
		for(var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
		return o;
	};
	colourShuffle(colours);

	function getTotal()
	{
		var total = 0;
		for (var j = 0; j < data.length; j++) {
		total += (typeof data[j] == 'number') ? data[j] : 0;
		}
		return total;
	}

	function plotData() 
	{
		//var rotate = Math.random()*Math.PI*2;
		var lastend = 0;
		var total = getTotal();
		context.lineWidth = 2;
	
		for (var i = 0; i < data.length; i++) 
		{
			context.fillStyle = colours[i];
			context.beginPath();
			context.moveTo(135,100);			
			context.arc(135,100,90,lastend,lastend+(Math.PI*2*(data[i]/total)),false);
			context.lineTo(135,100);
			context.strokeStyle="black";
			context.stroke();				
			context.fill();
			lastend += Math.PI*2*(data[i]/total);
		}
		x1 = 135;
		y1 = 100;
		
		/*context.translate(x1,y1);
		context.rotate(rotate);*/
		context.beginPath();
		context.lineWidth = 1;
		context.moveTo(x1+10,y1);
		context.lineTo(x1+10,y1+10);
		context.lineTo(x1,y1+10);
		
		context.fillStyle = "black";
		//context.fillText(clothes[0],x1+30,y1+50);
		context.fillText(clothes[0],x1+90*Math.cos(Math.PI*(data[0]/total))-38,y1+90*Math.sin(Math.PI*(data[0]/total))-10);
		//context.fillText(clothes[1],x1-50,y1+100);
		//context.fillText(num1,x1-10,y1+105);
		var x_clothes1 = x1+90*Math.cos(Math.PI*(data[1]+2*data[0])/total)
		var y_clothes1 = y1+90*Math.sin(Math.PI*(data[1]+2*data[0])/total)-90
		context.fillText(clothes[1],x_clothes1-60,y_clothes1+120);
		context.fillText(num1,x_clothes1-10,y_clothes1+110);
		context.moveTo(x_clothes1-13,y_clothes1+112);
		context.lineTo(x_clothes1-3,y_clothes1+112);
		context.strokeStyle="black";
		context.stroke();
		if (den1 >= 10)
		{
			context.fillText(den1,x_clothes1-14,y_clothes1+122);
		}
		else
		{
			context.fillText(den1,x_clothes1-10,y_clothes1+122);
		}
		//context.fillText(clothes[2],x1-130,y1+30);
		context.fillText(clothes[2],x1+90*Math.cos(Math.PI*(data[2]+2*data[1]+2*data[0])/total)-38,y1+90*Math.sin(Math.PI*(data[2]+2*data[1]+2*data[0])/total));
		context.fillText(clothes[3],x1-120,y1-40);
		context.fillText(num2,x1-115,y1-30);
		context.moveTo(x1-118,y1-28);
		context.lineTo(x1-106,y1-28);
		context.strokeStyle="black";
		context.stroke();
		if (den2 >= 10)
		{
			context.fillText(den2,x1-119,y1-18);
		}
		else
		{
			context.fillText(den2,x1-115,y1-18);
		}
		//context.fillText(clothes[4],x1+85,y1-40);
		context.fillText(clothes[4],x1+90*Math.cos(Math.PI*(data[4]+2*data[3]+2*data[2]+2*data[1]+2*data[0])/total)+5,y1+90*Math.sin(Math.PI*(data[4]+2*data[3]+2*data[2]+2*data[1]+2*data[0])/total));
		context.fillText("P",x1-105,y1+5);
		context.fillText("Q",x1+95,y1+5);

	}

	plotData();
}

function DrawPieChart3(data,colours,percent1,percent2,percent3)
{
	WindowReady();	

	function getTotal()
	{
		var total = 0;
		for (var j = 0; j < data.length; j++) {
		total += (typeof data[j] == 'number') ? data[j] : 0;
		}
		return total;
	}

	function plotData() 
	{
		//var rotate = Math.random()*Math.PI*2;
		var lastend = 0;
		var total = getTotal();
		context.lineWidth = 2;
	
		for (var i = 0; i < data.length; i++) 
		{
			context.fillStyle = colours[i];
			context.beginPath();
			context.moveTo(135,100);			
			context.arc(135,100,90,lastend,lastend+(Math.PI*2*(data[i]/total)),false);
			context.lineTo(135,100);
			context.strokeStyle="black";
			context.stroke();				
			context.fill();
			lastend += Math.PI*2*(data[i]/total);
		}
		x1 = 135;
		y1 = 100;

		context.beginPath();
		context.fillStyle = "black";
		//context.fillText(percent1+"%",x1-20,y1+80);
		context.fillText(percent1+"%",x1+90*Math.cos(Math.PI*(data[1]+2*data[0])/total)+10,y1+90*Math.sin(Math.PI*(data[1]+2*data[0])/total)-10);
		//context.fillText(percent2+"%",x1-80,y1+15);
		context.fillText(percent2+"%",x1+90*Math.cos(Math.PI*(data[2]+2*data[1]+2*data[0])/total)+10,y1+90*Math.sin(Math.PI*(data[2]+2*data[1]+2*data[0])/total));
		//context.fillText(percent3+"%",x1-80,y1-10);
		context.fillText(percent3+"%",x1+90*Math.cos(Math.PI*(data[3]+2*data[2]+2*data[1]+2*data[0])/total)+10,y1+90*Math.sin(Math.PI*(data[3]+2*data[2]+2*data[1]+2*data[0])/total)+10);

		context.fillText("A",x1-105,y1+5);
		context.fillText("B",x1+95,y1+5);
	}
	plotData();
}
