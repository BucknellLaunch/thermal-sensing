# Installation

To install and run this application, make sure you have [Google App Engine](https://developers.google.com/appengine/downloads) and Python version 2.7 installed. To install, it would be best to follow the instructions found in their documentation. Here is a brief version:

```
$ wget {google app engine download url}
$ unzip {zip file}

$ ~/developer
$ mv google_appengine ~/developer

# open up your bashrc and append the location to your path
# type "echo $PATH at the prompt and copy the output"
# in your .bashrc, add the following lines:
export PATH={whatever you got as output from echo}
PATH=$PATH:$HOME/developer/google_appengine
```

## Clone the repository

```
$ mkdir ~/src
$ cd ~/src
$ git clone https://github.com/jcomo/thermal-sensing.git
```

## Create the config.py file

```
$ cd ~/src/thermal-sensing
$ touch config.py
```

Use the following structure for the configuration. Parameters for you to fill in are denoted between double curly brackets. We don't recommend that you change the other parameters.

```
# file: config.py

app_config = {
	# Application parameters
	'debug': False,
	'SECRET_KEY': '{{ anything here -- keep this secret! }}',
	'hostname': '{{ hostname the app runs on (eg. sensing.bucknell.edu) }}',

	# Numerical parameters
	'submission_timeout': {{ timeout in minutes -- how often users should be able to submit }},
	'graph_refresh': {{ timeout in minutes  -- how often new graph data is fetched }},
	'data_api_max_results': {{ max number of records to display with the data api }},

	# Memcache keys
	'MC_LOCATIONS_KEY': 'LOCATIONS',
	'MC_GRAPH_DATA_KEY': 'GRAPH_DATA_'
}
```

## Run the server

```
$ screen
$ cd ~/developer/google_appengine
$ sudo python dev_appserver.py --host 0.0.0.0 --port 80 ~/src/thermal-sensing
```

Detach the screen with C-a C-d


## Adding the first admin

It is necessary to add an admin through the console to get up and running. After that,
control of the application can be controlled with the web interface (found at `/dashboard`).

```
cd ~/src/thermal-sensing
remote_api_shell.py -s localhost

# you will be prompted for an email and password
# simply enter any valid email address and leave the password blank

> from models import Admin
> a = Admin.register('username', 'password', display='display name')
> a.put()
> exit()
```

Now you will be able to access `/dashboard` to log in and control the application.