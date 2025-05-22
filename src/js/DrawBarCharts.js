var canvasWidth = 500;
var canvasHeight = 350;


//global variable
var context;
window.DivID = '0';

function SetDivID(DivID)
{
	window.DivID = DivID;
}

function WindowReady(canvasWidth,canvasHeight)
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
function P4DrawBarGraph1(MaxNumber,Interval, Bars, BarHeights, BarNames, YAxisLabel, XAxisLabel, BarColours)
{
	WindowReady(500,250);
	var MaxNumber = MaxNumber;
	var Interval = Interval;
	var Bars = Bars;
	var ChartHeight = 180;
	var ChartWidth = 420;

	var x1 = 50;
	var y1 = 20;
	context.beginPath();
	context.lineWidth = 1;
	context.moveTo(x1,y1);
	context.lineTo(x1,y1+ChartHeight);
	context.lineTo(x1+ChartWidth,y1+ChartHeight);	
	context.strokeStyle="black";
	context.stroke();
	
	context.beginPath();
	context.lineWidth = 0.5;
	var HorizontalLineInterval = ChartHeight/(MaxNumber/Interval);

	// Drawing lines
	for (i=0;i<(MaxNumber/Interval);i++)
	{
		context.moveTo(x1-7,y1+i*HorizontalLineInterval);
		context.lineTo(x1+ChartWidth,y1+i*HorizontalLineInterval);
	}
	
	for (i=0;i<=MaxNumber;i++)
	{
		context.moveTo(x1,y1+i*HorizontalLineInterval/Interval);
		context.lineTo(x1-5,y1+i*HorizontalLineInterval/Interval);
	}
	context.strokeStyle="black";
	context.stroke();
	
	//Drawing bars
	var SpaceBetweenBars = 30;
	var BarsWidth = (ChartWidth-Bars*SpaceBetweenBars)/Bars;

	x1 = x1 + SpaceBetweenBars/2;	
	var HeightUnit = ChartHeight / MaxNumber;
	
	for (i=0;i<Bars;i++)
	{
		//drawing the dotted lines
		if(BarHeights[i][1]==1)
		{
			context.moveTo(x1+i*(BarsWidth+SpaceBetweenBars),y1+ChartHeight-HeightUnit*BarHeights[i][0]);
			context.dashedLine(x1+i*(BarsWidth+SpaceBetweenBars),y1+ChartHeight-HeightUnit*BarHeights[i][0],50,y1+ChartHeight-HeightUnit*BarHeights[i][0],4);
			context.strokeStyle="black";
			context.stroke();
		}
 
		context.beginPath();
		context.fillStyle = eval(BarColours)[i];
		context.fillRect(x1+i*(BarsWidth+SpaceBetweenBars),y1+ChartHeight,BarsWidth,-HeightUnit*BarHeights[i][0]);
		context.fill();
	}
	
	//y-axis
	x1 = 50;
	y1 = 25;
	for (i=0;i<=(MaxNumber/Interval);i++)
	{
		context.fillStyle = "black"; 
		context.fillText(MaxNumber-i*Interval,x1-20,y1+i*HorizontalLineInterval);
	}
	
	//x-axis
	x1 = x1 + SpaceBetweenBars/2;
	
	for (i=0;i<Bars;i++)
	{
		context.fillStyle = "black"; 
		context.fillText(eval(BarNames)[i],x1+i*(BarsWidth+SpaceBetweenBars),y1+ChartHeight+10,BarsWidth);
	}
	
	//Y-axis label (writing it vertical)
	var x1 = 50;
	var y1 = 20;
	context.save();
	context.translate(x1, y1+ChartHeight/2);  
	context.rotate(-Math.PI/2);  
	context.textAlign = "center";  
	context.fillText(eval(YAxisLabel)[0], 0, -40);  
	context.restore(); 
	
	//X-axis label
	var xaxis = eval(XAxisLabel)[0];
	context.fillText(xaxis,x1+(ChartWidth-xaxis.length)/2,y1+ChartHeight+35);
}

