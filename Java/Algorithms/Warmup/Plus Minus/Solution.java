package qvizt;

import java.util.Scanner;

/**
 * Solution for Plus Minus
 */
public class Solution {

    /*
     * Complete the plusMinus function below.
     */
    static void plusMinus(int[] arr) {
        int positive = 0;
        int negative = 0;
        int zeroes = 0;

        for (int i = 0; i < arr.length; i++) {
            int value = arr[i];
            if (value > 0) {
                positive++;
            } else if (value < 0) {
                negative++;
            } else {
                zeroes++;
            }
        }

        System.out.println(positive / (double) arr.length);
        System.out.println(negative / (double) arr.length);
        System.out.println(zeroes / (double) arr.length);
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine().trim());

        int[] arr = new int[n];

        String[] arrItems = scan.nextLine().split(" ");

        for (int arrItr = 0; arrItr < n; arrItr++) {
            int arrItem = Integer.parseInt(arrItems[arrItr].trim());
            arr[arrItr] = arrItem;
        }

        plusMinus(arr);
    }
}