package qvizt;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

/**
 * Solution for Day 23: BST Level-Order Traversal
 */
public class Solution {

    static void levelOrder(Node root) {
        Deque<Node> queue = new ArrayDeque<>();
        StringBuilder str = new StringBuilder();
        queue.addLast(root);

        while (!queue.isEmpty()) {
            Node node = queue.removeFirst();

            if (node.left != null) {
                queue.addLast(node.left);
            }

            if (node.right != null) {
                queue.addLast(node.right);
            }

            str.append(node.data + " ");
        }

        System.out.println(str.toString());
    }

    public static Node insert(Node root, int data) {
        if (root == null) {
            return new Node(data);
        } else {
            Node cur;
            if (data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        Node root = null;
        while (T-- > 0) {
            int data = sc.nextInt();
            root = insert(root, data);
        }
        levelOrder(root);
        sc.close();
    }
}

class Node {
    Node left, right;
    int data;

    Node(int data) {
        this.data = data;
        left = right = null;
    }
}