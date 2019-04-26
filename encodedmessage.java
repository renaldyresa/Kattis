import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int in = sc.nextInt();
        String [] hls = new String [in];
        for (int k = 0; k < in; k++) {
            String  kata = sc.next();
            int pangkat = 0 ;
            int ul = 0 ;
            while(true){
                ul++;
                pangkat = ul*ul;
                if(kata.length()<= pangkat){
                    int cl = pangkat-kata.length();
                    for (int i = 0; i <cl; i++) {
                        kata = kata + "*" ;
                    }
                    break ;
                }
            }
            String [][] kt =  new String [ul][ul];
            int d = 0;
            for (int i = 0; i < ul; i++) {
                for (int j = ul-1; j >=0; j--) {
                    kt[j][i]= kata.charAt(d)+"";
                    d++;
                }
            }
            String kta="" ;
            for (int i = 0; i < ul; i++) {
                for (int j = 0; j < ul; j++) {
                    kta = kta+kt[i][j];
                }
            }
            hls [k] = kta ;
        }
        for (int i = 0; i < in; i++) {
            System.out.println(hls[i]);
        }
        
    }
    
}
