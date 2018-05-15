package qvizt;

import java.util.Scanner;

/**
 * Solution for Day 9: Multiple Linear Regression
 */
public class Solution {

    /*
     * Modified code based on the code at
     * 
     * https://www.codeproject.com/Articles/405128/Matrix-operations-in-Java
     */

    public static double[][] transpose(double[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        double[][] transposed = new double[cols][rows];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                transposed[j][i] = matrix[i][j];
            }
        }
        return transposed;
    }

    public static double[][] createSubMatrix(double[][] matrix,
            int excludingRow, int excludingCol) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        double[][] subMatrix = new double[rows - 1][cols - 1];
        int r = -1;
        for (int i = 0; i < rows; i++) {
            if (i == excludingRow) {
                continue;
            }
            r++;
            int c = -1;
            for (int j = 0; j < cols; j++) {
                if (j == excludingCol) {
                    continue;
                }
                subMatrix[r][++c] = matrix[i][j];
            }
        }
        return subMatrix;
    }

    public static double determinant(double[][] matrix) {
        if (matrix.length == 1) {
            return matrix[0][0];
        }
        if (matrix.length == 2) {
            return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]);
        }
        double sum = 0.0;
        for (int i = 0; i < matrix[0].length; i++) {
            sum += getSign(i) * matrix[0][i]
                    * determinant(createSubMatrix(matrix, 0, i));
        }
        return sum;
    }

    public static double[][] multiply(double[][] a, double[][] b) {
        int aRows = a.length;
        int aCols = a[0].length;
        int bCols = b[0].length;
        double[][] matrix = new double[aRows][bCols];
        for (int i = 0; i < aRows; i++)
            for (int j = 0; j < bCols; j++)
                for (int k = 0; k < aCols; k++)
                    matrix[i][j] += a[i][k] * b[k][j];
        return matrix;
    }

    public static double getSign(int i) {
        return i % 2 == 0 ? 1 : -1;
    }

    public static double[][] cofactor(double[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        double[][] cofactor = new double[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                cofactor[i][j] = getSign(i) * getSign(j)
                        * determinant(createSubMatrix(matrix, i, j));
            }
        }

        return cofactor;
    }

    public static double[][] multiplyByConstant(double[][] matrix,
            double constant) {
        double[][] multMatrix = new double[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                multMatrix[i][j] = matrix[i][j] * constant;
            }
        }
        return multMatrix;
    }

    public static double[][] inverse(double[][] matrix) {
        return multiplyByConstant(transpose(cofactor(matrix)),
                1.0 / determinant(matrix));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        double[][] xMatrix = new double[n][m + 1];
        double[][] yMatrix = new double[n][1];

        for (int i = 0; i < n; i++) {
            xMatrix[i][0] = 1.0;
            for (int k = 1; k <= m; k++) {
                xMatrix[i][k] = scanner.nextDouble();
            }
            yMatrix[i][0] = scanner.nextDouble();
        }

        double[][] x = multiply(
                multiply(inverse(multiply(transpose(xMatrix), xMatrix)),
                        transpose(xMatrix)),
                yMatrix);

        int q = scanner.nextInt();
        for (int i = 0; i < q; i++) {
            yMatrix = new double[1][m + 1];
            yMatrix[0][0] = 1;
            for (int k = 1; k <= m; k++) {
                yMatrix[0][k] = scanner.nextDouble();
            }

            double[][] ymxtx = multiply(yMatrix, x);
            System.out.printf("%.2f\n", ymxtx[0][0]);
        }

        scanner.close();
    }
}
