"""
You are given a string S, and you have to find all the amazing substrings of S.
An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
Constraints

1 <= length(S) <= 1e6
S can have special characters
Example

Input
    ABEC

Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.
"""

from decorators.decorators_util import print_inp_op


@print_inp_op
def amazing_sub_array(inp: str):
    """
    TC - O(N) and SC - O(1)
    :param inp:
    :return:
    """
    n = len(inp)
    inp = inp.lower()
    count = 0
    for i in range(n):
        if inp[i] in "aeiou":
            count += n - i

    return count % 10003


amazing_sub_array("abec")
amazing_sub_array("abecdio")
