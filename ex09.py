import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn import svm
from sklearn import datasets
from sklearn import cross_validation
ionospheres = datasets.load_digits()
X_digits = ionospheres.data
y_digits = ionospheres.target
print(X_digits)
print(Y_digits)
