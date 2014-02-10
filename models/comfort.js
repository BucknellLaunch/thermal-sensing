var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var comfortSchema = new Schema({
  level:    	{ type: String, required: true },
  location: 	{ type: String, required: true },
  timestamp: 	{ type: Date, default: Date.now }
});

var Comfort = mongoose.model('Comfort', comfortSchema);

module.exports = Comfort;