#include <iostream>
using namespace std;

int main() {
   float numero1, numero2, porcentaje;

   // Pedir al usuario que ingrese dos números
   cout << "\nIngrese el primer numero: ";
   cin >> numero1;
   cout << "Ingrese el segundo numero: ";
   cin >> numero2;

   // Calcular el porcentaje
   porcentaje = (numero1 / numero2) * 100;

   // Mostrar el resultado
   cout << "\nEl porcentaje entre " << numero1 << " y " << numero2 << " es: %" << porcentaje << "\n"; 

   return 0;
}
