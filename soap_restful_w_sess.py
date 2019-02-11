#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests.auth import HTTPBasicAuth
import urllib
import requests

req_payload = {'key': 'value'}

enc_payload = urllib.urlencode(req_payload)

basic_auth = HTTPBasicAuth('Username', 'Password')

headers = {
    "Host": "web.mywebsite.com",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Content-Length": str(len(enc_payload))
}

sess = requests.Session()

res = sess.post('http://web.mywebsite.com/LPI/mywebsite/lpi.asmx/GetMyList')

cookies = dict(res.cookies)

res = sess.post(url="http://web.mywebsite.com/LPI/mywebsite/lpi.asmx/GetMyList",
               auth=basic_auth,
               headers=headers,
               data=enc_payload,
               cookies=cookies,
               verify=False)

print(res.content)
