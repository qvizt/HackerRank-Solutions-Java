package qvizt.solution;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Collections;

class Student {

    /*
     * Class as stub to program the solution without any warnings etc.
     */

}

/**
 * Solution for Java Reflection - Attributes
 */
public class Solution {

    public static void main(String[] args) {
        Class<?> student = Student.class;
        Method[] methods = student.getDeclaredMethods();

        ArrayList<String> methodList = new ArrayList<>();
        for (Method method : methods) {
            methodList.add(method.getName());
        }
        Collections.sort(methodList);
        for (String name : methodList) {
            System.out.println(name);
        }
    }
}
