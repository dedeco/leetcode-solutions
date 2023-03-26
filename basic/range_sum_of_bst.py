from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def interative_search(self, root: Optional[TreeNode], key):
        while root is not None:
            if root.val == key:
                return True
            elif key > root.val:
                root = root.right
            else:
                root = root.left
        return False

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
    if bst.interative_search(root, 15):
        print("Yes")
    else:
        print("No")
