
### TITLE : 은평구 아파트단지 시세조회 자동화
***
### Tools
***
![개발툴](https://user-images.githubusercontent.com/111418728/191774218-c5e6419d-28da-48d2-8d29-a6f176a16a87.jpg)
***
### Structure
---
*  README.md   : 가이드
*  urls.txt    : 크롤링 사이트 주소 (네이버 부동산)
*  crawlling.py : 크롤링 수집 파일 (Ajax형태의 동단위 아파트단지 시세데이터를 함수화 하여 모아둔 모듈)
*  preprocessing.py  : 데이터 전처리 파일

   (Request,Pandas,Json라이브러리를 이용 크롤링한 데이터를 데이터프레임화 시킨후 Rename매서드를 사용하여 컬럼들을 한글로 바꾸어줌,
                                         Replace매서드를 사용하여 불필요한 문자들을 제거해줌,
                                         최종 전처리한 데이터를 to_excel매서드를 사용하여 엑셀파일로 저장함
*  bot_start.py : 텔레그램 봇 자동화 파일 (텔레그램 외부 라이브러를 이용 텔레그램 어플리케이션에서 봇을 이용하여 해당지역의 시세조회가 가능하게 함)

* >Legion : 크롤링된 데이터들이 xlsx형식으로 저장되는 폴더
* >\Mod : 텔레그램 토큰 보관 폴더
* >\Mod\telegram_config : 텔레그램 토큰 키 보관 파일 
***
### Telegram Bot Name : autoMIN
