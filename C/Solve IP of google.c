#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>

int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("Error al inicializar Winsock\n");
        return 1;
    }

    struct addrinfo hints;
    struct addrinfo* res;
    struct sockaddr_in* addr;
    char ipstr[INET_ADDRSTRLEN];

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;

    if (getaddrinfo("www.google.com", "http", &hints, &res) != 0) {
        printf("Error al obtener dirección IP\n");
        WSACleanup();
        return 1;
    }

    addr = (struct sockaddr_in*) res->ai_addr;
    inet_ntop(AF_INET, &(addr->sin_addr), ipstr, sizeof(ipstr));

    printf("Direccion IP de google.com: %s\n", ipstr);
    
    freeaddrinfo(res);
    WSACleanup();
    
    return 0;
}
