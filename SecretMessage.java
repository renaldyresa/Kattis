import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        String kt = sc.nextLine();
        for (int i = 0; i < byk; i++) {
            kt = sc.nextLine();
            int k = 1,l=1;
            while(kt.length()>l){
                k++;
                l = k*k;
            }
            char[][] c = new char[k][k];
            int o = 0 ;
            for (int j = 0; j < k; j++) {
                for (int m = 0; m < k; m++) {
                    if (o<kt.length()) {
                         c[j][m] = kt.charAt(o);
                    }else c[j][m] = '*';
                    o++;
                }
            }
            for (int j = 0; j < k; j++) {
                for (int m = k-1; m >=0 ; m--) {
                    if (c[m][j]=='*') {
                        System.out.print("");
                    }else
                    System.out.print(c[m][j]);
                }
            }
            System.out.println("");
        }
    }
}
