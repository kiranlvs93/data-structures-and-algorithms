def using_loop(inp: str):
    print("Reversed by looping...")
    rev_str = ""
    for i in range(len(inp) - 1, -1, -1):
        rev_str += inp[i]
    print(rev_str)


def by_concatenating(inp: str):
    print("Reversed by looping and concatenating...")
    rev_str = ""
    for ch in inp:
        rev_str = ch + rev_str
    print(rev_str)


def by_slicing(inp: str):
    print("Reversed by slicing...")
    print(inp[::-1])


if __name__ == '__main__':
    inp_str = "abcd"
    using_loop(inp_str)
    by_slicing(inp_str)
    by_concatenating(inp_str)
