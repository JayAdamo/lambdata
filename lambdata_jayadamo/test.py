#!/usr/bin/env python

"""Test for the lambdata nat_parks module."""

import unittest

# unittest supports a type of tests called unit tests
# A unit is the smallest cohesive piece of code we can test
# (usually something like a function or method)

from nat_parks import Park

class ParkTest(unittest.TestCase):
    def test_name(self):
       """Test that the name field is assigned correctly."""
        park_1 = ParkTest('Mammoth Cave')
        park_2 = Park('Yellowstone')
        park_3 = Park('Grand Canyon')
        self.assertEqual(park_1.name, 'Mammoth Cave')
        self.assertEqual(park_2.name, 'Yellowstone')
        self.assertEqual(park_3.name, 'Grand Canyon')

    def test_state(self):
        """Test that the state field is assigned correctly."""
        park_1 = Park('Kentucky')
        park_2 = Park('Wyoming')
        park_3 = Park('Arizona')
        self.assertEqual(park_1.state, 'Kentucky')
        self.assertEqual(park_2.state, 'Wyoming')
        self.assertEqual(park_3.state, 'Arizona')

    def test_feature(self):
        """Test that the features are assigned correctly."""
        park_1 = Park('cave')
        park_2 = Park('hot springs')
        park_3 = Park('canyon')
        self.assertEqual(park_1.feature, 'cave')
        self.assertEqual(park_2.feature, 'hot springs')
        self.assertEqual(park_3.feature, 'canyon')

if __name__ == '__main__':
    # This conditional is for code that will be run
    # when we execute our file from the command line
    unittest.main()