from modules import console
from modules.config.enums import Actions
from modules.guard import GuardProcessor

from .state import State

class SleepingState(State):
    @staticmethod
    def execute(fsm, line):
        console.log('State', 'Sleeping state')
        processed = GuardProcessor.parse_line(line)

        if processed.action == Actions.WAKING:
            from .waking_state import WakingState
            fsm.to(WakingState)
        elif processed.action == Actions.NONE:
            from .end_state import EndState
            fsm.to(EndState)
