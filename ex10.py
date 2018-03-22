import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline

from sklearn import svm
from sklearn import metrics
from sklearn import model_selection
from sklearn import datasets

if __name__ == "__main__":
    feature_train, label_train = datasets.load_svmlight_file("ionosphere.scale")

    clf = model_selection.GridSearchCV(
            estimator = svm.SVC(),
            param_grid = {
                "C" : [0.5, 1.0, 2.0],
                "gamma" : ["auto", 1, 2, 3, 4, 5, 6]
                },
            cv = 10,
            #scoring = "roc_auc",
            scoring = "f1",
            )

    clf.fit(feature_train, label_train)
    predicted = clf.predict(feature_train)
    precision = metrics.precision_score(label_train, predicted)
    recall = metrics.recall_score(label_train, predicted)
    mcc = metrics.matthews_corrcoef(label_train, predicted)
    roc_auc = metrics.roc_auc_score(label_train, predicted)
    f_score = metrics.f1_score(label_train, predicted)
    print(clf.best_params_)
    print("precision: %s" % precision)
    print("recall: %s" % recall)
    print("MCC: %s" % mcc)
    print("AUROC: %s" % roc_auc)
    print("F-score: %s" % f_score)
