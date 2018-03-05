import numpy as np
import sklearn.datasets
import sklearn.cluster
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

Nclusters = 3
Nparticles = 100
w = .5

def init_clustering_or_speed_or_r(min_=-2, max_=2):
    return np.array([[np.random.uniform(min_, max_) for j in range(X.shape[1])] for i in range(Nclusters)])

def fitness(clustering, X):
    return sum(min(np.linalg.norm(sample-c) for c in clustering) for sample in X) / len(X)

particles = np.array([init_clustering_or_speed_or_r() for i in range(100)])
local_best_x = copy.deepcopy(particles)
local_best_f = np.array([fitness(p, X) for p in particles])

v = np.array([init_clustering_or_speed_or_r() / 4 for p in particles])

print(fitness(particles[0], X) ** .5)

for i in range(1000):
    particles += v
    scores = [fitness(p, X) for p in particles]
    is_better = [s < local_best_f[i] for i, s in enumerate(scores)]
    local_best_f[is_better] = [s for s, b in zip(scores, is_better) if b]
    local_best_x[is_better] = particles[is_better]
    global_best_f = min(local_best_f)
    global_best_x = local_best_x[np.argmin(local_best_f)]
    v = w * v
    r1 = init_clustering_or_speed_or_r(0, 1)
    r2 = init_clustering_or_speed_or_r(0, 1)
    for i, velo in enumerate(v):
        velo += r1 * (local_best_x[i] - particles[i]) + r2 * (global_best_x - particles[i])

print(fitness(particles[0], X) ** .5)
print(X.shape)

kmeans_model = sklearn.cluster.KMeans(3, init='random')
kmeans_model.fit(X)

print(fitness(kmeans_model.cluster_centers_, X) ** .5)
