import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        float [] hls1 = new float [byk];
        float [] hls2= new float [byk];
        for (int i = 0; i < byk; i++) {
            float ak1 = sc.nextInt();
            float ak2 = sc.nextFloat();
            hls2[i] = 60*ak1/ak2;
            hls1[i] = 60/ak2;

        }
        for (int i = 0; i < byk; i++) {
            System.out.println(String.format("%.4f", (hls2[i]-hls1[i]))+String.format(" %.4f", hls2[i])+String.format(" %.4f", (hls2[i]+hls1[i])));
        }
    }
    
}
