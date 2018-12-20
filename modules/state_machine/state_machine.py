from modules import Container
from .state import State

class FiniteStateMachine:
    def __init__(self, start_state: State):
        self.state = start_state
        self.context = Container()

    def execute(self, item):
        self.state.execute(self, item)

    def to(self, target_state: State):
        self.state = target_state
