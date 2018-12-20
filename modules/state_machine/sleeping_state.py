from modules import console
from modules.config.enums import Actions, SleepState
from modules.guard import GuardProcessor

from .state import State
from .state_machine import FiniteStateMachine

class SleepingState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        # console.log('State', 'Sleeping state')
        processed = GuardProcessor.parse_line(line)

        if processed.action == Actions.WAKING:
            end_sleep = int(processed.minute)
            sleep_range = end_sleep - fsm.context.started_sleeping

            for index in range(fsm.context.started_sleeping, sleep_range + fsm.context.started_sleeping):
                fsm.context.schedule[index] = SleepState.ASLEEP

            fsm.context.started_sleeping = None

            from .waking_state import WakingState
            fsm.to(WakingState)
        elif processed.action == Actions.NONE:
            fsm.context.log.append(LogDetails(fsm.context.date, fsm.context.guard, fsm.context.schedule))

            from .end_state import EndState
            fsm.to(EndState)
