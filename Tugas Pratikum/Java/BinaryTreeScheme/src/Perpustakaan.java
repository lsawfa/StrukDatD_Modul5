import java.util.Scanner;

public class Perpustakaan<T> {
    Node<T> root;

    Node insert(Node<T> root, T value) {
        if (root == null) {
            root = new Node(value);
            return root;
        }
        if (value.toString().compareTo(root.value.toString()) <= 0) {
            root.left = insert(root.left, value);
        } else {
            root.right = insert(root.right, value);
        }

        return root;
    }

    void preorderTraversal(Node<T> node) {
        if (node != null) {
            System.out.println(node.value);
            preorderTraversal(node.left);
            preorderTraversal(node.right);
        }
    }

    void inorderTraversal(Node<T> node) {
        if (node != null) {
            inorderTraversal(node.left);
            System.out.println(node.value);
            inorderTraversal(node.right);
        }
    }

    void postorderTraversal(Node<T> node) {
        if (node != null) {
            postorderTraversal(node.left);
            postorderTraversal(node.right);
            System.out.println(node.value);
        }
    }

    public static void main(String[] args) {
        Perpustakaan binaryTree = new Perpustakaan();
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("=== BOOK ORGANIZING SYSTEM ===");
            System.out.println("1. Insert Book Data");
            System.out.println("2. Show Book Data");
            System.out.println("3. Exit");
            System.out.print("Pilih menu: ");
            int menu = scanner.nextInt();
            if (menu == 1) {
                System.out.println("\n-------------------------------------------");
                System.out.println("Rules: \n- Gunakan underscore sebagai pengganti spasi. Misal: Bumi_Manusia\n- Inputan bisa berupa judul buku atau ID buku");
                System.out.print("Jumlah data buku yang akan dimasukkan: ");
                int n = scanner.nextInt();
                for (int i = 0; i < n; i++) {
                    System.out.print("Data buku ke-" + (i + 1) + ": ");
                    String value = scanner.next();
                    binaryTree.root = binaryTree.insert(binaryTree.root, value);
                }
            } else if (menu == 2) {
                System.out.println("\n-------------------------------------------");
                System.out.println("Susunan Buku dengan Preorder Traversal:");
                binaryTree.preorderTraversal(binaryTree.root);
                System.out.println("\nSusunan Buku dengan Inorder Traversal:");
                binaryTree.inorderTraversal(binaryTree.root);
                System.out.println("\nSusunan Buku dengan Postorder Traversal:");
                binaryTree.postorderTraversal(binaryTree.root);
            } else if (menu == 3) {
                break;
            } else {
                System.out.println("Invalid Menu");
            }
        }
    }
}