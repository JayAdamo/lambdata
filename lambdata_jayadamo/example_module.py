#!/usr/bin/env python

''' 
example of a module 
'''

import pandas as pd
import numpy as np

TEST = pd.DataFrame(np.ones(10))
COLORS = ('Blue', 'Orange', 'Red', 'Green', 'Violet', 'Cyan')

def increment(number):
    """Increases a given number by 1"""
    return number + 1