var mongoose = require('mongoose');
var Key = require('../models/key');
var encrypt = require('../lib/encrypt');

/*
 * Displays the index page that allows the user to
 * input comfort level and location
 */
function index(req, res) {
	// Make the unique key first
	secretKey = encrypt.generateKey()
  res.render('index', {
  	title: 'Thermal Sensing',
  	key: secretKey
  });

  var key = new Key({ value: secretKey });
  key.save(function (err) {
  	if (err) { console.log('ERROR SAVING KEY!'); }
  });
}

function accessPoints(req, res) {
	// TODO read in the access points
	res.send('this will be a list of access points');
}

module.exports.controller = function(app) {
	app.get('/', index);
	app.get('/api/aplist', accessPoints);
}