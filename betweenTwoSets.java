import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static int getMaxValue(int[] array) {
        int maxValue = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > maxValue) {
                maxValue = array[i];
            }
        }
        return maxValue;
    }

    static boolean inB(int x,int[] b){
        int j = 0;
        for(int i=0; i<b.length; i++){
            if (b[i]%x==0){
               j++;
            }
            else{break;}
        }
        if(j==b.length){return true;}
        else{return false;}
    }

    static boolean inA(int x,int[] a){
         int j =0;
         for(int i = 0;i<a.length;i++){
             if(x%a[i]==0){
                 j++;
             }
             else{break;}
         }
         if(j==a.length){
             return true;
         }
         else{
             return false;
         }
    }
    
    static int getTotalX(int[] a, int[] b) {
        
        int x=0;
        int z = getMaxValue(b);
        for(int i =1; i<=z; i++){
            if(inB(i,b)){
                if(inA(i,a)){
                    x++;
                }
            }
        }
     return x;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[] a = new int[n];
        for(int a_i = 0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
        int[] b = new int[m];
        for(int b_i = 0; b_i < m; b_i++){
            b[b_i] = in.nextInt();
        }
        int total = getTotalX(a, b);
        System.out.println(total);
        in.close();
    }
}
