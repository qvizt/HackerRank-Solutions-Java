package qvizt;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Solution for Java Stack
 */
public class Solution {

    public static void main(String[] argh) {
        Scanner sc = new Scanner(System.in);

        Map<Character, Character> brackets = new HashMap<>();
        brackets.put(')', '(');
        brackets.put(']', '[');
        brackets.put('}', '{');

        while (sc.hasNext()) {
            String input = sc.next();
            char[] chars = input.toCharArray();

            /*
             * Every opening bracket needs a closing bracket, thus the number of
             * characters must be equal.
             */
            if (chars.length % 2 == 1) {
                System.out.println(false);
            } else {
                Deque<Character> leftBrackets = new ArrayDeque<>();
                boolean correct = true;
                for (int i = 0; i < chars.length && correct; i++) {
                    Character bracket = chars[i];
                    if (!brackets.containsKey(bracket)) {
                        leftBrackets.addFirst(bracket);
                    } else {
                        Character expectedLeftBracket = brackets.get(bracket);
                        Character actualLeftBracket = leftBrackets.pollFirst();
                        if (!expectedLeftBracket.equals(actualLeftBracket)) {
                            correct = false;
                        }
                    }
                }
                System.out.println(correct);
            }
        }

        sc.close();
    }
}