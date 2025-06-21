from decorators.decorators_util import print_inp_op

@print_inp_op
def search_insert(arr, se):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if se == arr[mid] :
            return mid
        elif se < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    return low

search_insert(arr = [1,3,5], se = 4)