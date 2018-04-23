package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 6: Let's Review.
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        scanner.nextLine();

        for (int i = 0; i < t; i++) {
            String line = scanner.nextLine();
            char[] chars = line.toCharArray();

            StringBuilder evenIndexedChars = new StringBuilder();
            StringBuilder oddIndexedChars = new StringBuilder();

            for (int k = 0; k < chars.length; k++) {
                if (k % 2 == 0) {
                    evenIndexedChars.append(chars[k]);
                } else {
                    oddIndexedChars.append(chars[k]);
                }
            }

            System.out.println(evenIndexedChars + " " + oddIndexedChars);
        }

        scanner.close();
    }
}
