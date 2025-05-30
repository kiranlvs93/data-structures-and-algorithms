from decorators.decorators_util import print_inp_op


@print_inp_op
def post_fix_operations(inp: list[str]):
    stack = list()
    res = -1

    def operate(x, y, operand):
        if operand == "*":
            return x * y
        elif operand == "-":
            return x - y
        elif operand == "+":
            return x + y
        elif operand == "/":
            return x // y

    for ele in inp:
        if (ele.startswith("-") and len(ele) > 1) or ele.isdigit():
            stack.append(ele)
        else:
            b = stack.pop()
            a = stack.pop()
            res = operate(int(a), int(b), ele)
            stack.append(res)
    return res


# post_fix_operations(['5','2','*', '3', '-'])
# post_fix_operations(['3', '5', '+', '2', '-', '2', '5', '*', '-'])
# post_fix_operations(['-500','-10','/'])
post_fix_operations(["5", "1", "2", "+", "4", "*", "+", "3", "-"])
