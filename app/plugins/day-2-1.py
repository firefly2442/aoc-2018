import click

from modules import console, Timer, DataProvider

def has(count, id):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if id.count(letter) == count:
            return True
    return False

@click.command()
def executor():
    console.header('day 2, part 1')

    timer = Timer()
    pair_count = 0
    triplet_count = 0

    timer.start()
    for id in DataProvider.load('day2'):
        if has(2, id):
            pair_count += 1
        if has(3, id):
            triplet_count += 1
    timer.end()

    console.log('Pairs', str(pair_count), fg='cyan', bold=True, color_status=True, include_brackets=True)
    console.log('Triplets', str(triplet_count), fg='cyan', bold=True, color_status=True, include_brackets=True)
    console.log('Checksum', str(pair_count * triplet_count), fg='cyan', bold=True, color_status=True, include_brackets=True)

    timer.output()
