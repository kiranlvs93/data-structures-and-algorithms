from decorators.decorators_util import print_inp_op


@print_inp_op
def sum_of_even_indexed_in_range(inp_arr, query):
    # calculate PFS
    # for odd index, carry forward prev index sum
    pfs = [inp_arr[0]]
    for idx in range(1, len(inp_arr)):
        if idx & 1:
            pfs.append(pfs[-1])
        else:
            pfs.append(pfs[-1] + inp_arr[idx])

    print(f"{pfs=}")
    # iterate through the query and find the sum from PFS
    range_sum = []
    for q in query:
        if q[0] == 0:
            range_sum.append(pfs[q[1]])
        else:
            range_sum.append(
                pfs[q[1]] - pfs[q[0] - 1]
            )
    return range_sum


sum_of_even_indexed_in_range([2, 8, 3, 9, 15], [[1, 4], [0, 2], [2, 3]])
sum_of_even_indexed_in_range([5, 15, 25, 35, 45], [[1, 1], [0, 0]])
