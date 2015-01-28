#!/usr/bin/python  
#-*-coding:utf-8-*- 
#start from 2012300101
#end in 2012303607
import urllib2
import urllib
import cookielib
import re
import chardet
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def PostDate(StuId):
    data={
        "LS_XH":StuId,
        "resultPage":"http://222.24.192.69:80/reportFiles/cj/cj_zwcjd.jsp?"
    }
    post_data=urllib.urlencode(data)
    return post_data;

def getImage(addr,StuId):
    u = urllib.urlopen(addr)
    data = u.read()
    filename = [str(StuId),'.jpg']
    filename = ''.join(filename)
    f = open(filename, 'wb')
    f.write(data)
    f.close()


headers ={
    "Host":"222.24.192.69", 
    "Referer": "http://222.24.192.69/reportFiles/cj/cj_zwcjd.jsp"
}
loginurl = 'http://222.24.192.69/loginAction.do?dlfs=mh&mh_zjh=2012302611&mh_mm=GQGQHT'
searchurl = 'http://222.24.192.69/setReportParams'
picmatch = re.compile(r'img src="([^<>\/].+?)"')
iSfemale = r'<td class="report1_2_1">Ů</td>'

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
opener.open(loginurl)
StuId = 2010300001
while StuId < 2010303570:
    print StuId
    req=urllib2.Request(searchurl,PostDate(StuId),headers)
    result = opener.open(req)
    string = result.read()
    if iSfemale in string:
        if len(picmatch.findall(string))!=0:
            getImage(picmatch.findall(string)[0],StuId)
    StuId += 1