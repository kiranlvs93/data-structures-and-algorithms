"""
Problem Description
-------------------
Design a stack that supports **push**, **pop**, **top**, and **retrieving the minimum element** in constant time.
    push(x)  -- Push element x onto stack.
    pop()    -- Removes the element on top of the stack.
    top()    -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

NOTE:
-----
- All the operations have to be constant time operations.
- getMin() should return -1 if the stack is empty.
- pop() should return nothing if the stack is empty.
- top() should return -1 if the stack is empty.


Problem Constraints
-------------------
1 <= Number of Function calls <= 10^6
It is guaranteed that at least one call is made to either getMin() or top().

Input Format
------------
Functions will be called by the checker code automatically.

Output Format
-------------
Each function should return the values as defined by the problem statement.

Example Input
-------------
Input 1:
    push(1)
    push(2)
    push(-2)
    getMin()
    pop()
    getMin()

Example Output
--------------
    -2
     1

Explanation
-----------
After pushing 1, 2, -2 -> Stack becomes [1, 2, -2] with min -2
getMin() returns -2
pop() removes -2 -> Stack becomes [1, 2]
getMin() now returns 1

"""


class Stack:
    """
    A simple stack implementation using Python's built-in list.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        :return: None
        """
        self.array = list()

    def pop(self):
        """
         Removes and returns the top element of the stack.
        :return: Top element if stack is not empty, else None
        :rtype: Any or None
        :return:
        """
        if not self.is_empty():
            return self.array.pop()

    def top(self):
        """

        :return:
        """
        if not self.is_empty():
            return self.array[-1]

    def push(self, ele) -> None:
        """
        Pushes an element onto the top of the stack.
        :param ele: Element to be added to the stack
        """
        self.array.append(ele)

    def is_empty(self) -> bool:
        return len(self.array) == 0

    def get_size(self) -> int:
        """
        Returns the number of elements in the stack.
        """
        return len(self.array)

    def clear(self) -> None:
        """
        Removes all elements from the stack.
        :return: None
        """
        self.array.clear()

    def __contains__(self, ele) -> bool:
        """
        Checks if an element exists in the stack.
        :param ele: Any
        """
        return ele in self.array

    def __repr__(self) -> str:
        return f"{''.join(map(str, self.array))}"
