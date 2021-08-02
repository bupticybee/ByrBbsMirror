# -*-coding: utf-8 -*-
from time import sleep

__author__ = 'pb'

import http.client
import urllib.parse

def request(url, cookie=''):
    ret = urllib.parse.urlparse(url)    # Parse input URL
    if ret.scheme == 'http':
        conn = http.client.HTTPConnection(ret.netloc)
    elif ret.scheme == 'https':
        conn = http.client.HTTPSConnection(ret.netloc)

    url = ret.path
    if ret.query: url += '?' + ret.query
    if ret.fragment: url += '#' + ret.fragment
    if not url: url = '/'

    #conn.request(method='GET', url=url , headers={'Cookie': cookie,'':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
    conn.request(method='GET', url=url , headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})
    return conn.getresponse()

if __name__ == '__main__':
    cookie_strs = ["""nforum[UTMPUSERID]=notahacker; nforum[UTMPKEY]=29938492; nforum[UTMPNUM]=4098; nforum[PASSWORD]=kZ2C%2FPnxDZDj83wdOguXDQ%3D%3D; Hm_lvt_a2cb7064fdf52fd51306dd6ef855264a=1461911480,1462106702,1462106821,1462951535; Hm_lpvt_a2cb7064fdf52fd51306dd6ef855264a=1464109087""","""nforum[UTMPUSERID]=notahacker; nforum[UTMPKEY]=76903706; nforum[UTMPNUM]=4098; nforum[PASSWORD]=kZ2C%2FPnxDZDj83wdOguXDQ%3D%3D; Hm_lvt_a2cb7064fdf52fd51306dd6ef855264a=1461911480,1462106702,1462106821,1462951535; Hm_lpvt_a2cb7064fdf52fd51306dd6ef855264a=1464109136""","""nforum[UTMPUSERID]=icybee; nforum[UTMPKEY]=91812778; nforum[UTMPNUM]=4111; nforum[PASSWORD]=seheEHFPSZZhAF0%2B8cuRcg%3D%3D; Hm_lvt_a2cb7064fdf52fd51306dd6ef855264a=1461911480,1462106702,1462106821,1462951535; Hm_lpvt_a2cb7064fdf52fd51306dd6ef855264a=1464109280"""]
    #url = 'https://bbs.byr.cn/'
    url = 'http://bbs.byr.cn/#!default'
    for i in range(1):
        for cookie_str in cookie_strs:
            cur = request(url, cookie_str).read().decode('utf-8','ignore')
            print(cur)
            break
