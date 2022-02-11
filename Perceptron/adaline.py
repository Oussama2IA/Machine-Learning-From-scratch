import numpy as np


class Adaline:
    def __init__(self, max_iters=1000):
        self.params = None
        self.max_iters = max_iters

    
    def sign(self, X):
        return np.where(X >= 0, 1, -1)

    def compute_loss(self, X, y, w, b):
        n = X.shape[0]
        S = np.dot(y - (np.dot(w, X.T) + b), (y - (np.dot(w, X.T) + b)).T)
        Ls = S / n
        return Ls

    def init_params(self, dim):
        w_0 = np.zeros(dim)
        b_0 = 0
        return w_0, b_0

    def fit(self, X, y):
        n = X.shape[0]
        w, b = self.init_params(X.shape[1])
        loss = self.compute_loss(X, y, w, b)
        losses = [loss]
        for _ in range(self.max_iters):
            for i in range(n):
                linear_output = np.dot(X[i], w) + b
                e_i = y[i] - linear_output
                if e_i != 0:
                    w = w + 0.01 * e_i * X[i]
                    b = b + 0.01 * e_i 
            loss = self.compute_loss(X, y, w, b)
            losses.append(loss)      
        self.params = {
            'w': w,
            'b': b
        }
        return losses

    def get_params(self):
        return self.params

    def set_params(self, **params):
        w = params.get('w')
        b = params.get('b')
        self.params = {
            'w': w,
            'b': b
        }
        return self

    def predict(self, X):
        w = self.params.get('w')
        b = self.params.get('b')
        linear_output = np.dot(X, w) + b
        y_pred = self.sign(linear_output)
        return y_pred

    def score(self, X, y):
        n_samples = X.shape[0]
        y_pred = self.predict(X)
        score = 1 - 1/n_samples * (np.abs(y - y_pred)).sum()
        return score