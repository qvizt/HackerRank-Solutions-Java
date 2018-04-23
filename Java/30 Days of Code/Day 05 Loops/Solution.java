package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 5: Loops.
 */
public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.close();

        for (int i = 1; i <= 10; i++) {
            int product = n * i;
            System.out.println(n + " x " + i + " = " + product);
        }
    }

}
