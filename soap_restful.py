#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests.auth import HTTPBasicAuth
import urllib
import requests

req_payload = {'facilityOrigin': 'ALL'}

enc_payload = urllib.urlencode(req_payload)

basic_auth = HTTPBasicAuth('myname', 'myname password')

headers = {
    "Host": "web.mywebsite.com",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Content-Length": str(len(enc_payload))
}

res = requests.post(url="http://web.mywebsite.com/LPI/mywebsite/lpi.asmx/GetMyList",
                    auth=basic_auth,
                    headers=headers,
                    data=enc_payload,
                    verify=False)

print(res.content)


'''
$ nc -kl 8888
res = requests.post(url="http://localhost:8888",
                    auth=basic_auth,
                    headers=headers,
                    data=enc_payload,
                    verify=False)

'''
