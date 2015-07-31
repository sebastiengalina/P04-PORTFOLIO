$(document).ready(function() {
	$(".contact-toggle").click(function() {
		$("#footer-main").removeClass("active");
		$("#footer-main").addClass("active").delay(1000).queue(function() {
			$(this).removeClass("active").dequeue();
		});
	});
});