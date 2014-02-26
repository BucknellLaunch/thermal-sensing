var fs = require('fs');
var path = require('path');
var aplist = require('../private/aplist.json');   // cache the AP list
var locations = undefined;                        // cache the locations

function getLocation(req, res) {
  accessPoint = req.query.ap;

  if (!accessPoint) {
    res.location('/');
    res.redirect('/');
    return;
  }

  var data = { accessPoint: accessPoint };

  data.location = aplist[accessPoint];
  if (!data.location) {
    data.location = 'Unknown';
    data.errors = ['Could not determine location.'];
  }

  res.send(data);
}

function allLocations(req, res) {
  var locationsPath = path.join(__dirname, '../private/locations');
  if (!locations) locations = fs.readFileSync(locationsPath);
  res.type('text/plain');
  res.send(locations);
}


module.exports.controller = function(app) {
	app.get('/api/location', getLocation);
  app.get('/api/locations', allLocations);
}