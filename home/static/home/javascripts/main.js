function updateCountdown(){
	var currentVal = jQuery('#message').val();

	//140 is the max number of characters
	var remaining = 2500 - jQuery('#message').val().length;
	jQuery(".countdown").text(remaining);

	if(remaining <= 20 && remaining > 10){
		$(".countdown").addClass("warn");
	}else if(remaining <= 10 && remaining >= 0){
		$("#message").removeClass("highlight_text");
		$(".countdown").removeClass("warn");
		$(".countdown").addClass("superwarn");
		$('#submit').prop('disabled', false);
	}else if(remaining < 0){
		$("#message").addClass("highlight_text");
		$(".countdown").addClass("max-reached");
		$('#submit').prop('disabled', true); //To disabled
	}else{
		$(".countdown").attr("class", "countdown");
	}
}

jQuery(document).ready(function($){
	updateCountdown();
	$("#message").change(updateCountdown);
	$("#message").keyup(updateCountdown);
})