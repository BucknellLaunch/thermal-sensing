var aplist = require('../private/aplist.json');   // cache the AP list

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


module.exports.controller = function(app) {
	app.get('/api/location', getLocation);
}