import pymongo
import pandas as pd
import requests
from selenium import webdriver

# 함수로 만들기
def get_articles(page):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome("/home/ubuntu/python3/notebook/Tech/chromedriver", options=options)
    url = 'http://www.zdnet.co.kr/newskey/?lstcode=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&page={}'.format(page)
    driver.get(url)
    #여러데이터 모으기
    articles = driver.find_elements_by_css_selector("body > div.contentWrapper > div > div.left_cont > section > div")
    
    #제목
    title_list = []
    for article in articles:
        title = article.find_element_by_css_selector("div.assetText > a > h3").text 
        title_list.append(title)
    title =pd.DataFrame(title_list, columns=['title'])
    
    #링크만 뽑아내기
    link_list = []
    for article in articles:
        link = article.find_element_by_css_selector("a").get_attribute("href")
        link_list.append(link)
    link= pd.DataFrame(link_list, columns=['link'])
    
    #상세내용 뽑아내기
    preview_list = []
    for article in articles:
        preview = article.find_element_by_css_selector("div.assetText > a > p").text
        preview_list.append(preview)
    preview=pd.DataFrame(preview_list,columns=['preview'])
    
    result=pd.concat([title, link,preview], axis=1)
    driver.quit()
    return result

# 자동으로 일정 페이지 크롤링해줘서 데이터프레임 만들어주기
def zd_net(startpage, endpage):
    import pandas as pd
    df=pd.DataFrame([])
    for i in range(startpage, endpage+1):
        temp=get_articles(i)
        df= pd.concat([df,temp],axis=0)
    #index 번호 다시 매기기
    df.reset_index(drop=True, inplace=True)
    return df
final_df= zd_net(1,2)      
final_df.to_csv("/home/ubuntu/python3/notebook/Tech/csv_files/zd_net.csv", index=False, encoding='utf-8' )

