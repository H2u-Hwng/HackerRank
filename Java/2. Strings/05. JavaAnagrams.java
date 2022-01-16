// Problem: https://www.hackerrank.com/challenges/java-anagrams/problem

import java.io.*;
import java.util.*;

public class Solution {
    
    public static String sort(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        String sorted = new String(chars);
        return sorted;
    }
    
    public static boolean isAnagram(String a, String b) {
        a = sort(a.toLowerCase());
        b = sort(b.toLowerCase());
        return a.equals(b);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s1 = in.next();
        String s2 = in.next();
        if (isAnagram(s1, s2)) {
            System.out.println("Anagrams");
        } else {
            System.out.println("Not Anagrams");
        }
    }
}
