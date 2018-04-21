package qvizt.solution;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Solution for Java Arraylist
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        List<List<Integer>> list = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            int d = scanner.nextInt();
            List<Integer> numbers = new ArrayList<>(d);
            for (int k = 0; k < d; k++) {
                int value = scanner.nextInt();
                numbers.add(value);
            }
            list.add(numbers);
        }

        int q = scanner.nextInt();
        for (int i = 0; i < q; i++) {
            int x = scanner.nextInt() - 1;
            int y = scanner.nextInt() - 1;
            try {
                Integer number = list.get(x).get(y);
                System.out.println(number);
            } catch (IndexOutOfBoundsException ex) {
                System.out.println("ERROR!");
            }
        }

        scanner.close();
    }
}
