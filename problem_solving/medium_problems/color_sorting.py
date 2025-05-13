"""
Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will represent the colors as,

red -> 0
white -> 1
blue -> 2

Note: Using the library sort function is not allowed.

Problem Constraints
1 <= N <= 1000000
0 <= A[i] <= 2

Input Format: First and only argument of input contains an integer array A.

Output Format: Return an integer array in asked order

Example Input:
Input 1 : A = [0, 1, 2, 0, 1, 2]
Input 2:  A = [0]

Example
Output 1: [0, 0, 1, 1, 2, 2]
Output 2: [0]
"""

from decorators.decorators_util import print_inp_op


@print_inp_op
def sort_colors(inp):
    if len(inp) == 1:
        return inp

    # Count the frequency of the colors
    freq = {0: 0, 1: 0, 2: 0}
    for col in inp:
        freq[col] = freq.get(col, 0) + 1

    sorted_colors = list()
    for col, f in freq.items():
        sorted_colors.extend([col] * f)
    return sorted_colors


# sort_colors([0, 1, 2, 0, 1, 2])


@print_inp_op
def sort_colors_with_dnf(inp):
    if len(inp) == 1:
        return inp

    low, mid = 0,0
    high = len(inp)-1

    while mid<=high:
        if inp[mid] == 0:
            inp[low],inp[mid] = inp[mid], inp[low]
            low += 1
            mid += 1
        elif inp[mid] == 1:
            mid += 1
        elif inp[mid] == 2:
            inp[high],inp[mid] = inp[mid], inp[high]
            high -= 1
    return inp


sort_colors_with_dnf([0, 1, 2, 0, 1, 2])