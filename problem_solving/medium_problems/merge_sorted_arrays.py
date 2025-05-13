from decorators.decorators_util import print_inp_op

@print_inp_op
def merge_sorted_arrays(arr_a, arr_b):
    # Start iterating for both the arrays as 0th position
    i, j = 0, 0

    # Create an empty result list
    result = list()

    # Iterate through both the input arrays
    # Populate the result based on the conditions
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] <= arr_b[j]:
            result.append(arr_a[i])
            i += 1
        elif arr_b[j] < arr_a[i]:
            result.append(arr_b[j])
            j += 1

    # Append the remaining elements to the result
    while i < len(arr_a):
        result.append(arr_a[i])
        i += 1
    while j < len(arr_b):
        result.append(arr_b[j])
        j += 1
    return result



merge_sorted_arrays([1,2,3,4,9,10], [1,8])
