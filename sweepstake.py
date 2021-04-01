import random
from contestants import Contestant
from interface import interface


class Sweepstakes:
    def __init__(self, name):
        self.contestants = {}
        self.name = name

    def register_contestant(self, contestant):
        self.contestants[contestant.registration_number] = contestant

    def pick_winner(self):
        key_list = list(self.contestants.keys())
        val_list = list(self.contestants.values())
        contestant = random.choice(list(val_list))
        return contestant

    def print_contestant_info(self, contestant):
        print(f'name: {contestant.first_name} {contestant.last_name}')
        print(f' email address: {contestant.email_address}')
        print(f' registration number: {contestant.registration_number}')