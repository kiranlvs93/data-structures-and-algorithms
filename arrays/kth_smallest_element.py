from decorators.decorators_util import print_inp_op


@print_inp_op
def kth_smallest_element_bubble_sort(inp_arr, k):
    n = len(inp_arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if inp_arr[j + 1] < inp_arr[j]:
                inp_arr[j], inp_arr[j + 1] = inp_arr[j + 1], inp_arr[j]
    print(inp_arr)
    return inp_arr[k - 1]


# kth_smallest_element_bubble_sort([3, 2, 1], 1)
# kth_smallest_element_bubble_sort([0, 3, 2, 1, 7], 1)
# kth_smallest_element_bubble_sort([2, 1, 4, 3, 2], 3)
# kth_smallest_element_bubble_sort([1, 2], 2)


@print_inp_op
def kth_smallest_element_selection_sort(arr, k):
    n = len(arr)
    for i in range(n):
        small = arr[0]
        index = 0
        for j in range(n - i):
            if arr[j] < small:
                small = arr[j]
                index = j
        arr[j], arr[index] = arr[index], arr[j]
        if i == k:
            break
    print(arr)
    return arr[-k]

kth_smallest_element_selection_sort([3, 2, 1], 1)
kth_smallest_element_selection_sort([0, 3, 2, 1, 7], 1)
kth_smallest_element_selection_sort([2, 1, 4, 3, 2], 3)
kth_smallest_element_selection_sort([1, 2], 2)