$(document).ready(function ($) {
	$.ajax({
		url: 'http://yamaha.bucknell.edu/cgi-bin/client_status.pl',
		dataType: 'html',
		headers: {
			Origin: 'http://bucknell.edu'
		},
		success: function() {
			console.log('got dat data');
		}
	});
});