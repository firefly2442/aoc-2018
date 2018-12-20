from modules import console, Container
from modules.config.enums import Actions, SleepState
from modules.guard import GuardProcessor, LogDetails

from .state import State
from .state_machine import FiniteStateMachine

class WakingState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        # console.log('State', 'Waking state')

        processed = GuardProcessor.parse_line(line)
        if not processed:
            processed = Container()
            processed.action = Actions.NONE

        if processed.action == Actions.WORKING:
            fsm.context.log.append(LogDetails(fsm.context.current_date, fsm.context.current_guard, fsm.context.schedule))

            fsm.context.current_date = processed.date
            fsm.context.current_guard = processed.guard
            fsm.context.schedule = [SleepState.AWAKE]*60
            fsm.context.started_sleeping = None

            from .working_state import WorkingState
            fsm.to(WorkingState)
        elif processed.action == Actions.SLEEPING:
            fsm.context.started_sleeping = int(processed.minute)

            from .sleeping_state import SleepingState
            fsm.to(SleepingState)
        elif processed.action == Actions.NONE:
            fsm.context.log.append(LogDetails(fsm.context.current_date, fsm.context.current_guard, fsm.context.schedule))

            from .end_state import EndState
            fsm.to(EndState)
