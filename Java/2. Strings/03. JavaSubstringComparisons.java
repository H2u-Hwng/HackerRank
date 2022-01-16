// Problem: https://www.hackerrank.com/challenges/java-string-compare/problem

import java.io.*;
import java.util.*;

public class Solution {
    
    public static String getSmallestAndLargest(String s, int k) {
        SortedSet<String> sets = new TreeSet<String>();
        
        for (int i = 0; i <= s.length() - k; i++) {
            sets.add(s.substring(i, i + k));
        }
 
        return sets.first() + "\n" + sets.last();
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        int n = in.nextInt();
        
        System.out.println(getSmallestAndLargest(s, n));
    }
}
