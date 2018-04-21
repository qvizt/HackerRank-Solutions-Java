package qvizt.solution;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Solution for Java List
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> list = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            int number = scanner.nextInt();
            list.add(number);
        }

        int q = scanner.nextInt();

        for (int i = 0; i < q; i++) {
            String operation = scanner.next();
            int x = scanner.nextInt();
            switch (operation) {
                case "Insert":
                    int y = scanner.nextInt();
                    list.add(x, y);
                    break;
                case "Delete":
                    list.remove(x);
                    break;
            }
        }

        scanner.close();

        for (Integer i : list) {
            System.out.print(i + " ");
        }
    }
}
