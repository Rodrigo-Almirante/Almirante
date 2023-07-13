#include <iostream>
using namespace std;

int main() {
   float numero1, numero2, porcentaje,diferencia;

   // Pedir al usuario que ingrese dos números
   cout << "\nIngrese el primer numero: ";
   cin >> numero1;
   cout << "Ingrese el segundo numero: ";
   cin >> numero2;

    // Verificar si el primer número es mayor que el segundo
    while (numero1 <= numero2) {
        cout << "El segundo numero debe ser menor que el primero. Por favor, ingrese un numero valido." << endl;
        
        cout << "Ingrese el segundo numero nuevamente: ";
        cin >> numero2;
    }

   // Calcular el porcentaje
   diferencia = numero1 - numero2;
   porcentaje = (diferencia / numero2) * 100;


   // Mostrar el resultado
   cout << "\nEl porcentaje entre " << numero1 << " y " << numero2 << " es: %" << porcentaje << "\n"; 

    // Esperar a que se toque una tecla para continuar
    cout << "\nPresione enter para continuar...";
    cin.ignore();
    cin.get();
    


   return 0;
}
