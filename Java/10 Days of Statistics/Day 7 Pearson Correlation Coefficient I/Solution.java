package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 7: Pearson Correlation Coefficient I
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

        double pxy = getPearsonCorrelationCoefficient(x, y);
        System.out.printf("%.3f", pxy);
    }

    public static double getMean(double[] values) {
        double sum = 0;

        for (double i : values) {
            sum += i;
        }

        double mean = sum / values.length;

        return mean;
    }

    public static double getStandardDeviation(double[] values, double mean) {
        double numerator = 0;

        for (int i = 0; i < values.length; i++) {
            double distance = values[i] - mean;
            double squaredDistance = distance * distance;
            numerator += squaredDistance;
        }

        double fraction = numerator / values.length;
        return Math.sqrt(fraction);
    }

    // not required, but can be used to calculate pxy
    public static double getCovariance(double[] x, double[] y) {
        double xMean = getMean(x);
        double yMean = getMean(y);
        double sum = 0;
        int n = x.length;

        for (int i = 0; i < n; i++) {
            sum += (x[i] - xMean) * (y[i] - yMean);
        }

        double covariance = (1.0 / n) * sum;

        return covariance;
    }

    // not required, but can be used to calculate pxy
    public static double getCovarianceAlternative(double[] x, double[] y) {
        double sum = 0;
        int n = x.length;

        for (int i = 0; i < n; i++) {
            double innerSum = 0;
            for (int j = i + 1; j < n; j++) {
                innerSum += (x[i] - x[j]) * (y[i] - y[j]);
            }
            sum += innerSum;
        }

        double covariance = (1.0 / Math.pow(n, 2)) * sum;

        return covariance;
    }

    public static double getPearsonCorrelationCoefficient(double[] x,
            double[] y) {
        int n = x.length;
        double xMean = getMean(x);
        double yMean = getMean(y);
        double xStdDev = getStandardDeviation(x, xMean);
        double yStdDev = getStandardDeviation(y, yMean);

        double numerator = 0; // the sum
        for (int i = 0; i < n; i++) {
            numerator += (x[i] - xMean) * (y[i] - yMean);
        }

        double denomiator = n * xStdDev * yStdDev;

        double pxy = numerator / denomiator;

        return pxy;
    }
}
