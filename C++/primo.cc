#include <iostream>
#include <ctime>

using namespace std;
unsigned t0, t1;
bool esPrimo(int numero);

int main() {
    t0=clock();
    int numero, numero2, cont = 0;
    cout << "Escribe el Lim Inferior:\n";
    cin >> numero;
    cout << "Escribe el Lim Superior:\n";
    cin >> numero2;
    for(int i = numero; i<=numero2; i++){
      if (esPrimo(i)) {
        cout << "Es primo: "<<i<<endl;
        cont++;
      }
    }
    cout<<"La cantidad de primos es:"<<cont; 
    double time = (double(t1-t0)/(CLOCKS_PER_SEC));
    cout << "\nTiempo de ejecucion: " << time << endl;
    return 0;
}

bool esPrimo(int numero) {
  if (numero == 0 || numero == 1 || numero == 4) return false;
  for (int x = 2; x < numero / 2; x++) {
    if (numero % x == 0) return false;
  }
  return true;
}