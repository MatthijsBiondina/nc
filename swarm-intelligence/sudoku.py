import numpy as np

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

    return -dups

sudoku = np.array([[np.random.randint(9) + 1 for y in range(9)] for x in range(9)])
print(sudoku)
print(fitness(sudoku))
