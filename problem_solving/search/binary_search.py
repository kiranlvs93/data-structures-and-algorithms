from decorators.decorators_util import print_inp_op


@print_inp_op
def binary_search(arr, se):
    """
    Time complexity - O(log N) where N is the length of the elements
    Space complexity
    :param arr:
    :param se:
    :return:
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if se == arr[mid]:
            return mid
        elif se < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# binary_search([-5,-5,-3,0,0,1,1,5,5,5,5], 5)


@print_inp_op
def first_occurrence(arr, se):
    """
    Time complexity - O(log N) where N is the length of the elements
    Space complexity
    :param arr:
    :param se:
    :return:
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if se == arr[mid]:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                right = mid - 1
        elif se < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# first_occurrence([-5, -5, -3, 0, 0, 1, 1, 5, 5, 5, 5], 10)
# first_occurrence([1, 2, 3, 5, 5, 5, 5, 5, 8], 5)
# first_occurrence([1, 2, 3, 5, 5, 5, 5, 5, 8], 8)
# first_occurrence([1, 2, 3, 5, 5, 5, 5, 5, 8], 1)


@print_inp_op
def last_occurrence(arr, se):
    """
    Time complexity - O(log N) where N is the length of the elements
    Space complexity
    :param arr:
    :param se:
    :return:
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if se == arr[mid]:
            if mid == right or arr[mid + 1] != arr[mid]:
                return mid
            else:
                left = mid + 1
        elif se < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


last_occurrence([-5, -5, -3, 0, 0, 1, 1, 5, 5, 5, 5], 10)
last_occurrence([1, 2, 3, 5, 5, 5, 5, 5, 8], 5)
last_occurrence([1, 2, 3, 5, 5, 5, 5, 5, 8], 8)
last_occurrence([1, 2, 3, 5, 5, 5, 5, 5, 8], 1)
