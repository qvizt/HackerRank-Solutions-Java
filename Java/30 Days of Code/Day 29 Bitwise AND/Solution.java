package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 29: Bitwise AND
 */
public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String[] nk = scanner.nextLine().split(" ");
            int n = Integer.parseInt(nk[0]);
            int k = Integer.parseInt(nk[1]);

            int max = 0;

            for (int a = 1; a <= n - 1; a++) {
                for (int b = a + 1; b <= n; b++) {
                    int result = a & b;
                    if (result < k) {
                        max = Math.max(max, result);
                    }
                }
            }

            System.out.println(max);
        }

        scanner.close();
    }

}
