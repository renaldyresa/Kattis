import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int  byk = sc.nextInt();
        float hls = 0 ;
        for (int i = 0 ; i < byk ; i++){
            float a = sc.nextFloat();
            float b = sc.nextFloat();
            hls = hls + (a*b);
        }
        System.out.println(String.format("%.3f",hls));
    }
    
}
