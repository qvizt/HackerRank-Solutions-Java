package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 25: Running Time and Complexity
 */
public class Solution {

    public static boolean isPrime(int nr) {
        if (nr <= 1) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(nr); i++) {
            if (nr % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            int nr = scanner.nextInt();
            if (isPrime(nr)) {
                System.out.println("Prime");
            } else {
                System.out.println("Not prime");
            }
        }

        scanner.close();
    }
}
