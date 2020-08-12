import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Exercise 1, loading data
diabetes = pd.read_csv("data/pima_diabetes.csv")
print(diabetes.head())

X = diabetes.drop('class', axis=1)
y = diabetes['class']

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Exercise 2
# Training KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

print("test set score of knn:", knn.score(X_test, y_test))

# Training RandomForest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
print("training score of random forest: ", rf.score(X_train, y_train))
print("test score of random forest: ", rf.score(X_test, y_test))

