#!/usr/bin/env python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input('Enter a number between 1 and 100: '))
    x = N % 2

    if x != 0:
        print('Weird')
    elif x == 0 and N >= 2 and N <= 5:
        print('Not Weird')
    elif x == 0 and N >= 6 and N <= 20:
        print('Weird')
    elif x == 0 and N > 20 and N <= 100:
        print('Not Weird')
    else:
        print('Weird')
