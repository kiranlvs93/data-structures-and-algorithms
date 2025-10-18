from decorators.decorators_util import print_inp_op


@print_inp_op
def range_sum_query(inp_arr, query):
    # calculate pre fix sum
    pfs = [inp_arr[0]]
    n = len(inp_arr)
    for i in range(1, n):
        pfs.append(pfs[i - 1] + inp_arr[i])

    print(f"{pfs=}")
    # calculate the range_sum
    # sum of arr[i,j] = pfs[j] - pfs[i-1]
    range_sum = []
    for q in query:
        s = q[0]
        e = q[1]
        if s > 0:
            range_sum.append(pfs[e] - pfs[s - 1])
        else:
            range_sum.append(pfs[e])
    return range_sum


# range_sum_query([1, 2, 3], [[1,2],[0,2]])
# range_sum_query([1, 2, 3, 4, 5], [[0,3],[1,2]])
# range_sum_query([2, 2, 2], [[0,0],[1,2]])
range_sum_query([-7, 1, 5, 2, -4, 3, 0], [[1, 1], [0, 0]])
