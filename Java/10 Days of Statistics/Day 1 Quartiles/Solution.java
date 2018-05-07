package qvizt;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Solution for Day 1: Quartiles
 */
public class Solution {

    private static double getFirstQuartile(int[] values) {
        int half = values.length / 2;
        if (half % 2 == 0) {
            int leftMidIndex = (int) half / 2 - 1;
            int rightMidIndex = leftMidIndex + 1;
            return (values[leftMidIndex] + values[rightMidIndex]) / 2.0;
        } else {
            int index = (int) half / 2;
            return values[index];
        }
    }

    public static double getSecondQuartile(int[] values) {
        if (values.length % 2 == 1) {
            int index = (values.length + 1) / 2 - 1;
            return values[index];
        } else {
            int leftMidIndex = values.length / 2 - 1;
            int rightMidIndex = leftMidIndex + 1;
            return (values[leftMidIndex] + values[rightMidIndex]) / 2.0;
        }
    }

    private static double getThirdQuartile(int[] values) {
        int half = values.length / 2;
        if (half % 2 == 1) {
            int index = (values.length + half) / 2;
            return values[index];
        } else {
            int leftMidIndex = (values.length + half) / 2;
            if (values.length % 2 == 0) {
                leftMidIndex -= 1;
            }
            int rightMidIndex = leftMidIndex + 1;
            return (values[leftMidIndex] + values[rightMidIndex]) / 2.0;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
        }
        scanner.close();

        Arrays.sort(values);
        System.out.println(Arrays.toString(values));
        System.out.printf("%.0f\n", getFirstQuartile(values));
        System.out.printf("%.0f\n", getSecondQuartile(values));
        System.out.printf("%.0f", getThirdQuartile(values));
    }
}
