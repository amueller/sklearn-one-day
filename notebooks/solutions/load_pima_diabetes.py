import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

diabetes = pd.read_csv("data/pima_diabetes.csv")
print(diabetes.head())

X = diabetes.drop('class', axis=1)
y = diabetes['class']

print("Dataset size: %d  number of features: %d  number of classes: %d"
      % (X.shape[0], X.shape[1], len(np.unique(y))))

X_train, X_test, y_train, y_test = train_test_split(X, y)

pd.plotting.scatter_matrix(X, c=y=='tested_positive', cmap='Paired', figsize=(10, 10));
