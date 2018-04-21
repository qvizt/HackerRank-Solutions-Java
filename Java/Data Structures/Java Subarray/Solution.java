package qvizt.solution;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Solution for Java Subarray
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < array.length; i++) {
            array[i] = scanner.nextInt();
        }
        scanner.close();

        int negativeSumCounter = 0;
        for (int i = 0; i < array.length; i++) {
            for (int k = i + 1; k <= array.length; k++) {
                int sum = Arrays.stream(array, i, k).sum();
                if (sum < 0) {
                    negativeSumCounter++;
                }
            }
        }

        System.out.println(negativeSumCounter);
    }
}
