#include <stdio.h>

int main() {
   float numero1, numero2, porcentaje,diferencia;

   // Pedir al usuario que ingrese dos números
   printf("\nIngrese el primer numero: ");
   scanf("%f", &numero1);
   printf("Ingrese el segundo numero: ");
   scanf("%f", &numero2);

    // Verificar si el primer número es mayor que el segundo
    while (numero1 <= numero2) {
        printf("El segundo numero debe ser menor que el primero. Por favor, ingrese un numero valido.\n");
        printf("Ingrese el segundo numero nuevamente: ");
        scanf("%f", &numero2);
    }


   // Calcular el porcentaje
   diferencia = numero1 - numero2;
   porcentaje = (diferencia / numero2) * 100;

   // Mostrar el resultado
   printf("\nEl porcentaje entre %.2f y %.2f es: %%%.2f\n", numero1, numero2, porcentaje);
   
   return 0;
}
