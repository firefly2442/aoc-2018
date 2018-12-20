from modules import console

from .state import State
from .state_machine import FiniteStateMachine

class EndState(State):
    @staticmethod
    def execute(fsm: FiniteStateMachine, line):
        console.log('State', 'End state')
