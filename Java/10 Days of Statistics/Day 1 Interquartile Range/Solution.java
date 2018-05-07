package qvizt;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Solution for Day 1: Interquartile Range
 */
public class Solution {

    private static double getFirstQuartile(int[] values) {
        int half = values.length / 2;
        if (half % 2 == 1) {
            int index = (half + 1) / 2 - 1;
            return values[index];
        } else {
            int leftMidIndex = half / 2 - 1;
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
        int[] ints = new int[n];
        for (int i = 0; i < n; i++) {
            ints[i] = scanner.nextInt();
        }

        int sumCount = 0;
        int[] counts = new int[n];
        for (int i = 0; i < n; i++) {
            counts[i] = scanner.nextInt();
            sumCount += counts[i];
        }
        scanner.close();

        int[] values = new int[sumCount];
        for (int i = 0, index = 0; i < ints.length; i++) {
            for (int k = 0; k < counts[i]; k++, index++) {
                values[index] = ints[i];
            }
        }

        Arrays.sort(values);
        double diff = getThirdQuartile(values) - getFirstQuartile(values);
        System.out.printf("%.1f", diff);
    }
}
