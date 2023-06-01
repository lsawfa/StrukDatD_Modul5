class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Perpustakaan:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            root = Node(value)
            return root
        
        if str(value) <= str(root.value):
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    def preorderTraversal(self, node):
        if node is not None:
            print(node.value)
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if node is not None:
            self.inorderTraversal(node.left)
            print(node.value)
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if node is not None:
            self.postorderTraversal(node.left)
            self.postorderTraversal(node.right)
            print(node.value)

binaryTree = Perpustakaan()
while True:
    print("=== BOOK ORGANIZING SYSTEM ===")
    print("1. Insert Book Data")
    print("2. Show Book Data")
    print("3. Exit")
    menu = int(input("Pilih menu: "))
    if menu == 1:
        print("\n-------------------------------------------")
        print("Rules: \n- Gunakan underscore sebagai pengganti spasi. Misal: Bumi_Manusia\n- Inputan bisa berupa judul buku atau ID buku")
        n = int(input("Jumlah data buku yang akan dimasukkan: "))
        for i in range(n):
            value = input("Data buku ke-" + str(i + 1) + ": ")
            binaryTree.root = binaryTree.insert(binaryTree.root, value)
    elif menu == 2:
        print("\n-------------------------------------------")
        print("Susunan Buku dengan Preorder Traversal:")
        binaryTree.preorderTraversal(binaryTree.root)
        print("\nSusunan Buku dengan Inorder Traversal:")
        binaryTree.inorderTraversal(binaryTree.root)
        print("\nSusunan Buku dengan Postorder Traversal:")
        binaryTree.postorderTraversal(binaryTree.root)
    elif menu == 3:
        break
    else:
        print("Invalid Menu")