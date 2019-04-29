import java.util.Scanner;

public class Kattis {

    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int byk = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < byk; i++) {
            String kt = sc.nextLine();
            int a = 1 ;
            System.out.print("Case #"+(i+1)+": ");
            for (int j = 0; j < kt.length(); j++) {
                if (kt.charAt(j)=='a') { if (a!=2) System.out.print("2"); else System.out.print(" 2"); a = 2;  continue;}
                if (kt.charAt(j)=='b') { if (a!=2) System.out.print("22"); else System.out.print(" 22"); a = 2;  continue;}
                if (kt.charAt(j)=='c') { if (a!=2) System.out.print("222"); else System.out.print(" 222"); a = 2;  continue;}
                if (kt.charAt(j)=='d') { if (a!=3) System.out.print("3"); else System.out.print(" 3"); a = 3;  continue;}
                if (kt.charAt(j)=='e') { if (a!=3) System.out.print("33"); else System.out.print(" 33"); a = 3;  continue;}
                if (kt.charAt(j)=='f') { if (a!=3) System.out.print("333"); else System.out.print(" 333"); a = 3;  continue;}
                if (kt.charAt(j)=='g') { if (a!=4) System.out.print("4"); else System.out.print(" 4"); a = 4;  continue;}
                if (kt.charAt(j)=='h') { if (a!=4) System.out.print("44"); else System.out.print(" 44"); a = 4;  continue;}
                if (kt.charAt(j)=='i') { if (a!=4) System.out.print("444"); else System.out.print(" 444"); a = 4;  continue;}
                if (kt.charAt(j)=='j') { if (a!=5) System.out.print("5"); else System.out.print(" 5"); a = 5;  continue;}
                if (kt.charAt(j)=='k') { if (a!=5) System.out.print("55"); else System.out.print(" 55"); a = 5;  continue;}
                if (kt.charAt(j)=='l') { if (a!=5) System.out.print("555"); else System.out.print(" 555"); a = 5;  continue;}
                if (kt.charAt(j)=='m') { if (a!=6) System.out.print("6"); else System.out.print(" 6"); a = 6;  continue;}
                if (kt.charAt(j)=='n') { if (a!=6) System.out.print("66"); else System.out.print(" 66"); a = 6;  continue;}
                if (kt.charAt(j)=='o') { if (a!=6) System.out.print("666"); else System.out.print(" 666"); a = 6;  continue;}
                if (kt.charAt(j)=='p') { if (a!=7) System.out.print("7"); else System.out.print(" 7"); a = 7;  continue;}
                if (kt.charAt(j)=='q') { if (a!=7) System.out.print("77"); else System.out.print(" 77"); a = 7;  continue;}
                if (kt.charAt(j)=='r') { if (a!=7) System.out.print("777"); else System.out.print(" 777"); a = 7;  continue;}
                if (kt.charAt(j)=='s') { if (a!=7) System.out.print("7777"); else System.out.print(" 7777"); a = 7;  continue;}
                if (kt.charAt(j)=='t') { if (a!=8) System.out.print("8"); else System.out.print(" 8"); a = 8;  continue;}
                if (kt.charAt(j)=='u') { if (a!=8) System.out.print("88"); else System.out.print(" 88"); a = 8;  continue;}
                if (kt.charAt(j)=='v') { if (a!=8) System.out.print("888"); else System.out.print(" 888"); a = 8;  continue;}
                if (kt.charAt(j)=='w') { if (a!=9) System.out.print("9"); else System.out.print(" 9"); a = 9;  continue;}
                if (kt.charAt(j)=='x') { if (a!=9) System.out.print("99"); else System.out.print(" 99"); a = 9;  continue;}
                if (kt.charAt(j)=='y') { if (a!=9) System.out.print("999"); else System.out.print(" 999"); a = 9;  continue;}
                if (kt.charAt(j)=='z') { if (a!=9) System.out.print("9999"); else System.out.print(" 9999"); a = 9;  continue;}
                if (kt.charAt(j)==' ') { if (a!=0) System.out.print("0"); else System.out.print(" 0"); a = 0;  continue;}
            }
            System.out.println("");
        }
    }
}
