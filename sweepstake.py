import random
from contestants import Contestant
from interface import interface


class Sweepstakes:
    def __init__(self, name):
        self.contestants = {}
        self.name = name
        self.subscribers = set()

    def register_contestant(self, contestant):
        self.contestants[contestant.registration_number] = contestant
        self.register(contestant)

    def pick_winner(self):
        key_list = list(self.contestants.keys())
        val_list = list(self.contestants.values())
        contestant = random.choice(list(val_list))
        self.dispatch(contestant.registration_number)
        return contestant

    def print_contestant_info(self, contestant):
        print(f'name: {contestant.first_name} {contestant.last_name}')
        print(f' email address: {contestant.email_address}')
        print(f' registration number: {contestant.registration_number}')

    def register(self, user):
        self.subscribers.add(user)

    def unregister(self, user):
        self.subscribers.discard(user)

    def dispatch(self, registration_number):
        for subscriber in self.subscribers:
            subscriber.notify(subscriber.registration_number == registration_number)