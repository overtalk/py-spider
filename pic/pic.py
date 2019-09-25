import requests

url = 'http://image.nationalgeographic.com.cn/2017/1122/20171122113404332.jpg'

f = open('./1.png', 'wb')  # 打开文件
f.write(requests.get(url).content)
f.close()
