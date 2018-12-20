from modules import console

from .state import State

class EndState(State):
    @staticmethod
    def execute(fsm, line):
        console.log('State', 'End state')
