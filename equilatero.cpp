#include <iostream>
#include <cmath>
#include <vector>
#include <graphics.h> // Asegúrate de que esta biblioteca esté disponible

using namespace std;

struct Point {
    int x, y;
};

// DDA Algorithm for drawing lines
void DDA(int x1, int y1, int x2, int y2) {
    int dx = abs(x2 - x1), dy = abs(y2 - y1);
    int steps = (dx > dy) ? dx : dy;
    float xIncrement = (float)(x2 - x1) / steps;
    float yIncrement = (float)(y2 - y1) / steps;

    float x = x1, y = y1;

    for (int k = 0; k <= steps; k++) {
        putpixel(round(x), round(y), WHITE); // Dibuja el pixel
        x += xIncrement;
        y += yIncrement;
    }
}

int main() {
    // Inicializa la ventana gráfica
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    Point P0, P1, P2;

    // Definir puntos
    cout << "Ingrese las coordenadas del primer punto (x, y): ";
    cin >> P0.x >> P0.y;
    cout << "Ingrese las coordenadas del segundo punto (x, y): ";
    cin >> P1.x >> P1.y;

    // Calcular el tercer punto para un triángulo equilátero
    float se = M_PI / 3; // 60 grados en radianes
    P2.x = P0.x + (P1.x - P0.x) * cos(se) - (P1.y - P0.y) * sin(se);
    P2.y = P0.y + (P1.x - P0.x) * sin(se) + (P1.y - P0.y) * cos(se);

    // Dibujar el triángulo
    DDA(P0.x, P0.y, P1.x, P1.y);
    DDA(P1.x, P1.y, P2.x, P2.y);
    DDA(P0.x, P0.y, P2.x, P2.y);

    getch(); // Espera a que se presione una tecla
    closegraph(); // Cierra la ventana gráfica
    return 0;
}