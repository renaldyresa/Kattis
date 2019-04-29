import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int a , b ;
        while(true){
            a = sc.nextInt();
            b = sc.nextInt();
            if (a == 0 && b ==0) {
                break;
            }
            if (a+b==13) {
                System.out.println("Never speak again.");
            }else if (a-b==0) {
                System.out.println("Undecided.");
            }else if (a-b>0) {
                System.out.println("To the convention.");
            }else{
                System.out.println("Left beehind.");
            }
        }
        
    }
}
