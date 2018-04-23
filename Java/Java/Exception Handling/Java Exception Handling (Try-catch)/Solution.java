package qvizt.solution;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Solution for Java Exception Handling (Try-catch)
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int result = x / y;
            System.out.println(result);
        } catch (InputMismatchException ime) {
            System.out.println(ime.getClass().getName());
        } catch (ArithmeticException ae) {
            System.out.println(ae);
        }
        scanner.close();
    }
}
