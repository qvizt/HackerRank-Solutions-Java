package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Day 2: Operators.
 */
public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double meal_cost = in.nextDouble();
        int tip_percent = in.nextInt();
        int tax_percent = in.nextInt();
        in.close();

        double tip = meal_cost * (tip_percent / 100.0);
        double tax = meal_cost * (tax_percent / 100.0);
        long totalCost = Math.round(meal_cost + tip + tax);
        System.out.println("The total meal cost is " + totalCost + " dollars.");
    }

}
