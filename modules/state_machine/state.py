from abc import abstractmethod

class State:
    @staticmethod
    @abstractmethod
    def execute(fsm, item):
        pass
