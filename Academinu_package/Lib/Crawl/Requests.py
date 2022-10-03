from urllib import response
import requests

response = requests.get("http://www.naver.com")
html = response.text
print(html)


