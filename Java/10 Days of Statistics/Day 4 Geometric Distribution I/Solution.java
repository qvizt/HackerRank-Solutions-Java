package qvizt;

/**
 * Solution for Day 4 Geometric Distribution I
 */
public class Solution {

    public static void main(String[] args) {
        int n = 5;
        double p = 1.0 / 3;
        double geoDis = geometricDistribution(n, p);

        System.out.printf("%.3f", geoDis);
    }

    private static double geometricDistribution(int n, double p) {
        double q = 1 - p;
        double geoDis = Math.pow(q, n - 1) * p;
        return geoDis;
    }
}
