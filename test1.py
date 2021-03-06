#daum실검 크롤링->그 데이터를 쿼리스트링으로 넘겨서 1위부터 10위까지 사이트로 순차접근->접근한 사이트에서 각각 정보 획득(까페 제목3개/ 블로그 개시글 제목 3개 등등...)
from bs4 import BeautifulSoup
import requests as rq

#dau실검 1~10까지 dict로 반환해주는 함수 구현
def crol_RealTimeContents():
    url_main_p = 'https://www.daum.net/'  # daum main page url
    res_main_p = rq.get(url_main_p)
    soup_main = BeautifulSoup(res_main_p.text, 'html.parser')
    # print(soup_main)
    dic = {}  # 순위와 내용을 메핑시킬 dict선언 {'rank':'content'}
    result = soup_main.find('div', {'class': 'hotissue_mini'})  # 실검 관련 테크로 접근
    # print(result)
    contents = result.find_all('a', {'class': 'link_issue'})
    for i in range(1, 11):
        dic[i] = contents[i - 1].text
    return dic

dic=crol_RealTimeContents()
print(dic)
print("="*300)




for j in dic.values():
    print('='*100+j+'='*100)
    # url에 q부분에 실검 내용을 포함시키면 그 주소로 이동함!
    url_search = 'https://search.daum.net/search?w=tot&DA=ATG'
    res1 = rq.get(url_search, params={'q': j})
    soup_search = BeautifulSoup(res1.text, 'html.parser')
    #print(soup_search.prettify())  # prettify-> html code를 좀더 보기 쉽게 만들기
    # 블로그 개시글 재목 4개 가져오기
    route_bolg_title = soup_search.find('div', {'id': 'blogColl'})
    bolg_title = route_bolg_title.find_all('a', {'class': 'f_link_b'})
    blog_title_list=[]
    print("<bolg title>")
    for i in bolg_title:
        print(i.text)
        blog_title_list.append(i.text)
    # 뉴스 개시글 재목 가져오기
    route_news_title = soup_search.find('div', {'id': 'newsColl'})
    news_title = route_news_title.find_all('a', {'class': 'f_link_b'})
    news_title_list=[]
    print('<news title>')
    for i in news_title:
        print(i.text)
        news_title_list.append(i.text)
    # 관련 검색어 가져오기
    route_relevant_content = soup_search.find('div', {'id': 'netizenColl_right'})
    relevant_content = route_relevant_content.find_all('span', {'class': 'txt_keyword'})
    relevant_content_list=[]
    print('<relevant title>')
    for i in relevant_content:
        print(i.text)
        relevant_content_list.append(i.text)
