import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Importing the pattern Calulator custom module to analyze and calculate additional columns
import Custom_Features_Calc

# Importing the custom modules to analyze and calculate results for various ML Methods
import Adaboost,SVM,DecisionTree,NaiveBayes,RandomForest 


# Reading data from the combined csv file including bots and non bots
data=pd.read_csv("Data/Combined_1.1.csv")

# Calculating number of occurences of 'bots' word and its variations in decription field and also number of days since account was created
data=Custom_Features_Calc.Calculate_Decription_Days(data)

# Splitting the data : 60% training and 40% testing
train, test = train_test_split(data, test_size = 0.4)


# As per the best features using graph analysis and RFE results, creating the features vectors for training and testing
features_train=train[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','has_extended_profile','default_profile']]
features_test=test[['Age','desc_bot','followers_count','friends_count','favourites_count','statuses_count','listed_count','verified','has_extended_profile','default_profile']]

# creating testing and training labels  
train_labels=np.array(train['bot'])
test_labels=np.array(test['bot'])

# creating index and columns for our final dataframe which contains results
index=['NaiveBayes - Gaussion','SVM','Decision Tree','Random Forest','Adaboost']
columns=['Accuracy','Precision','Recall','F1_Score','AUC_Score']

# Initializing the dataframe
results=pd.DataFrame(index=index,columns=columns)


# Calling each of the ML methods and saving the corresponding returned accuracy
naiveb=NaiveBayes.TrainTest(features_train,train_labels,features_test,test_labels)
results['Accuracy']['NaiveBayes - Gaussion'],results['Precision']['NaiveBayes - Gaussion'],results['Recall']['NaiveBayes - Gaussion'],results['F1_Score']['NaiveBayes - Gaussion'],results['AUC_Score']['NaiveBayes - Gaussion']=naiveb

svm=SVM.TrainTest(features_train,train_labels,features_test,test_labels)
results['Accuracy']['SVM'],results['Precision']['SVM'],results['Recall']['SVM'],results['F1_Score']['SVM'],results['AUC_Score']['SVM']=svm

dtree=DecisionTree.TrainTest(features_train,train_labels,features_test,test_labels)
results['Accuracy']['Decision Tree'],results['Precision']['Decision Tree'],results['Recall']['Decision Tree'],results['F1_Score']['Decision Tree'],results['AUC_Score']['Decision Tree']=dtree

RForest=RandomForest.TrainTest(features_train,train_labels,features_test,test_labels)
results['Accuracy']['Random Forest'],results['Precision']['Random Forest'],results['Recall']['Random Forest'],results['F1_Score']['Random Forest'],results['AUC_Score']['Random Forest']=RForest

Aboost=Adaboost.TrainTest(features_train,train_labels,features_test,test_labels)
results['Accuracy']['Adaboost'],results['Precision']['Adaboost'],results['Recall']['Adaboost'],results['F1_Score']['Adaboost'],results['AUC_Score']['Adaboost']=Aboost


# Displaying the results stored in the pandas dataframe
print(results)
