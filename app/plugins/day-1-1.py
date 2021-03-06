import click, time

from modules import console, Timer, DataProvider

@click.command()
def executor():
    console.header('day 1, part 1')
    timer = Timer()

    timer.start()
    total = sum([int(freq) for freq in DataProvider.load('day1')])
    timer.end()

    console.log('Total', total, fg='cyan', bold=True, color_status=True, include_brackets=True)
    timer.output()
