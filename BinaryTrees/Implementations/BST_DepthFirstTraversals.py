from BinaryTrees.Node import Node


class BinarySearchTree(object):
    def level_order_traversal(self, node):
        if node:
            self.level_order_traversal(node.left)
            print(node.data)
            self.level_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data)

    def pre_order_traversal(self, node):
        if node:
            print(node.data)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)


def main():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    bst = BinarySearchTree()
    print("Pre order traversal of binary tree is")
    bst.pre_order_traversal(node)
    print("In order traversal of binary tree is")
    bst.level_order_traversal(node)
    print("Post order traversal of binary tree is")
    bst.post_order_traversal(node)


if __name__ == '__main__':
    main()
