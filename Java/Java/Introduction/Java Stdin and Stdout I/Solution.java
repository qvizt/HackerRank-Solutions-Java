package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java Stdin and Stdout I
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

        scan.close();
    }
}
