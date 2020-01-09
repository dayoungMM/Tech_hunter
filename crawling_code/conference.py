# -*- coding: utf-8 -*-

# 함수로 만들기
def get_articles():
    import requests
    import re
    import pandas as pd
    from bs4 import BeautifulSoup
    
    url= 'http://conference.etnews.com/'

    response= requests.get(url)
    dom = BeautifulSoup(response.content, "html.parser")
    
    exchange = dom.select('body > div > main > div > ul ')
    
    
    
    #제목,일시,장소

    #제목,일시,장소

    title_list = []
    date_list = []
    place_list = []
    exchange_title = dom.select('body > div > main > div > ul > li > a > dl  ')


    for contents in exchange_title:
        content = contents.text.strip().split("\n")
        title = content[0]
        date = content[1]
        place = content[2]

        title_list.append(title)
        date_list.append(date)
        place_list.append(place)

    title = pd.DataFrame(title_list, columns=['title'])
    date = pd.DataFrame(date_list, columns=['date'])
    place = pd.DataFrame(place_list, columns=['place'])

    
    
    
    #링크 데이터프레임
    link_list = []
    exchange_link = dom.select('body > div > main > div > ul > li > a  ')

    for links in exchange_link:
        a = "http://conference.etnews.com/"
        link = (a+links.attrs['href'])
        link_list.append(link)
    link =pd.DataFrame(link_list, columns=['link'])

    
    
    
    
    #이미지 데이터프레임

    img_list = []
    exchange_img = dom.select('body > div > main > div > ul > li > a > dl > dd.thumb > img')

    for imgs in exchange_img:

        img = imgs.attrs['src']
        img_list.append(img)


    img =pd.DataFrame(img_list, columns=['img'])


    result=pd.concat([title, date, place, link, img], axis=1)
    
     
    return result

result = get_articles()

result.to_csv("/home/ubuntu/python3/notebook/Tech/csv_files/conference.csv", index=False, encoding='utf-8' )
