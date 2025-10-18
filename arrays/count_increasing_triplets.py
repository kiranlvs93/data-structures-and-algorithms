from decorators.decorators_util import print_inp_op


@print_inp_op
def counting_triplets(arr: list):
    n = len(arr)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] < arr[j] < arr[k]:
                    count += 1
    return count


counting_triplets([1, 2, 4, 3])
counting_triplets([2, 1, 2, 3])
counting_triplets([1, 2, 4, 3, 9, 5])
