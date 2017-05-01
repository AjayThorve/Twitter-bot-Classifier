import pandas as pd
from dateutil import parser
import datetime
import math
pd.options.mode.chained_assignment = None  # default='warn'

def isNaN(num):
    return num != num

def Calculate_Decription_Days(data):
    data['desc_bot']=0
    data['screen_bot']=0
    data['Age']=0
    data['loc']=0
    now=datetime.datetime.now()  #todays date
    data['description'] = data['description'].fillna('No Description')
    data['has_extended_profile'] = data['has_extended_profile'].fillna(False)
    
    for index,row in data.iterrows():
        temp=row['description']
        temp1=row['screen_name']
        temp2=row['name']
        loc=row['location']

        date=row['created_at']
        str(temp)
        if "bot".lower() in str(temp).lower() or " bot".lower() in str(temp).lower():
            data['desc_bot'][index]=1
        if "bot".lower() in str(temp1).lower() or " bot".lower() in str(temp1).lower() or "bot".lower() in str(temp2).lower() or " bot".lower() in str(temp2).lower():
            data['screen_bot'][index]=1
        if isNaN(loc):
            data['loc']=1
        
        temp=parser.parse(date)
        difference=now-temp
        data['Age'][index]=difference.days
    return data