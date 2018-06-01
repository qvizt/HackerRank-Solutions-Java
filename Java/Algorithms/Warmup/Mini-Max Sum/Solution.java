package qvizt;

import java.util.Scanner;

/**
 * Solution for Mini-Max Sum
 */
public class Solution {

    // Complete the miniMaxSum function below.
    static void miniMaxSum(int[] arr) {
        long sum = 0;
        long max = Long.MIN_VALUE;
        long min = Long.MAX_VALUE;
        
        for(int i = 0; i < arr.length; i++) {
            int value = arr[i];
            sum += value;
            max = Math.max(max, value);
            min = Math.min(min, value);
        }
        
        long maxSum = sum - min;
        long minSum = sum - max;
        System.out.printf("%d %d", minSum, maxSum);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[] arr = new int[5];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < 5; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        miniMaxSum(arr);

        scanner.close();
    }
}
