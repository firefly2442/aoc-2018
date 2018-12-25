import click
from scipy.spatial import distance
import numpy as np
from modules import console, Timer, DataProvider

@click.command()
def executor():
    console.header('day 6, part 1')

    timer = Timer()

    timer.start()

    data = DataProvider.load('day6')
    points_x = []
    points_y = []
    for row in data:
        s = row.split(', ')
        points_x.append(int(s[0].strip()))
        points_y.append(int(s[1].strip()))

    grid = np.empty(shape=[max(points_x)+2, max(points_y)+2], dtype="S10") # S10 is string of length 10
    for row in range(0, max(points_x)+2):
        print(row/(max(points_x)+2))
        for col in range(0, max(points_y)+2):
            # calculate Manhattan distance for all possible combinations
            mins_calc = list()
            for i in range(0, len(points_x)):
                d = distance.cityblock([row, col, 0], [points_x[i], points_y[i], 0])
                mins_calc.append(d)
                if d == 0:
                    break
            
            if (0 in mins_calc):
                grid[row,col] = "*"
            elif mins_calc.count(min(mins_calc)) > 1: # found multiple matching mins
                grid[row,col] = "."
            else:
                grid[row,col] = mins_calc.index(min(mins_calc))
            # print(row, col, grid[row,col])
            # print(mins_calc)
            # print("")

    # print(np.transpose(grid)) # I think something is backwards here thus the transpose? :/

    # find the "finite" points
    # walk the edge, anything not in the list will be finite
    infinite_set = list()
    for i in range(0, np.shape(grid)[0]):
        infinite_set.append(grid[i,0].decode('UTF-8')) # .decode('UTF-8') converts a byte literal to a string
    for i in range(0, np.shape(grid)[1]):
        infinite_set.append(grid[0,i].decode('UTF-8'))
    for i in range(0, np.shape(grid)[1]):
        infinite_set.append(grid[np.shape(grid)[0]-1,i].decode('UTF-8'))
    for i in range(0, np.shape(grid)[0]):
        infinite_set.append(grid[i,np.shape(grid)[1]-1].decode('UTF-8'))
    # print(infinite_set)

    finite_set = list()
    for i in range(0, len(data)):
        if str(i) not in infinite_set:
            finite_set.append(str(i).encode('UTF-8'))
    # print(finite_set)

    # find the largest area of the finite set
    unique, counts = np.unique(grid, return_counts=True)
    # print(unique)
    counts = counts + 1 # add one for each actual point (* symbol)
    # print(counts)
    max_counts = 0
    for v in finite_set:
        if max_counts < counts[np.where(unique == v)[0]]:
            max_counts = counts[np.where(unique == v)[0]]

    timer.end()

    console.header('output')
    console.log('Max Finite Single Area', max_counts)
    # console.log('Output', output)
    timer.output()
