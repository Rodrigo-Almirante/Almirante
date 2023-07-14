#include <iostream>
#include <cmath>

using namespace std;

// Funcion para convertir un digito hexadecimal a decimal
int hexToDec(char hexDigit) {
    if (hexDigit >= '0' && hexDigit <= '9') {
        return hexDigit - '0';
    }
    else if (hexDigit >= 'A' && hexDigit <= 'F') {
        return hexDigit - 'A' + 10;
    }
    else if (hexDigit >= 'a' && hexDigit <= 'f') {
        return hexDigit - 'a' + 10;
    }
    else {
        return -1; // Valor inválido
    }
}

// Funcion para convertir un numero hexadecimal a decimal
int hexToDecimal(string hexNumber) {
    int decNumber = 0;
    int power = 0;
    
    // Convertir cada digito hexadecimal y sumar al numero decimal
    for (int i = hexNumber.length() - 1; i >= 0; i--) {
        int decDigit = hexToDec(hexNumber[i]);
        if (decDigit == -1) {
            cout << "Numero hexadecimal inválido" << endl;
            return -1;
        }
        decNumber += decDigit * pow(16, power);
        power++;
    }
    
    return decNumber;
}

// Funcion para convertir un numero hexadecimal a octal
string hexToOctal(string hexNumber) {
    int decNumber = hexToDecimal(hexNumber);
    if (decNumber == -1) {
        return ""; // Convertir a octal no válido
    }
    
    string octalNumber = "";
    
    // Convertir numero decimal a octal
    while (decNumber != 0) {
        int octDigit = decNumber % 8;
        octalNumber = to_string(octDigit) + octalNumber;
        decNumber /= 8;
    }
    
    return octalNumber;
}

// Funcion para convertir un numero hexadecimal a binario
string hexToBinary(string hexNumber) {
    int decNumber = hexToDecimal(hexNumber);
    if (decNumber == -1) {
        return ""; // Convertir a binario no válido
    }
    
    string binaryNumber = "";
    
    // Convertir numero decimal a binario
    while (decNumber != 0) {
        int binDigit = decNumber % 2;
        binaryNumber = to_string(binDigit) + binaryNumber;
        decNumber /= 2;
    }
    
    return binaryNumber;
}

int main() {
    string hexNumber;
    
    // Validar que el numero hexadecimal sea válido
    bool validHex = false;
    while (!validHex) {
        cout << "Ingrese un numero hexadecimal: ";
        cin >> hexNumber;
        
        // Validar que cada digito sea hexadecimal
        validHex = true;
        for (char digit : hexNumber) {
            if (!(digit >= '0' && digit <= '9') && !(digit >= 'A' && digit <= 'F') && !(digit >= 'a' && digit <= 'f')) {
                validHex = false;
                break;
            }
        }
        
        if (!validHex) {
            cout << "Numero hexadecimal inválido. Intente nuevamente." << endl;
        }
    }
    
    // Convertir a decimal
    int decNumber = hexToDecimal(hexNumber);
    if (decNumber == -1) {
        return 0;
    }
    else {
        cout << "\nEl numero hexadecimal " << hexNumber << " en decimal es: " << decNumber << endl;
    }
    
    // Convertir a octal
    string octalNumber = hexToOctal(hexNumber);
    if (octalNumber == "") {
        return 0;
    }
    else {
        cout << "\nEl numero hexadecimal " << hexNumber << " en octal es: " << octalNumber << endl;
    }
    
    // Convertir a binario
    string binaryNumber = hexToBinary(hexNumber);
    if (binaryNumber == "") {
        return 0;
    }
    else {
        cout << "\nEl numero hexadecimal " << hexNumber << " en binario es: " << binaryNumber << endl;
    }
 
    // Esperar a que se toque una tecla para continuar
    cout << "\nPresione enter para continuar...";
    cin.ignore();
    cin.get();

 
    return 0;
}