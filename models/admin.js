var encrypt = require('../lib/encrypt');
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var adminSchema = new Schema({
	name: {
		first: 	String,
		last: 	String
	},
  email: 			{ type: String, required: true, index: { unique: true } },
  pwhash: 		{ type: String, required: true },
  salt:  			String
});

Admin.virtual('id').get(function() {
	return this._id.toHexString();
});

Admin.virtual('name.full').get(function() {
	return this.name.first + ' ' + this.name.last;
});

Admin.virtual('password').set(function(password) {
	this.salt = encrypt.makeSalt();
	this.pwhash = encrypt.makePasshash(this.email, password, this.salt);
});


// Should people be able to get the password?
Admin.virtual('password').get(function() {
	return this.pwhash + ',' + this.salt;
});

var Admin = mongoose.model('Admin', adminSchema);

module.exports = Admin;