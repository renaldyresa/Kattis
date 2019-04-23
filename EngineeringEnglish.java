import java.util.ArrayList;
import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        ArrayList<String> hls = new ArrayList<>();
        while(sc.hasNextLine()){
            String data = sc.nextLine();
            String data1[] = data.split(" ");
            String data2[] = data.toLowerCase().split(" ");
            for (int i = 0; i < data1.length; i++) {
                if (hls.contains(data2[i])) {
                    System.out.print(". ");
                }else{
                    hls.add(data2[i]);
                    System.out.print(data1[i]+" ");
                }
            }
            System.out.println("");
        }
    }
}
