"""
N/3 Repeat Number

Problem Description:
You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.
Note: Read-only array means that the input array should not be modified in the process of solving the problem

Problem Constraints:
1 <= N <= 7*105
1 <= A[i] <= 109

Input Format: The only argument is an integer array A.

Output Format: Return an integer.

Example Input:
Input 1: [1 2 3 1 1]
Input 2: [1 2 3]

Example Output:
Output 1: 1
Output 2: -1
"""


from decorators.decorators_util import print_inp_op


@print_inp_op
def find_repeated_numbers(inp_arr):
    """
    TC - O(N) | SC - O(N)
    :param inp_arr:
    :return:
    """
    freq = dict()
    n = len(inp_arr)
    desired_freq = n / 3

    for num in inp_arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > desired_freq:
            return num
    return -1


find_repeated_numbers([3,3,3,3,1,1,1,1])
find_repeated_numbers([2,3,1])