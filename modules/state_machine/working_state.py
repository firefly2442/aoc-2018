from modules import console
from modules.config.enums import Actions
from modules.guard import GuardProcessor

from .state import State
from .state_machine import FiniteStateMachine

class WorkingState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        console.log('State', 'Working state')
        processed = GuardProcessor.parse_line(line)

        if processed.action == Actions.SLEEPING:
            # TODO: Update this day's action register to begin sleeping here
            from .sleeping_state import SleepingState
            fsm.to(SleepingState)
        elif processed.action == Actions.WORKING:
            # TODO: Process the current guards items, archive them, and then change
            from .working_state import WorkingState
            fsm.to(WorkingState)
        elif processed.action == Actions.NONE:
            # TODO: No more items, process current guard, archive and then end
            from .end_state import EndState
            fsm.to(EndState)
