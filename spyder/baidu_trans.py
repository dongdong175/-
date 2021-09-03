'''
百度翻译的破解，但只能翻译单词或短语，无法翻译长句子
(阿贾克斯命令)
'''

import requests
import json

# 1.获取url
youdao_url = 'https://fanyi.baidu.com/sug'
# 2.进行UA伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68'}
# 3.参数处理
i = input('请输入需要翻译的内容：')
data = {'kw':i}
# 4.发送请求
response = requests.post(url = youdao_url, data = data, headers = headers)
# 5.接受数据
obj = response.json()
#json.loads(obj)
print(obj['data'][0])