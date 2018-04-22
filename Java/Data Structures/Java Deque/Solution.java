package qvizt;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * Solution for Java Dequeue
 */
public class Solution {

    public static void main(String[] args) {
        /*
         * This solution is based on a set which stores the currently processed
         * numbers as unique entries.
         */
        Scanner in = new Scanner(System.in);
        Deque<Integer> deque = new ArrayDeque<>();
        int n = in.nextInt();
        int m = in.nextInt();

        int maxUniqueNumbers = 0;
        Set<Integer> uniqueDequeNumbers = new HashSet<>();
        for (int i = 0; i < n; i++) {
            int num = in.nextInt();
            deque.offerFirst(num);
            uniqueDequeNumbers.add(num);
            if (deque.size() == m) {
                maxUniqueNumbers = Math.max(maxUniqueNumbers,
                        uniqueDequeNumbers.size());
                int last = deque.pollLast();
                if (!deque.contains(last)) {
                    uniqueDequeNumbers.remove(last);
                }
            }

        }
        System.out.println(maxUniqueNumbers);
        in.close();

        /*-
         * This solution works without any hashing but consumes a lot of memory.
         * It is fast enough to solve all test cases within the time limit.
         */
        //        Scanner in = new Scanner(System.in);
        //        Deque<Integer> deque = new ArrayDeque<>();
        //        int n = in.nextInt();
        //        int m = in.nextInt();
        //
        //        int maxUniqueNumbers = 0;
        //        int currentUnique = 0;
        //        int[] numbers = new int[10_000_000];
        //        for (int i = 0; i < n; i++) {
        //            int num = in.nextInt();
        //            if (numbers[num] == 0) {
        //                currentUnique++;
        //            }
        //            numbers[num]++;
        //            deque.offerFirst(num);
        //            if (deque.size() == m) {
        //                maxUniqueNumbers = Math.max(maxUniqueNumbers, currentUnique);
        //                int last = deque.pollLast();
        //                numbers[last]--;
        //                if (numbers[last] == 0) {
        //                    currentUnique--;
        //                }
        //            }
        //
        //        }
        //        System.out.println(maxUniqueNumbers);
        //        in.close();
    }
}
