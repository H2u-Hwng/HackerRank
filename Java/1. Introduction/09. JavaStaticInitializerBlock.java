// Problem: https://www.hackerrank.com/challenges/java-static-initializer-block/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int breadth = in.nextInt();
        int height = in.nextInt();
        
        if (breadth <= 0 || height <= 0) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        } else {
            System.out.println(breadth * height);
        }
    }
}
