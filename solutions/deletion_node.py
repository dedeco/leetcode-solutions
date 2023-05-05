class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order(node: Node):
    if not node:
        return
    in_order(node.left)
    print(node.data, end=" ")
    in_order(node.right)


def delete(root: Node, key: int) -> Node:
    if not root:
        return None
    if root.right is None and root.left is None:
        if root.data == key:
            return None
        else:
            return root
    q = [root]
    item = last = key_node = None
    while q:
        item = q.pop(0)
        if item.data == key:
            key_node = item
        if item.right:
            last = item
            q.append(item.right)
        if item.left:
            last = item
            q.append(item.left)

    if key_node:
        key_node.data = item.data
        if last.right == item:
            last.right = None
        else:
            last.left = None

    return root


#      9
#     / \
#    2   8
#   / \
#  4   7
#
if __name__ == "__main__":
    root = Node(9)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(7)
    root.right = Node(8)

    print('\nbefore deletion')

    in_order(root)

    delete(root, 7)

    print('\nafter deletion')

    in_order(root)
