# 导入requests库
import requests

"""

# requests方法。网络请求，如果返回结果是<200>,说明请求网址成功
# "http://bj.xiaozhu.com/" 北京小住网
res = requests.get("http://bj.xiaozhu.com/")

print(res)

print(res.text)

"""

"""

北京小住网，网络访问过于频繁，已被限制访问  = =!  汗

_headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

_baidu = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

r = requests.get("https://www.baidu.com/", headers=_baidu)

print(r.text)

"""


