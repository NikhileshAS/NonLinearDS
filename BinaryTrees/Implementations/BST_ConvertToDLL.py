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
    def print(head: TreeNode):
        while head is not None:
            print(head.data)
            head = head.right


def main():
    bst = BinarySearchTree()
    node = TreeNode(10)
    bst.insert(node, 12)
    bst.insert(node, 15)
    bst.insert(node, 25)
    bst.insert(node, 30)
    bst.insert(node, 36)
    convert_bst_to_dll = ConvertToDoublyLL()
    convert_bst_to_dll.convert(node)
    convert_bst_to_dll.print(convert_bst_to_dll.head)


if __name__ == '__main__':
    main()

