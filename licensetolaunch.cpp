#include <iostream>

using namespace std;

int main()
{
    int byk ;
    cin >> byk ;
    int dt [byk];
    for (int i=0 ; i<byk ; i++){
        cin >> dt[i];
    }
    int mi = dt[0];
    int hls = 0 ;
    for(int i=1 ; i<byk ;i++){
        if (dt[i]<mi){
            mi = dt[i];
            hls =i ;
        }
    }
    cout<<hls<<endl;
    return 0;
}
