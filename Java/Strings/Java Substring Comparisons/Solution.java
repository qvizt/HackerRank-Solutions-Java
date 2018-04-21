package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java Substring Comparisons
 */
public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";

        if (s.length() >= k) {
            smallest = s.substring(0, k);
            largest = s.substring(0, k);

            for (int i = 1; i < s.length() - k + 1; i++) {
                String current = s.substring(i, i + k);
                if (current.compareTo(smallest) < 0) {
                    smallest = current;
                } else if (current.compareTo(largest) > 0) {
                    largest = current;
                }
            }
        }

        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
