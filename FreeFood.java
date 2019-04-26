import java.util.ArrayList;
import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        ArrayList<Integer> hls = new ArrayList<Integer>();
        int byk = sc.nextInt();
        int [] dt1 = new int [byk];
        int [] dt2 = new int [byk];
        for (int i = 0; i < byk; i++) {
            dt1[i] = sc.nextInt();
            dt2[i] = sc.nextInt();
        }
        for (int i = 0; i < byk; i++) {
            for (int j = dt1[i]; j < dt2[i]+1; j++) {
                int t = 0 ;
                for (int k = 0; k < hls.size(); k++) {
                    if ( j == hls.get(k)) {
                        t = 1 ;
                        break ;
                    }
                }
                if (t==0) {
                    hls.add(j);
                }
            }
        }
        System.out.println(hls.size());
    }
    
}
