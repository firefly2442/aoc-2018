import click, numpy, re
from modules import console, Timer, DataProvider
from modules.state_machine import FiniteStateMachine, StartState, EndState

@click.command()
def executor():
    console.header('day 4, part 1')

    timer = Timer()
    days = DataProvider.load('day4')

    fsm = FiniteStateMachine(StartState)

    timer.start()
    days.sort()
    for day in days:
        fsm.execute(day.strip())

    fsm.to(EndState)
    fsm.execute(None)
    timer.end()

    console.log('Minute', '', fg='cyan', bold=True, color_status=True, include_brackets=True)
    timer.output()
