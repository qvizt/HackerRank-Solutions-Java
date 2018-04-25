package qvizt;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Solution for Day 11: 2D Arrays
 */
public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                arr[i][j] = in.nextInt();
            }
        }
        in.close();

        int max = Integer.MIN_VALUE;
        for (int i = 0; i <= 3; i++) {
            for (int k = 0; k <= 3; k++) {
                int top = Arrays.stream(arr[i], k, k + 3).sum();
                int mid = arr[i + 1][k + 1];
                int bottom = Arrays.stream(arr[i + 2], k, k + 3).sum();
                int sum = top + mid + bottom;
                max = Math.max(max, sum);
            }
        }
        System.out.println(max);
    }
}
