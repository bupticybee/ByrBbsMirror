# -*-coding: utf-8 -*-
from time import sleep

__author__ = 'icybee'

import  urllib2, urllib
import cookielib


def post(url, data):  
    req = urllib2.Request(url)  
    data = urllib.urlencode(data)  
    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    opener.addheaders.append(('Cookie', 'nforum[UTMPUSERID]=notahacker2; nforum[UTMPKEY]=47086690; nforum[UTMPNUM]=4149; nforum[PASSWORD]=85pdI27XmRI9pdWLe%2Fk6CQ%3D%3D; Hm_lvt_a2cb7064fdf52fd51306dd6ef855264a=1472200699; Hm_lpvt_a2cb7064fdf52fd51306dd6ef855264a=1472974880'))
    response = opener.open(req, data)  
    return response.read()  

def reply(board,articleid,subject,reply):  
    posturl = "http://m.byr.cn/article/%s/post/%s" % (board,articleid)  
    data = {'content':reply,'subject':subject}  
    result = post(posturl, data)  
    if '请休息几秒后再试' in result:
	print 'failed'
    else:
        print 'success'
  
if __name__ == '__main__':  
    main()  

