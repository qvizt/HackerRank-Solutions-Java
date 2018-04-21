package qvizt.solution;

import java.time.LocalDate;
import java.util.Scanner;

/**
 * Solution for Java Date and Time
 */
public class Solution {

    /*-
     * Be aware that the import statement has to be written before the public
     * class declaration in the buffer window on line 3, e.g.:
     * 
         import java.time.LocalDate;
         public class Solution { ......
     * 
     */
    public static String getDay(String day, String month, String year) {
        int dayAsInteger = Integer.valueOf(day);
        int monthAsInteger = Integer.valueOf(month);
        int yearAsInteger = Integer.valueOf(year);

        LocalDate date = LocalDate.of(yearAsInteger, monthAsInteger,
                dayAsInteger);
        return date.getDayOfWeek().toString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();

        System.out.println(getDay(day, month, year));
        in.close();
    }
}
