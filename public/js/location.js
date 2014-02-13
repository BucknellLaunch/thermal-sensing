function getAccessPoints() {
	// fetch from the server
}

function extractAP(rawHtml) {
	// TODO implement this method
	return undefined;
}

$(document).ready(function ($) {
	$.ajax({
		url: 'http://yamaha.bucknell.edu/cgi-bin/client_status.pl',
		dataType: 'html',
		success: function(data) {
			accessPoints = getAccessPoints();
			userAP = extractAP(data);
			location = accessPoints[userAP];
			form = document.forms['comfort'];
			form.elements['location'].value = location;
		},
		error: function(reqObj, err, exception) {
			$connectionError = $(
				'<div class="alert alert-warning error">'
				+'<p>'
				+'<strong>WARNING</strong> '
				+'Connect to WiFi to improve your location.'
				+'</p>'
				+'</div>');
			$('#content').prepend($connectionError);
		}
	});
});