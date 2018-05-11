package qvizt;

/**
 * Solution for Day 5: Poisson Distribution II
 */
public class Solution {

    public static void main(String[] args) {
        double a = 0.88;
        double b = 1.55;

        double ca = 160 + 40 * (a + Math.pow(a, 2));
        double cb = 128 + 40 * (b + Math.pow(b, 2));

        System.out.printf("%.3f\n", ca);
        System.out.printf("%.3f", cb);
    }

}
