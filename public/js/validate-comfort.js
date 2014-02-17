$('.error').hide();

var comfortForm = $(document.forms['comfort']);
comfortForm.submit(function(event) {
	$('.error').hide();

	var shouldProceed = true;
	var level = $('input:radio[name=level]:checked').val();
	var location = $('input[name=location]').val();

	if (!level) {
		$('#level-error').show();
		shouldProceed = false;
	} else if (!parseInt(level) || (level > 3 || level < -3)) {
		// No need to display an error. If a user submits a level in the
		// wrong range, they are likely doing it from a CLI not a browser.
		shouldProceed = false;
	}

	if (location == "") {
		$('#location-error').show();
		shouldProceed = false;
	}

	if (shouldProceed) {
		$.post(comfortForm.attr('action'));
	} else {
		return false;
	}
});