#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>

int main()
{
 WSADATA wsaData;
 if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) 
 {
  printf("Error al inicializar Winsock\n");
  return 1;
 }

char hostname[256];
if (gethostname(hostname, sizeof(hostname)) == SOCKET_ERROR) 
 {
  printf("Error al obtener el nombre del host\n");
  WSACleanup();
  return 1;
 }

printf("\nNombre de esta computadora en la red local: %s\n",hostname);

struct hostent* host;
host = gethostbyname(hostname);
if (host == NULL) 
 {
  printf("Error al obtener la información del host\n");
  WSACleanup();
  return 1;
 }


char* ip = inet_ntoa(*(struct in_addr*)host->h_addr);

printf("Direccion IP local: %s\n", ip);

WSACleanup();
return 0;
}
