class MinStack:
    """
    A stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Internally uses two stacks:
    - `array` for storing all elements.
    - `min_stack` for keeping track of the current minimum at each level.
    """

    def __init__(self) -> None:
        """
        Initializes an empty MinStack.
        """
        self.array = list()
        self.min_stack = list()

    def push(self, x: int) -> None:
        """
        Pushes an element onto the stack.
        Also updates the min_stack if the new element is smaller than or equal to the current minimum.

        :param x: Integer value to be pushed onto the stack
        """
        self.array.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        """
        Removes the top element from the stack.
        Also pops from the min_stack if the removed element is the current minimum.
        """
        if not self.is_empty():
            ele = self.array.pop()
            if len(self.min_stack) > 0 and self.min_stack[-1] == ele:
                self.min_stack.pop()

    def top(self) -> int:
        """
        Returns the top element of the stack.

        :return: Top element if stack is not empty, else -1
        """
        if not self.is_empty():
            return self.array[-1]
        else:
            return -1

    def get_min(self) -> int:
        """
        Retrieves the minimum element in the stack.

        :return: Minimum element if stack is not empty, else -1
        """
        if not self.is_empty():
            return self.min_stack[-1]
        else:
            return -1

    def is_empty(self) -> bool:
        """
        Checks whether the stack is empty.

        :return: True if the stack is empty, else False
        """
        return len(self.array) == 0
