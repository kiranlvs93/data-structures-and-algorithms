def factorial_using_for_loop(n: int):
    """
    Finding factorial using for loop
    :param n:
    :return:
    """
    fact = 1
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            fact *= i
        return fact


def factorial_using_recursion(n: int):
    """
    Finding factorial using recursion
    :param n:
    :return:
    """
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_using_recursion(n - 1)


if __name__ == '__main__':
    nos = [-1, 0, 1, 5]
    for no in nos:
        # print(f"Factorial for no {no} is {factorial_using_for_loop(no)}")
        print(f"Factorial for no {no} is {factorial_using_recursion(no)}")
