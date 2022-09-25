import requests
import json
import pandas as pd
import crawlling as cw

headers= {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
      } 


def crawl(url):
  res = requests.get(url, headers=headers)

  #크롤링한 데이터를 Json형태로 변환
  data = json.loads(res.text)
  items = data['result']

  #변환된 Json데이터를 DataFrame화
  df = pd.DataFrame.from_dict(items)
  df = df.rename(columns={'hscpNm':'단지명','dealPrcMin':'매매최저가','dealPrcMax':'매매최고가',
                        'leasePrcMin':'전세최저가','leasePrcMax':'전세최고가','useAprvYmd':'승인날짜'})

  #불필요한 문자들 정규식으로 삭제
  df["매매최저가"].replace("[a-z<='_>/]", "", regex=True, inplace = True) 
  df["매매최고가"].replace("[a-z<='_>/]", "", regex=True, inplace = True)
  df["전세최저가"].replace("[a-z<='_>/]", "", regex=True, inplace = True) 
  df["전세최고가"].replace("[a-z<='_>/]", "", regex=True, inplace = True)

  #원하는 DataFrame 컬럼을 뽑아온뒤 지역엑셀 파일로 저장
  P_list = df[['단지명','전세최저가','전세최고가','승인날짜','매매최저가','매매최고가']]

  return P_list

#지속적인 전처리 실행시 해당 사이트의 봇방지 프로그램 작동으로 전처리실행이 안될수 있음!!!

#수색동
su = crawl(cw.url_susaek)
su.to_excel('./Legion/수색.xlsx')

#갈현동
gal1 = crawl(cw.url_galhyun1)
gal2 = crawl(cw.url_galhyun2)
gal3 = crawl(cw.url_galhyun3)

#여러개의 데이터 프레임을 하나의 데이터프레임으로 병합
galdf = pd.concat([gal1, gal2, gal3], ignore_index = True)
galdf.to_excel('./Legion/갈현.xlsx')

#구산동
gu1 = crawl(cw.url_gusan1)
gu2 = crawl(cw.url_gusan2)
gu3 = crawl(cw.url_gusan3)
gudf = pd.concat([gu1, gu2, gu3], ignore_index = True)
gudf.to_excel('./Legion/구산.xlsx')

#녹번동
nok = crawl(cw.url_nokbun)
nok.to_excel('./Legion/녹번.xlsx')

#대조동
dae1 = crawl(cw.url_daejo1)
dae2 = crawl(cw.url_daejo2)
dae3 = crawl(cw.url_daejo3)
daedf = pd.concat([dae1, dae2, dae3], ignore_index= True)
daedf.to_excel('./Legion/대조.xlsx')

#불광동
bul1 = crawl(cw.url_bulkwang1)
bul2 = crawl(cw.url_bulkwang2)
bul3 = crawl(cw.url_bulkwang3)
bul4 = crawl(cw.url_bulkwang4)
bul5 = crawl(cw.url_bulkwang5)
buldf = pd.concat([bul1, bul2, bul3, bul4, bul5], ignore_index= True)
buldf.to_excel('./Legion/불광.xlsx')

#신사동
sinsa1 = crawl(cw.url_sinsa1)
sinsa2 = crawl(cw.url_sinsa2)
sinsa3 = crawl(cw.url_sinsa3)
sinsa4 = crawl(cw.url_sinsa4)
sinsa5 = crawl(cw.url_sinsa5)
sindf = pd.concat([sinsa1, sinsa2, sinsa3, sinsa4, sinsa5], ignore_index= True)
sindf.to_excel('./Legion/신사.xlsx')

#역촌동
yekchon1 = crawl(cw.url_yekchon1)
yekchon2 = crawl(cw.url_yekchon2)
yekchon3 = crawl(cw.url_yekchon3)
yekchon4 = crawl(cw.url_yekchon4)
yekchon5 = crawl(cw.url_yekchon5)
yekchon6 = crawl(cw.url_yekchon6)
yekdf = pd.concat([yekchon1, yekchon2, yekchon3, yekchon4, yekchon5, yekchon6], ignore_index= True)
yekdf.to_excel('./Legion/역촌.xlsx')

#응암동
engam1 =crawl(cw.url_engam1)
engam2 =crawl(cw.url_engam2)
engam3 =crawl(cw.url_engam3)
engam4 =crawl(cw.url_engam4)
engam5 =crawl(cw.url_engam5)
engam6 =crawl(cw.url_engam6)
engam7 =crawl(cw.url_engam7)
engam8 =crawl(cw.url_engam8)
engdf = pd.concat([engam1, engam2, engam3, engam4, engam5, engam6, engam7, engam8], ignore_index= True)
engdf.to_excel('./Legion/응암.xlsx')

#증산동
jeng1 = crawl(cw.url_jengsan1)
jeng2 = crawl(cw.url_jengsan2)
jeng3 = crawl(cw.url_jengsan3)
#jeng4 = crawl(cw.url_jengsan4)
jeng5 = crawl(cw.url_jengsan5)
#jeng6 = crawl(cw.url_jengsan6)
jeng7 = crawl(cw.url_jengsan7)
jeng8 = crawl(cw.url_jengsan8)
jeng9 = crawl(cw.url_jengsan9)
jengdf = pd.concat([jeng1, jeng2, jeng3, jeng5, jeng7, jeng8, jeng9], ignore_index= True)
jengdf.to_excel('./Legion/증산.xlsx')


#진관동
jin1 = crawl(cw.url_jinkwan1)
jin2 = crawl(cw.url_jinkwan2)
jin3 = crawl(cw.url_jinkwan3)
#jin4 = crawl(cw.url_jinkwan4)
jin5 = crawl(cw.url_jinkwan5)
#jin6 = crawl(cw.url_jinkwan6)
#jin7 = crawl(cw.url_jinkwan7)
jin8 = crawl(cw.url_jinkwan8)
jin9 = crawl(cw.url_jinkwan9)
jin10 = crawl(cw.url_jinkwan10)
jindf = pd.concat([jin1, jin2, jin3, jin5, jin8, jin9, jin10], ignore_index=True)
jindf.to_excel('./Legion/진관.xlsx')

