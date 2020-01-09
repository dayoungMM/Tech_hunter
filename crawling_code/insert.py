import pymongo
import pandas as pd
import requests

# 데이터베이스 서버 연결
client = pymongo.MongoClient("mongodb://localhost:27017/")

# #컬렉션 삭제
client.crawling.drop_collection("news_db")
client.crawling.drop_collection("bigdata_db")

# 데이터 베이스와 컬렉션 생성
#서버.데이터베이스.컬렉션
news_db = client.crawling.news_db
bigdata_db = client.crawling.bigdata_db


final_df=pd.read_csv("csv_files/zd_net.csv",encoding="utf-8")
final_df2=pd.read_csv("csv_files/Tech_crunch.csv",encoding="utf-8")
final_df3=pd.read_csv("csv_files/zdnet_bigdata.csv",encoding="utf-8")
final_df4=pd.read_csv("csv_files/itworld_bigdata.csv",encoding="utf-8")
final_df5=pd.read_csv("csv_files/conference.csv",encoding="utf-8")


items1= final_df.to_dict("records")
items2= final_df2.to_dict("records")
items3= final_df3.to_dict("records")
items4= final_df4.to_dict("records")
items5= final_df5.to_dict("records")

ids=news_db.insert(items1)
ids=news_db.insert(items2)
ids=bigdata_db.insert(items3)
ids=bigdata_db.insert(items4)
ids=bigdata_db.insert(items5)
