import pymongo
import pandas as pd
import requests
from selenium import webdriver



#ZDNET

# 함수로 만들기
def get_articles(page):
    url = 'http://www.zdnet.co.kr/newskey/?lstcode=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&page={}'.format(page)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    d = webdriver.Chrome('./',chrome_options=chrome_options)
    d.get('url')

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
    
    #이미지만 뽑아내기
    img_list = []
    for article in articles:
        img = article.find_element_by_css_selector("div.assetThumb > a > figure > img").get_attribute("src") 
        img_list.append(img)
    img=pd.DataFrame(img_list,columns=['img'])
    
    result=pd.concat([img, title, link], axis=1)
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
      
final_df= zd_net(1,5)
final_df.to_csv("zd_net.csv", index=False, encoding='utf-8' )

# 데이터베이스 서버 연결
client = pymongo.MongoClient("mongodb://15.165.1.169:27017/")
client

#컬렉션 삭제
client.crawling.drop_collection("news_db")

# 데이터 베이스와 컬렉션 생성
#서버.데이터베이스.컬렉션
news_db = client.crawling.news_db
news_db

# csv파일로 불러오고 싶을때
# zd_net_df=pd.read_csv("zd_net.csv",encoding="utf-8")

#딕셔너리형태로 만들어주는 함수
items= final_df.to_dict("records")

#mongodb에 insert
ids=news_db.insert(items)

#TECHCRUNCH
# 함수로 만들기
def get_articles(page):
    from selenium import webdriver
    import time
    import pandas as pd

    url = 'http://www.itworld.co.kr/search/?q=AI'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    d = webdriver.Chrome('./',chrome_options=chrome_options)
    d.get('url')
  
    driver.find_element_by_xpath("""//*[@id="___gcse_0"]/div/div/div/div[5]/div[2]/div[1]/div/div[2]/div/div[%s]""" %page).click()
    time.sleep(1)
    
    
    
    #여러데이터 모으기
    articles = driver.find_elements_by_css_selector("#___gcse_0 > div > div > div > div.gsc-wrapper > div.gsc-resultsbox-visible > div.gsc-resultsRoot.gsc-tabData.gsc-tabdActive > div > div.gsc-expansionArea > div > div.gs-webResult.gs-result")
    
    
    #제목
    title_list = []
    for article in articles:
        title = article.find_element_by_css_selector("div.gsc-thumbnail-inside > div > a").text 
        title_list.append(title)
    title =pd.DataFrame(title_list, columns=['title'])
    
   
    #링크만 뽑아내기
    link_list = []
    for article in articles:
        link = article.find_element_by_css_selector("div.gsc-url-top > div.gs-bidi-start-align.gs-visibleUrl.gs-visibleUrl-long").text
        link_list.append(link)
    link= pd.DataFrame(link_list, columns=['link'])
    
    #이미지만 뽑아내기
    img_list = []
    for article in articles:
        img = article.find_element_by_css_selector("div.gsc-table-cell-thumbnail.gsc-thumbnail > div > a > img").get_attribute("src") 
        
        
        img_list.append(img)
    img=pd.DataFrame(img_list,columns=['img'])
    
    result=pd.concat([img, title, link], axis=1) #axis=1 은 열 !!! 
   
    driver.quit()
    return result

# 자동으로 일정 페이지 크롤링해줘서 데이터프레임 만들어주기
def Tech_crunch(startpage, endpage):
    import pandas as pd
    df=pd.DataFrame([])
    for i in range(startpage, endpage+1):
        temp=get_articles(i)
        df= pd.concat([df,temp],axis=0)
    #index 번호 다시 매기기
    df.reset_index(drop=True, inplace=True)
    return df


final_df= Tech_crunch(1,5)
final_df.to_csv("Tech_crunch.csv", index=False, encoding='utf-8' )

# 데이터베이스 서버 연결
client = pymongo.MongoClient("mongodb://15.165.1.169:27017/")
client


# 데이터 베이스와 컬렉션 생성
#서버.데이터베이스.컬렉션
news_db = client.crawling.news_db
news_db

# csv파일로 불러오고 싶을때
# zd_net_df=pd.read_csv("zd_net.csv",encoding="utf-8")

#딕셔너리형태로 만들어주는 함수
items= final_df.to_dict("records")

#mongodb에 insert
ids=news_db.insert(items)




