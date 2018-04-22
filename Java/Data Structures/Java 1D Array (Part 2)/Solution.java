package qvizt;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * Solution for Java 1D Array (Part 2)
 */
public class Solution {

    public static boolean canWin(int leap, int[] game) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);

        while (!queue.isEmpty()) {
            int index = queue.poll();

            int leapDestination = index + leap;
            if (index == game.length - 1 || leapDestination >= game.length) {
                return true;
            }

            if (game[leapDestination] == 0) {
                queue.offer(leapDestination);
            }

            int forward = index + 1;
            if (game[forward] == 0) {
                queue.offer(forward);
            }

            int backward = index - 1;
            if (backward >= 0 && game[backward] == 0) {
                queue.offer(backward);
            }

            /*
             * IMPORTANT: Flag the current game index as "processed". Otherwise
             * an infinite loop might occur. This way is possible because the
             * game array is not required after evaluation anymore.
             */
            game[index] = 1;
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();

            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println((canWin(leap, game)) ? "YES" : "NO");
        }
        scan.close();
    }
}
