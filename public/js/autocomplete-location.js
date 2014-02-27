var locationForm = document.getElementById('autocomplete');

var auto = completely(locationForm, {
  name: 'location',
	className: 'location-input form-control',
  placeholder: 'Where are you?'
});

$.ajax({
  url: '/api/locations',
  dataType: 'json',
  success: function(options) {
    auto.onChange = function(text) {
      if (text.length == 0) {
        auto.options = [];
      } else {
        auto.options = options;
      }
      auto.repaint();
      return;
    }
    setTimeout(function() {
      auto.input.focus();
    }, 0);
  },
  error: function(errorObj) {
    console.log('errr nerrrr');
  }
});