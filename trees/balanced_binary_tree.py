"""
Given a root of binary tree A, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Problem Constraints
1 <= size of tree <= 100000

Input Format
First and only argument is the root of the tree A.

Output Format:
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Example Input:
Input 1:
    1
   / \
  2   3

Input 2:
       1
      /
     2
    /
   3
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_height_balanced(root: TreeNode):
    """
    Function to check if the Tree is height balanced
    :param root:
    :return: (bool, ht)
    """
    if root is None:
        return True, -1

    # Check if left subtree is height is balanced
    left_bal, left_ht = check_height_balanced(root.left)
    if not left_bal:
        return False, -1

    # Check if right subtree is height is balanced
    right_bal, right_ht = check_height_balanced(root.right)
    if not right_bal:
        return False, -1

    # If the height is balanced, return True
    if abs(left_ht - right_ht) <= 1:
        return True, max(left_ht, right_ht) + 1

    # If the height is not balanced, return False, in the end
    return False, -1
