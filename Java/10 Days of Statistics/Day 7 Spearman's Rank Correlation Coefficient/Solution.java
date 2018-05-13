package qvizt;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Solution for Day 7: Spearman's Rank Correlation Coefficient
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        double[] x = new double[n];
        for (int i = 0; i < n; i++) {
            x[i] = scanner.nextDouble();
        }

        double[] y = new double[n];
        for (int i = 0; i < n; i++) {
            y[i] = scanner.nextDouble();
        }

        scanner.close();

        double rxy = getSpearmanRankCorrelationCoefficient(n, x, y);
        System.out.printf("%.3f", rxy);
    }

    public static double getSpearmanRankCorrelationCoefficient(int n,
            double[] x, double[] y) {

        double[] xRanking = Arrays.copyOf(x, x.length);
        Arrays.sort(xRanking);

        double[] yRanking = Arrays.copyOf(y, y.length);
        Arrays.sort(yRanking);

        double sum = 0;
        for (int i = 0; i < n; i++) {
            int xRank = getRank(x[i], xRanking);
            int yRank = getRank(y[i], yRanking);
            int difference = xRank - yRank;
            sum += Math.pow(difference, 2);
        }

        double numerator = 6 * sum;

        double denominator = n * (Math.pow(n, 2) - 1);

        double rxy = 1 - numerator / denominator;

        return rxy;
    }

    private static int getRank(double value, double[] ranking) {
        int rank = -1;
        for (int i = 0; i < ranking.length; i++) {
            if (value == ranking[i]) {
                rank = i;
                break;
            }
        }
        return rank;
    }
}
