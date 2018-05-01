package qvizt;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

/**
 * Solution for Day 18: Queues and Stacks
 */
public class Solution {

    private Deque<Character> stack;
    private Deque<Character> queue;

    private Solution() {
        this.stack = new ArrayDeque<>();
        this.queue = new ArrayDeque<>();
    }

    private void pushCharacter(Character c) {
        stack.addFirst(c);
    }

    private void enqueueCharacter(Character c) {
        queue.offerLast(c);
    }

    private Character popCharacter() {
        return stack.removeFirst();
    }

    private Character dequeueCharacter() {
        return queue.pollFirst();
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        scan.close();

        // Convert input String to an array of characters:
        char[] s = input.toCharArray();

        // Create a Solution object:
        Solution p = new Solution();

        // Enqueue/Push all chars to their respective data structures:
        for (char c : s) {
            p.pushCharacter(c);
            p.enqueueCharacter(c);
        }

        // Pop/Dequeue the chars at the head of both data structures and compare them:
        boolean isPalindrome = true;
        for (int i = 0; i < s.length / 2; i++) {
            if (p.popCharacter() != p.dequeueCharacter()) {
                isPalindrome = false;
                break;
            }
        }

        //Finally, print whether string s is palindrome or not.
        System.out.println("The word, " + input + ", is "
                + ((!isPalindrome) ? "not a palindrome." : "a palindrome."));
    }
}