
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Make the graphs a bit prettier, and bigger
#pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)

data=pd.read_csv('MLData.csv')
data['Class'].value_counts().plot(kind='bar')
for index,row in data.iterrows():
    row['Screen name']=row['Screen name'].replace('@','')
print (data['Screen name'].tolist())
print (data['Class'].value_counts())      #count of various types of classes
bots=data[data['Class']=="Bot"]    #list of bots
print (bots.head())
#plt.show()