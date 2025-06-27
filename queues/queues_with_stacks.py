"""
Implement a First In First Out (FIFO) queue using stacks only.

The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the UserQueue class:

void push(int X) : Pushes element X to the back of the queue.
int pop() : Removes the element from the front of the queue and returns it.
int peek() : Returns the element at the front of the queue.
boolean empty() : Returns true if the queue is empty, false otherwise.
NOTES:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Problem Constraints:
1 <= X <= 109
At most 1000 calls will be made to push, pop, peek, and empty function.
All the calls to pop and peek are valid. i.e. pop and peek are called only when the queue is non-empty.

Example Input:
Input 1:
1) UserQueue()
 2) push(20)
 3) empty()
 4) peek()
 5) pop()
 6) empty()
 7) push(30)
 8) peek()
 9) push(40)
 10) peek()

Input 2:
1) UserQueue()
 2) push(10)
 3) push(20)
 4) push(30)
 5) pop()
 6) pop()


Example Output:
Output 1:
 false
 20
 20
 true
 30
 30

Output 2:
 10
 20
"""


from stacks.stack import Stack


class UserQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.push_stack.is_empty() and self.pop_stack.is_empty()


q = UserQueue()
q.push(20)
print(q.empty())
print(q.peek())
q.pop()
print(q.empty())
q.push(30)
print(q.peek())
q.push(40)
print(q.peek())
print(q)