#include <bits/stdc++.h>
#include <ctime>
#include <unistd.h>

using namespace std;
unsigned t0, t1;
unsigned int microsecond = 1000000;
int myNum[3] = {10, 20, 30};

int main() {
    t0=clock();
    int res;
    // move value to register %eax
    // move value to register %ebx
    // subtracting and storing result in res
    __asm__ (   "movl $20, %%eax;"
                "movl $10, %%ebx;"
                "subl %%ebx, %%eax ":"=a"(res));
    cout<<res<<endl;
   
    
    for(int i = 0; i<3; i++){
        cout<<myNum[i]<<endl;
    }
    usleep(10 * microsecond);//sleeps for 3 second
    t1 = clock();
    double time = (double(t1-t0)/(CLOCKS_PER_SEC));
    cout << "Execution Time: " << time << endl;
    return 0; 
}
