inp_arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def rec_sum(arr):
    """
    Sum of array O(n) | O(d)
    :param arr:
    :return:
    """
    sum_pdt = 0
    for i in range(len(arr)):
        if type(ele := arr[i]) == list:
            sum_pdt += rec_sum(ele)
        else:
            sum_pdt += ele
    return sum_pdt


def sum_pdt_recursion(arr, depth=1):
    """
    Time complexity O(n) where n is the total number of elements in the main array + sub array
    E.g., [1,[2,[3,4]],5] has these elements
    * At first level -> 1, [2,[3,4]], 5 -> 3
    * At second level -> 2,[3,4] -> 2
    * At third level -> [3,4] -> 2
    * Total = 3 + 2 + 2 = 7 elements
    Space complexity O(D) - D is the greatest depth of the sub-array
    :param arr:
    :param depth:
    :return:
    """
    sum_pdt = 0
    for ele in arr:
        if type(ele) is list:
            sum_pdt += sum_pdt_recursion(ele, depth + 1)
        else:
            sum_pdt += ele
    return sum_pdt * depth


# print("Sum of array is::", rec_sum(inp_arr))
print("Sum product of array is::", sum_pdt_recursion(inp_arr, 1))
