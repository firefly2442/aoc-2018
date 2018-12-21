import click

from modules import console, Timer, DataProvider
from modules.graph import Node

def parse(data):
    children, metas = data[:2]

    scores = []
    data = data[2:]

    for child in range(children):
        score, data = parse(data)
        scores.append(score)

    if children == 0:
        return sum(data[:metas]), data[metas:]
    else:
        score = 0
        for meta_key in data[:metas]:
            if meta_key > 0 and meta_key <= len(scores):
                score += scores[meta_key - 1]
        return score, data[metas:]

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
    score, rest = parse(elements)
    timer.end()

    console.header('output')
    console.log('Score', score)
    console.log('Rest', rest)
    timer.output()
