class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None

    def new_node(self, data):
        self.root = self._new_node(self.root, Node(data))

    def _new_node(self, root, new_data):
        if root is None:
            root = new_data
            return root
        if new_data.data < root.data:
            root.left = self._new_node(root.left, new_data)
        else:
            root.right = self._new_node(root.right, new_data)
        return root

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def pre_order(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")

pohon = BinaryTree()
pohon.new_node(20)
pohon.new_node(2)
pohon.new_node(25)
pohon.new_node(37)
pohon.new_node(16)

print("\nPre Order: ")
pohon.pre_order(pohon.root)
print("\nIn Order: ")
pohon.in_order(pohon.root)
print("\nPost Order: ")
pohon.post_order(pohon.root)