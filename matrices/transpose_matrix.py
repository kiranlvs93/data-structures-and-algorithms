from decorators.decorators_util import print_inp_op


@print_inp_op
def transpose_square_matrix(matrix: list[list]):
    """
    TC - O(N2) | SC - O(1)
    :param matrix:
    :return:
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(row, cols):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

    return matrix


# transpose_square_matrix([[1,2],[3,4]])
# transpose_square_matrix([[1,2,3],[4,5,6],[7,8,9]])
# transpose_square_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
transpose_square_matrix([[1, 2], [1, 2], [1, 2]])
