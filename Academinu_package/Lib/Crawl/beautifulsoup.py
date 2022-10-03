import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.naver.com/")
html = response.text
soup = BeautifulSoup(html, 'html.parser')

word = soup.select_one('#NM_set_home_btn')
print(word.text)