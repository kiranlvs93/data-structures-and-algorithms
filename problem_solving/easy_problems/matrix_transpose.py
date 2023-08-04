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


print(get_transpose(array_to_transpose))
