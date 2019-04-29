import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int j =1 ;
        while(sc.hasNextInt()){
            int ak = sc.nextInt();
            int max = 0 , min = 0, range ;
            for (int i = 0; i < ak; i++) {
                int b = sc.nextInt();
                if (i==0) {
                    min = b ;
                    max = b ;
                    continue ;
                }
                if (b<min) {
                    min=b;
                }
                if (b>max) {
                    max=b;
                }
            }
            System.out.println("Case "+j+": "+min+" "+max+" "+(max-min));
            j++;
        }
    sc.close();
    }
}