function P3DrawBarGraph1(MaxNumber,Interval, Bars, BarHeights, BarNames, YAxisLabel, XAxisLabel, BarColours, BarTitle)
{
	WindowReady(500,420);
	var MaxNumber = MaxNumber;
	var Interval = Interval;
	var Bars = Bars;
	var ChartHeight = 330;
	var ChartWidth = 420;

	var x1 = 50;
	var y1 = 60;
	context.beginPath();
	context.lineWidth = 1;
	context.moveTo(x1,y1);
	context.lineTo(x1,y1+ChartHeight);
	context.lineTo(x1+ChartWidth,y1+ChartHeight);	
	context.strokeStyle="black";
	context.stroke();
	
	context.beginPath();
	context.lineWidth = 0.5;
	var HorizontalLineInterval = ChartHeight/(MaxNumber/Interval);

	// Drawing lines
	for (i=0;i<(MaxNumber/Interval);i++)
	{
		context.moveTo(x1-7,y1+i*HorizontalLineInterval);
		context.lineTo(x1+ChartWidth,y1+i*HorizontalLineInterval);
	}
	
	for (i=0;i<=MaxNumber;i+=Interval/2)
	{
		context.moveTo(x1,y1+i*HorizontalLineInterval/Interval);
		context.lineTo(x1-5,y1+i*HorizontalLineInterval/Interval);
	}
	context.strokeStyle="black";
	context.stroke();
	
	//Drawing bars
	var SpaceBetweenBars = (ChartWidth-20)/(Bars*2);
	//var BarsWidth = (ChartWidth-Bars*SpaceBetweenBars)/Bars;
	var BarsWidth = SpaceBetweenBars;
	
	x1 = x1 + SpaceBetweenBars;	
	var HeightUnit = ChartHeight / MaxNumber;
	
	for (i=0;i<Bars;i++)
	{		
		//drawing the dotted lines
		if(BarHeights[i][1]==1)
		{
			context.moveTo(x1+i*(BarsWidth+SpaceBetweenBars),y1+ChartHeight-HeightUnit*BarHeights[i][0]);
			context.dashedLine(x1+i*(BarsWidth+SpaceBetweenBars),y1+ChartHeight-HeightUnit*BarHeights[i][0],50,y1+ChartHeight-HeightUnit*BarHeights[i][0],4);
			context.strokeStyle="black";
			context.stroke();
		}

		context.beginPath();
		context.fillStyle = eval(BarColours)[i];
		context.fillRect(x1+i*(BarsWidth+SpaceBetweenBars),y1+ChartHeight-1,BarsWidth,-HeightUnit*BarHeights[i][0]);
		context.fill();


	}
	
	//y-axis
	x1 = 50;
	y1 = 60;
	for (i=0;i<=(MaxNumber/Interval);i++)
	{
		context.fillStyle = "black"; 
		context.font = "10pt Calibri";
		context.textAlign = "right"; 
		context.fillText(MaxNumber-i*Interval,x1-10,y1+i*HorizontalLineInterval);
	}
	
	//x-axis
	x1 = x1 + SpaceBetweenBars;
	
	for (i=0;i<Bars;i++)
	{
		context.fillStyle = "black";
		context.font = "10pt Calibri";
		context.textAlign = "center"; 
		context.fillText(eval(BarNames)[i],x1+i*(BarsWidth+SpaceBetweenBars)+BarsWidth/2,y1+ChartHeight+15,BarsWidth);
	}
	
	//Y-axis label (writing it vertical)
	var x1 = 50;
	var y1 = 25;
	context.save();
	context.translate(x1, y1+ChartHeight/2);  
	context.rotate(-Math.PI/2);  
	context.textAlign = "center";  
	context.font = "11pt Calibri";
	context.fillText(eval(YAxisLabel)[0], -30, -40);  
	context.restore(); 
	
	//X-axis label
	var xaxis = eval(XAxisLabel)[0];
	context.fillText(xaxis,x1+(ChartWidth-xaxis.length)/2,y1+ChartHeight+35);
	
	//bar title
	context.font = "bold 14pt Calibri";
	context.fillText(BarTitle,x1+(ChartWidth/2),y1);
	
}


