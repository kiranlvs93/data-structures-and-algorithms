def solve(A):
    factors = 0
    if A == 1:
        return 0
    for i in range(1, A+1):
        if A % i == 0:
            factors += 1
        if factors > 2:
            return 0
    return 1

# print(solve(374980901))
import math


def factors(A: int) -> int:
    count = 0
    for i in range(1, int(A ** 0.5) + 1):  # Loop till sqrt(A)
        if A % i == 0:
            if i == A // i:
                count += 1  # Perfect square case
            else:
                count += 2  # Pair of divisors
    return count

# print(factors(36))

def is_prime_no(A):
    """

    :param A:
    :return:
    """
    if A == 1:
        return 0
    for i in range(2, math.isqrt(A)+1):
        if A% i == 0:
            return 0
    return 1

# print(is_prime_no(2))

def count_prime_nos(a):
    count = 0
    for n in range(2, a+1):
        if is_prime_no(n):
            count += 1
    return count

# print(count_prime_nos(19))

import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        sum_of_factors = 0
        for i in range(1,math.isqrt(A)+1):
            if A % i == 0:
                if A//i == i:
                    sum_of_factors += i
                else:
                    sum_of_factors += i + A//i
        if sum_of_factors == A:
            return

