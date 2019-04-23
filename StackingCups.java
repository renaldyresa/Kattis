import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        String[] hls = new String[byk];
        String kt = sc.nextLine();
        for (int i = 0; i < byk; i++) {
            kt = sc.nextLine();
            if (kt.charAt(0)<58) {
                hls[i] = kt.split(" ")[1] + " "+kt.split(" ")[0] ;
            }else {
                String s = kt.split(" ")[1];
                int d = Integer.parseInt(s)*2;
                hls[i] = kt.split(" ")[0] + " "+String.valueOf(d) ;
            }
        }
        for (int i = 0; i < byk-1; i++) {
            for (int j = i+1; j < byk; j++) {
                int c = Integer.parseInt(hls[i].split(" ")[1]);
                int d = Integer.parseInt(hls[j].split(" ")[1]);
                if (c>d) {
                    String a = hls[j];
                    hls[j] = hls[i];
                    hls[i] = a ;
                }
            }
        }
        for (int i = 0; i < byk; i++) {
            System.out.println(hls[i].split(" ")[0]);
        }
    }
}
