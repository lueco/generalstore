#!/usr/bin/python  
#-*-coding:utf-8-*- 
import re
import chardet
import sys
reload(sys)
sys.setdefaultencoding('utf8')

old = open('1.sql','r')
new = open('2.sql','w')
result = list()
for line in open('1.sql'):
    line = old.readline()
    if "women_head" in line:
    	pass
    elif "men_head" in line:
    	pass
    else:
    	new.write(line)
old.close()
new.close()

