#!/usr/bin/python  
#-*-coding:utf-8-*- 
import re
import chardet
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def readhtml(offset):
	htmlfile = open("./face/"+str(offset)+".html")
	string = htmlfile.read()
	return string


picmatch = re.compile(r'img data-src="([^<>\/].+?)"')
urlmatch = re.compile(r'target="_blank" href="([^<>\/].+?)"')
idmatch = re.compile(r'id=([^<>\/].+?)&')
offset = 0
while offset < 50:
	string = readhtml(offset)
	pic = picmatch.findall(string)
	url = urlmatch.findall(string)
	nu = 0
	while nu < 10:
		rrid = idmatch.findall(url[nu])[0]
		print 'INSERT INTO `npuface`.`rrface` (`id`, `picurl`, `rrid`) VALUES (NULL, \''+pic[nu]+'\','+str(rrid)+') ON DUPLICATE KEY UPDATE `rrid` = '+str(rrid)+' ;'
		nu = nu+1
	offset = offset+1