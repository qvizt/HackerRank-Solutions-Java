package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java 1D Array
 */
public class Solution {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < a.length; i++) {
            a[i] = scan.nextInt();
        }

        scan.close();

        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}
