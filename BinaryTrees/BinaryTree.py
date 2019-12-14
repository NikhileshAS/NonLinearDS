from BinaryTrees.Node import Node


class BinaryTree(object):
    def insert(self, root: Node, newNode: Node ) -> Node:
        if root is None:
            root = newNode
        self.insert(root.left, newNode)
        self.insert(root.right, newNode)
