#Coding a Perceptron

import numpy as np

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
        self.weights = np.zeros(X.shape[1]).round(1)
        self.bias = 0.0
        for epochs in range(self.epochs):
            for i in range(X.shape[0]):
                prediction = self.predict(X[i:i+1])[0]
                error = y[i] - prediction #error step
                self.weights += error*self.lr*X[i]
                self.bias += self.lr*error

X = np.random.randint(0,2,size = (6,2)) #randint is exclusive so right bound is at 2 so you generate 0 and 1
y = [] #initialise a empty list
for amt in X:
    if amt[0] == 1 and amt[1] == 1: #because if you put a != for both then what happens is that fi you have '' or some shit like that it will classify as 0
        y.append(1)
    else:
        y.append(0)
y = np.array(y)


perceptron = Perceptron(learning_rate = 0.1, epochs = 25)
perceptron.fit(X,y)

print("Actual Target: ",y)
print("Model's guess: ",perceptron.predict(X)) 
#Compiled on 11/07/2026 00:08


