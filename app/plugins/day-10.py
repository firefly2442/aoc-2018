import click, re, collections

from os.path import join
from time import sleep
from modules import console, Timer, DataProvider

@click.command()
@click.pass_context
def executor(ctx):
    console.header('day 10, both parts')

    timer = Timer()
    data = DataProvider.load('day10')

    # data = [
    #     'position=< 9,  1> velocity=< 0,  2>',
    #     'position=< 7,  0> velocity=<-1,  0>',
    #     'position=< 3, -2> velocity=<-1,  1>',
    #     'position=< 6, 10> velocity=<-2, -1>',
    #     'position=< 2, -4> velocity=< 2,  2>',
    #     'position=<-6, 10> velocity=< 2, -2>',
    #     'position=< 1,  8> velocity=< 1, -1>',
    #     'position=< 1,  7> velocity=< 1,  0>',
    #     'position=<-3, 11> velocity=< 1, -2>',
    #     'position=< 7,  6> velocity=<-1, -1>',
    #     'position=<-2,  3> velocity=< 1,  0>',
    #     'position=<-4,  3> velocity=< 2,  0>',
    #     'position=<10, -3> velocity=<-1,  1>',
    #     'position=< 5, 11> velocity=< 1, -2>',
    #     'position=< 4,  7> velocity=< 0, -1>',
    #     'position=< 8, -2> velocity=< 0,  1>',
    #     'position=<15,  0> velocity=<-2,  0>',
    #     'position=< 1,  6> velocity=< 1,  0>',
    #     'position=< 8,  9> velocity=< 0, -1>',
    #     'position=< 3,  3> velocity=<-1,  1>',
    #     'position=< 0,  5> velocity=< 0, -1>',
    #     'position=<-2,  2> velocity=< 2,  0>',
    #     'position=< 5, -2> velocity=< 1,  2>',
    #     'position=< 1,  4> velocity=< 2,  1>',
    #     'position=<-2,  7> velocity=< 2, -2>',
    #     'position=< 3,  6> velocity=<-1, -1>',
    #     'position=< 5,  0> velocity=< 1,  0>',
    #     'position=<-6,  0> velocity=< 2,  0>',
    #     'position=< 5,  9> velocity=< 1, -2>',
    #     'position=<14,  7> velocity=<-2,  0>',
    #     'position=<-3,  6> velocity=< 2, -1>',
    # ]

    lines = [[int(i) for i in re.findall(r'-?\d+', line)] for line in data]
    index = -1
    size = -1

    console.log('Task', 'Finding smallest sized object to work with')
    timer.start()
    for i in range(20000):
        minx = min(x + i * vx for (x, y, vx, vy) in lines)
        maxx = max(x + i * vx for (x, y, vx, vy) in lines)
        miny = min(y + i * vy for (x, y, vx, vy) in lines)
        maxy = max(y + i * vy for (x, y, vx, vy) in lines)

        test_size = maxx - minx + maxy - miny

        if size == -1 or test_size < size:
            size = test_size
            index = i

    console.log('Found', 'Min Size {} for index {}'.format(size, index))

    console.log('Task', 'Building data map')
    my_map = [[' ']*200 for j in range(400)]
    for (x, y, vx, vy) in lines:
        my_map[y + index * vy][x + index * vx -250] = '*'

    console.log('Task', 'Saving map to file')
    with open(join(ctx.obj['BASE_PATH'], 'output.txt'), 'w+') as handle:
        for m in my_map:
            handle.write(''.join(m) + '\n')

    timer.end()

    console.header('output')
    timer.output()
