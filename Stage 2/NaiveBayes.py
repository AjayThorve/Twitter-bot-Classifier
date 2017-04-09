import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,average_precision_score,recall_score,f1_score,roc_auc_score


def TrainTest(features_train,train_labels,features_test,test_labels):
    clf=GaussianNB()
    clf.fit(features_train,train_labels)
    solution=clf.predict(features_test)

    accuracy=accuracy_score(test_labels, solution)

    precision=average_precision_score(test_labels, solution)

    recall=recall_score(test_labels,solution,average="binary", pos_label=1)

    f1=f1_score(test_labels,solution,average="binary", pos_label=1)

    y_true=np.array(test_labels)
    y_scores=np.array(solution)
    auc=roc_auc_score(y_true, y_scores)
    
    return accuracy,precision,recall,f1,auc