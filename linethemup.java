import java.util.Scanner;

public class LineThemUp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int byk = sc.nextInt();
        String[] kt = new String[byk+1];
        int hls = 0 ;
        for (int i = 0; i < kt.length; i++) {
            kt[i] = sc.nextLine();
        }
        for (int i = 2; i < kt.length; i++) {
            int k = 0 ;
            while(kt[i-1].charAt(k)==kt[i].charAt(k)){
                k++;
            }
            if (kt[i-1].charAt(k)<kt[i].charAt(k)) {
                hls++;
            }
        }
        if (hls+1==byk) {
            System.out.println("INCREASING");           
        }else if (hls == 0){
            System.out.println("DECREASING");
        }else{
            System.out.println("NEITHER");
        }
        
    }
}
