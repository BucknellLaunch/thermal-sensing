var express = require('express');
var fs = require('fs');
var path = require('path');

var app = express.createServer(express.logger());

app.configure(function() {
  app.use(express.static(path.join(__dirname, '/public')));
});

app.get('/', function(request, response) {
  var index_data = fs.readFileSync(path.join(__dirname, '/public/index.html')).toString('utf8');
  response.send(index_data);
});


var port = process.env.PORT || 8080;
app.listen(port, function() {
  console.log("Listening on " + port);
});
