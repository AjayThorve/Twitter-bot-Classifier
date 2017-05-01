import pandas as pd
from dateutil import parser
import datetime
import math
pd.options.mode.chained_assignment = None  # default='warn'

def isNaN(num):
    return num != num

def Calculate_Decription_Days(data):
    data['desc_bot']=0
    data['desc_length']=0
    data['Age']=0
    data['loc']=1
    now=datetime.datetime.now()  #todays date
    data['description'] = data['description'].fillna('No Description')
    data['has_extended_profile'] = data['has_extended_profile'].fillna(False)
    data['verified'] = data['verified'].fillna(False)
    data['listed_count']=data['listed_count'].fillna(0)
    data['friends_count']=data['friends_count'].fillna(0)
    data['statuses_count']=data['statuses_count'].fillna(0)
    data['followers_count']=data['followers_count'].fillna(0)
    data['favourites_count']=data['favourites_count'].fillna(0)
    data['default_profile'] = data['default_profile'].fillna(False)



    for index,row in data.iterrows():
        temp=row['description']
        temp1=row['screen_name']
        temp2=row['name']
        loc=row['location']
 
        date=row['created_at']
        if "bot" in str(temp).lower():
            data['desc_bot'][index]=1
           # print(str(temp1))
        elif "bot" in str(temp1).lower():
            data['desc_bot'][index]=1
            #print(str(temp1))
        elif "bot" in str(temp2).lower():
            data['desc_bot'][index]=1
           # print(str(temp1))
        
        if isNaN(loc):
            data['loc']=0
        
        temp=parser.parse(date)
        difference=now-temp
        data['Age'][index]=difference.days

    return data