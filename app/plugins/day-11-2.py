import click, numpy

from modules import console, Timer
    
def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += 3214
    power *= rack
    return (power // 100 % 10) - 5

@click.command()
def executor():
    console.header('day 11, part 2')

    timer = Timer()
    GRID = 301
    negatives = 0
    true_settings = (4,)

    timer.start()
    console.log('Task', 'Build grid...')
    grid = numpy.fromfunction(power, (300, 300))

    console.log('Task', 'Grid search')
    for width in range(3, 300):
        windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
        maximum = int(windows.max())
        location = numpy.where(windows == maximum)

        if maximum < 0:
            negatives += 1

        if negatives > 6:
            console.warning('Found too many negatives in a row; quitting')
            break

        if maximum > true_settings[0]:
            true_settings = (maximum, width, location[0][0] + 1, location[1][0] + 1)
        
        console.log('Max, Width, X, Y', '{}, {}, {}, {}'.format(maximum, width, location[0][0] + 1, location[1][0] + 1))
    timer.end()

    console.header('output')
    (total, width, x, y) = true_settings
    console.log('Best', total)
    console.log('Width', width)
    console.log('Location', '{}, {}'.format(x, y))
    timer.output()
