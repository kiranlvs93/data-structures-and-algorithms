"""
Problem Description
Given a number A, check if it is a magic number or not.
A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1, then the number is a magic number.

Problem Constraints
1 <= A <= 109

Input Format
The first and only argument is an integer A.

Output Format
Return an 1 if the given number is magic else return 0.

Example Input
Input 1: A = 83557
Input 2: A = 1291

Example Output
Output 1: 1
Output 2: 0
"""


def sum_of_digits(n):
    """
    Time Complexity - O(N) - length of the stack
    Space Complexity - O(N) - Since there are N stacks
    :param n:
    :return:
    """
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


x = 1291

while x >= 10:
    x = sum_of_digits(x)
print(x)
