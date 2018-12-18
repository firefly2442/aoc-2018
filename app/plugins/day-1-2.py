import click, time

from modules import Constants, console, Timer

@click.command()
def executor():
    console.header('day 1 - part 2')

    master_freq = 0
    master_freq_set = set([master_freq])
    master_freq_list = [master_freq]

    count = 0

    timer = Timer()

    timer.start()
    try:
        while True:
            count += 1
            for freq in Constants.Day1:
                master_freq = master_freq + int(freq)
                master_freq_set.add(master_freq)
                master_freq_list.append(master_freq)

                if len(master_freq_set) != len(master_freq_list):
                    raise Exception('Found it!')
            if count % 10 == 0:
                console.log(' ', 'Looped {} times so far.'.format(count))
    except:
        pass
    timer.end()

    console.log('Dupe', master_freq, fg='cyan', bold=True, color_status=True, include_brackets=True)
    timer.output()
