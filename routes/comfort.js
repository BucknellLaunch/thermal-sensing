/*
 * Functions for recording comfort level and getting records
 */

function recordcomfort(db) {
	return function(req, res) {
		
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