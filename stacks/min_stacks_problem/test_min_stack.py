import time
from stacks.min_stacks_problem.min_stack import MinStack


# Positive Test Case 1: Basic stack usage
def test_push_pop_getmin_normal():
    stack = MinStack()
    stack.push(5)
    stack.push(2)
    stack.push(8)
    assert stack.get_min() == 2
    stack.pop()
    assert stack.top() == 2
    assert stack.get_min() == 2
    stack.pop()
    assert stack.get_min() == 5


# Positive Test Case 2: Push same min multiple times
def test_duplicate_mins():
    stack = MinStack()
    stack.push(3)
    stack.push(3)
    stack.push(3)
    assert stack.get_min() == 3
    stack.pop()
    assert stack.get_min() == 3
    stack.pop()
    assert stack.get_min() == 3
    stack.pop()
    assert stack.get_min() == -1


# Negative Test Case 1: Pop from empty stack
def test_pop_empty():
    stack = MinStack()
    stack.pop()  # Should not raise an error
    assert stack.get_min() == -1
    assert stack.top() == -1


# Negative Test Case 2: get_min/top on empty stack
def test_getmin_top_empty():
    stack = MinStack()
    assert stack.get_min() == -1
    assert stack.top() == -1


# TLE Test Case: 10^6 operations under time threshold
def test_stress_performance():
    stack = MinStack()
    n = 10 ** 6
    start = time.time()

    for i in range(n):
        stack.push(i)

    for _ in range(n):
        _ = stack.get_min()
        stack.pop()

    end = time.time()
    assert (end - start) < 2.0, "TLE: Stack operations exceeded time limit"
