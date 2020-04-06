import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    # seqList = [[]]*n
    # above will end up creating same list n times and created problem when updated.(reflects n times.)
    # instead use list comprehension as below.
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    ansArr = []

    for q in queries:
        indx = ((q[1] ^ lastAnswer) % n)
        if(q[0] == 1):
            seq = seqList[indx]
            seq.append(q[2])
        elif(q[0] == 2):
            seq = seqList[indx]
            l = len(seq)
            indx = (q[2] % l)
            lastAnswer = seq[indx]
            ansArr.append(lastAnswer)

    return ansArr


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
