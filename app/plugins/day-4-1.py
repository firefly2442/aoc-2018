import click, numpy

from modules import Constants, console, Timer, DataProvider

def get_guard_id(day):
    index = day.find('#')
    if index < 0:
        raise click.ClickException('Oops...')

    return day[index+1:].replace('begins shift', '').strip()


@click.command()
def executor():
    console.header('day 4, part 1')

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

    timer = Timer()
    guards = {}

    timer.start()
    days.sort()

    current_guard = None
    current_guard_cycle = numpy.zeros([60])

    for day in days:
        if day.endswith('begins shift'):
            if current_guard is not None:
                if current_guard not in guards:
                    guards[current_guard] = []
                guards[current_guard].append(current_guard_cycle)

            current_guard = get_guard_id(day)
            current_guard_cycle = []
        else:
            current_guard_cycle.append(day)

    timer.end()

    print(guards)

    console.log('Minute', '', fg='cyan', bold=True, color_status=True, include_brackets=True)
    timer.output()
