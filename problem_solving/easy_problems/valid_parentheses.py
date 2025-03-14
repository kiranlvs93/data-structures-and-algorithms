"""
LeetCode - Easy - String

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
def check_valid_parentheses(s):
    """
    Time Complexity - O(N) since we are iterating through the N elements, where N = length of S
    Space Complexity - O(N) + O(1) = O(N)
        Parentheses_map - has O(1) space
        Stack has O(N) space

    :param s: s is the input string of parentheses
    :return:
    """
    # If the string doesn't have even characters, then it is not valid because, valid parentheses always occur in pairs
    if len(s) % 2 != 0:
        return False
    # Initialise the closing brackets with the opening brackets
    parentheses_map = {"{": "}", "(": ")", "[": "]"}
    # List acting as a stack - FIFO
    stack = list()
    for bracket in s:
        if bracket in parentheses_map.keys():
            stack.append(bracket)
        elif len(stack) == 0 or bracket != parentheses_map[stack.pop()]:
            return False
    return len(stack) == 0

print(check_valid_parentheses("{}[]()"))
print(check_valid_parentheses("((()))"))
print(check_valid_parentheses(")))"))
print(check_valid_parentheses("]["))
print(check_valid_parentheses("([{}])"))
print(check_valid_parentheses("{[(])}"))
