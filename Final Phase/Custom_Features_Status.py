import tweepy
import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
import csv
import json
#Variable that contain user credentials to access Twitter API
access_token="1705054591-UmF3EDjblZ7rknx7JKYmu716X2PTbiyoVv9Tcrr"
access_token_secret="fykQJomSAXCxVa3WDvGjWS61AOtofv8E7RRdSm5lil1eC"
consumer_key="SbciRjxB88YQZTxnfVvlfGrQR"
consumer_secret="waNX7roMCQoKxVXfRJYSg42uybrWKIMthxjoTVsPnXMRIBAio4"

#Handles twitter authentication and connects to twitter Stream API
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


data=pd.read_csv("test_data1.csv")

csvFile = open('status.csv', 'a')
columns="screen_name entities-hashtags entities-url source_url geo coordinates".split()
w=csv.DictWriter(csvFile,columns)
i=0
fields="status".split()
data=data[431:]
for index,row in data.iterrows():
    user = api.get_user(screen_name=row['screen_name'])
    d={}
    d['screen_name']=str(row['screen_name'])
    for k in set(user._json.keys()).intersection(fields):
            d['entities-hashtags']=str(getattr(user,k)._json['entities']['hashtags'])
            d['entities-url']=str(getattr(user,k)._json['entities']['urls'])
            d['source_url']=str(getattr(user,k).source_url)
            d['geo']=str(getattr(user,k).geo)
            d['coordinates']=str(getattr(user,k).coordinates)
    if i==0:
        w.writeheader()
        i=1   
    w.writerow(d)    
    
    