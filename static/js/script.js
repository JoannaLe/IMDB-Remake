$(document).ready(function(){
	$(".clickable").click(function() {
		console.log('hello');
		console.log($(this).data("href"));
		window.location = "/details/" + $(this).data("href") + "/";
	});

	$(".delete").click(function() {
		$("#movie-update").val() = $(this).attr("input")
		console.log(movie)
		window.location = "/delete/" + movie;
	});

	$(".update").click(function() {
		$("#movie-update").val() = $(this).attr("input")
		console.log(movie)
		window.location = "/update/" + movie;
	});

});