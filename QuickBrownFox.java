import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        String [] data = new String[byk+1]; 
        for (int i = 0; i < byk+1; i++) {
            data[i] = sc.nextLine();
            data[i] = data[i].toLowerCase();
        }
        String [] hls = new String [byk+1];
        for (int i = 1; i < byk+1; i++) {
            hls[i]="";
            if (data[i].indexOf("a")==-1) hls[i]+="a";
            if (data[i].indexOf("b")==-1) hls[i]+="b"; 
            if (data[i].indexOf("c")==-1) hls[i]+="c";
            if (data[i].indexOf("d")==-1) hls[i]+="d";
            if (data[i].indexOf("e")==-1) hls[i]+="e";
            if (data[i].indexOf("f")==-1) hls[i]+="f";
            if (data[i].indexOf("g")==-1) hls[i]+="g";
            if (data[i].indexOf("h")==-1) hls[i]+="h";
            if (data[i].indexOf("i")==-1) hls[i]+="i";
            if (data[i].indexOf("j")==-1) hls[i]+="j";
            if (data[i].indexOf("k")==-1) hls[i]+="k";
            if (data[i].indexOf("l")==-1) hls[i]+="l";
            if (data[i].indexOf("m")==-1) hls[i]+="m";
            if (data[i].indexOf("n")==-1) hls[i]+="n";
            if (data[i].indexOf("o")==-1) hls[i]+="o";
            if (data[i].indexOf("p")==-1) hls[i]+="p";
            if (data[i].indexOf("q")==-1) hls[i]+="q";
            if (data[i].indexOf("r")==-1) hls[i]+="r";
            if (data[i].indexOf("s")==-1) hls[i]+="s";
            if (data[i].indexOf("t")==-1) hls[i]+="t";
            if (data[i].indexOf("u")==-1) hls[i]+="u";
            if (data[i].indexOf("v")==-1) hls[i]+="v";
            if (data[i].indexOf("w")==-1) hls[i]+="w";
            if (data[i].indexOf("x")==-1) hls[i]+="x";
            if (data[i].indexOf("y")==-1) hls[i]+="y";
            if (data[i].indexOf("z")==-1) hls[i]+="z";           
        }
        for (int i = 1; i < byk+1; i++) {
            if (hls[i].length()==0) {
                System.out.println("pangram");
            }else 
                System.out.println("missing "+hls[i]);
        }
    }
}
