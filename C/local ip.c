#include <windows.h>
#include <stdio.h>
#include <wininet.h>

#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "user32.lib")


int main() {
    DWORD bufferSize = 256;
    char buffer[256];
	
	BOOL isConnected;
	

    // Obtener el estado de la conexión
    isConnected = InternetGetConnectedState(&bufferSize, *buffer);

    if (isConnected) {
        printf("Connected\n");
        printf("Local IP: %s\n", buffer);
    }
    else {
        printf("Not connected\n");
    }

    return 0;
}
