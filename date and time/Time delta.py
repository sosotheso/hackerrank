#!/bin/python3

import os
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    d1 = datetime.strptime(t1, '%a %d %b %Y %X %z')
    d2 = datetime.strptime(t2, '%a %d %b %Y %X %z')
    return str(int(abs((d1 - d2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        # print(t1)
        t2 = input()
        # print(t2)
        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
