from BinaryTrees.Node import Node


class BinaryTree(object):
    def insert(self, root: Node, newNode: Node ) -> None:
        if root is None:
            root = newNode
            return
        self.insert(root.left, newNode)
        self.insert(root.right, newNode)
        return
