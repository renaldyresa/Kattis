import java.util.ArrayList;
import java.util.Scanner;

public class MixedFractions {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> hls1 = new ArrayList<Integer>();
        ArrayList<Integer> hls2 = new ArrayList<Integer>();
        ArrayList<Integer> hls3 = new ArrayList<Integer>();
        int i = 0 ;
        while(true){
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (a==0 && b==0) {
                break ;
            }
            int c=0;
            while(a>=b){
                int d = a-b ;
                a = d ;
                c++;
            }
            hls1.add(c);
            hls2.add(a);
            hls3.add(b);
        }
        for (int j = 0; j < hls1.size(); j++) {
            System.out.println(hls1.get(j)+" "+hls2.get(j)+" / "+hls3.get(j));           
        }
    }
}
