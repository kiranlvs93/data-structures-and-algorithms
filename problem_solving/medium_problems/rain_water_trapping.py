"""
Imagine a histogram where the bars' heights are given by the array A. Each bar is of uniform width, which is 1 unit. When it rains, water will accumulate in the valleys between the bars.
Your task is to calculate the total amount of water that can be trapped in these valleys.
Example: The Array A = [5, 4, 1, 4, 3, 2, 7] is visualized as below. The total amount of rain water trapped in A is 11.

Problem Constraints:
1 <= |A| <= 105
0 <= A[i] <= 105

Input Format: First and only argument is the Integer Array, A.

Output Format: Return an Integer, denoting the total amount of water that can be trapped in these valleys

Example Input
Input 1: A = [0, 1, 0, 2]
Input 2: A = [1, 2]

Example Output
Output 1: 1
Output 2: 0
"""
from decorators.decorators_util import print_inp_op


def brute_force_solution(arr):
    """
    Solution - Brute Force

    :param arr:
    :return:
    """
    pass


@print_inp_op
def optimized_solution(arr):
    """
    Solution - Optimized
    :param arr:
    :return:
    """
    # find max height on left of every element and carry forward the max height
    N = len(arr)
    max_left = [arr[0]]
    for i in range(1, N):
        max_ele = max(arr[i], max_left[i - 1])
        max_left.append(max_ele)
    print(f"{max_left=}")

    # find max height on right of every element and carry forward the max height
    max_right = [0] * N
    max_right[N-1] = arr[N-1]
    for i in range(N - 2, -1, -1):
        max_right[i] = max(max_right[i+1], arr[i])
    print(f"{max_right=}")

    # Find sum of trapped water
    trapped_water = 0
    for i in range(N):
        trapped_water += min(max_left[i], max_right[i]) - arr[i]
    return trapped_water



# optimized_solution([5, 4, 1, 4, 3, 2, 7])
optimized_solution([1, 4, 3, 5, 7, 2, 4, 3, 6, 8, 2])
# optimized_solution([3, 2, 1, 4, 7, 9])
