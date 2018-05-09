package qvizt;

import java.time.LocalDate;
import java.util.Scanner;

/**
 * Solution for Day 26: Nested Logic
 */
public class Solution {

    public static int getFee(LocalDate actDate, LocalDate expDate) {
        int fee = 0;
        if (actDate.isAfter(expDate)) {
            if (actDate.getYear() > expDate.getYear()) {
                fee = 10000;
            } else if (actDate.getMonthValue() > expDate.getMonthValue()) {
                fee = (actDate.getMonthValue() - expDate.getMonthValue()) * 500;
            } else {
                fee = (actDate.getDayOfMonth() - expDate.getDayOfMonth()) * 15;
            }
        }

        return fee;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int actDay = scanner.nextInt();
        int actMonth = scanner.nextInt();
        int actYear = scanner.nextInt();
        int expDay = scanner.nextInt();
        int expMonth = scanner.nextInt();
        int expYear = scanner.nextInt();
        scanner.close();

        LocalDate actDate = LocalDate.of(actYear, actMonth, actDay);
        LocalDate expDate = LocalDate.of(expYear, expMonth, expDay);

        int fee = getFee(actDate, expDate);
        System.out.println(fee);
    }

}
