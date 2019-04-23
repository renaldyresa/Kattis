import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        String a = sc.nextLine();
        int hls1[] = new int [4] ;
        hls1[0] = 0 ;
        hls1[1] = 0 ;
        hls1[2] = 0 ;
        hls1[3] = 0 ;
        for (int i = 0; i < a.length(); i++) {
            int dd = a.charAt(i);
            if (a.charAt(i)=='_') {
                hls1[0]++;
            }else if (dd>= 65 && dd<= 90) {
                hls1[2]++;
            }else if (dd>= 97 && dd<=122) {
                hls1[1]++;
            }else{
                hls1[3]++;
            }
        }
        for (int i = 0; i < 4; i++) {
            double b = a.length();
            double c = hls1[i];
            double hls = c/b;
            System.out.println(hls);
        }
    }
    
}
