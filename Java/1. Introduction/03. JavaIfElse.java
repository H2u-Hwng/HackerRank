import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        
        String result = (num % 2 != 0 || (num % 2 == 0 && num >= 6 && num <= 20)) ? "Weird" : "Not Weird";
        System.out.println(result); 
    }
}
