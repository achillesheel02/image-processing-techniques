import numpy as np

class Perceptron:
    def __init__(self,N,alpha=.1):
        self.W=np.random.randn(N+1)/np.sqrt(N)
        self.alpha=alpha

    def step(self,x):
        return 1 if x>0 else 0

    def fit(self,X,y,epochs=10):
        X=np.c_[X,np.ones((X.shape[0]))]

        for epoch in np.arrange(0,epochs):
            