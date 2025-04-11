from decorators.decorators_util import print_inp_op

@print_inp_op
def find_min_swaps(arr, b):
    """
    Given an array of integers A and an integer B, find and return the minimum number of swaps required
    to bring all the numbers less than or equal to B together.
    Note: It is possible to swap any two elements, not necessarily consecutive.
    :param arr:
    :param b:
    :return:
    """
    # This can be resolved using window technique
    # Window_size = (number of elements <=b)
    window = sum(1 for ele in arr if ele <= b)
    size = len(arr)

    # Just assuming that the min_swaps required is equal to the size of the array
    min_swaps = size

    # Iterate through the array and for each window check how many elements > b
    for i in range(size):
        temp = 0
        for j in range(window):
            if arr[j] > b:
                temp += 1
        min_swaps = min(min_swaps, temp)
    # The least of these numbers give the minimum swaps
    return min_swaps


# find_min_swaps([1, 12, 10, 3, 14, 10, 5], 8)
find_min_swaps([5, 17, 100, 11], 20)
