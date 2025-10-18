from decorators.decorators_util import print_inp_op


@print_inp_op
def special_sub_seq(inp_str):
    count_a = 0
    count_ag = 0

    for ch in inp_str:
        if ch == 'A':
            count_a += 1
        if ch == 'G':
            count_ag += count_a
    return count_ag


special_sub_seq("ABCGAG")
special_sub_seq("GAB")