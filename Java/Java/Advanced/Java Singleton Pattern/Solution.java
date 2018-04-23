package qvizt.solution;

/**
 * Solution for Java Singleton Pattern
 */
public class Solution {

}

class Singleton {

    private static Singleton singleton;

    public String str;

    private Singleton() {
        // private on purpose
    }

    public static Singleton getSingleInstance() {
        if (singleton == null) {
            singleton = new Singleton();
        }
        return singleton;
    }
}