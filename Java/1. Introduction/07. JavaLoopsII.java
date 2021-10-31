import java.util.*;
import java.io.*;

class Solution {
    public static void main(String[] argh) {
        Scanner input = new Scanner(System.in);
        int q = input.nextInt(); 
        for (int i = 0; i < q; i ++) {
            int a = input.nextInt();
            int b = input.nextInt();
            int n = input.nextInt();
            int s = a;
            for (int j = 0; j < n; j ++) {
                s += Math.pow(2, j) * b;
                System.out.printf("%d ", s);
            }
            System.out.println();
        }
        input.close();  
    }
}
