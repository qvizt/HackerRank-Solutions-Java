package qvizt;

/**
 * Solution for Day 6: The Central Limit Theorem III
 */
public class Solution {

    public static void main(String[] args) {
        int n = 100;
        double mean = 500;
        double standardDeviation = 80;
        double z = 1.96;

        /*-
         * See Wikipedia
         * 
         * https://en.wikipedia.org/wiki/Normal_distribution#Confidence_intervals
         * 
         * https://en.wikipedia.org/wiki/Confidence_interval#Basic_steps
         * 
         */
        double a = mean - (z * standardDeviation) / Math.sqrt(n);
        double b = mean + (z * standardDeviation) / Math.sqrt(n);

        System.out.printf("%.2f\n", a);
        System.out.printf("%.2f", b);
    }

}
