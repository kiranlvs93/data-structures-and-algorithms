"""
This function takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose
absolute difference is closest to zero, and returns an array containing these two numbers, with the number
from the first array in the first position.
"""


def smallest_diff_best_method(array_one, array_two):
    """
    Two pointer solution
    Sort the arrays and move the pointers in each array such that diff is close to zero
    Time complexity O(NlogN + MlogM) - since we are sorting and then iterating once through the elements
    Space complexity O(1) - Since data stored is independent of array length
    :param array_one:
    :param array_two:
    :return:
    """
    array_one.sort()
    array_two.sort()

    m, n = 0, 0
    smallest_diff = float("inf")
    smallest_pair = []

    while m < len(array_one) and n < len(array_two):
        first_num = array_one[m]
        second_num = array_two[n]
        current_diff = abs(first_num-second_num)
        if first_num < second_num:  # Increment the first pointer
            m += 1
        elif first_num > second_num:  # Increment the second pointer
            n += 1
        else:  # if two numbers are equal, then the difference is zero, so return these numbers
            return [first_num, second_num]

        # If the difference is small, update it
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            smallest_pair = [first_num, second_num]
    return smallest_pair


def smallest_difference(array_one, array_two):
    """
    Brute force method
    Time complexity O(n^2)
    Space complexity O(1)
    :param array_one:
    :param array_two:
    :return:
    """
    smallest_diff = [array_one[0], array_two[0]]
    for a1 in array_one:
        for a2 in array_two:
            if abs(a1 - a2) < abs(smallest_diff[0] - smallest_diff[1]):
                smallest_diff = [a1, a2]
    return smallest_diff


arr1 = [-1, 5, 10, 20, 28, 3]
arr2 = [26, 134, 135, 15, 17]
print(smallest_difference(arr1, arr2))
print(smallest_diff_best_method(arr1, arr2))

arr1 = [-1, 3, 5, 20, 30, 38]
arr2 = [15, 25, 36, 134, 135]
print(smallest_difference(arr1, arr2))
print(smallest_diff_best_method(arr1, arr2))