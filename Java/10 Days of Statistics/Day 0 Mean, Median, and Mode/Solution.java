package qvizt;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Solution for Day 0: Mean, Median, and Mode
 */
public class Solution {

    public static double getMean(int[] values) {
        int sum = 0;

        for (int i : values) {
            sum += i;
        }

        double mean = (double) sum / values.length;

        return mean;
    }

    public static double getMedian(int[] values) {
        Arrays.sort(values);

        double median = 0;

        if (values.length % 2 == 1) {
            int index = (values.length + 1) / 2;
            median = values[index];
        } else {
            int leftMidIndex = (values.length - 1) / 2;
            int rightMidIndex = leftMidIndex + 1;
            median = (double) (values[leftMidIndex] + values[rightMidIndex])
                    / 2;
        }

        return median;
    }

    public static int getMode(int[] values) {
        Map<Integer, Integer> valuesCount = new HashMap<>();

        for (int val : values) {
            Integer counter = valuesCount.get(val);
            if (counter == null) {
                counter = new Integer(0);
            }
            counter++;
            valuesCount.put(val, counter);
        }

        int mode = values[0];

        for (int i = 1; i < values.length; i++) {
            int val = values[i];
            int modeCount = valuesCount.get(mode);
            int valCount = valuesCount.get(val);
            if (valCount > modeCount || (valCount == modeCount && val < mode)) {
                mode = val;
            }
        }

        return mode;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
        }
        scanner.close();

        double mean = getMean(values);
        double median = getMedian(values);
        int mode = getMode(values);

        System.out.println(mean);
        System.out.println(median);
        System.out.println(mode);
    }

}
