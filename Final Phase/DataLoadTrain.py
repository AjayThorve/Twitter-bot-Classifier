#Import the necessary methods from tweepy library
import tweepy
import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
import csv
import json
#Variable that contain user credentials to access Twitter API
access_token="USE YOUR API ACCESS CREDENTIALS"
access_token_secret="USE YOUR API ACCESS CREDENTIALS"
consumer_key="USE YOUR API ACCESS CREDENTIALS"
consumer_secret="USE YOUR API ACCESS CREDENTIALS"


access_token1="USE YOUR API ACCESS CREDENTIALS"
access_token_secret1="USE YOUR API ACCESS CREDENTIALS"
consumer_key1="USE YOUR API ACCESS CREDENTIALS"
consumer_secret1="USE YOUR API ACCESS CREDENTIALS"

#Handles twitter authentication and connects to twitter Stream API
#auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#auth.set_access_token(access_token,access_token_secret)

auth=tweepy.OAuthHandler(consumer_key1,consumer_secret1)
auth.set_access_token(access_token1,access_token_secret1)

api=tweepy.API(auth)
fields = "id id_str screen_name location description url followers_count friends_count listed_count created_at \
    favourites_count verified \
    statuses_count lang default_profile status default_profile_image has_extended_profile name Bot".split()


labels = "id id_str screen_name location description url followers_count friends_count listed_count created_at \
    favourites_count verified \
    statuses_count lang default_profile status default_profile_image has_extended_profile name Bot entities-hashtags \
    entities-url source_url geo coordinates".split()

data=pd.read_csv('Data/training_data_2_csv_UTF.csv')        
#data['bot'].value_counts().plot(kind='bar')
#for index,row in data.iterrows():
#    row['Screen name']=row['Screen name'].replace('@','')

csvFile = open('train_data1.csv', 'a')
w=csv.DictWriter(csvFile,labels)
i=0
#data=data[2595:]
data=data.head(900)     # 900 records each time to counter the 900 requests per 15 minute window by twitter api
for index,row in data.iterrows():
    try:
        user = api.get_user(screen_name = row['screen_name'])
        d={}
        for k in set(user._json.keys()).intersection(fields):
            if k=="status":
                d['entities-hashtags']=str(getattr(user,k)._json['entities']['hashtags'])
                d['entities-url']=str(getattr(user,k)._json['entities']['urls'])
                d['source_url']=str(getattr(user,k).source_url)
                d['geo']=str(getattr(user,k).geo)
                d['coordinates']=str(getattr(user,k).coordinates)
            else:
                d[k]=str(getattr(user,k))
        if row['bot']=="1":
            d['Bot']=1
        else:
            d['Bot']=0
        if i==0:
            w.writeheader()
            i=1
        w.writerow(d)
    except Exception as e:
        print (row['screen_name'],e)
        pass
#for f in fields:
#    print (user.id)
#print (user)
#print(df)
#df.to_csv('results.csv')
