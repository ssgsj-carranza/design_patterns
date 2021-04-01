from sweep_stack import Stack
from sweepstake import Sweepstakes


class StackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)

    def get_sweepstakes(self, sweepstakes):
        self.stack.pop(sweepstakes)
