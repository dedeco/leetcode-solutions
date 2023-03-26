"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
          10
       5     15
      / \    / \
     3   7  null 18

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:

             10
        5         15
      /   \     /   \
     3     7   13   18
   /  \   /
  1 null 6

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""

from typing import Optional

from basic.range_sum_of_bst import TreeNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total = 0

    def dfs(self, root: Optional[TreeNode], low: int, high: int):
        if root:
            if low <= root.val <= high:
                self.total += root.val
            if root.val > low:
                self.dfs(root.left, low, high)
            if root.val < high:
                self.dfs(root.right, low, high)
        return

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.dfs(root, low, high)
        return self.total

    def insert(self, node: Optional[TreeNode], data):
        if node is None:
            return TreeNode(data)

        if data < node.val:
            node.left = self.insert(node.left, data)
        elif data > node.val:
            node.right = self.insert(node.right, data)

        return node


# Driver Code
if __name__ == '__main__':

    # Let us create following BST
    #      50
    #    30  70
    #   / \   / \
    #  20 40  60 80

    bst = Solution()
    root = None
    root = bst.insert(root, 50)
    bst.insert(root, 30)
    bst.insert(root, 20)
    bst.insert(root, 40)
    bst.insert(root, 70)
    bst.insert(root, 60)
    bst.insert(root, 80)
    assert bst.rangeSumBST(root, 20, 60) == 200
