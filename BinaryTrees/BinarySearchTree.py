from BinaryTrees.Node import Node
import queue


class BinarySearchTree(object):
    def insert(self, root: Node, data: int) -> Node:
        if not root:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def print_tree(self, root: Node) -> None:
        if root is None:
            return
        print(root.data)
        self.print_tree(root.left)
        self.print_tree(root.right)

    def serialize(self, root: Node) -> str:
        if root is None:
            return 'X,'
        left_sub_tree = self.serialize(root.left)
        right_sub_tree = self.serialize(root.right)
        return str(root.data) + ',' + left_sub_tree + right_sub_tree

    def deserialize(self, token: str) -> Node:
        q = queue.Queue()
        for t in token.split(','):
            q.put(t)
        return self.deserialize_helper(q)

    def deserialize_helper(self, q: queue):
        val = q.get()
        if val == 'X':
            return None
        root = Node(int(val))
        root.left = self.deserialize_helper(q)
        root.right = self.deserialize_helper(q)
        return root

    def get_child_to_parent_mapping(self, relation: dict, node: Node) -> dict:
        if node is None:
            return
        if node.left is not None:
            relation[node.left] = node
            self.get_child_to_parent_mapping(relation, node.left)
        if node.right is not None:
            relation[node.right] = node
            self.get_child_to_parent_mapping(relation, node.right)
        return relation


if __name__ == '__main__':
    node = Node(7)
    bst = BinarySearchTree()
    bst.insert(node, 4)
    bst.insert(node, 11)
    bst.insert(node, 2)
    bst.insert(node, 6)
    bst.insert(node, 9)
    # bst.insert(node, 1)
    # bst.insert(node, 0)
    # token = bst.serialize(node)
    # print(token)
    # bst.deserialize(token)
    # bst.print_tree(node)
    relation = {}
    relation = bst.get_child_to_parent_mapping(relation, node)
    for child in relation:
        print(child.data, ' --> ', relation[child].data)
