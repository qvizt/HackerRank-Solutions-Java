package qvizt.solution;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

/**
 * Solution for Java Sort
 */
class Student {
    private int id;
    private String fname;
    private double cgpa;

    public Student(int id, String fname, double cgpa) {
        super();
        this.id = id;
        this.fname = fname;
        this.cgpa = cgpa;
    }

    public int getId() {
        return id;
    }

    public String getFname() {
        return fname;
    }

    public double getCgpa() {
        return cgpa;
    }
}

/**
 * Solution for Java Sort
 */
public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());

        List<Student> studentList = new ArrayList<Student>();
        while (testCases > 0) {
            int id = in.nextInt();
            String fname = in.next();
            double cgpa = in.nextDouble();

            Student st = new Student(id, fname, cgpa);
            studentList.add(st);

            testCases--;
        }

        Comparator<Student> studentComparator = new Comparator<Student>() {

            @Override
            public int compare(Student o1, Student o2) {
                int result = Double.compare(o2.getCgpa(), o1.getCgpa());
                if (result == 0) {
                    result = o1.getFname().compareTo(o2.getFname());
                }
                if (result == 0) {
                    result = Integer.compare(o1.getId(), o2.getId());
                }
                return result;
            }

        };
        Collections.sort(studentList, studentComparator);

        for (Student st : studentList) {
            System.out.println(st.getFname());
        }

        in.close();
    }

}
