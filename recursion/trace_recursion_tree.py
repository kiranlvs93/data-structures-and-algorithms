def trace_forward_example(n):
    """
    Example to show trace forward recursion
    :param n:
    :return:
    """
    if n > 0:
        print("Forward ", n)
        trace_forward_example(n - 1)


def trace_backward_example(n):
    """
    Example to show trace backward recursion
    :param n:
    :return:
    """
    if n > 0:
        trace_backward_example(n - 1)
        print("Backward", n)


def trace_forward_backward_example(n):
    """
    Example to show trace forward/backward recursion
    :param n:
    :return:
    """
    if n > 0:
        print("Forward ", n)
        trace_forward_backward_example(n - 1)
        print("Backward", n)


def tree_recursion(n):
    if n > 0:
        print("Forward ", n)
        tree_recursion(n - 1)
        tree_recursion(n - 1)
        print("Backward ", n)


if __name__ == '__main__':
    # trace_forward_example(3)
    # trace_backward_example(3)
    # trace_forward_backward_example(3)
    tree_recursion(3)
