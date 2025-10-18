from decorators.decorators_util import print_inp_op


@print_inp_op
def smallest_sa_avg_index_brute_force(inp_arr, b):
    avg = 10 ** 5
    index = -1
    n = len(inp_arr)
    for i in range(0, n - b + 1):
        curr_sa_avg = sum(inp_arr[i:i + b]) / b
        if curr_sa_avg < avg:
            avg = curr_sa_avg
            index = i
    return index


# smallest_sa_avg_index_brute_force([3, 7, 90, 20, 10, 50, 40], 3)
# smallest_sa_avg_index_brute_force([3, 7, 5, 20, -10, 0, 12], 2)
smallest_sa_avg_index_brute_force([20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11], 9)


@print_inp_op
def smallest_sa_avg_index_sliding_window(inp_arr, b):
    avg = 10 ** 5
    index = -1
    n = len(inp_arr)

    start = 0
    end = start + b -1
    curr_sum = sum(inp_arr[start:end+1])

    while start <= n - b:
        curr_avg = curr_sum / b
        if curr_avg < avg:
            avg = curr_avg
            index = start
        end += 1
        if end < n:
            curr_sum = curr_sum - inp_arr[start] + inp_arr[end]
        start += 1
    return index

# smallest_sa_avg_index_sliding_window([3, 7, 90, 20, 10, 50, 40], 3)
# smallest_sa_avg_index_sliding_window([3, 7, 5, 20, -10, 0, 12], 2)
smallest_sa_avg_index_sliding_window([20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11], 9)