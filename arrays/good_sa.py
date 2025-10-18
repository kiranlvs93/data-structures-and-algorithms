from decorators.decorators_util import print_inp_op


@print_inp_op
def good_sub_arrays(inp_arr, target):
    count = 0
    n = len(inp_arr)
    for i in range(n):
        for j in range(i, n):
            sa = inp_arr[i:j + 1]
            len_sa = j + 1 - i
            sa_sum = sum(sa)
            if (len_sa % 2 == 0 and sa_sum < target) or (len_sa % 2 != 0 and sa_sum > target):
                count += 1
    return count


# good_sub_arrays([1, 2, 3, 4, 5], 4)
# good_sub_arrays([13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9], 65)


@print_inp_op
def good_sub_arrays_optimized(inp_arr, target):
    count = 0
    n = len(inp_arr)
    for i in range(n):
        sa_sum = 0
        for j in range(i, n):
            len_sa = j + 1 - i
            sa_sum += inp_arr[j]
            if (len_sa % 2 == 0 and sa_sum < target) or (len_sa % 2 != 0 and sa_sum > target):
                count += 1
    return count


good_sub_arrays_optimized([1, 2, 3, 4, 5], 4)
good_sub_arrays_optimized([13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9], 65)
