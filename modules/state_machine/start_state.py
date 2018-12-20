from modules import console
from modules.guard import GuardProcessor
from modules.config.enums import Actions

from .state import State

class StartState(State):
    @staticmethod
    def execute(fsm, item):
        console.log('State', 'Start state')
        processed = GuardProcessor.parse_line(item)

        if processed.action == Actions.WORKING:
            from .working_state import WorkingState
            fsm.to(WorkingState)
        else:
            # TODO: add line to internal register, and continue
            pass
