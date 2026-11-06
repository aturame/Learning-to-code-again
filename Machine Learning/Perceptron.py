#Coding a Perceptron

import numpy as np
import pandas
X =X
class Perceptron: #init methods, set learning rate to arbitrary 0.1 later do a grid sweep and epochs just set to 25 for now
    def __init__(self,learning_rate=0.1, epochs=25):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None #np.zeros(len(X.shape[1])).round(1)- add this to the predict step
        self.bias = None


    def predict(self, X):
        score = np.dot(X, self.weights)+self.bias
        predictions = np.where(score>0,1,0) #score more than 0 ->1 if not keep it at 0, so it's binary classification
        return predictions

    def fit(self,X,y):
        self.weights = np.zeros(len(X.shape[1])).round(1)
        self.bias = 0.0
        for epochs in self.epochs:
            for i in range(len(X.shape[0])):
                predict(self,X[i])
                







