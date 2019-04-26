#include <iostream>

using namespace std;

int faktorial (int bil)
{
      if(bil==1)
            return 1;
      else
            return bil*faktorial(bil-1);
}

int main()
{
    int byk ;
    cin >> byk ;
    int hls [byk];
    for(int i=0 ; i<byk ; i++){
        int ak ;
        cin >> ak ;
        hls[i] = faktorial(ak);
    }
    for (int i=0 ; i<byk ; i++){
        cout << hls[i]%10 << endl;
    }
    return 0;
}
