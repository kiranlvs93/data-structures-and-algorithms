"""
Leetcode - Array - Easy

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""
from decorators.decorators_util import print_inp_op

s = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l", ":",
     " ", "P", "a", "n", "a", "m", "a"]


# s = ["a", "b", "c", "d"]
# s = ["h", "a", "n", "n", "a", "H"]
# s = ["h", "e", "l", "l", "o"]


@print_inp_op
def swapping_in_place(inp):
    rev = inp[::-1]
    print(f"Expected reversed string {rev}")
    iterations = len(inp) // 2
    for i in range(iterations):
        inp[i], inp[-i - 1] = inp[-i - 1], inp[i]
    print(f"Reversed string          {inp}")
    return inp == rev


@print_inp_op
def two_pointer_approach(inp):
    rev = inp[::-1]
    print(f"Expected reversed string {rev}")
    left, right = 0, len(inp) - 1
    while left < right:
        inp[left], inp[right] = inp[right], inp[left]
        left += 1
        right -= 1
    print(f"Reversed string          {inp}")
    return inp==rev


# swapping_in_place(s)
two_pointer_approach(s)
