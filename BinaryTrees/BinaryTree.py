from BinaryTrees.Node import Node


class BinaryTree(object):
    def insert(self, root: Node, newNode: Node ) -> None:
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            if node.left is None:
                node.left = newNode
                return
            queue.append(node.left)
            if node.right is None:
                node.right = newNode
                return
            queue.append(node.right)
