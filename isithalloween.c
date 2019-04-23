#include <stdio.h>
#include <string.h>
int main() {
    char bulan[3];
    int hari ;
    scanf("%s",&bulan);
    scanf("%d",&hari);
    if(strcmp(bulan,"OCT")==0 && hari==31){
        printf("yup");
    }else if (strcmp(bulan,"DEC")==0 && hari==25){
        printf("yup");
    }else printf("nope");
    return 0 ;
}
