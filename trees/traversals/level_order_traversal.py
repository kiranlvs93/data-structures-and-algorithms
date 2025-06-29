from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order_traversal(head: TreeNode):
    # Create a queue to add the nodes of a level
    q = deque()

    # Result list which is a list of lists, where each level is a list
    solution = list()

    # Add the node to the queue
    q.append(head)

    # For each node in the queue, starting left, find the nodes in next level and add them to queue
    while len(q) != 0:
        size = len(q)
        level = list()
        for _ in range(size):
            node = q.popleft()

            level.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        solution.append(level)
    return solution
