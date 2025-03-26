from decorators.decorators_util import print_inp_op


@print_inp_op
def check_base_difference(A):
    A = sorted(A)
    base_diff = A[0] - A[1]
    for i in range(1, len(A) - 1):
        ele_diff = A[i] - A[i + 1]
        if ele_diff != base_diff:
            return 0
    return 1


# check_base_difference([3,5,1])

@print_inp_op
def noble_integer(A):
    """
    Let me explain with an example. Take [1,1,3,3]:

    After sorting it's already [1,1,3,3]
    At first 1 (i=0):
    Initially greater_count = len(A)-i-1 = 4-0-1 = 3
    We find a duplicate 1, so reduce greater_count by 1 (now 2)
    This 2 is correct as only two 3's are greater than 1
    Skip second 1
    At first 3 (i=2):
    greater_count = 4-2-1 = 1
    We find a duplicate 3, so reduce greater_count by 1 (now 0)
    This 0 is correct as no elements are greater than 3
    :param A:
    :return:
    """
    A.sort()
    i = 0
    while i < len(A):
        greater_count = len(A) - i - 1
        # Skip duplicates and adjust count
        while i + 1 < len(A) and A[i] == A[i + 1]:
            greater_count -= 1
            i += 1
        # Check if current element equals count of greater elements
        if A[i] == greater_count:
            return 1
        i += 1
    return -1


noble_integer([3, 1, 1, 3])
