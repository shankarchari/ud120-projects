#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################




def train_and_score(C=10000):
	from sklearn import svm 
	from sklearn.metrics import accuracy_score
	clf = svm.SVC(C=C, kernel='rbf')
	t0 = time()
	clf.fit(features_train, labels_train)
	print "training time:", round(time()-t0, 3), "s"

	t0 = time()
	pred = clf.predict(features_test)
	print "prediction time:", round(time()-t0, 3), "s"

	accuracy = accuracy_score(labels_test, pred)
	return pred

x = [10, 26, 50]
preds = train_and_score()

y = [ 1 for index in range(len(preds)) if preds[index] == 1]
print(sum(y))