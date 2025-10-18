from decorators.decorators_util import print_inp_op


@print_inp_op
def minimum_cost(arr: list):
    arr.sort(reverse=True)
    initial_sum  = sum(arr)
    cost = initial_sum

    for ele in arr:
        initial_sum = initial_sum - ele
        cost += initial_sum

    return cost

minimum_cost([1,2,3])
minimum_cost([1,2])
minimum_cost([5])