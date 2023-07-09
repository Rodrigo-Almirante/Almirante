#include <stdio.h>

void decimalToHexadecimal(int numero) {
    char hexadecimal[100];
    int i = 0;
    
    while (numero != 0) {
        int resto = numero % 16;
        
        if (resto < 10) {
            hexadecimal[i] = resto + '0';
        } else {
            hexadecimal[i] = resto + 'A' - 10;
        }
        
        numero = numero / 16;
        i++;
    }
    
    printf("El numero en hexadecimal es: ");
    
    for (int j = i - 1; j >= 0; j--) {
        printf("%c", hexadecimal[j]);
    }
    
    printf("\n");
}

void decimalToOctal(int numero) {
    int octal = 0, i = 1;
    
    while (numero != 0) {
        octal = octal + (numero % 8) * i;
        numero = numero / 8;
        i = i * 10;
    }
    
    printf("El numero en octal es: %d\n", octal);
}

void decimalToBinario(int numero) {
    int binario[100], i = 0;
    
    while (numero != 0) {
        binario[i] = numero % 2;
        numero = numero / 2;
        i++;
    }
    
    printf("El numero en binario es: ");
    
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binario[j]);
    }
    
    printf("\n");
}

int main() {
    int numero;
    
    printf("Ingrese un numero decimal: ");
    scanf("%d", &numero);
    
    decimalToHexadecimal(numero);
    decimalToOctal(numero);
    decimalToBinario(numero);
    
    return 0;
}
