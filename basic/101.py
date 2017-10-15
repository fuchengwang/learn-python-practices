"""
101. Write a Python program to access and print a URL's content to the console.
"""

from urllib import request


def use_urllib():
    url = 'http://ip.cn'
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    res = request.urlopen(req)
    text = res.read().decode('utf-8')

    print(text)


def use_http_client():
    from http.client import HTTPConnection
    conn = HTTPConnection('ip.cn', 80)
    conn.set_debuglevel(1)

    conn.connect()
    conn.putrequest('GET', '/')
    conn.putheader('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    conn.endheaders()
    res = conn.getresponse()
    print('\n', res.read().decode('utf-8'))
    conn.close()


use_http_client()
