package qvizt.solution;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Method;
import java.util.HashSet;
import java.util.Set;

import static java.lang.System.in;

/*
 * Do not forget to import in via "import static java.lang.System.in"
 * to have access to "in".
 */
class Prime {

    public void checkPrime(int... numbers) {
        StringBuilder line = new StringBuilder();

        loopNumbers: for (int i = 0; i < numbers.length; i++) {
            int number = numbers[i];
            if (number >= 2) {
                int root = (int) Math.sqrt(number);
                for (int k = 2; k <= root; k++) {
                    if (number % k == 0) {
                        continue loopNumbers;
                    }
                }

                line.append(number);
                if (i < numbers.length - 1) {
                    line.append(" ");
                }
            }
        }

        System.out.println(line);
    }
}

/**
 * Solution for Prime Checker
 */
public class Solution {

    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(in));
            int n1 = Integer.parseInt(br.readLine());
            int n2 = Integer.parseInt(br.readLine());
            int n3 = Integer.parseInt(br.readLine());
            int n4 = Integer.parseInt(br.readLine());
            int n5 = Integer.parseInt(br.readLine());
            Prime ob = new Prime();
            ob.checkPrime(n1);
            ob.checkPrime(n1, n2);
            ob.checkPrime(n1, n2, n3);
            ob.checkPrime(n1, n2, n3, n4, n5);
            Method[] methods = Prime.class.getDeclaredMethods();
            Set<String> set = new HashSet<>();
            boolean overload = false;
            for (int i = 0; i < methods.length; i++) {
                if (set.contains(methods[i].getName())) {
                    overload = true;
                    break;
                }
                set.add(methods[i].getName());

            }
            if (overload) {
                throw new Exception("Overloading not allowed");
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
