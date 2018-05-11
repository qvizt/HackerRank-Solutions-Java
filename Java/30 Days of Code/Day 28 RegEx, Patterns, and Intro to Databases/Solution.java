package qvizt;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

/**
 * Solution for Day 28: RegEx, Patterns, and Intro to Databases
 */
public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        List<String> firstNames = new ArrayList<>();
        String regex = "[a-z.]{2,20}@gmail.com";

        for (int NItr = 0; NItr < N; NItr++) {
            String[] firstNameEmailID = scanner.nextLine().split(" ");
            String firstName = firstNameEmailID[0];
            String emailID = firstNameEmailID[1];

            if (emailID.matches(regex)) {
                firstNames.add(firstName);
            }
        }

        Collections.sort(firstNames);

        for (String name : firstNames) {
            System.out.println(name);
        }

        scanner.close();
    }
}
