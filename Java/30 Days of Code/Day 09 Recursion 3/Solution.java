package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 9: Recursion 3
 */
public class Solution {

    static int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.close();
        int result = factorial(n);
        System.out.println(result);
    }
}
