#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime> 

using namespace std;
unsigned t0, t1;

long long factorial(long long k) {
	unsigned long long int res = 1;
	if(k == 0){
        return res;
    }
    while (k > 0) {
	    res *= k--;	
    }
	return res;
}

int main(){
    t0=clock();
    unsigned long long int X, N, Y;
    long double Pow, S = 0, S1, S2;
    cout<<"Ingresa X: "<<endl;
    cin>>X;
    cout<<"Ingresa N: "<<endl;
    cin>>N;

    for(int i = 0; i != N; i++){
        Pow = pow(X, i);
        Y = factorial(i);
        S1 = Pow/Y;
        S = S + S1;
    }
    cout<<"Valor decimal de sigma de tayor exponencial: "<<setprecision(10)<<S<<endl;
    t1 = clock();
    double time = (double(t1-t0)/(CLOCKS_PER_SEC));
    cout << "Execution Time: " << time << endl;
    return 0;
}

