from BinaryTrees.Node import Node
from BinaryTrees.BinarySearchTree import BinarySearchTree
from collections import deque


class LevelOrderTraversal(object):
    @staticmethod
    def level_order(root: Node, queue: deque) -> None:

        if root is not None:
            queue.append(root)
        while queue.__len__() != 0:
            current_node = queue.popleft()
            print(current_node.data)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)


if __name__ == '__main__':
    node = Node(10)
    bst = BinarySearchTree()
    bst.insert(node, 5)
    bst.insert(node, 23)
    bst.insert(node, 9)
    bst.insert(node, 16)
    level_order_traversal = LevelOrderTraversal()
    queue = deque()
    level_order_traversal.level_order(node, queue)


