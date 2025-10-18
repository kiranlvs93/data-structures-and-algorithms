from decorators.decorators_util import print_inp_op


@print_inp_op
def sub_arrays_with_sum_brute_force(inp_arr, exp_sum):
    n = len(inp_arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if sum(inp_arr[i:j + 1]) < exp_sum:
                count += 1
    return count


@print_inp_op
def sub_arrays_with_sum_optimised(inp_arr, exp_sum):
    n = len(inp_arr)
    count = 0
    for i in range(n):
        sa_sum = 0
        for j in range(i, n):
            sa_sum += inp_arr[j]
            if sa_sum < exp_sum:
                count += 1
    return count


sub_arrays_with_sum_optimised([2, 5, 6], 10)
sub_arrays_with_sum_optimised([1, 11, 2, 3, 15], 10)
