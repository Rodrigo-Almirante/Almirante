#include <iostream>
using namespace std;

void mover_disco(int num_disco, char torre_or, char torre_des, char torre_aux) {
// Si solo hay un disco, se mueve directamente a la torre de destino
if(num_disco == 1) {
    cout << "Mover disco 1 de torre " << torre_or << " a torre " << torre_des << endl;
    return;
}

// Mover n-1 discos a la torre auxiliar
mover_disco(num_disco - 1, torre_or, torre_aux, torre_des);

// Mover el disco restante a la torre de destino
cout << "Mover disco " << num_disco << " de torre " << torre_or << " a torre " << torre_des << endl;

// Mover los discos de la torre auxiliar a la torre de destino
mover_disco(num_disco - 1, torre_aux, torre_des, torre_or);
}

int main() {
int num_discos;

cout << "Ingrese el numero de discos: ";
cin >> num_discos;

// Mover los discos de la torre A a la torre C utilizando la torre B como auxiliar
mover_disco(num_discos, 'A', 'C', 'B');

return 0;
}
