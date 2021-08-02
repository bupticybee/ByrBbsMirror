# -*-coding: utf-8 -*-
from time import sleep
import redis
from redis import Redis
__author__ = 'icybee'
import  urllib2, urllib
import cookielib
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def post(url, data):
	req = urllib2.Request(url)
	data = urllib.urlencode(data)
	#enable cookie
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	opener.addheaders.append(('Cookie', 'nforum[UTMPUSERID]=notahacker2; nforum[UTMPKEY]=47086690; nforum[UTMPNUM]=4149; nforum[PASSWORD]=85pdI27XmRI9pdWLe%2Fk6CQ%3D%3D; Hm_lvt_a2cb7064fdf52fd51306dd6ef855264a=1472200699; Hm_lpvt_a2cb7064fdf52fd51306dd6ef855264a=1472974880'))
	response = opener.open(req, data)
	return response.read()

def api_reply(board,articleid,subject,reply):
	posturl = "http://m.byr.cn/article/%s/post/%s" % (board,articleid)
	data = {'content':reply,'subject':subject}
	result = post(posturl, data)
	if '请休息几秒后再试' in result:
		print 'failed'
		return False
	else:
		print 'success'
		return True

def testgetter():
	#r = Redis()
	r = Redis()
	p = r.pubsub()
	p.subscribe('post_reply')
	for message in p.listen():
		#message = re.sub(r"(,?)(\w+?)\s+?:", r"\1'\2' :", str(message));
		#message = message.replace("'", "\"");
		message = message['data']
		if not isinstance(message,str):
			continue
		msgjson = json.loads(str(message))
		board = msgjson['board']
		articleid = msgjson['articleid']
		subject = msgjson['title']
		reply = msgjson['reply']
		for i in range(5):
			result = None
			try:
				result = api_reply(board,articleid,subject,reply)
			except:
				pass
			if result:
				break
			sleep(5)

if __name__ == "__main__":
		testgetter()
