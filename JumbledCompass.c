#include <stdio.h>

int main()
{
    int a, b , j=1;
    scanf("%d", &a);
    scanf("%d", &b);
    int hls = (360-a)+b;
    while (hls>360){
        hls = hls-360;
    }
    if(hls<=180){
        printf("%d",hls);
    }else{
        hls = hls-360;
        printf("%d",hls);
    }
    return 0;
}
