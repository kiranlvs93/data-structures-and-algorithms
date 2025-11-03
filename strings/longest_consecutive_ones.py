"""
Given an array of 1s and 0s, you are allowed to replace a 0 with 1. Find the maximum number of consecutive 1s that can be obtained after the initial replacement

Inp - 100111
Op - 4 (Since this can be done 101111
"""

from decorators.decorators_util import print_inp_op


@print_inp_op
def longest_consecutive_ones_by_replacement(inp_arr):
    n = len(inp_arr)
    curr_count = 0
    count_ones = 0

    # consecutive ones on left of zero
    con_ones_l = []

    for i in range(n):
        if inp_arr[i] == '1':
            con_ones_l.append(-1)
            curr_count += 1
            count_ones += 1
        else:
            con_ones_l.append(curr_count)
            curr_count = 0
    # print(con_ones_l)

    if count_ones == n:
        return n

    # consecutive ones on right of zero
    curr_count = 0

    con_ones_r = [-1] * n
    for i in range(n - 1, -1, -1):
        if inp_arr[i] == '1':
            con_ones_r[i] = -1
            curr_count += 1
        else:
            con_ones_r[i] = curr_count
            curr_count = 0

    # print(con_ones_r)

    max_ones = 0
    for i in range(n):
        if inp_arr[i] == '0':
            max_ones = max(max_ones, con_ones_l[i] + con_ones_r[i] + 1)

    return max_ones


longest_consecutive_ones_by_replacement(list("1110001100"))
longest_consecutive_ones_by_replacement(list("111000"))
longest_consecutive_ones_by_replacement(list("111011101"))
longest_consecutive_ones_by_replacement(list("11111110"))
longest_consecutive_ones_by_replacement(list("100111111100"))
longest_consecutive_ones_by_replacement(list("000111111100"))


@print_inp_op
def longest_consecutive_ones_by_swap(inp_arr):
    """
    Swap a 1 with zero and find the length of the max consecutive ones
    TC - O(N) | SC = O(N)
    :param inp_arr:
    :return:
    """
    n = len(inp_arr)
    total_count_ones = 0

    # count of consecutive onse to left
    con_left = [-1] * n
    count_ones = 0

    for i in range(n):
        if inp_arr[i] == '1':
            count_ones += 1
            total_count_ones += 1
        else:
            con_left[i] = count_ones
            count_ones = 0
    # If all elements are 1s, that becomes the highest num of consecutive ones we can form
    if count_ones == n:
        return n

    con_right = [-1] * n
    count_ones = 0

    for i in range(n - 1, -1, -1):
        if inp_arr[i] == '1':
            count_ones += 1
        else:
            con_right[i] = count_ones
            count_ones = 0

    max_cons_ones = 0

    for i in range(n):
        if inp_arr[i] == '0':
            ones = con_right[i] + con_left[i]
            if ones == total_count_ones:
                max_cons_ones = max(max_cons_ones, ones)
            else:
                max_cons_ones = max(max_cons_ones, ones + 1)

    return max_cons_ones


longest_consecutive_ones_by_swap(list("1110001100"))
longest_consecutive_ones_by_swap(list("111000"))
longest_consecutive_ones_by_swap(list("111011101"))
longest_consecutive_ones_by_swap(list("11111110"))
longest_consecutive_ones_by_swap(list("100111111100"))
longest_consecutive_ones_by_swap(list("000111111100"))
longest_consecutive_ones_by_swap(list("11110"))