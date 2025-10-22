from decorators.decorators_util import print_inp_op


@print_inp_op
def rotate_matrix(matrix: list[list]):
    """
    TC - O(N2) | SC - O(1)
    :param matrix:
    :return:
    """

    rows = len(matrix)
    cols = len(matrix[0])

    # transpose the matrix
    for row in range(rows):
        for col in range(row, cols):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

    # reverse each row
    for row in range(rows):
        matrix[row] = matrix[row][::-1]
    return matrix


rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
rotate_matrix([[1, 2], [3, 4]])
