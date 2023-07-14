#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int esHexadecimal(char c) {
    return ((c >= '0' && c <= '9') || (toupper(c) >= 'A' && toupper(c) <= 'F'));
}

int main() {
    char numero_hex[100];
    int decimal, octal, i, longitud;

    while(1) {
        printf("Ingrese un numero hexadecimal: ");
        scanf("%s", numero_hex);
        
        // Validar si el número ingresado es hexadecimal
        longitud = strlen(numero_hex);
        int valido = 1;
        for(i = 0; i < longitud; i++) {
            if(!esHexadecimal(numero_hex[i])) {
                valido = 0;
                break;
            }
        }
        
        if (valido) {
            break;
        } else {
            printf("Numero invalido. Ingrese un numero hexadecimal.\n");
        }
    }

    // Convertir de hexadecimal a decimal
    decimal = 0;
    for(i = 0; i < longitud; i++) {
        decimal = decimal * 16;
        if(isdigit(numero_hex[i])) {
            decimal += numero_hex[i] - '0';
        } else {
            decimal += toupper(numero_hex[i]) - 'A' + 10;
        }
    }

    // Convertir de decimal a octal

    octal = 0;
    i = 1;
    int original_decimal = decimal;
    while(decimal != 0) {
        octal += (decimal % 8) * i;
        decimal /= 8;
        i *= 8;
    }

    // Convertir de decimal a binario

    int resto, binario[100], indice = 0;
    decimal = original_decimal;
    while(decimal != 0) {
        resto = decimal % 2;
        binario[indice++] = resto;
        decimal /= 2;
    }

    // Imprimir resultados
    printf("\nNumero decimal equivalente: %d\n", original_decimal);
    printf("\nNumero octal equivalente: %o\n", octal);
    printf("\nNumero binario equivalente: ");
    for(i = indice - 1; i >= 0; i--) {
        printf("%d", binario[i]);
    }
    printf("\n");

   printf("\n         Presione cualquier tecla para continuar\n");  
   getch();

   return 0;
}
