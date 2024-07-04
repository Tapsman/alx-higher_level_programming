#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    This function will return the peak of unsorted
    integers
    """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    mn = int(length / 2)
    peak = list_of_integers[mn]
    if peak > list_of_integers[mn - 1] and peak > list_of_integers[mn + 1]:
        return peak
    elif peak < list_of_integers[mn - 1]:
        return find_peak(list_of_integers[:mn])
    else:
        return find_peak(list_of_integers[mn + 1:])
