#Import the necessary methods from tweepy library
import tweepy
import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
import csv
import json
#Variable that contain user credentials to access Twitter API
access_token="my-key"
access_token_secret="my-key"
consumer_key="my-key"
consumer_secret="my-key"

#Handles twitter authentication and connects to twitter Stream API
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
fields = "id id_str screen_name location description url followers_count friends_count listed_count created_at \
    favourites_count verified \
    statuses_count lang default_profile status default_profile_image has_extended_profile name Bot".split()

data=pd.read_csv('MLData.csv')
data['Class'].value_counts().plot(kind='bar')
for index,row in data.iterrows():
    row['Screen name']=row['Screen name'].replace('@','')

csvFile = open('Data_ML_project.csv', 'a')
w=csv.DictWriter(csvFile,fields)
i=0
for index,row in data.iterrows():
    user = api.get_user(screen_name = row['Screen name'])
    d={}
    for k in set(user._json.keys()).intersection(fields):
            d[k]=str(getattr(user,k))
    if row['Class']=="Bot":
        d['Bot']=1
    else:
        d['Bot']=0
    if i==0:
        w.writeheader()
        i=1
    w.writerow(d)
#for f in fields:
#    print (user.id)
#print (user)
#print(df)
#df.to_csv('results.csv')




