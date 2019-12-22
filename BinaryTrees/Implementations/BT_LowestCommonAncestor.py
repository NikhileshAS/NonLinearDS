from BinaryTrees.BinaryTree import BinaryTree
from BinaryTrees.Node import Node


class LowestCommonAncestor(object):
    def get_lca(self, root: Node, x: Node, y: Node) -> Node:
        if root is None:
            return
        if root.data == x.data or y.data:
            return root
        left_subtree = self.get_lca(root.left, x, y)
        right_subtree = self.get_lca(root.right, x, y)

        if left_subtree is None:
            return right_subtree
        if right_subtree is None:
            return left_subtree
        return root


if __name__ == '__main__':
    node = Node(6)
    bt = BinaryTree()
    bt.insert(node, Node(4))
    x = Node(2)
    y = Node(7)
    bt.insert(node, x)
    bt.insert(node, y)
    bt.insert(node, Node(9))
    bt.insert(node, Node(10))
    lca = LowestCommonAncestor()
    lca_node = lca.get_lca(node, x, y)
    print(lca_node.data)
