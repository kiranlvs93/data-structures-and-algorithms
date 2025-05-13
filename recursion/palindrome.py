def palindrome(inp_str, start, end):
    if start > end:
        return 1
    if inp_str[start] != inp_str[end]:
        return 0
    return palindrome(inp_str, start + 1, end - 1)


# print(palindrome("abcba", 0, -1))


def palindrome1(inp_str, start, end):
    if start > end:
        return 1
    if inp_str[start] == inp_str[end] and palindrome1(inp_str, start + 1, end - 1):
        return True
    return False


print(palindrome1("abcba", 0, -1))



