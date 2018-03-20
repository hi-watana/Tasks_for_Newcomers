from sklearn import svm, datasets, model_selection, metrics

if __name__ == "__main__":
    X, y = datasets.load_svmlight_file("ionosphere.scale")
    clf = svm.SVC(random_state=0)
    print("[precision, recall, MCC, AUROC, F-score]")
    for i, j in model_selection.StratifiedKFold(n_splits=10).split(X, y):
        clf.fit(X[i], y[i])
        predicted = clf.predict(X[j])
        print(
                [f(y[j], predicted) for f in [
                    metrics.precision_score,
                    metrics.recall_score,
                    metrics.matthews_corrcoef,
                    metrics.roc_auc_score,
                    metrics.f1_score,
                    ]
                    ]
                )
