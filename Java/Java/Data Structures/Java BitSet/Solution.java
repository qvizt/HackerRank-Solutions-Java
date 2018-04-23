package qvizt.solution;

import java.util.BitSet;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * Solution for Java BitSet
 */
public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        BitSet one = new BitSet(n);
        BitSet two = new BitSet(n);

        Set<String> twoSetOperations = new HashSet<>(3);
        twoSetOperations.add("AND");
        twoSetOperations.add("OR");
        twoSetOperations.add("XOR");

        for (int i = 0; i < m; i++) {
            String operation = scanner.next();
            int leftOperand = scanner.nextInt();
            int rightOperand = scanner.nextInt();
            BitSet leftBitSet = leftOperand == 1 ? one : two;

            if (twoSetOperations.contains(operation)) {
                BitSet rightBitSet = rightOperand == 2 ? two : one;
                switch (operation) {
                    case "AND":
                        leftBitSet.and(rightBitSet);
                        break;
                    case "OR":
                        leftBitSet.or(rightBitSet);
                        break;
                    case "XOR":
                        leftBitSet.xor(rightBitSet);
                        break;
                }
            } else {
                switch (operation) {
                    case "FLIP":
                        leftBitSet.flip(rightOperand);
                        break;
                    case "SET":
                        leftBitSet.set(rightOperand);
                        break;
                }
            }

            System.out.println(one.cardinality() + " " + two.cardinality());
        }

        scanner.close();
    }
}
