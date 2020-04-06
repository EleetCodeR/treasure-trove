
#  ======= BRUTE FORCE: TOO SLOW =======

# if __name__ == '__main__':
#     nd = input().split()

#     n = int(nd[0])

#     d = int(nd[1])

#     a = list(map(int, input().rstrip().split()))

#     for _ in range(d):
#         last = a[0]
#         for i in range(1, n):
#             a[i-1] = a[i]
#         a[n-1] = last

#     for el in a:
#         print(el, end=" ")

# ========= OPTIMIZED ( Juggling Algorithm )============


import sys
import re
import random
import os
import math


def arr_leftRotate(arr, d, n):
    d = d % n
    gcd = get_gcd(d, n)
    for i in range(gcd):
        temp = arr[i]
        j = i
        while 1:
            k = j+d
            if k >= n:
                k = k-n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)


def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    arr_leftRotate(a, d, n)
    printArray(a, n)
