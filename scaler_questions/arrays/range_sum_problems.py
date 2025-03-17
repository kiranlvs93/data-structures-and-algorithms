"""
Given is a series of numbers where positive number indicates profit and negative number indicates loss.
For a given number of queries with 2 values each, where first number is begin and second number is end, calculate the
profit or loss

E.g.: [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
L | R | Sum
-----------
4   8   9
3   7   10
1   3   12
0   4   14
7   7   -9
"""


def brute_force_solution(input_array: list, queries: list[list[int]]):
    """
    Time Complexity - O(Q) * O(K) since we are iterating through the Q queries and slicing the input_array with K elements
    Space Complexity - O(1) since there is no stored variable
    :param input_array:
    :param queries:
    :return:
    """
    for q in queries:
        start, end = q[0], q[1]
        print(sum(input_array[start: end + 1]))


inp_arr = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
query = [[4, 8],
         [3, 7],
         [1, 3],
         [0, 4],
         [7, 7]]


# brute_force_solution(inp_arr, query)


def prefix_sum_approach(input_array: list, queries: list[list[int]]):
    """
    Space complexity -> O(N) where N = length of input_array
    Time Complexity -> O(N) to get prefix sum + O(Q) to iterate through Q queries
    :param input_array:
    :param queries:
    :return:
    """

    def get_prefix_sum(arr: list):
        """
        Space Complexity - O(N) N elements in the arr
        Time Complexity - O(N) N elements in the arr
        :param arr:
        :return:
        """
        pfs = [arr[0]]
        for ele in arr[1:]:
            pfs.append(pfs[-1] + ele)
        return pfs

    prefix_sum = get_prefix_sum(input_array)
    for q in queries:
        start, end = q[0], q[1]
        if start == 0:
            print(prefix_sum[end])
        else:
            print(prefix_sum[end] - prefix_sum[start - 1])


# prefix_sum_approach(inp_arr, query)

"""
Given an array of size N and Q queries with start and end index. 
For each query, return the sum of all even indexed elements from start to end

A = [2,3,1,6,4,5]

S | E | Sum
-----------
1   3   1
2   5   5
0   4   7
3   3   0
"""


def prefix_sum_for_even_index(input_array: list, queries: list[list[int]]):
    def get_prefix_even_sum(arr: list):
        """
        Calculate prefix
        :param arr:
        :return:
        """
        pfs = list()
        for index, number in enumerate(arr):
            if index == 0:
                pfs.append(number)
                continue
            if index % 2 == 0:
                pfs.append(pfs[index - 1] + number)
            else:
                pfs.append(pfs[index - 1])
        return pfs

    prefix_sum = get_prefix_even_sum(input_array)
    for q in queries:
        start, end = q[0], q[1]
        if start == 0:
            print(prefix_sum[end])
        else:
            print(prefix_sum[end] - prefix_sum[start - 1])


prefix_sum_for_even_index([2, 3, 1, 6, 4, 5], [[1, 3], [2, 5], [0, 4], [3, 3]])
