import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        String kata = sc.nextLine();
        kata = kata.toLowerCase();
        String hls = "";
        for (int i = 0; i < kata.length(); i++) {
            if (kata.charAt(i)=='a') { hls +="@"; continue; }
            if (kata.charAt(i)=='b') { hls +="8"; continue; }
            if (kata.charAt(i)=='c') { hls +="("; continue; }
            if (kata.charAt(i)=='d') { hls +="|)"; continue; }
            if (kata.charAt(i)=='e') { hls +="3"; continue; }
            if (kata.charAt(i)=='f') { hls +="#"; continue; }
            if (kata.charAt(i)=='g') { hls +="6"; continue; }
            if (kata.charAt(i)=='h') { hls +="[-]"; continue; }
            if (kata.charAt(i)=='i') { hls +="|"; continue; }
            if (kata.charAt(i)=='j') { hls +="_|"; continue; }
            if (kata.charAt(i)=='k') { hls +="|<"; continue; }
            if (kata.charAt(i)=='l') { hls +="1"; continue; }
            if (kata.charAt(i)=='m') { hls +="[]\\/[]"; continue; }
            if (kata.charAt(i)=='n') { hls +="[]\\[]"; continue; }
            if (kata.charAt(i)=='o') { hls +="0"; continue; }
            if (kata.charAt(i)=='p') { hls +="|D"; continue; }
            if (kata.charAt(i)=='q') { hls +="(,)"; continue; }
            if (kata.charAt(i)=='r') { hls +="|Z"; continue; }
            if (kata.charAt(i)=='s') { hls +="$"; continue; }
            if (kata.charAt(i)=='t') { hls +="']['"; continue; }
            if (kata.charAt(i)=='u') { hls +="|_|"; continue; }
            if (kata.charAt(i)=='v') { hls +="\\/"; continue; }
            if (kata.charAt(i)=='w') { hls +="\\/\\/"; continue; }
            if (kata.charAt(i)=='x') { hls +="}{"; continue; }
            if (kata.charAt(i)=='y') { hls +="`/"; continue; }
            if (kata.charAt(i)=='z') { hls +="2"; continue; }
            if (kata.charAt(i)==' ') { hls +=" "; continue; }
            hls+=kata.charAt(i);
        }
        System.out.println(hls);
    }
}
