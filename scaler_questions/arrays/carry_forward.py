"""
Given a string S of lower case letters, return the count of pairs (i,j) such that i<j and S[i] = 'a' and S[j] = 'g'

S = "abegag"
Answer:  3 pairs - (0,3) / (0,5) / (4,5)

S = "acgdgag"
Answer: 4 pairs - (0,2) / (0,4) / (0,6) / (5,6)
"""
from decorators.decorators_util import print_inp_op

def brute_force(inp_str):
    """
    Time complexity - O(N^2)
    :param inp_str:
    :return:
    """
    ag_pair_count = 0
    for i, ch_a in enumerate(inp_str):
        if ch_a != "a":
            continue

        for j, ch_g in enumerate(inp_str[i + 1:]):
            if ch_g == "g":
                ag_pair_count += 1

    print(ag_pair_count)


# brute_force("abegag")
# brute_force("acgdgag")

def using_inbuilt_count_method(inp_str):
    """
    Time complexity - O(N^2) - Since the ".count()" method essentially scans the substring inp_str[i + 1:] ch by ch
    :param inp_str:
    :return:
    """
    ag_pair_count = 0
    for i, ch_a in enumerate(inp_str):
        if ch_a != "a":
            continue
        ag_pair_count += inp_str[i + 1:].count("g")
    print(ag_pair_count)


# using_inbuilt_count_method("abegag")
# using_inbuilt_count_method("acgdgag")


@print_inp_op
def carry_forward_solution(inp_str):
    """
    Time complexity - O(N) - N is the length of the string
    Space complexity - O(1)
    :param inp_str:
    :return:
    """
    pairs_count = 0
    count_a = 0
    for ch in inp_str:
        if ch == 'a':
            count_a += 1
        elif ch == "g":
            pairs_count += count_a
    return pairs_count


carry_forward_solution("bcaggaag")
carry_forward_solution("aaggaag")
