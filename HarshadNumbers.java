import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        String byk = sc.next();
        int p = 0 , c,ak=Integer.parseInt(byk);
        while(true){
            c = 0 ;
            for (int i = 0; i < byk.length(); i++) {
                int a = Integer.parseInt(byk.charAt(i)+"");
                c = c + a ;
            }
            int d = Integer.parseInt(byk);
            int hls1 = d/c ;
            if ((hls1*c) == d) {
                break ;
            }
            ak = Integer.parseInt(byk)+1;
            byk = String.valueOf(ak);
            p++;
        }
        System.out.println(ak);
    }
    
}
