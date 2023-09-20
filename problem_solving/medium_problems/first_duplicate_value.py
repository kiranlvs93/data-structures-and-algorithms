"""
Given an array of integers between 1 and n, inclusive, where n is the length of the array,
write a function that returns the first integer that appears more than once (when the array is read from left to right)
"""
array = [2, 1, 5, 2, 3, 3, 4]


def first_duplicate_value(inp_arr):
    """
    Time complexity O(N) - since we are iterating once through all the elements
    Space complexity O(N) - since we are storing the elements in a new variable
    :param inp_arr:
    :return:
    """
    visited = set()
    for num in inp_arr:
        if num in visited:
            return num
        else:
            visited.add(num)
    return -1


def first_duplicate_value_slicing(inp_arr):
    """
    Time complexity O(N) - since we are iterating once through all the elements
    Space complexity O(1) - since we are not storing any element
    :param inp_arr:
    :return:
    """
    for i in range(len(inp_arr)):
        if (curr := inp_arr[i]) in inp_arr[:i]:
            return curr
    return -1


def first_duplicate_value_pop(inp_arr):
    """
    Time complexity O(N) - since we are iterating once through all the elements
    Space complexity O(1) - since we are popping the element from the original array and storing in another variable,
    the space is going to remain constant
    :param inp_arr:
    :return:
    """
    visited = set()
    while len(inp_arr) > 0:
        curr = inp_arr.pop(0)
        if curr in visited:
            return curr
        visited.add(curr)
    return -1


print(first_duplicate_value(array))
print(first_duplicate_value_slicing(array))
print(first_duplicate_value_pop(array))
