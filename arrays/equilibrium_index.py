from decorators.decorators_util import print_inp_op


@print_inp_op
def equilibrium_index(inp_arr):
    pfs = [inp_arr[0]]
    for ele in inp_arr[1:]:
        pfs.append(pfs[-1] + ele)
    print(f"{pfs=}")

    n = len(inp_arr)
    for i in range(n):
        if i == 0:
            l_sum = 0
        else:
            l_sum = pfs[i - 1]

        u_sum = pfs[n - 1] - pfs[i]

        if l_sum == u_sum:
            return i

    return -1


equilibrium_index([-7, 1, 5, 2, -4, 3, 0])
equilibrium_index([1, 2, 3])
equilibrium_index([1, 2, 3, 7, 1, 2, 3])
