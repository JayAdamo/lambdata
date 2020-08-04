#!/usr/bin/env python

'''
US National Parks by location and feature
'''

# Creating a class for a park by name, state, feature
class Park():
    def __init__(self, name, state, feature):
        ''' These are attributes '''
        self.name = name
        self.state = state
        self.feature = feature

# Helper function by class
if __name__ == "__main__":

    # New "instance" of the class
    park_1=park(name="Mammoth Cave", state="Kentucky", feature="cave") 
    print(park_1.name)
    print(park_1.state)
    print(park_1.feature)

    # Another "instance" of the class
    park_2=park(name="Yellowstone", state="Wyoming", feature="hot springs") 
    print(park_2.name)
    print(park_2.state)
    print(park_2.feature)

    # Another "instance" of the class
    park_3=park(name="Grand Canyon", state="Arizona", feature="canyon") 
    print(park_3.name)
    print(park_3.state)
    print(park_3.feature)