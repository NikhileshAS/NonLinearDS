from BinaryTrees.Node import Node
from BinaryTrees.BinarySearchTree import BinarySearchTree


class LargestNode(object):
    def kth_largest_node(self, node: Node, k: int, c: list) -> Node:
        if not node or (c[0] >= k):
            return node
        self.kth_largest_node(node.right, k, c)
        c[0] += 1
        if c[0] == k:
            print(node.data)
            return node
        self.kth_largest_node(node.left, k, c)


def main():
    node = Node(50)
    bst = BinarySearchTree()
    largest_node = LargestNode()
    c = [0]
    k = 4
    bst.insert(node, 30)
    bst.insert(node, 20)
    bst.insert(node, 40)
    bst.insert(node, 70)
    bst.insert(node, 60)
    bst.insert(node, 80)
    largest_node.kth_largest_node(node, k, c)


if __name__ == '__main__':
    main()
