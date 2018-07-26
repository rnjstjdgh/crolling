#daum실검 크롤링->daum 메인 창에서 일단 실검 1~10까지 크롤링해서 순위별로 dict로 묶어두자
from bs4 import BeautifulSoup
import requests as rq

url_main_p='https://www.daum.net/'  #daum main page url
res_main_p=rq.get(url_main_p)
soup_main=BeautifulSoup(res_main_p.text,'html.parser')

#print(soup_main)
dic={} #순위와 내용을 메핑시킬 dict선언 {'rank':'content'}

result=soup_main.find('div',{'class':'hotissue_mini'})  #실검 관련 테크로 접근
#print(result)

contents=result.find_all('a',{'class':'link_issue'})

for i in range(1,11):
    dic[i]=contents[i-1].text

print(dic)
