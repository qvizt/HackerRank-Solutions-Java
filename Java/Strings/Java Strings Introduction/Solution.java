package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java Strings Introduction
 */
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        sc.close();

        int sumLength = A.length() + B.length();
        String IsALexiLargerThanB = A.compareTo(B) > 0 ? "Yes" : "No";
        String capitalizedA = A.substring(0, 1).toUpperCase() + A.substring(1);
        String capitalizedB = B.substring(0, 1).toUpperCase() + B.substring(1);

        System.out.println(sumLength);
        System.out.println(IsALexiLargerThanB);
        System.out.println(capitalizedA + " " + capitalizedB);
    }

}
