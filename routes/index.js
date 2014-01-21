
/*
 * GET home page.
 */

function index(req, res) {
	res.render('index', { title: 'Thermal Sensing' });
}

// Module exports
exports.index = index;