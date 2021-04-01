from sweepstake import Sweepstakes


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    # using dependency injection below so that the user can choose between stack or queue

    def create_sweepstakes(self):
        sweepstakes = Sweepstakes(input("Enter sweepstakes name"))
        self.manager.insert_sweepstakes(sweepstakes)


class MarketingFirmCreator:
    def __init__(self):
        self.manager = MarketingFirm()
