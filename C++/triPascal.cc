#include <iostream>
using namespace std;
 
// Function to print the Pascal's Triangle
void print_pascal(int row_num){
    for(int n = 1; n <= row_num; n++){
        int val = 1;
        for(int r = 1; r <= n; r++){
            
            
            //cout<<val<<"   ";
            if(val%2 == 0){
                cout<<"0"<<"   ";
            }else{
                cout<<"1"<<"   ";
            }
            
            val = val * (n - r)/r;
        }
        cout<<endl;
    }
}
 
int main(){
 
    int row_num = 36;
    print_pascal(row_num);
 
    return 1;
}