function P3DrawBarGraph2(MaxNumber,Interval, Bars, BarHeights, BarNames, YAxisLabel, XAxisLabel, BarColours,BarTitle)
{
	WindowReady(500,430);
	var MaxNumber = MaxNumber;
	var Interval = Interval;
	var Bars = Bars;
	var ChartHeight = 320;
	var ChartWidth = 420;

	var x1 = 50;
	var y1 = 60;
	context.beginPath();
	context.lineWidth = 1;
	context.moveTo(x1,y1);
	context.lineTo(x1+ChartWidth,y1);
	context.moveTo(x1,y1+ChartHeight);
	context.lineTo(x1,y1+ChartHeight);
	context.lineTo(x1+ChartWidth,y1+ChartHeight);
	context.lineTo(x1+ChartWidth,y1);
	context.strokeStyle="black";
	context.stroke();
	
	context.beginPath();
	context.lineWidth = 0.5;
	var VerticalLineInterval = ChartWidth/(MaxNumber/Interval);

	// Drawing lines
	for (i=0;i<(MaxNumber/Interval);i++)
	{
		context.moveTo(x1+i*VerticalLineInterval,y1);
		context.lineTo(x1+i*VerticalLineInterval,y1+ChartHeight+7);
	}
	
	for (i=0;i<=MaxNumber;i+=Interval/2)
	{
		context.moveTo(x1+i*VerticalLineInterval/Interval,y1+ChartHeight);
		context.lineTo(x1+i*VerticalLineInterval/Interval,y1+ChartHeight+5);
	}
	context.strokeStyle="black";
	context.stroke();
	
	//Drawing bars
	var SpaceBetweenBars = 30;
	var BarsWidth = (ChartHeight-Bars*SpaceBetweenBars)/Bars;

	//x1 = x1 + SpaceBetweenBars/2;
	y1 = y1 - SpaceBetweenBars/2;
	var HeightUnit = ChartWidth / MaxNumber;
	
	for (i=0;i<Bars;i++)
	{
		//drawing the dotted lines
		if(BarHeights[i][1]==1)
		{
			context.moveTo(x1+HeightUnit*BarHeights[i][0],y1+ChartHeight-i*(BarsWidth+SpaceBetweenBars));
			context.dashedLine(x1+HeightUnit*BarHeights[i][0],y1+ChartHeight-i*(BarsWidth+SpaceBetweenBars),x1+HeightUnit*BarHeights[i][0],y1+ChartHeight+14,4);
			context.strokeStyle="black";
			context.stroke();
		}
 
		context.beginPath();
		context.fillStyle = eval(BarColours)[i];
		context.fillRect(x1+1,y1+ChartHeight-i*(BarsWidth+SpaceBetweenBars),HeightUnit*BarHeights[i][0],-BarsWidth);
		context.fill();
	}
	
	//y-axis
	x1 = 50;
	y1 = 60;
	for (i=0;i<=(MaxNumber/Interval);i++)
	{
		context.fillStyle = "black"; 
		context.fillText(MaxNumber-i*Interval,x1+ChartWidth-i*VerticalLineInterval-7,y1+ChartHeight+18);
	}
		
	//x-axis
	y1 = y1 - SpaceBetweenBars;
	
	for (i=0;i<Bars;i++)
	{
		context.fillStyle = "black"; 
		context.font = "10pt Calibri";
		context.textAlign = "right"; 
		
		context.fillText(eval(BarNames)[i],x1-5,y1+ChartHeight-i*(BarsWidth+SpaceBetweenBars),BarsWidth+15);
	}
	
	//Y-axis label (writing it vertical)
	var x1 = 50;
	var y1 = 40;
	context.save();
	context.translate(x1, y1+ChartHeight/2);  
	context.rotate(-Math.PI/2);  
	context.textAlign = "center";  
	context.font = "12pt Calibri";
	context.fillText(eval(YAxisLabel)[0], 0, -40);  
	context.restore(); 
	
	//X-axis label
	var xaxis = eval(XAxisLabel)[0];
	context.font = "12pt Calibri";
	context.textAlign = "center";
	context.fillText(xaxis,x1+(ChartWidth)/2,y1+ChartHeight+60);
		
	//bar title
	context.font = "bold 14pt Calibri";
	context.fillText(BarTitle,x1+(ChartWidth/2),y1);
	
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