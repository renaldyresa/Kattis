import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        String in =  sc.next();
        int jml = 0;
        char [] dt1 = in.substring(0, in.length()/2).toCharArray();
        char [] dt2 = in.substring(in.length()/2).toCharArray();
        int [] hls1 = new int[dt1.length];
        int [] hls2 = new int[dt2.length];
        char[] hls = new char[dt1.length];
        for (int i = 0; i < dt1.length; i++) {
            jml = jml+(dt1[i]-65);
        }
        for (int i = 0; i < dt1.length; i++) {
            hls1[i] = (((dt1[i]-65)+jml)%26);
        }
        jml =0 ;
        for (int i = 0; i < dt2.length; i++) {
            jml = jml+(dt2[i]-65);
        }
        for (int i = 0; i < dt2.length; i++) {
            hls2[i] = (((dt2[i]-65)+jml)%26);
        }
        for (int i = 0; i < hls1.length; i++) {
            hls[i] = (char)(((hls1[i]+hls2[i])%26)+65) ;
        }
        for (int i = 0; i < hls.length; i++) {
            System.out.print(hls[i]);
        }
        System.out.println("");
    }
    
}
