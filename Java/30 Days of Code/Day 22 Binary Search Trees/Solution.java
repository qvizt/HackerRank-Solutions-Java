package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 22: Binary Search Trees
 */
public class Solution {

    public static int getHeight(Node node) {
        int left = 0;
        int right = 0;

        if (node.left != null) {
            left = getHeight(node.left) + 1;
        }

        if (node.right != null) {
            right = getHeight(node.right) + 1;
        }

        return Math.max(left, right);
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
        int height = getHeight(root);
        System.out.println(height);
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