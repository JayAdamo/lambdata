#!/usr/bin/env python

''' A helper function to track banking transactions '''

def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = make_account()
b = make_account()

# assuming a zero balance to start
# ex. deposit(a, 100)
# will return = 100