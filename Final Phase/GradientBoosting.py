from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,average_precision_score,recall_score,f1_score,roc_auc_score,roc_curve,auc
import matplotlib.pyplot as plt
import random

def TrainTest(features_train,train_labels,features_test):
    clf=GradientBoostingClassifier(n_estimators=200, learning_rate=1.0,max_depth=1, random_state=2)
    clf.fit(features_train,train_labels)
    solution=clf.predict(features_test)
    #return solution
    return clf