"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def Classifier(test):
	data = pd.read_csv('complete.csv', sep=',', header=None)
	RFClassifier = RandomForestClassifier(n_estimators=500)
	
	y = data[1]
	data.drop([0, 1], axis=1, inplace=True)
	
	RFClassifier.fit(data, y)
	return RFClassifier.predict(test)
"""

def Classifier(test):
	a = 5