var mongoose = require('mongoose');
var Key = require('../models/key');
var path = require('path');
var fs = require('fs');
var encrypt = require('../lib/encrypt');

/*
 * Displays the index page that allows the user to
 * input comfort level and location
 */
function index(req, res) {
	// Make the unique key first. If scaled in the future, this could be used
  // in tandem with memcache instead of writing to and reading from the database
  // upon accessing the home page.
	secretKey = encrypt.generateKey()
  res.render('index', {
  	title: 'Thermal Sensing',
  	key: secretKey
  });

  var key = new Key({ value: secretKey });
  key.save(function (err) {
  	if (err) console.log(err);
  });
}


function accessPoints(req, res) {
  secretKey = req.query.key;
  Key.findOneAndRemove({ value: secretKey }, function(err, key) {
    if (err || !key) {
      res.send({ error: "406", message: "Key not found"});
    }

    apListLoc = path.join(__dirname, '../private/aplist.json');
    fs.readFile(apListLoc, function (err, data) {
      if (err) console.log(err);
      res.send(data);
    });
  });
}


module.exports.controller = function(app) {
	app.get('/', index);
	app.get('/api/aplist', accessPoints);
}