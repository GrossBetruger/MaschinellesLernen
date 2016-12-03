from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 
from random import choice 
from scipy.spatial import distance 

iris = datasets.load_iris()

X = iris.data 
y = iris.target 

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)


class ScrappyKNN():
	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train

	def predict(self, X_test):
		predictions = []
		for row in X_test:
			label = self.nearest(row)
			predictions.append(label)
		return predictions

	def nearest(self, row):
		best_dist = self.euc_dis(row, self.X_train[0])
		best_index = 0
		for i in range(1, len(self.X_train)):
			dist = self.euc_dis(row, X_train[i])
			if dist < best_dist:
				best_dist = dist 
				best_index = i
		return self.y_train[best_index]

	def euc_dis(self, a, b):
		return distance.euclidean(a, b)


def train_and_test_classifier(Classifier):
	classifier = Classifier()	
	classifier.fit(X_train, y_train)
	predictions = classifier.predict(X_test)
	return accuracy_score(y_test, predictions)


if __name__=="__main__":
	print train_and_test_classifier(ScrappyKNN)