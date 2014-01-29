/* Admin routes */

function rickshaw(req, res) {
	res.render('rickshaw', { title: 'Rickshaw Example'});
}

// Module exports
exports.rickshaw = rickshaw;