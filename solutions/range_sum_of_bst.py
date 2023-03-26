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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from basic.range_sum_of_bst import TreeNode


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
