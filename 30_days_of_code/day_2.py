#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = meal_cost

    tip = meal_cost * (tip_percent/100)

    tax = meal_cost * (tax_percent/100)

    total = round(meal_cost + tip + tax)

    print('The total meal cost is ' + str(total) + ' dollars.')

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
