package qvizt;

/**
 * Solution for Day 4 Geometric Distribution II
 */
public class Solution {

    public static void main(String[] args) {
        /*
         * Taking a different approach: Instead of solving "What is the
         * probability that the first the defect is found during the first five
         * inspections?" i am going to do "What is the probability that no
         * defect is found?" and subtract the probability for no defect from 1.
         * 
         * Another approach is to use the geometric distribution for defect on
         * first inspection, defect on second inspection and so on and sum the
         * results.
         */

        int n = 5;
        double p = 1 - (1.0 / 3);
        double noDefectProbability = negativeBinomialDistribution(5, n, p);
        double defectProbabilty = 1 - noDefectProbability;

        System.out.printf("%.3f", defectProbabilty);

        // Solution with geometric distribution
        //        System.out.println();
        //        p = 1.0 / 3;
        //        defectProbabilty = 0;
        //        for (int i = 1; i <= n; i++) {
        //            defectProbabilty += geometricDistribution(i, p);
        //        }
        //        System.out.printf("%.3f", defectProbabilty);

    }

    private static double negativeBinomialDistribution(int x, int n, double p) {
        double pPow = Math.pow(p, x);
        double q = 1 - p;
        double qPow = Math.pow(q, (n - x));
        int nChooseX = combinations(n - 1, x - 1);
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

    private static double geometricDistribution(int n, double p) {
        double q = 1 - p;
        double geoDis = Math.pow(q, n - 1) * p;
        return geoDis;
    }
}
