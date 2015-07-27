$(document).ready(function() {
	$("#menu .dropdown-toggle").click(function() {
		$("#menu .button-grid .grid").toggleClass("active");
	});

	$("#wrap").click(function() {
		$("#menu .button-grid .grid").removeClass("active");
	});
});