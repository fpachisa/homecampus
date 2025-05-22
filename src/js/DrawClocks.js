var canvasWidth = 150;
var canvasHeight = 150;
var clockImage;

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

}

function DrawClock1(hours,minutes)
{
	var clockRadius = 70;
	WindowReady();
	var hours = hours;
    var minutes = minutes;
    hours = hours > 12 ? hours - 12 : hours;
    var hour = hours + minutes / 60;
    var minute = minutes;

    // save current context
    context.save();
    
    context.translate(canvasWidth / 2, canvasWidth / 2);
    context.beginPath();

    // draw numbers
    context.font = '16px Arial';
    context.fillStyle = '#000';
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    for (var n = 1; n <= 12; n++) {
        var theta = (n - 3) * (Math.PI * 2) / 12;
        var x = clockRadius * 0.7 * Math.cos(theta);
        var y = clockRadius * 0.7 * Math.sin(theta);
        context.fillText(n, x, y);
    }

    // draw hour
    context.save();
    var theta = (hour - 3) * 2 * Math.PI / 12;
    context.rotate(theta);
    context.beginPath();
    context.moveTo(-5, -1.5);
    context.lineTo(-5, 1.5);
    context.lineTo(clockRadius * 0.4, 1);
    context.lineTo(clockRadius * 0.4, -1);
    context.fillStyle = 'red';
    context.fill();
    context.restore();

    // draw minute
    context.save();
    var theta = (minute - 15) * 2 * Math.PI / 60;
    context.rotate(theta);
    context.beginPath();
    context.moveTo(-5, -1);
    context.lineTo(-5, 1);
    context.lineTo(clockRadius * 0.6, 1);
    context.lineTo(clockRadius * 0.6, -1);
    context.fillStyle = '#0f0';
    context.fill();
    context.restore();
}

function get_random_color() 
{
	var colour_code = Math.floor(Math.random()*56);
	var colours = ["antiquewhite", "aqua", "aquamarine", "bisque", "burlywood", "chartreuse", "coral", "cornflowerblue", "cyan", "darkorange", "darksalmon", "darkseagreen", "darkturquoise", "deepskyblue", "dodgerblue", "fuchsia", "gold", "goldenrod", "green", "greenyellow", "hotpink", "khaki", "lawngreen", "lightcoral", "lightgreen", "lightpink", "lightsalmon", "lightskyblue", "lime", "limegreen", "magenta", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "orange", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "peachpuff", "plum", "powderblue", "royalblue", "salmon", "sandybrown", "seagreen", "skyblue", "springgreen", "tomato", "turquoise", "violet", "yellow", "yellowgreen"];
	return colours[colour_code];
}