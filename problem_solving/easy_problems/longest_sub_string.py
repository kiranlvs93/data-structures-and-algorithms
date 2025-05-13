from decorators.decorators_util import print_inp_op


@print_inp_op
def longest_non_repeating_sub_string(inp_str):
    left, right = 0, 0
    max_count = 0
    chars = set()
    while right < len(inp_str):
        while inp_str[right] in chars:
            chars.remove(inp_str[left])
            left += 1
        chars.add(inp_str[right])
        right += 1
        max_count = max(max_count, len(chars))
    return max_count


# longest_non_repeating_sub_string("dadbc")
# longest_non_repeating_sub_string("abba")
# longest_non_repeating_sub_string("abcabcbb")

A = [1, -1, 3, 4, 5]
N = len(A)


@print_inp_op
def sa_sum_zero():
    for i in range(N):
        sa_sum = 0
        for j in range(i, N):
            sa_sum += A[j]
            if sa_sum == 0:
                return 1

    return 0


sa_sum_zero()
