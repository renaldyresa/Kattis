#include <stdio.h>

int main() {
    float ak ;
    scanf("%f",&ak);
    float a = 1000 ;
    float b = 5280 ;
    float c = 4854 ;
    float hls = a*(b/c)*ak;
    int hh = hls ;
    float d = hh ;
    if (hls-hh <= 0.5)printf("%d",hh);
    else printf("%d",(hh+1));
    return 0;
}
