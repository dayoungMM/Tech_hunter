from selenium import webdriver
import pymongo
import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings

warnings.simplefilter("ignore")

#Techcrunch
def get_itworld(page):
    from selenium import webdriver
    import pymongo
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    import warnings

    warnings.simplefilter("ignore")
    
    url= 'http://www.itworld.co.kr/t/54649/%EB%B9%85%20%EB%8D%B0%EC%9D%B4%ED%84%B0?page={}'.format(page)
    domain = 'http://www.itworld.co.kr'

    response= requests.get(url)
    # 2. BeautifulSoup을 이용하여 css selector를 사용할 수 있는 객체로 파싱
    # dom은 HTML 전체를 뷰티풀숩이 객체로 가져온것
    dom = BeautifulSoup(response.content, "html.parser")
    articles =dom.select('.news_list_')
    
    datas = []

    for article in articles:
        try:
            preview = article.select_one('.news_list_has_thumb_size > .news_body_summary').text.replace("\n", "").replace("\t", "").strip()
        except:
            preview = article.select_one('.news_list_full_size > .news_body_summary').text.replace("\n", "").replace("\t", "").strip()
        datas.append({
            "title" : article.select_one('div > h4 > a').text,
            "link" : domain + article.select_one('div > h4 > a')['href'],
            "preview": preview
        })

    bigdata_df = pd.DataFrame(datas)
    return bigdata_df

# 자동으로 일정 페이지 크롤링해줘서 데이터프레임 만들어주기
def Tech_itworld(startpage, endpage):
    import pandas as pd
    df=pd.DataFrame([])
    for i in range(startpage, endpage+1):
        temp=get_itworld(i)
        df= pd.concat([df,temp],axis=0)
    #index 번호 다시 매기기
    df.reset_index(drop=True, inplace=True)
    return df

final_df2= Tech_itworld(1,2)
final_df2.to_csv("csv_files/itworld_bigdata.csv", index=False, encoding='utf-8' )