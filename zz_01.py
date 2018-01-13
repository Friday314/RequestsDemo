# 导入requests库
import requests

"""

ConnectionError异常，原因为网络问题（如DNS查询失败、拒绝连接等等...）
Requests.raise_for_status()抛出一个HTTPError异常，原因为HTTP请求返回了不成功的状态（如网页不存在，返回404）
Requests抛出一个Timeout异常，原因为请求超时
Requests抛出一个TooManyRedirects异常，原因为请求超过了设定的最大重定向次数

"""

"""

# requests方法。网络请求，如果返回结果是<200>,说明请求网址成功
# "http://bj.xiaozhu.com/" 北京小住网
res = requests.get("http://bj.xiaozhu.com/")

print(res)

print(res.text)

"""


# 北京小住网，网络访问过于频繁，已被限制访问  = =!  汗
# 头文件
_headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# 添加头文件访问网址
r = requests.get("http://bj.xiaozhu.com/", headers=_headers)

# 错误抛出  try...except

try:

    print(r.text)

except ConnectionError:      # 出现错误会执行下面的操作

    print("拒绝访问")
