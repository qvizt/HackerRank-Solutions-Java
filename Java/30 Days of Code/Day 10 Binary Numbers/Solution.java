package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 10: Binary Numbers
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();

        int maxConsecutive = 0;
        int currentConsecutive = 0;

        while (n > 0) {
            int remainder = n % 2;
            if (remainder == 1) {
                currentConsecutive++;
                maxConsecutive = Math.max(maxConsecutive, currentConsecutive);
            } else {
                currentConsecutive = 0;
            }
            n = n / 2;
        }

        System.out.println(maxConsecutive);
    }
}
