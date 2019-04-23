import java.util.ArrayList;
import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        ArrayList<Integer> hls = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int in = sc.nextInt();
            int mod = in%42;
            if (hls.contains(mod)) {
                continue ;
            }
            hls.add(mod);
        } 
        System.out.println(hls.size());
    }    
}
