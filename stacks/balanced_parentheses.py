from decorators.decorators_util import print_inp_op


@print_inp_op
def is_valid_parentheses(inp):
    brackets = {"}": "{", ")": "(", "]": "["}
    stack = []

    for ele in inp:
        if ele in brackets.values():
            stack.append(ele)
        else:
            if len(stack) == 0 or brackets[ele] != stack.pop():
                return False
    return len(stack) == 0


# is_valid_parentheses("{{[{}][}}](())(")
# is_valid_parentheses("{{[{}]}}")
is_valid_parentheses("{{[{}]}}[](()))")
