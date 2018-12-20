from modules import console
from modules.config.enums import SleepState
from modules.guard import LogDetails

from .state import State
from .state_machine import FiniteStateMachine

class EndState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        # console.log('State', 'End state')

        fsm.context.log.append(LogDetails(fsm.context.current_date, fsm.context.current_guard, fsm.context.schedule))

        # for entry in fsm.context.log:
        #     console.log('{} #{} ({:3})'.format(entry.date, entry.guard, entry.get_minutes()), ''.join([str(e.value) for e in entry.schedule]), width=24)

        guards = set([entry.guard for entry in fsm.context.log])
        # print('Num Guards', str(len(guards)))

        max_minutes = -1
        max_minutes_guard = None
        for guard in guards:
            minutes = sum([entry.get_minutes() for entry in fsm.context.log if entry.guard == guard])
            # console.log('Guard #{}'.format(guard), str(minutes), width=20)
            if minutes > max_minutes:
                max_minutes = minutes
                max_minutes_guard = guard

        # console.log('Target Guard', str(max_minutes_guard))
        # console.log('Minutes', str(minutes))

        schedules = [entry.schedule for entry in fsm.context.log if entry.guard == max_minutes_guard]

        # for schedule in schedules:
        #     console.log('Schedule', ''.join([str(el.value) for el in schedule]))

        target_minute = -1
        max_count = -1
        for minute in range(60):
            count = 0
            for schedule in schedules:
                if schedule[minute] == SleepState.ASLEEP:
                    count += 1

            if count > max_count:
                target_minute = minute
                max_count = count

            #console.log('Minute {:2}'.format(minute), str(count))

        console.log('Guard', str(max_minutes_guard))
        console.log('Minute', str(target_minute))
        console.log('Hash', str(int(max_minutes_guard) * int(target_minute)))
        console.log('Count', str(max_count))
