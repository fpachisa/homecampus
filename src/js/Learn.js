function CreateVideoLink(videoID)
{ 		
            var VideoLink = '<object><param name="movie" value="http://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=1&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
    		VideoLink = VideoLink + '<embed src="http://www.youtube.com/v/';
            VideoLink = VideoLink + videoID;
    		VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=1&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
            return VideoLink;
}

function PrepareVideo(VideoID)
{
    if (VideoID != '')
    	{
    		$("#HomeTV").html(CreateVideoLink(VideoID));
    		$("#HomeTV").show("fast");
    	}
	
}

$(document).ready(function(){
	
	/*Open Learn section images in new tab when clicked --to provide better experience on mobile devices
	$(".hc-ans .img-thumbnail").on("click", function(evt){
		evt.preventDefault();
		var url = $(this).attr("src");
		window.open( url, '_blank');
	});
	*/
});