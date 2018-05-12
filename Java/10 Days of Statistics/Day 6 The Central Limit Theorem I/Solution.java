package qvizt;

/**
 * Solution for Day 6: The Central Limit Theorem I
 */
public class Solution {

    public static void main(String[] args) {

        int max = 9800;
        int n = 49;
        int mean = 205;
        int standardDeviation = 15;

        int meanLine = n * mean;
        double standardDeviationLine = Math.sqrt(n) * standardDeviation;

        double probability = cumulativeProbability(max, meanLine,
                standardDeviationLine);

        System.out.printf("%.4f", probability);
    }

    /*-
     * x
     * mean = mu
     * deviation = sigma
     */
    public static double cumulativeProbability(double x, double mean,
            double deviation) {
        double numeratorZ = x - mean;
        double denominatorZ = deviation * Math.sqrt(2);
        double z = numeratorZ / denominatorZ;
        double erf = erf(z);
        double phi = 0.5 * (1 + erf);

        return phi;
    }

    /*
     * Taken from:
     * https://introcs.cs.princeton.edu/java/21function/ErrorFunction.java.html
     */
    public static double erf(double z) {
        double t = 1.0 / (1.0 + 0.5 * Math.abs(z));

        // use Horner's method
        double ans = 1 - t * Math.exp(-z * z - 1.26551223 + t * (1.00002368
                + t * (0.37409196 + t * (0.09678418 + t * (-0.18628806
                        + t * (0.27886807 + t * (-1.13520398 + t * (1.48851587
                                + t * (-0.82215223 + t * (0.17087277))))))))));
        if (z >= 0)
            return ans;
        else
            return -ans;
    }
}
