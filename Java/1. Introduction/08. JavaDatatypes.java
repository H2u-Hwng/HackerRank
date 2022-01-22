// Problem: https://www.hackerrank.com/challenges/java-datatypes/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
            try {
                long x = in.nextLong();
                
                System.out.println(x + " can be fitted in:");
                
                if (x == (byte)x) System.out.println("* byte");
                if (x == (short)x) System.out.println("* short");
                if (x == (int)x) System.out.println("* int");
                if (x == (long)x) System.out.println("* long");
            }
            catch(Exception e) {
                System.out.println(in.next() + " can't be fitted anywhere.");
            }

        }
    }
}
