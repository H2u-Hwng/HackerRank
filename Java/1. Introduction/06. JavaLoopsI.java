import java.util.Scanner;

public class Solution {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        input.close();
        
        for (int i = 1; i < 11; i ++) {
            int result = num * i;
            System.out.printf("%d x %d = %d %n", num, i, result);
        }
    }
}
