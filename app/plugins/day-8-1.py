import click

from modules import console, Timer, DataProvider
from modules.graph import Node

def parse(data):
    children, metas = data[:2]

    grand_total = 0
    data = data[2:]

    for child in range(children):
        total, data = parse(data)
        grand_total += total

    grand_total += sum(data[:metas])
    return grand_total, data[metas:]

@click.command()
def executor():
    console.header('day 8, part 1')

    console.log('Task', 'Configure application...')
    timer = Timer()
    data = DataProvider.read('day8').strip()
    #data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    elements = [int(el) for el in data.split(' ')]

    timer.start()
    console.header('executing')
    total, rest = parse(elements)
    timer.end()

    console.header('output')
    console.log('Total', total)
    console.log('Rest', rest)
    timer.output()
