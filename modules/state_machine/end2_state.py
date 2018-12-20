from modules import console
from modules.config.enums import SleepState
from modules.guard import LogDetails

from .state import State
from .state_machine import FiniteStateMachine

class End2State(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        # console.log('State', 'End state')

        fsm.context.log.append(LogDetails(fsm.context.current_date, fsm.context.current_guard, fsm.context.schedule))
        guards = set([entry.guard for entry in fsm.context.log])

        max_guard_count = -1
        max_guard_minute = -1
        max_guard = -1
        for guard in guards:
            schedules = [entry.schedule for entry in fsm.context.log if entry.guard == guard]
            max_count = -1
            target_minute = -1
            for minute in range(60):
                count = 0
                for schedule in schedules:
                    if schedule[minute] == SleepState.ASLEEP:
                        count += 1
                if count > max_count:
                    target_minute = minute
                    max_count = count

            console.log('Guard', str(guard))
            console.log('Minute', str(target_minute))
            console.log('Count', str(max_count), fg='cyan')

            if max_count > max_guard_count:
                max_guard = guard
                max_guard_count = max_count
                max_guard_minute = target_minute

        console.header('output')
        console.log('Guard', str(max_guard))
        console.log('Minute', str(max_guard_minute))
        console.log('Hash', str(int(max_guard) * int(max_guard_minute)))
        console.log('Count', str(max_count))
