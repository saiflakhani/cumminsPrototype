$(window).on("load resize ", function() {
	var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
	$('.tbl-header').css({'padding-right':scrollWidth});
	let canvas = document.getElementById('canvas');
	var context = canvas.getContext('2d');
	context.font='14px FontAwesome';
	context.fillText('\uF047',20,50);
  }).resize();