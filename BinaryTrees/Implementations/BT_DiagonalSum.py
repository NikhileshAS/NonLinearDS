from BinaryTrees.BinaryTree import BinaryTree
from BinaryTrees.Node import Node
from BinaryTrees.Implementations.BST_LevelOrderTraversal import LevelOrderTraversal


class DiagonalSum(object):
    def calculate_sum(self, root: Node, distance: int, answer: dict):
        if root is None:
            return
        if distance not in answer:
            answer[distance] = 0
        answer[distance] += node.data
        if root.left is not None:
            self.calculate_sum(root.left, distance+1, answer)
        if root.right is not None:
            self.calculate_sum(root.right, distance, answer)

    def get_diagonal_sum(self, root: Node) -> dict:
        answer = {}
        self.calculate_sum(root, 0, answer)
        return answer

    def print_the_tree(self, root: Node):
        if root is None:
            return
        print(root.data)
        self.print_the_tree(root.left)
        self.print_the_tree(root.right)


if __name__ == '__main__':
    node = Node(1)
    bt = BinaryTree()
    bt.insert(node, Node(2))
    bt.insert(node, Node(3))
    bt.insert(node, Node(9))
    bt.insert(node, Node(6))
    bt.insert(node, Node(4))
    bt.insert(node, Node(5))
    bt.insert(node, Node(12))
    bt.insert(node, Node(11))
    bt.insert(node, Node(10))
    ds = DiagonalSum()
    bst_level_order = LevelOrderTraversal()
    bst_level_order.level_order(node, [])
    print(ds.get_diagonal_sum(node).values())

