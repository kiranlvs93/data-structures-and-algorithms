from decorators.decorators_util import print_inp_op


@print_inp_op
def row_wise_sum(arr):
    for row in arr:
        print(f"Sum of {row} -> {sum(row)}")


# row_wise_sum([[1, 1, 1], [2, 2, 2], [3, 3, 3]])


@print_inp_op
def col_wise_sum(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    for col in range(col_len):
        col_sum = 0
        for row in range(row_len):
            col_sum += arr[row][col]
        print(col_sum)


# col_wise_sum([[1, 1, 1], [2, 2, 2], [3, 3, 3]])


@print_inp_op
def principal_diagonal_sum(arr):
    """
    Brute force approach
    :param arr:
    :return:
    """
    row_len = len(arr)
    col_len = len(arr[0])
    diagonal_sum = 0

    for col in range(col_len):
        for row in range(row_len):
            if col == row:
                diagonal_sum += arr[row][col]
    return diagonal_sum


# principal_diagonal_sum([[1, 1, 1], [2, 2, 2], [3, 3, 3]])


@print_inp_op
def principal_diagonal_sum_optimised(arr):
    """
    Optimised to time complexity O(N) with space complexity O(1)
    :param arr:
    :return:
    """
    row_len = len(arr)
    diagonal_sum = 0

    for row in range(row_len):
        diagonal_sum += arr[row][row]
    return diagonal_sum


# principal_diagonal_sum_optimised([[1, 2, 3],
#                                   [4, 5, 6],
#                                   [7, 8, 9]])


@print_inp_op
def anti_diagonal_sum_optimised(arr):
    """
    Optimised to time complexity O(N) with space complexity O(1)
    :param arr:
    :return:
    """
    row_len = len(arr)
    diagonal_sum = 0

    for row in range(row_len):
        diagonal_sum += arr[row][row_len - row - 1]
    return diagonal_sum


# anti_diagonal_sum_optimised([[1, 2, 6],
#                              [4, 6, 6],
#                              [7, 8, 9]])


def sum_diagonals_in_rectangular_matrix(arr):
    # todo
    pass


@print_inp_op
def make_all_rows_or_cols_zero(arr):
    # Iterate all rows
    for row in range(len(arr)):
        # if there is a zero in the row, mark all non-zero elements as -1 and leave the zero elements intact
        if 0 in arr[row]:
            arr[row] = [-1 if ele > 0 else ele for ele in arr[row]]

    # Iterate all cols
    for col in range(len(arr[0])):
        # if there is a zero in the col, mark all non-zero elements as -1 and leave the zero elements intact
        for row in range(len(arr)):
            if arr[row][col] == 0:
                for row_1 in range(len(arr)):
                    arr[row_1][col] = -1
                break
    # Iterate the entire matrix again and if you find any -1, mark it as 0
    for row in range(len(arr)):
        if -1 in arr[row]:
            arr[row] = [0 if ele == -1 else ele for ele in arr[row]]
    return arr


# make_all_rows_or_cols_zero([[97,18,55,1,50,17,16,0,22,14],[58,14,75,54,11,23,54,95,33,23],[73,11,2,80,6,43,67,82,73,4],[61,22,23,68,23,73,85,91,25,7],[6,83,22,81,89,85,56,43,32,89],[0,6,1,69,86,7,64,5,90,37],[10,3,11,33,71,86,6,56,78,31],[16,36,66,90,17,55,27,26,99,59],[67,18,65,68,87,3,28,52,9,70],[41,19,73,5,52,96,91,10,52,21]])

@print_inp_op
def count_triplets(arr):
    """
    Brute Force approach
    :param arr:
    :return:
    """
    arr_len = len(arr)
    triplets = 0
    for i in range(arr_len):
        for j in range(i + 1, arr_len):
            for k in range(j + 1, arr_len):
                if arr[i] < arr[j] < arr[k]:
                    triplets += 1
    return triplets


# count_triplets([2, 1, 2, 3])


@print_inp_op
def count_triplets_optimised(arr):
    """
    For each element, find the number of elements on the
    1. left which are smaller than that number
    2. right which are larger than that number
    The product of left and right gives the valid triplets
    :param arr:
    :return:
    """
    arr_len = len(arr)
    triplets = 0
    for i in range(1, arr_len):
        left = 0
        for ele in arr[:i]:
            if ele < arr[i]:
                left += 1
        right = 0
        for ele in arr[i + 1:]:
            if ele > arr[i]:
                right += 1
        triplets += left * right
    return triplets


# count_triplets([2, 1, 2, 3])


@print_inp_op
def scaler_multiplication(arr, b):
    for i in range(len(arr)):
        arr[i] = [b * ele for ele in arr[i]]
    return arr


# scaler_multiplication([[1, 2, 3],
#                        [4, 5, 6],
#                        [7, 8, 9]], 2)

@print_inp_op
def get_transpose(arr):
    rows = len(arr)
    cols = len(arr[0])
    transpose = [rows * [0] for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            transpose[col][row] = arr[row][col]
    return transpose


# get_transpose([[1, 2, 3, 10],
#                [4, 5, 6, 11],
#                [7, 8, 9, 12],
#                [9, 9, 9, 9],
#                ])
# get_transpose([[1, 2], [3, 4], [5, 6]])


# def transpose_in_place(arr):
#     n = len(arr)
#     for i in range(1,n):
#         print(arr[])


@print_inp_op
def rotate_by_90_degree(arr):
    """
    Rotate the array by 90 degree
    :param arr:
    :return:
    """
    # transpose in place
    for row in range(len(arr)):
        for col in range(row, len(arr)):
            arr[row][col], arr[col][row] = arr[col][row], arr[row][col]
    # reverse the elements in each row
    for row in range(len(arr)):
        arr[row] = arr[row][::-1]

    return arr


rotate_by_90_degree([
    [1, 2],
    [3, 4],
])

rotate_by_90_degree([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
