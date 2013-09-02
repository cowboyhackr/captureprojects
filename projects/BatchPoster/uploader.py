import urllib2
import os
from poster.encode import multipart_encode, MultipartParam
from poster.streaminghttp import register_openers

class Uploader:
	"""Class to post image to server"""
	i = 12345
	def f(self):
		return 'hello world'
	def send(self):
		f = urlopen('http://www.google.com')
		return f.read(100)
	def test(self):
		return 'test hit'
	def postimage(self, data):
		# f = urlopen('http://www.google.com')
		d = data.encode('utf8')
		req = urlopen(url='http://google.com', data=d)
		print "poster.py"
	def postfile2(self, filepath):
                register_openers()
		print filepath
		filesize = os.path.getsize(filepath)
		print filesize
                #datagen, headers = multipart_encode({"file":open(filepath, "rb"),'Content-Length': str(filesize)})
		datagen, headers = multipart_encode({"file":open(filepath, "rb")})
                #req = urllib2.urlopen("http://www.webiste.com/sys/upload/save", datagen, headers)
                req = urllib2.Request("http://netduinoplus.azurewebsites.net/api/capture", datagen, headers)
                print urllib2.urlopen(req).read()
		os.unlink(filepath)
	def postfile_deletethis(self, filepath):
		register_openers()
		print filepath
		params = {'file': open(filepath, "rb"), 'name':'upload test'}
		datagen, headers = multipart_encode(params)
		req = urllib2.Request("http://netduinoplus.azurewebsites.net/api/capture", datagen, headers)
		print urllib2.urlopen(req).read()

	def postfile(self, filepath):
                register_openers()
		print filepath
		filesize = os.path.getsize(filepath)
		print filesize
                #datagen, headers = multipart_encode({"file":open(filepath, "rb"),'Content-Length': str(filesize)})
		datagen, headers = multipart_encode({"file":open(filepath, "rb")})
                req = urllib2.Request("http://netduinoplus.azurewebsites.net/api/capture", datagen, headers)

                print urllib2.urlopen(req).read()
		os.unlink(filepath)
		