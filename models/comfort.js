var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var comfortSchema = new Schema({
  level:    { type: String, required: true },
  location: { type: String, required: true },
  date:     { type: Date, default: Date.now }
});

var Comfort = mongoose.model('comfort', comfortSchema);

module.exports = Comfort;