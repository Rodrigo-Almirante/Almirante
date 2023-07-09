#include <iostream>
#include <string>

std::string decimalToHexadecimal(int numero) {
    std::string hexadecimal;
    
    while (numero != 0) {
        int resto = numero % 16;
        
        if (resto < 10) {
            hexadecimal.insert(0, std::to_string(resto));
        } else {
            char digito = 'A' + resto - 10;
            hexadecimal.insert(0, 1, digito);
        }
        
        numero = numero / 16;
    }
    
    return hexadecimal;
}

std::string decimalToOctal(int numero) {
    std::string octal;
    
    while (numero != 0) {
        int resto = numero % 8;
        octal.insert(0, std::to_string(resto));
        numero = numero / 8;
    }
    
    return octal;
}

std::string decimalToBinary(int numero) {
    std::string binario;
    
    while (numero != 0) {
        int resto = numero % 2;
        binario.insert(0, std::to_string(resto));
        numero = numero / 2;
    }
    
    return binario;
}

int main() {
    int numero;
    
    std::cout << "Ingrese un número decimal: ";
    std::cin >> numero;
    
    std::string hexadecimal = decimalToHexadecimal(numero);
    std::string octal = decimalToOctal(numero);
    std::string binario = decimalToBinary(numero);
    
    std::cout << "El número en hexadecimal es: " << hexadecimal << std::endl;
    std::cout << "El número en octal es: " << octal << std::endl;
    std::cout << "El número en binario es: " << binario << std::endl;
    
    return 0;
}
