import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv("data.csv")

X = data.drop(columns=['artists', 'name', 'id', 'release_date', 'mode', 'explicit',  'key'])
y = data['artists']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X_train, y_train)

pickle.dump(clf, open('model.pkl', 'wb'))
