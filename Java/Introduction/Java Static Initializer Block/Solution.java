package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java Static Initializer Block
 */
public class Solution {

    private static int B;
    private static int H;
    private static boolean flag = false;

    static {
        Scanner scanner = new Scanner(System.in);
        B = scanner.nextInt();
        H = scanner.nextInt();
        scanner.close();

        if (B > 0 && H > 0) {
            flag = true;
        } else {
            System.out.println(
                    "java.lang.Exception: Breadth and height must be positive");
        }
    }

    public static void main(String[] args) {
        if (flag) {
            int area = B * H;
            System.out.print(area);
        }
    }

}
