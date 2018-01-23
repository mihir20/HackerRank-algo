import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static String[] min = {"","one minute ","two minutes ","three minutes ","four minutes ",
    "five minutes ","six minutes ","seven minutes ","eight minutes ","nine minutes ",
    "ten minutes ","eleven minutes ","twelve minutes ","thirteen minutes ","fourteen minutes ",
    "quarter ","sixteen minutes ","seventeen minutes ","eighteen minutes ",
    "ninteen minutes ","twenty minutes ","twenty one minutes ","twenty two minutes ",
    "twenty three minutes ",
    "twenty four minutes ","twenty five minutes ","twenty six minutes ","twenty seven minutes ",
    "twenty eight minutes ", "twenty nine minutes ", "half "};
    static String[] hrs = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
     "eleven", "twelve"};

    static String timeInWords(int h, int m) {
        String s;
        if(m<=30 && m!=0){
            s=min[m]+"past "+hrs[h-1];
            return s;
        }else if(m==0){
            s=hrs[h-1]+" o' clock";
            return s;
        }else{
            s=min[30-m%30]+"to "+hrs[h];
            return s;
        }
        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int h = in.nextInt();
        int m = in.nextInt();
        String result = timeInWords(h, m);
        System.out.println(result);
        in.close();
    }
}
