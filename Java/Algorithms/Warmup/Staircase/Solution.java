package qvizt;

import java.util.Scanner;

/**
 * Solution for Staircase
 */
public class Solution {

    /*
     * Complete the staircase function below.
     */
    static void staircase(int n) {
        for (int i = 1; i <= n; i++) {
            StringBuilder step = new StringBuilder(i);
            for (int k = 1; k <= i; k++) {
                step.append("#");
            }

            System.out.printf("%" + n + "s\n", step.toString());
        }
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine().trim());

        staircase(n);
    }
}
