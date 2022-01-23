# 1

BRIDGE_FEE = 15
TAG_PRICE = 30


class BridgeNoMoney(Exception):
    def __init__(self, name, message='has no money to pass the bridge'):
        self.message = message
        self.name = name
        self.custom_message = f'{name} {message}'

    def __str__(self):
        return self.custom_message


class Person:
    def __init__(self, name, money, tag=False):
        self.name = name
        self.money = money
        self.tag = tag

    @property
    def get_balance(self):
        return self.money

    @property
    def get_tag(self):
        return self.tag


class fare:
    def __init__(self, func):
        self.func = func

    def __call__(self, person):
        if person.get_balance >= BRIDGE_FEE and person.get_tag:
            person.money -= BRIDGE_FEE
        elif person.get_balance >= BRIDGE_FEE and not person.get_tag:
            if person.get_balance >= BRIDGE_FEE + TAG_PRICE:
                person.money -= BRIDGE_FEE + TAG_PRICE
                person.tag = True
            else:
                raise BridgeNoMoney(person.name)
        else:
            raise BridgeNoMoney(person.name)
        return self.func(person)


@fare
def bridge(person):
    print(f'{person.name} passed the bridge with enough money. Current balance: {person.get_balance}. Tag: {person.get_tag}')


if __name__ == '__main__':
    nazar = Person(name='Nazar', money=45)
    bridge(nazar)





# 2*

import time
from datetime import datetime


class Logger:
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log = f'{func.__name__} with was executed at {datetime.now()}\n'
        print(log)
        with open(self.logfile, 'a') as file:
            file.write(log)


@Logger()
def my_func():
    """
    This is my func
    """
    print(f"{my_func().__name__} is running")


log = Logger()