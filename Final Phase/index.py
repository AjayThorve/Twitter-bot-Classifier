import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import GridSearchCV

# Importing the pattern Calulator custom module to analyze and calculate additional columns
import Custom_Features_Calc

# Importing the custom modules to analyze and calculate results for various ML Methods
import Adaboost,SVM,DecisionTree,NaiveBayes,RandomForest,GradientBoosting 


# Reading data from the combined csv file including bots and non bots
train=pd.read_csv("train_data1.csv")
test=pd.read_csv("test_data1.csv")

# Splitting the data : 60% training and 40% testing
#train, test = train_test_split(data, test_size = 0.4)

# Calculating number of occurences of 'bots' word and its variations in decription field and also number of days since account was created
train=Custom_Features_Calc.Calculate_Decription_Days(train)
test=Custom_Features_Calc.Calculate_Decription_Days(test)


# As per the best features using graph analysis and RFE results, creating the features vectors for training and testing
features_train_RandomForest=train[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','lang','default_profile','loc','has_extended_profile']]
features_test_RandomForest=test[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','lang','default_profile','loc','has_extended_profile']]

features_train_GradientBoosting=train[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','lang','default_profile','loc','has_extended_profile']]
features_test_GradientBoosting=test[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','lang','default_profile','loc','has_extended_profile']]

features_train_Adaboost=train[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','lang','default_profile','loc','has_extended_profile']]
features_test_Adaboost=test[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','lang','default_profile','loc','has_extended_profile']]

features_train_ECLF=train[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','lang','default_profile','loc','has_extended_profile']]
features_test_ECLF=test[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','lang','default_profile','loc','has_extended_profile']]



# creating testing and training labels  
train_labels=np.array(train['bot'])
#test_labels=np.array(test['bot'])

# creating index and columns for our final dataframe which contains results
index=['NaiveBayes - Gaussion','SVM','Decision Tree','Random Forest','Adaboost']
columns=['Accuracy','Precision','Recall','F1_Score','AUC_Score']

# Initializing the dataframe
results=pd.DataFrame(index=index,columns=columns)


# Calling each of the ML methods and saving the corresponding returned accuracy

clfRand=RandomForest.TrainTest(features_train_RandomForest,train_labels,features_test_RandomForest)

clfAda=Adaboost.TrainTest(features_train_Adaboost,train_labels,features_test_Adaboost)

clfGrad=GradientBoosting.TrainTest(features_train_GradientBoosting,train_labels,features_test_GradientBoosting)

##soft voting
#eclf = VotingClassifier(estimators=[('lr', clfRand), ('rf', clfAda), ('gnb', clfGrad)], voting='soft')

##Hard voting
eclf = VotingClassifier(estimators=[('lr', clfRand), ('rf', clfAda), ('gnb', clfGrad)], voting='hard')

eclf.fit(features_train_ECLF,train_labels)
solution=eclf.predict(features_test_ECLF)

print ("Id,Bot")
# Displaying the results for transfering to csv file
for i in range(len(solution)):
    print (test['id'][i],",",solution[i])


#execute using "python index.py > sol.csv"