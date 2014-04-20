from zipfile import ZipFile, ZIP_DEFLATED
from StringIO import StringIO

def create_with_files(files):
	"""Creates a zip archive with the files in the list files. Each file in the list
	must be formatted as a tuple --> (filename, data)"""

	file_stream = StringIO()
	zf = ZipFile(file_stream, 'w', ZIP_DEFLATED)

	try:
		for file in files:
			filename, data = file
			zf.writestr(filename, data)
	finally:
		zf.close()
		file_stream.seek(0)
		return file_stream.getvalue()