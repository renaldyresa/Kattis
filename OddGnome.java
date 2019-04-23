import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        int [] hls = new int[byk];
        for (int i = 0; i < byk; i++) {
            int byk1 = sc.nextInt();
            int[] b = new int[byk1] ;
            for (int j = 0; j < byk1; j++) {
                b[j] = sc.nextInt();
            }
            for (int j = 0; j < byk1; j++) {
                if (j!=0 && j!=byk1-1) {
                    if (b[j]-b[j-1]!=1) {
                        System.out.println(j+1);
                        break;
                    }
                }
            }
        }
    }
}
