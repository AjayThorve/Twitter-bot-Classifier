import pandas as pd
from dateutil import parser
import datetime
pd.options.mode.chained_assignment = None  # default='warn'

def Calculate_Decription_Days(data):
    data['desc_bot']=0
    data['Age']=0
    now=datetime.datetime.now()  #todays date

    for index,row in data.iterrows():
        temp=row['description']
        date=row['created_at']
        if "bot " in str(temp):
            data['desc_bot'][index]=1
        temp=parser.parse(date)
        difference=now-temp
        data['Age'][index]=difference.days
    return data