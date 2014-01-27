
/**
 * Module dependencies.
 */

var express = require('express');
var routes = require('./routes');
var comfort = require('./routes/comfort');
var http = require('http');
var path = require('path');
var expressValidator = require('express-validator');

// db connection
var mongo = require('mongodb');
var monk = require('monk');
var db = monk('localhost:27017/tsense');

var app = express();

// all environments
app.set('port', process.env.PORT || 8080);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.json());
app.use(express.urlencoded());
app.use(expressValidator());					// middleware for form validation
app.use(express.methodOverride());
app.use(express.cookieParser('your secret here'));
app.use(express.session());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

app.get('/', routes.index);
app.post('/', comfort.recordcomfort(db));
app.get('/thanks', routes.thanks);
app.get('/records', comfort.records(db));

http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});
