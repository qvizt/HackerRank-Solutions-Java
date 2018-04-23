package qvizt;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

class Student {

    private int id;
    private String name;
    private double CGPA;

    Student(int id, String name, double cgpa) {
        this.id = id;
        this.name = name;
        this.CGPA = cgpa;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getCGPA() {
        return CGPA;
    }

}

class Priorities {

    /*
     * Do not forget to import Comparator and PriorityQueue
     */

    private static Comparator<Student> studentComparator = new Comparator<Student>() {

        @Override
        public int compare(Student o1, Student o2) {
            int result = Double.compare(o2.getCGPA(), o1.getCGPA());
            if (result == 0) {
                result = o1.getName().compareTo(o2.getName());
            }
            if (result == 0) {
                result = Integer.compare(o1.getId(), o2.getId());
            }
            return result;
        }
    };

    private PriorityQueue<Student> queue;

    public Priorities() {
        queue = new PriorityQueue<>(studentComparator);
    }

    List<Student> getStudents(List<String> events) {
        List<Student> students = new ArrayList<>();

        for (int i = 0; i < events.size(); i++) {
            String event = events.get(i);
            String[] details = event.split(" ");
            switch (details[0]) {
                case "ENTER":
                    double cgpa = Double.valueOf(details[2]);
                    int id = Integer.valueOf(details[3]);
                    Student student = new Student(id, details[1], cgpa);
                    queue.offer(student);
                    break;
                case "SERVED":
                    queue.poll();
                    break;
            }
        }

        while (!queue.isEmpty()) {
            students.add(queue.poll());
        }
        return students;
    }

}

/**
 * Solution for Java Priority Queue
 */
public class Solution {

    private final static Scanner scan = new Scanner(System.in);
    private final static Priorities priorities = new Priorities();

    public static void main(String[] args) {
        int totalEvents = Integer.parseInt(scan.nextLine());
        List<String> events = new ArrayList<>();

        while (totalEvents-- != 0) {
            String event = scan.nextLine();
            events.add(event);
        }

        List<Student> students = priorities.getStudents(events);

        if (students.isEmpty()) {
            System.out.println("EMPTY");
        } else {
            for (Student st : students) {
                System.out.println(st.getName());
            }
        }
    }
}
