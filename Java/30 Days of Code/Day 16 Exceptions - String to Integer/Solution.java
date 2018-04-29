package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 16: Exceptions - String to Integer
 */
public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        in.close();

        try {
            int i = Integer.valueOf(S);
            System.out.println(i);
        } catch (NumberFormatException ex) {
            System.out.println("Bad String");
        }
    }
}
