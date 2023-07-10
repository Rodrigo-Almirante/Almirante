#include <stdio.h>

void hanoi(int n, char origen, char destino, char auxiliar){
    if(n==1){
        printf("Mover disco 1 de la varilla %c a la varilla %c\n", origen, destino);
        return;
    }
    hanoi(n-1, origen, auxiliar, destino);
    printf("Mover disco %d de la varilla %c a la varilla %c\n", n, origen, destino);
    hanoi(n-1, auxiliar, destino, origen);
}

int main(){
    int n;
    printf("Ingrese el numero de discos: ");
    scanf("%d", &n);
    hanoi(n, 'A', 'C', 'B'); // Las varillas se llamaran A, B y C respectivamente.
    return 0;
}
