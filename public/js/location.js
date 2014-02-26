function getLocation(accessPoint) {
	var key = $('#key').text();
	var form = document.forms['comfort'];
	$.ajax({
		url: '/api/location?ap=' + accessPoint,
		dataType: 'json',
		success: function(data) {
			console.log(data);
			var location = data.location;
			if (!data.errors) form.elements['location'].value = location;
		},
		error: function(req, err, exception) {
			console.log("couldn't get user location");
		}
	});
}

function extractAP(rawHtml) {
	// TODO implement this method
}

$(document).ready(function ($) {
	$.ajax({
		url: 'http://yamaha.bucknell.edu/cgi-bin/bssid.cgi',
		dataType: 'text',
		success: function(data) {
			userAP = extractAP(data);
			getLocation(userAP);
		},
		error: function(req, err, exception) {
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