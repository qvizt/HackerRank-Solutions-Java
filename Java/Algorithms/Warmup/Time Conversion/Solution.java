package qvizt;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

/**
 * Solution for Time Conversion
 */
public class Solution {

    /*
     * Complete the timeConversion function below.
     */
    static String timeConversion(String s) {
        try {
            DateFormat oldFormat = new SimpleDateFormat("hh:mm:ssa");
            Date date = oldFormat.parse(s);
            DateFormat newFormat = new SimpleDateFormat("HH:mm:ss");
            return newFormat.format(date);
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return null;
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(
                new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scan.nextLine();

        String result = timeConversion(s);

        bw.write(result);
        bw.newLine();

        bw.close();
    }
}
