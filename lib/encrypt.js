var crypto = require('crypto');

function makeSalt() {
	return Math.round(Date.now() * Math.random()) + '';
}

function generateKey() {
	salt = makeSalt();
	return crypto.createHmac('md5', salt).digest('hex');
}

module.exports.generateKey = generateKey;