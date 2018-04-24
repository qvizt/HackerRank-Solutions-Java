package qvizt;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Solution for Day 8: Dictionaries and Maps.
 */
public class Solution {

    public static void main(String[] argh) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        Map<String, Integer> map = new HashMap<>(n);
        for (int i = 0; i < n; i++) {
            String name = in.next();
            int phone = in.nextInt();
            map.put(name, phone);
        }

        while (in.hasNext()) {
            String s = in.next();
            Integer phone = map.get(s);
            if (phone != null) {
                System.out.println(s + "=" + phone);
            } else {
                System.out.println("Not found");
            }
        }
        in.close();
    }

}