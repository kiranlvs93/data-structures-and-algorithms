"""
Problem Description:
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Problem Constraints
1 <= number of nodes <= 105
-100000 <= B, value of nodes <= 100000

Input Format:
First argument is a root node of the binary tree, A.
Second argument is an integer B denoting the sum.

Output Format:
Return 1, if there exist root-to-leaf path such that adding up all the values along the path equals the given sum. Else, return 0.

Example Input:
Input 1:
 Tree:    5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1

 B = 22

Input 2:
 Tree:    5
         / \
        4   8
       /   / \
     -11 -13  4

 B = -1

Example Output:
Output 1: 1
Output 2: 0
"""


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_path_sum(root: TreeNode, k):
    if root is None:
        return 0

    # Check if the leaf node (both left and right are None) and value = k
    if root.left is None and root.right is None and root.value == k:
        return True

    # If left subtree matches, return 1
    left_match = check_path_sum(root.left, k - root.value)
    if left_match:
        return 1
    # If left subtree matches, return 1
    right_match = check_path_sum(root.left, k - root.value)
    if right_match:
        return 1
    return 0
