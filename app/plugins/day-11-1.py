import click

from modules import console, Timer, DataProvider

def power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    if power_level < 100:
        return -5
    power_level = int(power_level / 100)
    power_level = power_level % 10
    return power_level - 5

@click.command()
def executor():
    console.header('day 11, part 1')

    timer = Timer()
    serial_number = 3214

    GRID_X = 300
    GRID_Y = 300

    timer.start()
    console.log('Task', 'Building empty power grid')
    grid = [[0]*GRID_Y for i in range(GRID_X)]

    console.log('Task', 'Calculating power levels')
    for x in range(GRID_X):
        for y in range(GRID_Y):
            grid[x][y] = power_level(x, y, serial_number)

    max_x = GRID_X - 3
    max_y = GRID_Y - 3

    max_power = -999
    target_x = -1
    target_y = -1

    console.log('Task', 'Finding 3x3 grid with the highest power level')
    for x in range(max_x):
        for y in range(max_y):
            cell = grid[x:x+3]
            cell = [inner[y:y+3] for inner in cell]
            power = 0
            for row in cell:
                power += sum(row)
                
            if power > max_power:
                max_power = power
                target_x = x
                target_y = y
    timer.end()

    console.header('output')
    console.log('Power', max_power)
    console.log('X', target_x)
    console.log('Y', target_y)
    timer.output()
