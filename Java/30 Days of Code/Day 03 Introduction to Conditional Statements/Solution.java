package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 3: Intro to Conditional Statements.
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        String ans = "";

        // if 'n' is NOT evenly divisible by 2 (i.e.: n is odd)

        /*-
         * All numbers from 6 to 20 are "Weird".
         * 
         * Odd numbers combined with the even numbers between 6 and 20
         * leads to all numbers from 6 to 20 which can be written
         * as the if clause below. The condition will also evaluate to true
         * for all numbers that are odd but not within the range from 6 to 20.
         */
        if (n % 2 == 1 || (n >= 6 && n <= 20)) {
            ans = "Weird";
        } else {
            ans = "Not Weird";
        }
        System.out.println(ans);
    }
}
