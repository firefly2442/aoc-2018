from modules import console
from modules.guard import GuardProcessor
from modules.config.enums import Actions, SleepState

from .state import State
from .state_machine import FiniteStateMachine

class StartState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, item):
        # console.log('State', 'Start state')
        processed = GuardProcessor.parse_line(item)



        if processed.action == Actions.WORKING:
            if processed.guard is None:
                raise Exception('Action set to WORKING, but no guard identifier available')

            fsm.context.current_guard = processed.guard
            fsm.context.current_date = processed.date
            fsm.context.schedule = [SleepState.AWAKE]*60
            fsm.context.started_sleeping = None

            fsm.context.log = []

            from .working_state import WorkingState
            fsm.to(WorkingState)
