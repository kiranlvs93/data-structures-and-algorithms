from decorators.decorators_util import print_inp_op


@print_inp_op
def check_if_noble_integer_exists_brute_force(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for ele in arr:
            if ele > arr[i]:
                count += 1
        if count == arr[i]:
            return 1
    return -1


# check_if_noble_integer_exists_brute_force([3, 2, 1, 3])
# check_if_noble_integer_exists_brute_force([1, 3, 1, 3])
# check_if_noble_integer_exists_brute_force([-1, -2, 0, 0, 0, -3])
# check_if_noble_integer_exists_brute_force([1, 2, 2, 3])
# check_if_noble_integer_exists_brute_force([0, 0, 0])
# check_if_noble_integer_exists_brute_force([5, 5, 5])


@print_inp_op
def check_if_noble_integer_exists_optimized(arr):
    arr.sort()
    n = len(arr)
    i = 0
    while i < n:
        while i < n - 2 and arr[i] == arr[i + 1]:
            i += 1
        ele_to_right = n - 1 - i
        if arr[i] == ele_to_right:
            return 1
        i += 1
    return -1


# check_if_noble_integer_exists_optimized([0, 0, 0])
# check_if_noble_integer_exists_optimized([5, 5, 5])
# check_if_noble_integer_exists_optimized([3, 2, 1, 3])
# check_if_noble_integer_exists_optimized([1, 3, 1, 3])
# check_if_noble_integer_exists_optimized([-1, -2, 0, 0, 0, -3])
# check_if_noble_integer_exists_optimized([1, 2, 2, 3])
# check_if_noble_integer_exists_optimized([1, 2, 2, 2])




@print_inp_op
def check_if_noble_integer_exists_best_solution(arr):
    arr.sort()
    n = len(arr)
    for i in range(n-1):
        if arr[i] != arr[i+1] and arr[i] == n-i-1:
            return 1
    return 1 if arr[-1]==0 else -1

check_if_noble_integer_exists_best_solution([0, 0, 0])
check_if_noble_integer_exists_best_solution([5, 5, 5])
check_if_noble_integer_exists_best_solution([3, 2, 1, 3])
check_if_noble_integer_exists_best_solution([1, 3, 1, 3])
check_if_noble_integer_exists_best_solution([-1, -2, 0, 0, 0, -3])
check_if_noble_integer_exists_best_solution([1, 2, 2, 3])
check_if_noble_integer_exists_best_solution([1, 2, 2, 2])
