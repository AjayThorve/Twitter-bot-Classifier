import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,average_precision_score,recall_score,f1_score,roc_auc_score,roc_curve,auc
import matplotlib.pyplot as plt
import random

def TrainTest(features_train,train_labels,features_test,test_labels):
    clf=SVC()
    clf.fit(features_train,train_labels)
    solution=clf.predict(features_test)
    
    accuracy=accuracy_score(test_labels, solution)

    precision=average_precision_score(test_labels, solution)

    recall=recall_score(test_labels,solution,average="binary", pos_label=1)

    f1=f1_score(test_labels,solution,average="binary", pos_label=1)

    y_true=np.array(test_labels)
    y_scores=np.array(solution)
    auc1=roc_auc_score(y_true, y_scores)
    fpr, tpr, thresholds=roc_curve(y_true,y_scores,pos_label=1)
    roc_auc=auc(fpr,tpr)
    print(roc_auc)
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic SVM')
    plt.legend(loc="lower right")
    plt.show()
    return accuracy,precision,recall,f1,auc1