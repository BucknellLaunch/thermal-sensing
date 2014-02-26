# Data HTTP GET Requests

---

## Overview
The thermal sensing data API will return comfort data to a building administrator based on the parameters passed to the service. This document describes the protocol used to send data to the server and to return a response to the client.


## Location
The application root is assumed to be `sensing.bucknell.edu` but may be subject to change.

This is a RESTful API. The endpoint is `/api/data`

---

## Requests
The API can be accessed by sending an HTTP request to the endpoint with various parameters. The parameters are listed below with a brief description. All parameters are optional with the exception of key. A building administrator will have access to a unique API key* that he may use to access the API. Parameters can be specified via the query string in the HTTP request.

\* *At this point the key functionality is not implemented (requests can be made without it)*


### Parameters

* `key` **required** the API key unique to each admin -- found in the dashboard
* `location` **optional** the location to get data from
* `level` **optional** the level of comfort (can be specified as a range)
* `from` **optional** the time to go from
* `to` **optional** the time to go to
* `resolution` **optional** used to specify the resolution of the data (eg. weekly)

These parameters are independent and can be mixed and matched. No parameters can be specified (resulting in all data points being returned), all parameters can be specified (to get a fine level of control over the data returned), or any combination may be specified. A more detailed explanation of the parameters with examples can be found below.



#### Key
Used to authenticate yourself with the API. The key can be found in the admin dashboard.

`/api/data?key=AIzaSyAc67jazYdlcMitH7omJ3B9RhqpYN6k1W4`


#### Location
This parameter specifies the location to get data from. The location can be specified in the format "building-floor-room", "building-floor", or "building". The resulting data will be specific to that location.

`/api/data?location=dana-1-134`

`/api/data?location=breakiron-2`

`/api/data?location=coleman`


#### Level
This parameter is an integer between -3 and 3 (inclusive). A single level can be specified, or a range can be used. To use a range, prepend the character `g` or `l` to indicate greater than or less than, respectively.

`/api/data?level=3` Gets all data points with a level of +3

`/api/data?level=g-2` Gets all data points with a level > -2

`/api/data?level=l0` Gets all data points with a level < 0


#### Data Range
The `from` and `to` parameters can be used to specify a date range -- both, one, or neither can be provided. The dates are given in the format "MM-DD-YYYY", "MM-YYYY", or "YYYY".

`/api/data?from=01-2014` Get all data points starting with Jan 2014

`/api/data?to=02-16-2014` Get all data points from the beginning of time to Feb 16, 2014

`/api/data?from=2013&to=02-2014` Get all data points in the range Jan 1, 2013 to Feb 2014


#### Resolution
This parameter specifies the resolution of the data. Data points can be smoothed (averaged) over a given range. The acceptable values for this parameter are "hourly", "daily", "weekly", "monthly", and "yearly". If no parameter is specified, all data points will be returned in the response.

`/api/data?resolution=weekly`

This call will return all data points grouped by location with the level being an average of all of the data points for that location in a given week.*

\* *This functionality will be implemented later*

---


## Response
The response of an API call will be a JSON object. The JSON object will either contain a list of results or an error code accompanied by a message describing the error.


### Success
On success, a JSON object will be returned containing a list of results. Each result in the list will be of the form:

```
{
	"location": {
		"building": "dana",
		"floor": 1,
		"room":	134
		},
	"level": -2,
	"timestamp": "2014-02-25T21:59:09.828Z"
}
```


### Error
On error, the JSON object will contain the error value and a message describing what went wrong. An example:

```
{
	"error": 436,
	"message": "Location specified in an invalid format."
}
```
