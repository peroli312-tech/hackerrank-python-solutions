#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())


if n != 0:
    print('Weird')
elif n == 0 and 2 <= n <= 5:
    print('Not Weird')
elif n == 0 and 6 <= n <= 20:
    print('Weird')
elif n == 0 and 20 <= n <= 100:
    print('Not Weird')
else:
    print('Not a valid number')
    

    
