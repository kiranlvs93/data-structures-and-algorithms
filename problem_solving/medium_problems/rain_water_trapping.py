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
    if len(arr) < 3:
        return 0
    n = len(arr)
    max_height = [arr[0]]
    for i in range(1, n - 1):
        l = max(arr[:i])
        r = max(arr[i + 1:])
        m = min(l, r)
        if m > arr[i]:
            max_height.append(m)
        else:
            max_height.append(arr[i])
    max_height.append(arr[-1])
    water_ht = 0
    for i in range(n):
        water_ht += max_height[i] - arr[i]
    return water_ht


@print_inp_op
def rain_water_tapping(arr):
    n = len(arr)

    # Find the max on left for each position
    max_left = [arr[0]]
    for i in range(1, n):
        max_left.append(max(max_left[i - 1], arr[i]))

    # Find the max on right for each position
    max_right = [0] * n
    max_right[-1] = arr[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], arr[i])

    # Trapped water at each position = min(max_left,max_right) - current_position
    trapped_water = 0
    for i in range(n):
        trapped_water += min(max_left[i], max_right[i]) - arr[i]
    return trapped_water


rain_water_tapping([5, 4, 1, 4, 3, 2, 7])
rain_water_tapping([3, 2, 1, 4, 7, 9])
rain_water_tapping([1, 4, 3, 5, 7, 2, 4, 3, 6, 8, 2])
rain_water_tapping([5, 4, 1, 4, 3, 2, 7, 1, 8])
rain_water_tapping([0, 1, 0, 2])
rain_water_tapping([0, 1, 0, 2])
rain_water_tapping([5, 9, 10])
rain_water_tapping([5, 9, 7])
rain_water_tapping([5, 0, 7])
