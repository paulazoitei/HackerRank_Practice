#!/bin/python3

import math
import os
import random
import re
import sys



def solve(s):
    lista = []
    for i, term in enumerate(s):

        if i == 0:
            lista.append(term.upper())

        elif s[i - 1] == ' ' and term != ' ':
            lista.append(term.upper())
        else:
            lista.append(term)
    return ''.join(lista)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
