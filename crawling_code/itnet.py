from selenium import webdriver
import pymongo
import pandas as pd
import requests
import warnings

warnings.simplefilter("ignore")
#Techcrunch
def get_crunch(page):
    from selenium import webdriver
    import time
    import pandas as pd
    
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    url = 'http://www.itworld.co.kr/search/?q=AI'
    driver.get(url)
       
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
    
    #preview 뽑아내기
    preview_list = []
    for article in articles:
        preview = article.find_element_by_css_selector(" div.gsc-table-result > div.gsc-table-cell-snippet-close > div.gs-bidi-start-align.gs-snippet").text


        preview_list.append(preview)
    preview=pd.DataFrame(preview_list,columns=['preview'])
    
    result=pd.concat([title, link, preview], axis=1) #axis=1 은 열 !!! 
   
    driver.quit()
    return result

# 자동으로 일정 페이지 크롤링해줘서 데이터프레임 만들어주기
def Tech_crunch(startpage, endpage):
    import pandas as pd
    df=pd.DataFrame([])
    for i in range(startpage, endpage+1):
        temp=get_crunch(i)
        df= pd.concat([df,temp],axis=0)
    #index 번호 다시 매기기
    df.reset_index(drop=True, inplace=True)
    return df

final_df2= Tech_crunch(1,2)
final_df2.to_csv("csv_files/Tech_crunch.csv", index=False, encoding='utf-8' )
