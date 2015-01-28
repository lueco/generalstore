#!/usr/bin/python  
#-*-coding:utf-8-*- 
#start from 2012300101
#end in 2012303607
import urllib2
import urllib
import cookielib
import re
import chardet
import threading
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class mainLoop(threading.Thread):
	thread_stop = 0
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		global worm
		while Grade < 201430:
			while ID < 3700:
				flag = 0
		        StuId = Grade*10000+ID
		        req=urllib2.Request(searchurl,PostDate(StuId),headers)
		        result = opener.open(req)
		        string = result.read()
		        texturl = textGET.findall(string)[1]
		        for item in texturl:
		            if "text" in item:
		                texturl = item
		                break
		        req=urllib2.Request(texturl,PostDate(StuId),headers)
		        result = opener.open(req)
		        string = result.read()
		        if len(string)>600:
					conWorm.acquire()
					if worm >= 10:
						conWorm.wait()
					else:
						while worm < 10:
							result = opener.open(req)
							worm11 = Worm(result)
							worm11.start()
					conWorm.release()
		        ID=ID+1
			ID = 1
		Grade = Grade+100

class Worm(threading.Thread):
	def __init__(self,t_result):
		threading.Thread.__init__(self)
		self.result = t_result

	def run(self):
		global worm
		global rsufile
		global	errfile
		worm = worm +1
        string = self.result.read()
        texturl = textGET.findall(string)[1]
        for item in texturl:
            if "text" in item:
                texturl = item
                break
        req=urllib2.Request(texturl,PostDate(StuId),headers)
        result = opener.open(req)
        string = result.read()
        if len(string)>600:
            result = opener.open(req)
            string = result.readline()
            string = result.readline()
            string = result.readline()
            string = result.readline()
            clname = string.split("\t")[1]
            sumre_b = 0
            sumre_l = 0
            sumcr_b = 0
            sumcr_l = 0
            while string:
                if '\xcc\xe5\xd3\xfd' in string or '\xb4\xf3\xd1\xa7\xd3\xa2\xd3\xef' in string:
                    item    = string.split("\t")
                    name    = item[0]
                    cr1     = float(item[4])
                    re1     = float(item[5])
                    status1 = item[7]
                    time1   = int(item[8][0:6])
                    if '\xcc\xe5\xd3\xfd' in name or '\xb4\xf3\xd1\xa7\xd3\xa2\xd3\xef' in name and re1 >= 60:
                        sumre_b = sumre_b+cr1*re1
                        sumcr_b = sumcr_b+cr1
                        if 201309 <= time1:
                            sumre_l = sumre_l+cr1*re1
                            sumcr_l = sumcr_l+cr1
                    if len(item)>=14 and flag !=1:
                        if item[14]:
                            name2   = item[10]
                            cr2     = float(item[14])
                            re2     = float(item[15])
                            status2 = item[17]
                            time2   = int(item[18][0:6])
                            if '\xcc\xe5\xd3\xfd' in name2 or '\xb4\xf3\xd1\xa7\xd3\xa2\xd3\xef' in name2 and re2 >= 60:
                                sumre_b = sumre_b+cr2*re2
                                sumcr_b = sumcr_b+cr2
                                if 201309 <= time2:
                                    sumre_l = sumre_l+cr2*re2
                                    sumcr_l = sumcr_l+cr2
                    else:
                        flag = 1
                if '\xb1\xd8\xd0\xde' in string or '\xcf\xde\xd1\xa1' in string:
                    item    = string.split("\t")
                    cr1     = float(item[4])
                    re1     = float(item[5])
                    status1 = item[7]
                    time1   = int(item[8][0:6])
                    if re1 >= 60 and ('\xb1\xd8\xd0\xde' == status1 or '\xcf\xde\xd1\xa1' == status1):
                        sumre_b = sumre_b+cr1*re1
                        sumcr_b = sumcr_b+cr1
                        if 201309 <= time1:
                            sumre_l = sumre_l+cr1*re1
                            sumcr_l = sumcr_l+cr1
                    if len(item)>=14 and flag !=1:
                        if item[14]:
                            cr2     = float(item[14])
                            re2     = float(item[15])
                            status2 = item[17]
                            time2   = int(item[18][0:6])
                            if re2 >= 60  and ('\xb1\xd8\xd0\xde' == status2 or '\xcf\xde\xd1\xa1' == status2):
                                sumre_b = sumre_b+cr2*re2
                                sumcr_b = sumcr_b+cr2
                                if 201309 <= time2:
                                    sumre_l = sumre_l+cr2*re2
                                    sumcr_l = sumcr_l+cr2
                    else:
                        Flag = 1
                string = result.readline()
            if sumre_b !=0 and sumcr_b !=0 and sumre_l !=0 and sumcr_l !=0 and flag !=1:
                GPA_B = sumre_b/sumcr_b
                GPA_L = sumre_l/sumcr_l
                rsufile.writelines('%d %s %.2f %.2f\n'%(StuId,clname,GPA_B,GPA_L))
            else:
                errfile.writelines('%d\n'%StuId)
		conWorm.acquire()
		conWorm.notify()
		conWorm.release()


def PostDate(StuId):
    data={
        "LS_XH":StuId,
        "resultPage":"http://222.24.192.69:80/reportFiles/cj/cj_zwcjd.jsp?"
    }
    post_data=urllib.urlencode(data)
    return post_data;

def getINFO(info):
    print info


headers ={
    "Host":"222.24.192.69", 
    "Referer": "http://222.24.192.69/reportFiles/cj/cj_zwcjd.jsp"
}
loginurl = 'http://222.24.192.69/loginAction.do?dlfs=mh&mh_zjh=2012302611&mh_mm=GQGQHT'
searchurl = 'http://222.24.192.69/setReportParams'
it = re.compile(r'<tr([^<>\/].+?)</tr>')
textGET = re.compile(r'src = "([^<>\/].+?)"')
iSfemale = r'<td class="report1_2_1">Ů</td>'

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
opener.open(loginurl)
Grade = 201130
ID = 1
rsufile = open("result",'w')
errfile = open("error.log","w")


conWorm = threading.Condition()
worm = 0
main = mainLoop()

main.start()
main.join()
