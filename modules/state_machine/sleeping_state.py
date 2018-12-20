from modules import console
from modules.config.enums import Actions
from modules.guard import GuardProcessor

from .state import State
from .state_machine import FiniteStateMachine

class SleepingState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        console.log('State', 'Sleeping state')
        processed = GuardProcessor.parse_line(line)

        if processed.action == Actions.WAKING:
            from .waking_state import WakingState
            fsm.to(WakingState)
        elif processed.action == Actions.NONE:
            from .end_state import EndState
            fsm.to(EndState)
