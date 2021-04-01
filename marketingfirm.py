from sweepstake import Sweepstakes

class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstakes = Sweepstakes(input("Enter sweepstakes name"))
