#Import the necessary methods from tweepy library
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


access_token1="296764651-exhifySpL5spZ8S5LXbyq2UUe8yEdpEPua5KRP2W"
access_token_secret1="xlaX9OpwftHS1IK1c6IV6r7rx2woCC4AUshNQrdoO0J8Q"
consumer_key1="LAFkdEGGA2nU1menu7eBIU6Kt"
consumer_secret1="uNIDRBqqZ06aOq0wFQks6j7rwJbI1CrUTyTcRjlHQRLPFra6RA"

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

data=pd.read_csv('Data/test_data_4_students.csv')        
#data['bot'].value_counts().plot(kind='bar')
#for index,row in data.iterrows():
#    row['Screen name']=row['Screen name'].replace('@','')

csvFile = open('test_data1.csv', 'a')
w=csv.DictWriter(csvFile,labels)
i=0

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