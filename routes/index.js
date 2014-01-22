
/*
 * GET home page.
 */

function index(req, res) {
	res.render('index', { title: 'Thermal Sensing' });
}

function recordcomfort(db) {
	return function(req, res) {
		// TODO
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
exports.index = index;
exports.recordcomfort = recordcomfort;
exports.records = records;