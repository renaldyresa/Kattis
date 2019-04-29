import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int a =1 ;
        while(true){
            a = sc.nextInt();
            if (a==0) {
                break;
            }
            int hls1 = 0;
            long hls2 = 0;
            int k = 11 ;
            String ak1 = String.valueOf(a)+" ";
            for (int i = 0; i < ak1.length()-1; i++) {
                hls1 += Integer.parseInt(ak1.substring(i, i+1));
            }
            while(hls1 != hls2){
                hls2 = 0 ;
                String ak = String.valueOf(a*k)+" ";
                for (int i = 0; i < ak.length()-1; i++) {
                    hls2 += Integer.parseInt(ak.substring(i, i+1));
                }
                
                k++;
            }
            System.out.println(k-1);
        }
    }
}
