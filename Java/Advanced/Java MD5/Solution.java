package qvizt;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

/**
 * Solution Java MD5
 */
public class Solution {

    /*
     * Do not forget to import java.security.*
     */
    
    public static void main(String[] args) throws NoSuchAlgorithmException {
        Scanner scanner = new Scanner(System.in);
        String line = scanner.nextLine();
        scanner.close();

        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] bytes = md.digest(line.getBytes());
        for (byte b : bytes) {
            System.out.printf("%02x", b);
        }
    }
}
