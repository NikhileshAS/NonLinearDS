from BinaryTrees.BinaryTree import BinaryTree
from BinaryTrees.Node import Node


class AllNodesAtKDistance(object):
    def k_th_distance_node(self, root: Node, target: Node, k: int) -> list:
        relation = {}
        self.parent_child_relationship(relation, root, None)
        seen = [target]
        queue = [target]
        ans = []
        current_level = 0
        while len(queue) != 0:
            if current_level == k:
                while len(queue) != 0:
                    ans.append(queue.pop().data)
            queue_length = len(queue)
            for i in range(queue_length):
                current_node = queue.pop(0)
                if (current_node.left not in seen) and (current_node.left is not None):
                    seen.append(current_node.left)
                    queue.append(current_node.left)
                if (current_node.right not in seen) and (current_node.right is not None):
                    seen.append(current_node.right)
                    queue.append(current_node.right)
                if (relation[current_node] not in seen) and (relation[current_node] is not None):
                    seen.append(relation[current_node])
                    queue.append(relation[current_node])
            current_level += 1
        return ans

    def parent_child_relationship(self, relation: dict, child: Node, parent: Node):
        if child is None:
            return
        relation[child] = parent
        self.parent_child_relationship(relation, child.left, child)
        self.parent_child_relationship(relation, child.right, child)


def main():
    all_nodes = AllNodesAtKDistance()
    node = Node(6)
    bt = BinaryTree()
    bt.insert(node, Node(4))
    x = Node(2)
    y = Node(7)
    bt.insert(node, x)
    bt.insert(node, y)
    bt.insert(node, Node(9))
    bt.insert(node, Node(10))
    print(all_nodes.k_th_distance_node(node, x, 2))


if __name__ == '__main__':
    main()
