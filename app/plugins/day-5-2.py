import click

from modules import console, Timer, DataProvider
from modules.polymer import Polymer

@click.command()
def executor():
    console.header('day 5, part 2')

    timer = Timer()
    polymer = DataProvider.read('day5').strip()

    timer.start()
    polymer = Polymer.get_best_score(polymer)
    timer.end()

    console.log('Best', polymer)
    console.log('Length', str(len(polymer)))
    timer.output()
