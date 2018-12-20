from modules.config.enums import SleepState

class LogDetails:
    def __init__(self, date, guard, schedule):
        self.date = date
        self.guard = guard
        self.schedule = schedule

    def get_minutes(self):
        return len([x for x in self.schedule if x == SleepState.ASLEEP])
