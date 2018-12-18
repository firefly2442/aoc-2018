import click

from modules import console, Timer, DataProvider

def hamming_distance(s1, s2):
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

@click.command()
def executor():
    console.header('day 2, part 2')

    timer = Timer()
    used_ids = set([])
    pairs = []
    ids = DataProvider.load('day2')

    timer.start()
    for id in ids:
        if id not in used_ids:
            used_ids.add(id)
            for inner in ids:
                if inner in used_ids:
                    continue

                distance = hamming_distance(id, inner)

                if distance == 1:
                    pairs.append((id, inner,))
    timer.end()

    console.log(' ', 'Pairs', fg='cyan', bold=True, color_status=True, include_brackets=True)
    print(pairs)

    timer.output()
