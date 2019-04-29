import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        for (int i = 0; i < byk; i++) {
            int k = sc.nextInt();
            int n = sc.nextInt();
            int s1 = 0, s2 = 0 ,s3=0;         
            for (int j = 1; j < n+1; j++) {
                s1 += j ;
            }
            s3 = s1  + s1 ;
            s2 = s3 - n;
            System.out.println(k+" "+s1+" "+s2+" "+s3);
        }
        
    }
}
