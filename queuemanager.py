from sweep_queue import Queue
from sweepstake import Sweepstakes


class QueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue(sweepstakes)

    def get_sweepstakes(self, sweepstakes):
        self.queue.dequeue(sweepstakes)
