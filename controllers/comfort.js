var mongoose = require('mongoose');
var Comfort = require('../models/comfort');

/*
 * Displays the index page that allows the user to
 * input comfort level and location
 */
function index(req, res) {
  res.render('comfort/index', { title: 'Thermal Sensing' });
}

/*
 * Displays a thank you page when a user completes
 * the comfort form.
 */
function thanks(req, res) {
  res.render('comfort/thanks', { title: 'Thanks!' });
}

/*
 * Posts and records a comfort. This will do error
 * checking on the form to make sure the field are
 * not blank.
 */
function recordComfort(req, res) {
  var comfort = new Comfort({
    level: parseInt(req.body.level),
    location: req.body.location
  });

  comfort.save(function(err) {
    if (err) {
      res.send("There was an error adding to the DB");
    } else {
      Comfort.findById(comfort, function (err, doc) {
        console.log(doc);
      });
      res.location('/thanks');
      res.redirect('/thanks');
    }
  });
}

/*
 * Lists all of the comforts. This is used only for
 * debugging and will not be available in the production
 * version.
 */
function records(req, res) {
  Comfort.find({}, function(err, docs) {
    res.render('comfort/records', { title: 'Records', records: docs });
  });
}


module.exports.controller = function(app) {
  app.get('/', index);
  app.post('/', recordComfort);
  app.get('/thanks', thanks);
  app.get('/records', records);
}