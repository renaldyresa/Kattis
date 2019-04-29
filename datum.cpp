#include <ctime>
#include <iostream>

using namespace std;

int main()
{
    tm waktu = {};
    cin>>waktu.tm_mday;
    cin>>waktu.tm_mon;
    waktu.tm_mon-=1;
    waktu.tm_year=2009;
    waktu.tm_year-=1900;
    mktime( &waktu);
    char * hari[] = { "Sunday", "Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday"};
    cout << hari[waktu.tm_wday]<<endl;
    return 0;
}

