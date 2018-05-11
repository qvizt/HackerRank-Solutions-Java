package qvizt;

/**
 * Solution for Day 5: Poisson Distribution I
 */
public class Solution {

    public static void main(String[] args) {
        double mean = 2.5;
        int k = 5;
        double poisson = poissonDistribution(k, mean);
        System.out.printf("%.3f", poisson);
    }

    private static double poissonDistribution(int k, double lambda) {
        double numerator = Math.pow(lambda, k) * Math.pow(Math.E, -lambda);
        double denominator = factorial(k);
        double fraction = numerator / denominator;
        return fraction;
    }

    private static int factorial(int n) {
        int result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }

        return result;
    }
}
