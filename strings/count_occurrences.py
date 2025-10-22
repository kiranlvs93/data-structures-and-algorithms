"""
Find occurrences of "bob" in given string
"""

from decorators.decorators_util import print_inp_op


@print_inp_op
def count_occurrences(inp: str):
    """
    Time O(N2) | Space O(1)
    :param inp:
    :return:
    """
    n = len(inp)
    count = 0
    i = 0
    while i < n:
        index = inp.find("bob", i)
        if index > -1:
            count += 1
            i = index + 2
        else:
            i += 1
    return count
#
#
# count_occurrences("abobc")
# count_occurrences("bobob")
# count_occurrences("bobabtbobl")

@print_inp_op
def count_occurrences_optimized(inp: str):
    """
    Time O(N) | Space O(1)
    :param inp:
    :return:
    """
    return sum(1 for i in range(len(inp)) if inp[i:i + 3] == "bob")

count_occurrences_optimized("abobc")
count_occurrences_optimized("bobob")
count_occurrences_optimized("bobabtbobl")