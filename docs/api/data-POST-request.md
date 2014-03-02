# Data HTTP POST Requests


## Overview
The thermal sensing data API will return comfort data to a building administrator based on the parameters passed to the service. This document describes the protocol used to send data to the server and to return a response to the client.


## Location
The application root is assumed to be `sensing.bucknell.edu` but may be subject to change.

This is a RESTful API. The endpoint is `/api/data`

---

## POST Requests
The API can be accessed by sending an HTTP POST request to the endpoint with various parameters. The parameters are listed below with a brief description. All parameters are **required** for a POST request. A building administrator will have access to a unique API key that he may use to access the API. Parameters can be specified via the query string in the HTTP request.


### Parameters

* `key` the API key unique to each admin -- found in the dashboard
* `location` the location to get data from
* `level` the level of comfort (can be specified as a range)

#### Key
Used to authenticate yourself with the API. The key can be found in the admin dashboard.

`/api/data?key=eg8095v60b29`


#### Location
This parameter specifies the location to get data from. The location must be specified in either "building-floor-room" or "building-floor" format.

`/api/data?location=dana-1-134`

`/api/data?location=o'leary-3`



#### Level
This parameter is an integer between -3 and 3 (inclusive).

`/api/data?level=3`


### Example
The following is an example POST request to record data in the application without accessing the Web UI.

`/api/data?key=eg8095v60b29&location=olin-2-254&level=-1`

---

## Response
The response of an API call will be a JSON object. The JSON object will contain a result or an error code accompanied by a message describing the error.


### Success
On a successful POST request, the JSON object returned will be the one that was added to the database.

```
{
	"location": {
		"building": "breakiron",
		"floor": 1,
		"room":	166
		},
	"level": 1,
	"timestamp": "2014-02-28T21:59:09.828Z"
}
```


### Error
On error, the JSON object will contain the error value and a message describing what went wrong. An example:

```
{
	"error": 451,
	"message": "Invalid level. Please specify a level in the range [-3, 3]"
}
```