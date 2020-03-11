from BinaryTrees.BinarySearchTree import BinarySearchTree
from BinaryTrees.Node import Node as TreeNode


class ConvertToDoublyLL(object):
    prev = TreeNode
    head = TreeNode

    def convert(self, root: TreeNode):
        if root is None:
            return
        self.convert(root.left)
        if self.prev is None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root
        self.convert(root.right)

    @staticmethod
    def print_values(head: TreeNode):
        while head is not None:
            print(head.data)
            head = head.right


def main():
    bst = BinarySearchTree()
    node = TreeNode(7)
    bst.insert(node, 4)
    bst.insert(node, 11)
    bst.insert(node, 2)
    bst.insert(node, 6)
    bst.insert(node, 9)
    convert_bst_to_dll = ConvertToDoublyLL()
    convert_bst_to_dll.convert(node)
    convert_bst_to_dll.print_values(convert_bst_to_dll.head.right)


if __name__ == '__main__':
    main()

