/*
 * Functions for recording comfort level and getting records
 */

function recordcomfort(db) {
	return function(req, res) {
		
		// Make sure we have good input
		req.assert('level', "You need to select a comfort level!").notEmpty();
		req.assert('location', "You can't leave your location blank!").notEmpty();
		var errors = req.validationErrors();

		if (errors) {
			// Render the index and display the errors
			res.render('index', {
				title: 'Thermal Sensing',
				errors: errors
			});
		}
		else {
			// Get form values. We need the comfort level and location
			var level = parseInt(req.body.level);
			var location = req.body.location;
			var now = new Date();

			// Set the collection
			var collection = db.get('comfort');

			// Submit to the DB
			collection.insert({
				"level": level,
				"location": location,
				"timestamp": now.toJSON()
			}, function (e, doc) {
				if (e) {
					res.send("There was an error adding to the DB");
				}
				else {
					res.location('/thanks');
					res.redirect('/thanks');
				}
			});
		}
	}
}

function records(db) {
	return function(req, res) {
		var collection = db.get('comfort');
		collection.find({}, {}, function(e, docs) {
			res.render('records', { title: 'Records', records: docs });
		});
	}
}

// Module exports
exports.recordcomfort = recordcomfort;
exports.records = records;