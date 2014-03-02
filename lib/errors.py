def error(code, msg):
	return { 'error': code, 'message': msg }


# Error messages
INVALID_KEY_MSG = "Invalid API key."

INVALID_LOCATION_FORMAT_MSG = """
Invalid location format. Specify the location in either '<building>-<floor>-<room>',
'<building>-<floor>', or '<building>' format."""

INVALID_LEVEL_MSG = "Invalid level. Please specify a level in the range [-3, 3]"
INVALID_LEVEL_QUALIFIER_MSG = """
Invalid level inequality qualifier. Specify either 'g' or 'l' to get a level in
the range > or <, respectively. Eg. level=g1 returns comfort records with a level
> 1"""

INVALID_DATE_FORMAT_MSG = """
Invalid date format. Specify a date with the format 'MM-DD-YYYY', 'MM-YYYY', or
'YYYY'"""


# Errors
INVALID_KEY = error(431, INVALID_KEY_MSG)
INVALID_LOCATION_FORMAT = error(441, INVALID_LOCATION_FORMAT_MSG)
INVALID_LEVEL = error(451, INVALID_LEVEL_MSG)
INVALID_LEVEL_QUALIFIER = error(452, INVALID_LEVEL_QUALIFIER_MSG)
INVALID_DATE_FORMAT = error(461, INVALID_DATE_FORMAT_MSG)