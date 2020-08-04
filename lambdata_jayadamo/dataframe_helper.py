#!/usr/bin/env python

"""
Some functions to help cleaning and handling dataframes.
"""

# import libraries
import pandas as pd
import random


''' 
1) A function to find missing values in a dataframe 
'''

# defining report_missing_values
def report_missing_values(df):
    report_missing_values = pd.isnull  
    
    # Show missing values
    print(f'Here are the missing values:', report_missing_values)


''' 
2) A function to add 2 numbers by user input 
'''

# Define 2 possible values
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


''' 
3) Function to generate a random number between 0 and 9 
'''

# Shows random number
print(random.randint(0,9))