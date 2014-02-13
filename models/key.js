/*
 * This is the model for an api-key. A key will be created when the user
 * loads the front page of the application that will allow it to communicate
 * with the server on the backend and receive private data (eg. list of 
 * access points).
 */
var encrypt = require('../lib/encrypt');
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var keySchema = new Schema({
  value: { type: String, default: encrypt.generateKey },
  created: { type: Date, default: Date.now, expires: 60 }
});

var Key = mongoose.model('Key', keySchema);

module.exports = Key;