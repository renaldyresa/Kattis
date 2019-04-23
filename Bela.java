import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        char dom = sc.next().charAt(0);
        int hls = 0;
        for (int i = 0; i < byk*4; i++) {
            String in = sc.next();
            if (dom == in.charAt(1)) {
                if (in.charAt(0)=='A') {
                    hls += 11 ;
                }else if (in.charAt(0)=='K') {
                    hls += 4 ;
                }else if (in.charAt(0)=='Q') {
                    hls += 3 ;
                }else if (in.charAt(0)=='J') {
                    hls += 20 ;
                }else if (in.charAt(0)=='T') {
                    hls += 10 ;
                }else if (in.charAt(0)== '9') {
                    hls += 14 ;
                }
            }else {
                if (in.charAt(0)=='A') {
                    hls += 11 ;
                }else if (in.charAt(0)=='K') {
                    hls += 4 ;
                }else if (in.charAt(0)=='Q') {
                    hls += 3 ;
                }else if (in.charAt(0)=='J') {
                    hls += 2 ;
                }else if (in.charAt(0)=='T') {
                    hls += 10 ;
                }
            }
        }
        System.out.println(hls);
    }
    
}
