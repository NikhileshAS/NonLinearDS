from BinaryTrees.Node import Node
from BinaryTrees.BinarySearchTree import BinarySearchTree


class LevelOrderTraversal(object):
    @staticmethod
    def level_order(root: Node, queue: list) -> None:

        if root is not None:
            queue.append(root)
        while len(queue) != 0:
            current_node = queue.pop(0)
            print(current_node.data)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)


    def show_mirror_tree(self, root: Node) -> Node:
        if root is None:
            return root
        # temp = root
        self.show_mirror_tree(root.left)
        self.show_mirror_tree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

if __name__ == '__main__':
    node = Node(10)
    bst = BinarySearchTree()
    bst.insert(node, 5)
    bst.insert(node, 23)
    bst.insert(node, 9)
    bst.insert(node, 16)
    bst.insert(node, 0)
    level_order_traversal = LevelOrderTraversal()
    level_order_traversal.show_mirror_tree(node)
    level_order_traversal.level_order(node, [])



