import numpy as np
import sklearn.datasets
import copy

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
X = sklearn.preprocessing.normalize(data.data)

y = data.target

N = 3

def init_clustering_or_speed():
    return np.array([np.random.uniform(mi,ma) for i in range(N*len(data[0]))])

def fitness(clustering, X):
    return sum(min(np.linalg.norm(sample-c) for c in clustering) for sample in X) / len(X)

x0 = np.array([init_clustering_or_speed(-1,1) for i in range(100)])
v0 = np.array([init_clustering_or_speed(-1,1) for i in range(100)])
local_best_x = copy.deepcopy(x0)
local_best_f = np.array([fitness(p, X) for p in x0])

v = init_clustering_or_speed() / 4

print(fitness(particles[0], X))

for i in range(100):
    particles += 

    is_better = [fitness(p, X) < local_best_f[i] for i, p in enumerate(particles)]
    local_best_f[is_better] = [fitness(p, X) for p,b in zip(particles, is_better) if b]
    local_best_x[is_better] = particles[is_better]
    global_best_f = min(local_best_f)
    global_best_x = local_best_x[argmin(local_best_f)]

    r1

    # v = 
