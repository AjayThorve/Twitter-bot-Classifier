import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,average_precision_score,recall_score,f1_score,roc_auc_score,roc_curve,auc
import matplotlib.pyplot as plt
import random

def TrainTest(features_train,train_labels,features_test):
    clf=RandomForestClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
    clf.fit(features_train,train_labels)
    solution=clf.predict(features_test)
    #return solution
    return clf
