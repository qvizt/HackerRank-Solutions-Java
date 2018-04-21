package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java Loops II
 */
public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            String line = getResultLine(a, b, n);
            System.out.println(line);
        }
        in.close();
    }

    private static String getResultLine(int a, int b, int n) {
        StringBuilder line = new StringBuilder();
        for (int k = 0; k < n; k++) {
            int sum = a;
            for (int m = 0; m <= k; m++) {
                sum = sum + pow(2, m) * b;
            }
            line.append(sum + " ");
        }
        return line.toString();
    }

    private static int pow(int base, int exponent) {
        if (exponent == 0) {
            return 1;
        }
        if (exponent == 1) {
            return base;
        }
        if (exponent % 2 == 0) {
            return pow(base * base, exponent / 2);
        } else {
            return base * pow(base * base, exponent / 2);
        }
    }

}
