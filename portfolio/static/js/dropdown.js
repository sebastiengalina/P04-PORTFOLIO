$(document).ready(function() {
	$("#menu .dropdown-toggle").click(function() {
		$("#menu .button-grid .grid").toggleClass("active");
	});

	$("#wrap, #footer-main, #menu .button-grid .btn").click(function() {
		$("#menu .button-grid .grid").removeClass("active");
	});
});