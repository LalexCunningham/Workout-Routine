import pandas as pd
import dataGenerator

weight = input('Please enter a weight\n')

try:
    startingWeight = float(weight)
except ValueError:
    print('Please enter a valid weight')