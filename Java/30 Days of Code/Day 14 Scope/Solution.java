package qvizt;

import java.util.Scanner;

class Difference {

    private int[] elements;
    public int maximumDifference;

    Difference(int[] elements) {
        this.elements = elements;
    }

    void computeDifference() {
        int min = elements[0];
        int max = elements[0];
        for (int i = 1; i < elements.length; i++) {
            min = Math.min(min, elements[i]);
            max = Math.max(max, elements[i]);
        }
        maximumDifference = max - min;

        // The short version
        //        Arrays.sort(elements);
        //        maximumDifference = elements[elements.length - 1] - elements[0];
    }
}

/**
 * Solution for Day 14: Scope
 */
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();

        Difference difference = new Difference(a);

        difference.computeDifference();

        System.out.print(difference.maximumDifference);
    }
}