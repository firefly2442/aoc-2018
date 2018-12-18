import time

from .console import console

class Timer:
    def start(self):
        self.start = time.time()

    def end(self):
        self.end = time.time()

    def output(self):
        total_time = self.end - self.start
        console.log('Timing', '{:.4f} seconds'.format(total_time), fg='green' if total_time < 15 else 'red', bold=True, color_status=True, include_brackets=True)
