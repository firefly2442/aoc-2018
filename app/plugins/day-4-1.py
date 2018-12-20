import click, numpy, re
from modules import console, Timer, DataProvider
from modules.state_machine import FiniteStateMachine, StartState

@click.command()
def executor():
    console.header('day 4, part 1')

    timer = Timer()
    # days = DataProvider.load('day4')
    days = [
        '[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:05] falls asleep',
        '[1518-11-01 00:25] wakes up',
        '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up',
        '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep',
        '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift',
        '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up',
        '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep',
        '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift',
        '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up',
    ]

    fsm = FiniteStateMachine(StartState)

    timer.start()
    days.sort()
    for day in days:
        fsm.execute(day)
    timer.end()

    console.log('Minute', '', fg='cyan', bold=True, color_status=True, include_brackets=True)
    timer.output()
