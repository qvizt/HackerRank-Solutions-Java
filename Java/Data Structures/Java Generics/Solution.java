package qvizt.solution;

import java.lang.reflect.Method;

/**
 * Solution for Java Generics
 */
class Printer {

    <T> void printArray(T[] array) {
        for (T t : array) {
            System.out.println(t);
        }
    }
}

/**
 * Solution for Java Generics
 */
public class Solution {

    public static void main(String args[]) {
        Printer myPrinter = new Printer();
        Integer[] intArray = { 1, 2, 3 };
        String[] stringArray = { "Hello", "World" };
        myPrinter.printArray(intArray);
        myPrinter.printArray(stringArray);
        int count = 0;

        for (Method method : Printer.class.getDeclaredMethods()) {
            String name = method.getName();

            if (name.equals("printArray"))
                count++;
        }

        if (count > 1)
            System.out.println("Method overloading is not allowed!");

    }
}
