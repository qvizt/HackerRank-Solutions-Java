package qvizt;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

interface PerformOperation {
    boolean check(int a);
}

class MyMath {
    public static boolean checker(PerformOperation p, int num) {
        return p.check(num);
    }

    public PerformOperation isOdd() {
        return x -> x % 2 == 1;
    }

    public PerformOperation isPrime() {
        return x -> x <= 1 ? false
                : java.util.stream.IntStream.rangeClosed(2, (int) Math.sqrt(x))
                        .noneMatch(z -> x % z == 0);
    }

    public PerformOperation isPalindrome() {
        return x -> {
            String xString = String.valueOf(x);
            for (int i = 0; i < xString.length() / 2; i++) {
                char left = xString.charAt(i);
                char right = xString.charAt(xString.length() - 1 - i);
                if (left != right) {
                    return false;
                }
            }
            return true;
        };
    }
}

/**
 * Solution for Java Lambda Expressions
 */
public class Solution {

    public static void main(String[] args) throws IOException {
        MyMath ob = new MyMath();
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        PerformOperation op;
        boolean ret = false;
        String ans = null;
        while (T-- > 0) {
            String s = br.readLine().trim();
            StringTokenizer st = new StringTokenizer(s);
            int ch = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            if (ch == 1) {
                op = ob.isOdd();
                ret = ob.checker(op, num);
                ans = (ret) ? "ODD" : "EVEN";
            } else if (ch == 2) {
                op = ob.isPrime();
                ret = ob.checker(op, num);
                ans = (ret) ? "PRIME" : "COMPOSITE";
            } else if (ch == 3) {
                op = ob.isPalindrome();
                ret = ob.checker(op, num);
                ans = (ret) ? "PALINDROME" : "NOT PALINDROME";

            }
            System.out.println(ans);
        }
    }
}
