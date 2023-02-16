#include <iostream>
#include <fstream>
using namespace std;

int main(int argc,char **argv){
ofstream Outfile;
Outfile.open("num_aleatorios_rand.txt");	//Escribiré en este archivo
int contador=0;			//Contador de cuántos números aleatorios voy
int semilla;
for (int x=1; x<=215; x++){
	semilla=2*x; //Esto lo hago para que la semilla siempre de diferente, cambia cada 215 números aleatorios
	srand(semilla);
	for (int y=1; y<=215; y++){ //Uso 215 básicamente porque en mi algoritmo principal (el del computo)
								//cambia la semilla cada 215 en el peor de los casos (en realidad depende del
								// número de filas del cuadrado, pero el cuadrado más grande que tomo es de 215x215)
		contador++;
		Outfile << contador << " " << (double)rand()/(RAND_MAX+1.0) << "\n";	//Escribo en el archivo la cantidad de
																				//número aleatorios que voy  y el número aleatorio
	}
}
Outfile.close();
}
