import numpy as np
import sklearn.datasets

#initialize current position
x0 = np.array([[5,5],[8,3],[6,7]])
v0 = np.array([[2,2],[3,3],[4,4]])

#initialize local and social best
Xstar = np.array([[5,5],[7,3],[5,6]])
Xsocial = np.array([[5,5],[5,5],[5,5]])

#initialize hyperparameters
w = 0.1
r1 = 0.5
r2 = 0.5

#define update functions
v = lambda X,V: w*V + r1*(Xstar-X) + r2*(Xsocial-X)
x = lambda X,V: X+V

#run one step
#v1 = v(x0,v0)
#x1 = x(x0,v1)

#display new position
#print(x1)

data = sklearn.datasets.load_iris()
print(data)
