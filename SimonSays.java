import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        for (int i = 0; i < byk+1; i++) {
            String kata = sc.nextLine();
            if (kata.indexOf("Simon says")==0) {
                System.out.println(kata.substring(11));
            }
        }       
    }    
}
