from BinaryTrees.Node import Node


class BinarySearchTree(object):
    def insert(self, node: Node, data: int) -> Node:
        if not node:
            return Node(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node
