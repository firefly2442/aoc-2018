import click

from modules import console, Timer, DataProvider
from modules.polymer import Polymer

@click.command()
def executor():
    console.header('day 5, part 1')

    timer = Timer()
    polymer = DataProvider.read('day5').strip()

    timer.start()
    polymer = Polymer.react(polymer)
    timer.end()

    console.log('polymer', polymer)
    console.log('length', str(len(polymer)))
    timer.output()
