array_to_transpose = [
    [1, 2, 3],
    [4, 5, 6],
    # [7, 8, 9]
]


def get_transpose(array):
    """
    Transpose a matrix
    Time complexity - O (w*h) where w- width | h - height
    Space complexity - O (w*h) where w- width | h - height
    :param array:
    :return:
    """
    transpose = []
    for col in range(len(array[0])):
        new_row = []
        for row in range(len(array)):
            new_row.append(array[row][col])
        transpose.append(new_row)
    return transpose


def get_transpose_one_liner(array):
    """
    The "*" sign unpacks the matrix (removes the outer brackets).
    The "zip" function for each row, takes all the elements at index i, for each i, and forms a column,
    thus returning in the end an unpacked transposed matrix.
    The "list" function packs it back to a matrix.
    :param array:
    :return:
    """
    return list(zip(*array))


print(get_transpose(array_to_transpose))
print(get_transpose_one_liner(array_to_transpose))
