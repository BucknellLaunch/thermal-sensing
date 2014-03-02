# Data HTTP POST Requests


## Overview
The thermal sensing data API will send comfort data to a database server based on the parameters passed to the service. This document describes the protocol used to send data to the server.


## Location
The application root is assumed to be `sensing.bucknell.edu` but may be subject to change.

This is a RESTful API. The endpoint is `/`

---

## Requests
The API can be accessed by sending an HTTP request to the endpoint with various parameters. The parameters are listed below with a brief description. All parameters are required. Each user will have access to a unique API key* that he may use to access the API. Parameters can be specified via the query string in the HTTP request.

\* *At this point the key functionality is not implemented (requests can be made without it)*


### Parameters

* `key` **required** the API key unique to each user 
* `location` **required** the location to send data for
* `level` **required** the level of comfort 

These parameters are independent and can be mixed and matched. All parameters must be specified.  A more detailed explanation of the parameters with examples can be found below.

#### Key
Used to authenticate yourself with the API. 

`/key=AIzaSyAc67jazYdlcMitH7omJ3B9RhqpYN6k1W4`


#### Location
This parameter specifies the location to send data for. The location can be specified in the format "building-floor-room" or "building-floor". The data sent will be specific to that location.

`/location=dana-1-134`

`/location=breakiron-2`


#### Level
This parameter is an integer between -3 and 3 (inclusive). 

`/level=3` Sends a data point with a level of +3

---


## Response
The response of an API call will be a JSON object. The JSON object will either contain a thank you message or a message describing the error.


### Success
On success, a JSON object will be returned containing a thank you message. An example:

```
{
	"message": "We've received your feedback. Thanks for participating!"
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
