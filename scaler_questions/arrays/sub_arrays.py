from decorators.decorators_util import print_inp_op


@print_inp_op
def sub_array_sum(A, B, C):
    max_sa_sum = 0
    for i in range(A):
        for j in range(i, A):  # sub array
            sa_sum = sum(C[i:j + 1])
            if max_sa_sum < sa_sum <= B:
                max_sa_sum = sa_sum

    return max_sa_sum


# sub_array_sum(5, 12, [2, 1, 3, 4, 5])
# sub_array_sum(3, 1, [2, 2, 2])


@print_inp_op
def sub_array_sum_contrib(A):
    total_sum = 0
    for i in range(len(A)):
        contrib = A[i] * ((i + 1) * (len(A) - i))
        total_sum += contrib
    return total_sum


# sub_array_sum_contrib([2, 1, 3])

@print_inp_op
def count_sa_sum(A, B):
    sa_sum = sum(A[:B])
    min_avg_index = 0
    start_index = 1
    end_index = start_index + B - 1
    while end_index < len(A):
        sa_sum = (sa_sum - A[start_index - 1] + A[end_index])
        sa_avg = sa_sum / B
        if sa_avg < min_avg:
            min_avg = sa_avg
            min_avg_index = start_index
        start_index += 1
        end_index += 1
    return min_avg_index


@print_inp_op
def matching_subarray_sum(A, B, matching_sum):
    sum_0 = sum(A[:B])
    if sum_0 == matching_sum:
        return 1

    for i in range(1, len(A) - B):
        window_sum = sum_0 - A[i] + A[i+B-1]
        if window_sum == matching_sum:
            return 1


    return 0


matching_subarray_sum([1,2,3], 1, 6)
