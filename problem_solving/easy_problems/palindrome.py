"""
Find if a string is a palindrome or not.
"""


def palindrome_best_method(inp_str: str):
    """
    Space complexity O(1)
    Time complexity O(n)
    :param inp_str:
    :return:
    """
    for i in range(len(inp_str) // 2):
        if inp_str[-i] != inp_str[i - 1]:
            return False
    return True


def palindrome_new_str(inp_str: str):
    """
    Space complexity O(n)
    Time complexity O(n^2) since we are creating a new string at each iteration
    :param inp_str:
    :return:
    """
    rev_str = ""
    for i in reversed(range(len(inp_str))):  # O(n)
        rev_str += inp_str[i]  # O(n)
    return rev_str == inp_str


def palindrome_new_str_array(inp_str: str):
    """
    Space complexity O(n)
    Time complexity O(n)
    :param inp_str:
    :return:
    """
    rev_str = []
    for i in reversed(range(len(inp_str))):  # O(n)
        rev_str.append(inp_str[i])
    return "".join(rev_str) == inp_str


def palindrome_slicing(string: str):
    """
    Space complexity O(n) - Since we create a new reversed string of the same length as the input string
    Time complexity O(n)
    :param string:
    :return:
    """
    return string[::-1] == string


def palindrome_recursion(inp_str: str):
    """
    Space complexity O(n/2) ~ O(n) since each recursion call adds to the call stack
    Tail recursion can reduce the Space complexity to O(1)
    Time complexity O(n)
    :param inp_str:
    :return:
    """
    print(f"*******{inp_str}")
    if len(inp_str) <= 1:
        return True
    else:
        return inp_str[0] == inp_str[-1] and palindrome_recursion(inp_str[1:-1])


print(palindrome_new_str_array("aabaa"))
