#!/usr/bin/python3
"""find a peak"""


def find_peak(list_of_integers):

    n = len(list_of_integers)
    if n > 1:
        return recursion_find_peak(list_of_integers, 0, n - 1, n)


def recursion_find_peak(arr, low, high, n):
    center = int(low + (high - low)/2)

    if ((center == 0 or arr[center - 1] <= arr[center]) and
            (center == n - 1 or arr[center + 1] <= arr[center])):
        return arr[center]

    elif (center > 0 and arr[center - 1] > arr[center]):
        return recursion_find_peak(arr, low, (center - 1), n)

    else:
        return recursion_find_peak(arr, (center + 1), high, n)
