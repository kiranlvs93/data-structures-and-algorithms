from decorators.decorators_util import print_inp_op


@print_inp_op
def longest_palindrome_length(inp: str):
    if len(inp) == 1:
        return inp

    max_len = 0
    n = len(inp)

    for center in range(n):
        # odd length palindrome
        left = right = center

        while left >= 0 and right < n:
            if inp[left] != inp[right]:
                break
            left -= 1
            right += 1

        max_len = max(max_len, right - left - 1)

        # even length palindrome
        left = center
        right = center + 1

        while left >= 0 and right < n:
            if inp[left] != inp[right]:
                break
            left -= 1
            right += 1

        max_len = max(max_len, right - left - 1)

    return max_len


longest_palindrome_length("madam")
longest_palindrome_length("aabb")
longest_palindrome_length("aaabaaa")
longest_palindrome_length("abb")
longest_palindrome_length("bb")
longest_palindrome_length("a")
longest_palindrome_length("c")
longest_palindrome_length("ac")
longest_palindrome_length("acbbca")
longest_palindrome_length("aaaabaaa")
longest_palindrome_length("anaacbbca")
longest_palindrome_length("cacaccbabcabbbaacbbbbcaaaccaacbabcaccbccaacccaacbbaaabbbabcaaabc")
