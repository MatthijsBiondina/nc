import numpy as np
import copy

def fitness(sudoku):
    size = sudoku.shape[0]
    subsize = int(np.sqrt(size))
    dups = 0
    for row in sudoku:
        dups += size - len(np.unique(row))

    for column in sudoku.T:
        dups += size - len(np.unique(column))

    for hgrid in range(0, size, subsize):
        for vgrid in range(0, size, subsize):
            # print(np.unique(sudoku[hgrid:hgrid+subsize,vgrid:vgrid+subsize]))
            dups += size - len(np.unique(sudoku[hgrid:hgrid+subsize,vgrid:vgrid+subsize]))
    return 8*18 + 8*9 - dups
#    return -dups-0.1

rho = 0.01
def updatePheromone(new_pheromones,sudoku,fitness):
    for i,row in enumerate(new_pheromones):
        for j,tau in enumerate(row):
            new_pheromones[i,j,sudoku[i,j]] += rho*fitness
    return new_pheromones

alpha = 0
beta  = 1
Q     = 1
def generateSudoku(pheromones):
    size = pheromones.shape
    sudoku = np.ones(size[0:2]).astype(int) * 9
    for i,row in enumerate(sudoku):
        for j,square in enumerate(row):
            eta = Q/(np.bincount(np.concatenate((sudoku[i],sudoku[:,j])), minlength=10)[:-1]+1)
            probs = pheromones[i,j]**alpha *eta**beta / sum(pheromones[i,j]**alpha *eta**beta)
            sudoku[i,j] = np.random.choice(range(size[0]),p=probs).astype(int)
    # print(probs)
    return sudoku

def localSearch(sudoku,c_fitness):
    print(fitness, end='\r')
    for i,row in enumerate(sudoku):
        for j,square in enumerate(row):
            old_num = sudoku[i,j]
            for num in range(9):
                sudoku[i,j] = num
                new_fitness = fitness(sudoku)
                if new_fitness > c_fitness:
                    return localSearch(sudoku,new_fitness)
                else:
                    sudoku[i,j] = old_num
    return sudoku

pheromones = np.ones((9,9,9))
nr_of_ants    = 150

best_sudoku = np.array([[np.random.randint(8) for y in range(9)] for x in range(9)])
best_fitness = -99999

local_sudoku = localSearch(best_sudoku,best_fitness)
print(local_sudoku)
print(fitness(local_sudoku))


epochs = 100
for e in range(epochs):
    print(e,end='\r')
    new_pheromones = copy.deepcopy(pheromones)
    new_pheromones *= (1-rho)
    for ant in range(nr_of_ants):
        #sudoku := generate sudoku based on pheromones
        sudoku = generateSudoku(pheromones)
        #new_pheromones := update pheromones
        ant_fitness = fitness(sudoku)
        new_pheromones = updatePheromone(new_pheromones,sudoku,ant_fitness)
        # if sudoku is better than best, copy
        if ant_fitness > best_fitness:
            best_sudoku = sudoku
            best_fitness = ant_fitness
            print(str(e) + ": " + str(best_fitness),end='\r')
    pheromones = new_pheromones
print(best_sudoku)
print(best_fitness)
local_sudoku = localSearch(best_sudoku,best_fitness)
print(local_sudoku)
print(fitness(local_sudoku))
