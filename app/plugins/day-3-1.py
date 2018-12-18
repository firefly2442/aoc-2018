import click, numpy

from modules import console, Timer, Claim, DataProvider

@click.command()
def executor():
    console.header('day 3, part 1')

    max_x = 1000
    max_y = 1000
    count = 0
    timer = Timer()

    timer.start()
    claims = numpy.zeros([max_x, max_y])
    for element in DataProvider.load('day3'):
        claim = Claim(element)
        claims = claim.fill_claim(claims)

    for x in range(max_x):
        for y in range(max_y):
            if claims[x][y] > 1:
                count += 1
    timer.end()

    console.log('Count', str(count), fg='cyan', bold=True, color_status=True, include_brackets=True)
    timer.output()
