package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 0: Weighted Mean
 */
public class Solution {

    public static double getWeightedMean(int[] values, int weights[]) {
        int numeratorSum = 0;
        int denominatorSum = 0;

        for (int i = 0; i < values.length; i++) {
            int value = values[i];
            int weight = weights[i];
            int weightedValue = value * weight;

            numeratorSum += weightedValue;
            denominatorSum += weight;
        }

        return (double) numeratorSum / denominatorSum;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
        }

        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            weights[i] = scanner.nextInt();
        }
        scanner.close();

        double weightedMean = getWeightedMean(values, weights);
        System.out.printf("%.1f", weightedMean);
    }
}
