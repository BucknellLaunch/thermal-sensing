
/*
 * GET home page.
 */

function index(req, res) {
	res.render('index', { title: 'Thermal Sensing' });
}

function thanks(req, res) {
	res.render('thanks', { title: 'Thanks!' });
}

// Module exports
exports.index = index;
exports.thanks = thanks;