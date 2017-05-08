## 1. index.py

Contains the main code, to generate solutions by training and testing data using the ML techniques, run this file, using the following statement:

"Python index.py > solution.csv"


## 2. DataLoadtrain.py and DataLoadtest.py

Code to load data from Twitter API given the screen names


## 3. Custom_Features_Calc.py

Calculates the custom features like desc_bot and Age for the data provided


## 4. Feature_Selection_Techniques.py

To Rank the features for Ensemble techniques and analyze there impact on the classifiers


## 5. Classifier files

The rest of the files are as named, and have the code for the respective classifiers, and return the trained classifier, which is later used in index.py for the training the VotingClassifier.
