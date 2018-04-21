package qvizt.solution;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Solution for Java Map
 */
public class Solution {

    public static void main(String[] argh) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();

        Map<String, Integer> map = new HashMap<>(n);
        for (int i = 0; i < n; i++) {
            String name = in.nextLine();
            int phone = in.nextInt();
            map.put(name, phone);
            in.nextLine();
        }
        while (in.hasNext()) {
            String s = in.nextLine();
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
