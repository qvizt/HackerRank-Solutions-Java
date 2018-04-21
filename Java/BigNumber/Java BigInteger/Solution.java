package qvizt.solution;

import java.math.BigInteger;
import java.util.Scanner;

/**
 * Solution for Java BigInteger
 */
public class Solution {

    // Do not forget to import java.math.BigInteger
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BigInteger a = scanner.nextBigInteger();
        BigInteger b = scanner.nextBigInteger();
        scanner.close();

        BigInteger sum = a.add(b);
        BigInteger product = a.multiply(b);

        System.out.println(sum);
        System.out.println(product);
    }

}