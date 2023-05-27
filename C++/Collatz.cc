#include <iostream>
#include <ctime>

using namespace std;
unsigned t0, t1;
long int a = 0, cont = 0;

int main(){
    t0=clock();
    cout << "Ingresa un numero: "<<endl;
    cin>>a;
    while(true){
        if (a % 2 == 0)
        {
            cont++;
            a = a / 2;
            cout<<a<<endl;
        }
        else
        {
            a = (a * 3) + 1;
            cout<<a<<endl;
            cont++;
        }
        
        if(a == 1)
        {
            break;
        }
    }
    cout<<"Iteraciones: "<<cont<<endl;
    t1 = clock();
    double time = (double(t1-t0)/(CLOCKS_PER_SEC));
    cout << "Execution Time: " << time << endl;
    return 0;
}