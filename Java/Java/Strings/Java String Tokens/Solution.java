package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java String Tokens
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();

        s = s.trim();
        if (s.length() == 0) {
            System.out.println(0);
        } else if (s.length() <= 400_000) {
            String[] split = s.split("[ !,?._'@]+");
            System.out.println(split.length);
            for (String spl : split) {
                System.out.println(spl);
            }
        }
    }

}
