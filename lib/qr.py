from urllib2 import Request, URLError, urlopen

BASEURL = 'http://api.qrserver.com/v1/create-qr-code'

COLORS = {
	'black': '000000',
	'red': 'FF0000',
	'blue': '0000FF'
}

def colors():
	return [COLORS[color] for color in COLORS]

def __buildQueryString(**params):
	urlParams = ["%s=%s" % (key, value) for key, value in params.iteritems()]
	return '?%s' % ('&'.join(urlParams))

def generateQR(url, size, color=COLORS['black']):
	urlString = BASEURL + __buildQueryString(data=url, size=size, color=color)

	request = Request(urlString)
	qr_png = None
	try:
		response = urlopen(request)
		qr_png = response.read()
	except URLError, e:
		print 'No png, got error code: ' + e
	finally:
		return qr_png