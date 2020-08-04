#!/usr/bin/env python

''' Examples of Object Orientated Programming '''

import pandas as pandas

class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i
    
    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)

class SocialMediaUser:
    def __init__(self, name):
        self.name = name
        self.upvotes = 0
    
    def receive_upvote(self):
        self.upvotes += 1
    
    def is_popular(self):
        return self.upvotes > 100

# Parent Class
class Animal:
    """General representation of animals."""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = weight
        self.diet_type = diet_type
    
    def run(self):
        return 'Vroom!'
    
    def eat(self, food):
        return food + ' is delicious, yum!'

# Child class or subclass
class Tiger(Animal):
    """Representation of tigers, a subclass of Animal."""
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type) #this brings in the parent fields
        self.num_stripes = num_stripes
    
    def say_great(self):
        return "It's GREEAAAAAT!"
    
    # Example of overriding
    def run(self):
        return 'Scamperwoosh!'



"""
EXAMPLE OF OVERIDING AND THE CHILD CLASS

>>> from lambdata_jayadamo.oop_examples import *
>>> tony = Tiger('Tony', 140, "cereal", 37)
>>> tony.eat('cereal')
'cereal is delicious, yum!'
>>> tony.run()
'Scamperwoosh!'
>>> tony.weight
140
>>> tony.diet_type
'cereal'
>>> tony.num_stripes
37
""""

