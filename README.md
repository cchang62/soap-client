# SOAP Client 

#### Fetch Http Request Header
Terminal: open http request listener
```sh
$ nc -kl 8888
```
Python: use request lib and send your request to above listner
```sh
# Please update requeset info.
res = requests.post(url="http://localhost:8888",
                    auth=basic_auth,
                    headers=headers,
                    data=enc_payload,
                    verify=False)
```



#### Ref.

* [Python - Zeep](https://python-zeep.readthedocs.io/en/master/) 
* [StackOverFlow - Soap Sample]
* [StackOverFlow - Python request with session](https://stackoverflow.com/questions/35516483/cookies-must-be-enabled-in-your-browser-python-requests)

[StackOverFlow - Soap Sample]: <https://stackoverflow.com/questions/15569330/making-a-soap-request-using-python-requests-module/26907113>

