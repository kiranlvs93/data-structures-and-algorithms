"""
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.
The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Problem Constraints: 0 <= sum of length of all strings <= 1000000

Input Format: The only argument given is an array of strings A.

Output Format: Return the longest common prefix of all strings in A.

Examples
Input 1:
A = ["abcdefgh", "aefghijk", "abcefgh"]

Input 2:
A = ["abab", "ab", "abcd"];

Output 1: "a"
Output 2: "ab"
"""

from decorators.decorators_util import print_inp_op


@print_inp_op
def longest_common_prefix(inp_arr: list[str]):
    """
    TC: O(N*L*logN) + O(N*L) = O(N*L*log N)
    SC: O(N) from inp_arr.sort()
    :param inp_arr:
    :return:
    """
    inp_arr.sort()
    max_len = len(inp_arr[0])
    n = len(inp_arr)
    count = 0

    for i in range(max_len):
        for j in range(n - 1):
            if inp_arr[j][i] != inp_arr[j + 1][i]:
                return inp_arr[0][:count]
        count += 1
    return inp_arr[0][:count]


longest_common_prefix(["abcdefgh", "aefghijk", "abcefgh"])
longest_common_prefix(["abab", "ab", "abcd"])
