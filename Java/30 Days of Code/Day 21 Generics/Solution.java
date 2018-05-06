package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 21: Generics
 */
public class Solution {

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Integer[] intArray = new Integer[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = scanner.nextInt();
        }

        n = scanner.nextInt();
        String[] stringArray = new String[n];
        for (int i = 0; i < n; i++) {
            stringArray[i] = scanner.next();
        }
        scanner.close();

        Printer<Integer> intPrinter = new Printer<Integer>();
        Printer<String> stringPrinter = new Printer<String>();
        intPrinter.printArray(intArray);
        stringPrinter.printArray(stringArray);
        if (Printer.class.getDeclaredMethods().length > 1) {
            System.out.println(
                    "The Printer class should only have 1 method named printArray.");
        }
    }

}

class Printer<T> {

    /**
     * Method Name: printArray Print each element of the generic array on a new
     * line. Do not return anything.
     * 
     * @param array
     *            generic array
     **/
    void printArray(T[] array) {
        for (T t : array) {
            System.out.println(t);
        }
    }
}
