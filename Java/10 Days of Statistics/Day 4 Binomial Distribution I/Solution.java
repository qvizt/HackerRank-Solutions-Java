package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 4: Binomial Distribution I
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double leftRatio = scanner.nextDouble();
        double rightRatio = scanner.nextDouble();
        scanner.close();

        double p = leftRatio / (leftRatio + rightRatio);

        int n = 6;
        int x = 3;

        double sum = 0;
        for (int r = x; r <= n; r++) {
            sum += binomialDistribution(r, n, p);
        }

        System.out.printf("%.3f", sum);
    }

    private static double binomialDistribution(int x, int n, double p) {
        double pPow = Math.pow(p, x);
        double q = 1 - p;
        double qPow = Math.pow(q, (n - x));
        int nChooseX = combinations(n, x);
        double binDis = nChooseX * pPow * qPow;
        return binDis;
    }

    private static int combinations(int n, int x) {
        int numerator = factorial(n);
        int denominator = factorial(x) * factorial(n - x);
        int fraction = numerator / denominator;
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
