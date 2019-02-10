#!/usr/bin/env python
# -*- coding: utf-8 -*-
from requests.auth import HTTPBasicAuth
import requests

# Please replace payload content and correct URL.
req_payload = u'''
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
      <GetMyList xmlns="http://ws.mywebsite.com/LPI">
        <facilityOrigin>{0}</facilityOrigin>
      </GetMyList>
    </soap:Body>
</soap:Envelope>
'''.format('ALL')

enc_payload = req_payload.encode('utf-8')

basic_auth = HTTPBasicAuth('myname', 'myname password')

headers = {
    "Host": "web.mywebsite.com",
    "Content-Type": "application/xml,text/xml,application/soap+xml;charset=utf-8",
    "Content-Length": str(len(enc_payload)),
    "SOAPAction": "http://ws.mywebsite.com/LPI/GetMyList"
}

res = requests.post(url="http://web.mywebsite.com/LPI/mywebsite/lpi.asmx",
                    auth=basic_auth,
                    headers=headers,
                    data=enc_payload,
                    verify=False)

print(res.content)
