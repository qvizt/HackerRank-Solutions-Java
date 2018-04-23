package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java String Reverse
 */
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        sc.close();

        String output = "Yes";
        for (int i = 0; i < A.length(); i++) {
            if (A.charAt(i) != A.charAt(A.length() - 1 - i)) {
                output = "No";
                break;
            }
        }

        System.out.println(output);
    }
}
