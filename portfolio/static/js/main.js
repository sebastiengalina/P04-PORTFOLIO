$(document).ready(function() {
	$(".header-well").hide();
	$("#wrap").hide();
	$("#footer-main").hide();
	console.log(".header-well was hidden");
	console.log("#wrap was hidden");
	console.log("#footer-main was hidden");

	$(".header-well").delay(500).slideDown();
	$("#wrap").delay(500).slideDown();
	$("#footer-main").delay(1000).fadeIn();

	console.log(".header-well was shown");
	console.log("#wrap was shown");
	console.log("#footer-main was shown");
});