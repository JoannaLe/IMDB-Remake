$(document).ready(function(){
	autoComplete();

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

	$("#search").click(function() {
		v = $("#song-input").val();
		$("#song-input2").val(v);
		console.log("song searched")
	});

});

function autoComplete() {
	console.log('hello');
	let songs = [
      "Let It Go",
      "City of Stars",
      "Can\'t Help Falling in Love",
      "Sweet Home Alabama",
      "Kung Fu Fighting",
      "Stayin\' Alive",
      "What a Wonderful World",
      "For the First Time in Forever",
      "How Does A Moment Last Forever",
      "Fools Who Dream",
      "For Forever",
      "Somewhere in the Crowd",
	];

	$(".song-input").autocomplete({
		source: songs
	});

}