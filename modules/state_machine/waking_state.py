from modules import console
from modules.config.enums import Actions
from modules.guard import GuardProcessor

from .state import State
from .state_machine import FiniteStateMachine

class WakingState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        console.log('State', 'Waking state')

        processed = GuardProcessor.parse_line(line)

        if processed.action == Actions.WORKING:
            from .working_state import WorkingState
            fsm.to(WorkingState)
        elif processed.action == Actions.SLEEPING:
            from .sleeping_state import SleepingState
            fsm.to(SleepingState)
        elif processed.action == Actions.NONE:
            from .end_state import EndState
            fsm.to(EndState)
