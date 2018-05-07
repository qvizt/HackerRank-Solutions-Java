package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 1: Standard Deviation
 */
public class Solution {

    public static double getMean(int[] values) {
        int sum = 0;

        for (int i : values) {
            sum += i;
        }

        double mean = (double) sum / values.length;

        return mean;
    }

    public static double getStandardDeviation(int[] values, double mean) {
        double nominator = 0;

        for (int i = 0; i < values.length; i++) {
            double distance = values[i] - mean;
            double squaredDistance = distance * distance;
            nominator += squaredDistance;
        }

        double fraction = nominator / values.length;
        return Math.sqrt(fraction);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
        }

        scanner.close();

        double mean = getMean(values);
        double devi = getStandardDeviation(values, mean);
        System.out.printf("%.1f", devi);
    }
}
