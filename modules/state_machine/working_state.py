from modules import console
from modules.config.enums import Actions, SleepState
from modules.guard import GuardProcessor, LogDetails

from .state import State
from .state_machine import FiniteStateMachine

class WorkingState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        # console.log('State', 'Working state')
        processed = GuardProcessor.parse_line(line)

        if processed.action == Actions.SLEEPING:
            fsm.context.started_sleeping = int(processed.minute)

            from .sleeping_state import SleepingState
            fsm.to(SleepingState)
        elif processed.action == Actions.NONE:
            fsm.context.log.append(LogDetails(fsm.context.date, fsm.context.guard, fsm.context.schedule))
            from .end_state import EndState
            fsm.to(EndState)
