#include <iostream>
#include <random>
#include <string.h>

using namespace std;
default_random_engine generator;

int main(){
    int len=0, number;
    int dice_roll;
    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
    char special[] = "`~!@#$%^&*()_+=-][{}';:<>?/.,¿ñ";
    char numbers[] = "0123456789";
    string password= "";
    
    uniform_int_distribution<int> distribution(1,3);
    uniform_int_distribution<int> distribution2(0,strlen(alphabet));
    uniform_int_distribution<int> distribution3(0,strlen(special));
    uniform_int_distribution<int> distribution4(0,strlen(numbers));

    cout<<"Cuantos caracteres tiene que tener la contraseña? ";
    cin>>len;


    for(int i=0;i<len;i++){
        dice_roll = distribution(generator);  

        if(dice_roll == 2)//abecedario
        {
            number = distribution2(generator);  
            password = password + alphabet[number];
        }
        else if (dice_roll == 1)//especiales
        {
            number = distribution3(generator);  
            password = password + alphabet[number];
        }
        else if (dice_roll == 0)//numeros
        {
            number = distribution4(generator);  
            password = password + alphabet[number];
        }
    }

    cout<<password;
    return 0;
}