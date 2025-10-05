"""
Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
"""

from decorators.decorators_util import print_inp_op

@print_inp_op
def check_if_ap(inp_arr):
    inp_arr.sort()
    diff = inp_arr[0] - inp_arr[1]
    for i in range(1, len(inp_arr)-1):
        if inp_arr[i] - inp_arr[i+1] != diff:
            return 0
    return 1