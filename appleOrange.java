import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int[] appleAndOrange(int s, int t, int a, int b, int[] apple, int[] orange) {
       int apps = 0, orgs = 0;
       
        for(int i=0; i<apple.length; i++){
            if(apple[i]+a >= s && apple[i]+a <= t){apps++;}
        }
        for(int j=0;j<orange.length;j++){
            if(orange[j]+b >= s && orange[j]+b <= t){orgs++;}
        }      
                  return new int[]{apps,orgs}    ;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int t = in.nextInt();
        int a = in.nextInt();
        int b = in.nextInt();
        int m = in.nextInt();
        int n = in.nextInt();
        int[] apple = new int[m];
        for(int apple_i = 0; apple_i < m; apple_i++){
            apple[apple_i] = in.nextInt();
        }
        int[] orange = new int[n];
        for(int orange_i = 0; orange_i < n; orange_i++){
            orange[orange_i] = in.nextInt();
        }
        int[] result = appleAndOrange(s, t, a, b, apple, orange);
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + (i != result.length - 1 ? "\n" : ""));
        }
        System.out.println("");


        in.close();
    }
}
