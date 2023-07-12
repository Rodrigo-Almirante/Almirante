#include <stdio.h>

int main() {
   float numero1, numero2, porcentaje;

   // Pedir al usuario que ingrese dos números
   printf("\nIngrese el primer numero: ");
   scanf("%f", &numero1);
   printf("Ingrese el segundo numero: ");
   scanf("%f", &numero2);

   // Calcular el porcentaje
   porcentaje = (numero1 / numero2) * 100;

   // Mostrar el resultado
   printf("\nEl porcentaje entre %.2f y %.2f es: %%%.2f", numero1, numero2, porcentaje);

   return 0;
}
