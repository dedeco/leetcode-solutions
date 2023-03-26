from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root: Optional[TreeNode], low: int, high: int):
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    total += node.val
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return total

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)

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
