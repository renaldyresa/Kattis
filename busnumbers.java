import java.util.Arrays;
import java.util.Scanner;

public class Coba {

    public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i=0;i<n;i++)arr[i]=sc.nextInt();
        Arrays.sort(arr);
        System.out.print(arr[0]);
        for(int i=1;i<n;i++){
            if(arr[i]==arr[i-1]+1){
                if(n>i+1&&arr[i+1]==arr[i]+1){
                        System.out.print("-");
                        i+=2;
                        while(n>i&&arr[i]==arr[i-1]+1)i++;
                        i--;
                        System.out.print(arr[i]);
                }else System.out.print(" "+arr[i]);
            }else System.out.print(" "+arr[i]);
        }
        System.out.println();
    }
    
}
