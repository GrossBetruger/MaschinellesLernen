from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 

iris = datasets.load_iris()

X = iris.data 
y = iris.target 

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)


def train_and_test_classifier(Classifier):
	classifier = Classifier()	
	classifier.fit(X_train, y_train)
	predictions =  classifier.predict(X_test)
	return accuracy_score(y_test, predictions)


if __name__=="__main__":
	print train_and_test_classifier(DecisionTreeClassifier)
	print train_and_test_classifier(KNeighborsClassifier)
