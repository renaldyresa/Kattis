#include <stdio.h>

int main() {
    int byk ;
    scanf("%d",&byk);
    while(byk>0){
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        int hls = 0 ;
        while(c>0){
            hls += (c%b)*(c%b);
            c=c/b;
        }
        printf("%d %d\n",a,hls);
        byk--;
    }
    return 0 ;
}
