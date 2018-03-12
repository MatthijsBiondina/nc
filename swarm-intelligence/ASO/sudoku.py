import numpy as np

def fitness(sudoku):
	return

def updatePheromone():
	return

Q = 1
pheromones = np.zeros((9,9,9))
nr_of_ants    = 150
ant_fitnesses = np.zeros( nr_of_ants )

best_sudoku =  np.matrix(np.random.random((9,9))*8+1).round()
print(best_sudoku)


