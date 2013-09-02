#!/usr/bin/python

#process images from folder
#read into bytes
#post to webserver

from os import listdir
from os.path import isfile, join
import uploader
import time

from uploader import *

poster = Uploader()


mypath = "/usr/local/bin/imagedrop"

def post(item):
	poster.postfile(mypath + "/" + item)

while(True):
	
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	#print mypath
	print onlyfiles

	for item in onlyfiles:
		post(item)

	time.sleep(60)