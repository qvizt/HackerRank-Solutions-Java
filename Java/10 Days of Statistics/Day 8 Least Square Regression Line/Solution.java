package qvizt;

/**
 * Solution for Day 8: Least Square Regression Line
 */
public class Solution {

    public static void main(String[] args) {
        double[] x = { 95, 85, 80, 70, 60 };
        double[] y = { 85, 95, 70, 65, 70 };

        double b = getB(x, y);
        double a = getA(x, y, b);

        double result = a + b * 80;

        System.out.printf("%.3f", result);
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

    public static double getB(double[] x, double[] y) {
        double xMean = getMean(x);
        double xStdDev = getStandardDeviation(x, xMean);
        double yMean = getMean(y);
        double yStdDev = getStandardDeviation(y, yMean);
        double pxy = getPearsonCorrelationCoefficient(x, y);

        double b = pxy * (yStdDev / xStdDev);

        return b;
    }

    public static double getA(double[] x, double[] y) {
        double b = getB(x, y);
        return getA(x, y, b);
    }

    public static double getA(double[] x, double[] y, double b) {
        double xMean = getMean(x);
        double yMean = getMean(y);
        double a = yMean - b * xMean;

        return a;
    }

}
