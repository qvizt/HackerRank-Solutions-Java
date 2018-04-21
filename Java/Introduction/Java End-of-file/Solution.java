package qvizt.solution;

import java.util.Scanner;

/**
 * Solution for Java End-of-file
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lineNumber = 0;
        while (scanner.hasNextLine()) {
            lineNumber++;
            String line = scanner.nextLine();
            System.out.println(lineNumber + " " + line);
        }
        scanner.close();
    }
}
