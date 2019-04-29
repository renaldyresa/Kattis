#include <stdio.h>

int main()
{
    int a, b ,c, j;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    int hls = 0 ;
    for(j=1;j<=c;j++){
        if(j%a==0&&j%b==0){
            hls=1;
            break;
        }
    }
    if(hls==1)printf("yes");
    else printf("no");
    return 0;
}
