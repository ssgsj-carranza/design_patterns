from sweepstake import Sweepstakes


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstakes = Sweepstakes(input("Enter sweepstakes name"))
        self.manager.insert_sweepstakes(sweepstakes)
    #using dependency injection here so that the user can choose between stack or queue


