#include <iostream>
#include <fstream>		//Para crear y escribir archivos
#include <cmath>
#include <string>		//Para manejar strings
#include <sstream>		//Para solucionar un problema particular
#include <ctime> 		//Para calcular el tiempo que tarda el script en completarse
using namespace std;

int main(int argc,char **argv){
	unsigned t0, t1; //t0 es el tiempo de inicio, t1 será el tiempo final
	t0=clock(); 		//Para calcular el tiempo de inicio del script
	ofstream Outfile;
	for (int l=20;l<=20;l++){	//este l varía el número de filas y columnas
		//Lo siguiente es mero código para poder dar diferentes nombres al archivo de texto
		string str;
		str = "Computo_n";
		stringstream ss;
		ss << 5*l;
		str += ss.str();
		Outfile.open(str);

		int num=4000; //número de iteraciones

		//Número de celdas que uno quiere formar (en el eje x como en el eje y)
		int nxC=5*l;
		int nyC=5*l;

		//Estado de las celdas, 0 indica que no está activa (o desocupada) y 1 que lo está (ocupada)
		int gameState[nxC+1][nyC+1];

		//Seteo la primera fila y la primera columna como que las celdas no están activas. 
		//Esto lo hago para, por ejemplo, en
		//la primera fila (pero esta vez del sistema de percolación)
		//pueda analizar las celdas de arriba que son inexsistentes en el sistema y tomarlas como desocupadas.
		for (int k=0;k<=nxC;k++){
			gameState[k][0]=0;
			gameState[0][k]=0;
		}

		//label indicará las etiquetas de los clusters
		int label[nxC+1][nyC+1];

		int semilla;		//semilla del rand que irá variando
		int gate_2=1;		//Es una gate que usaré después
		int np=500;			//número de probabilidades a testear

		for (int t=1;t<=np; ++t){		//Este t hace variar la probabilidad de ocupación
			double p=(double)t/np;		//Probabilidad de ocupación
			int contador=0;				//Contador que se usará luego
			for (int h=1; h<=num; ++h){		//Este h hace que el sistema se repita num-veces
				int largest_label=0;		//Seteo la etiqueta más alta como 0
				int x_1=0;					//x_1, y_1 los explico más adelante
				int y_1=0;
				for (int y=1; y<=nyC; y++){			//Este y hace varias las filas del sistema
					semilla=(num+np+1)*y+h+t; 			//Esto lo hago para que la semilla siempre de diferente (por eso la forma que tiene)
					srand(semilla);						//Generador
					for (int x=1; x<=nxC; x++){				//x hace varias las columnas
						double n=(double)rand()/(RAND_MAX+1.0);		//Doy un número aleatorio entre 0 y 1
						if(n<=p){								//Si el número aleatorio es menor a la probabilidad de ocupación
							gameState[x][y]=1;					//Seteo la celda como activa (ocupada)
							int izquierda = gameState[(x-1)][y];		//Me fijo si la celda izquierda está activa o no
							int arriba = gameState[x][(y-1)];			//Me fijo si la celda de arriba está activa o no
							if ((izquierda==0) && (arriba==0)){     //Si ninguna de las dos celdas están activas
								largest_label++;      //Aumento el valor de la etiqueta más larga
								label[x][y]=largest_label;		//Y seteo la etiqueta de la celda como esa etiqueta larga (en su valor actual)
							}
							else if ((izquierda==1) && (arriba==0)){  //Si tiene activo el vecino izquierdo e inactivo el de arriba
									label[x][y] = label[(x-1)][y];			//Le pongo la etiqueta que tiene la celda de la izquierda
								}
							else if ((izquierda==0) && (arriba==1)){   //Si tiene inactivo el vecino izquierdo y activo el de arriba
									label[x][y] = label[x][(y-1)];		//Le pongo la etiqueta que tiene la celda de arriba
								}

							else{				//Si ambos vecinos están ocupados
								label[x][y] = label[x][(y-1)];	//Le pongo la etiqueta de la celda de arriba
								if (label[x][y-1]!=label[x-1][y]){ 		//En el caso de que la etiqueta izquierda y la de arriba sean diferentes
																		//entonces cambio todas las etiquetas del valor de la etiqueta de la izquierda y la
																		//cambio por el valor de la etiqueta de arriba
																		//De esta forma me garantizo que las celdas están en el mismo cluster
									for (int z=1; z<=y; z++){
										for (int j=1; j<=nxC; j++){
											if (label[j][z] == label[(x-1)][y]){
												label[j][z] = label[x][(y-1)];
											}
										}
									}
								}
							}
						}
						else{
							gameState[x][y]=0;		//En caso de que el número aleatorio haya sido mayor al de la probabilidad de
							label[x][y]=0;					//ocupación, seteo la celda como que no está ocupada y la etiqueta le pongo 0.
						}
					}
				}

				//El ciclo while que voy a hacer ahora es para elegir una celda aleatoria y fijarme si está ocupada,
				//si lo está entonces rompo el ciclo

				int gate_2=1;
				while (gate_2==1){		//Este while puede llegar a no salirse del loop, pero es poco probable
					x_1=rand()%nxC+1;		//Seteo x_1 como un número aleatorio entre 1 y nxC
					y_1=rand()%nyC+1;		//Seteo y_1 como un número aleatorio entre 1 y nyC
						if (gameState[x_1][y_1]==1){		//Si la celda está ocupada
							gate_2=0;		//Seteo la gate para que salga del loop del while
						}
				}
				int gate=1;		//Gate que ahora la explico


				//Lo siguiente analiza si hay o no percolación, si la hay entonces me fijo si la casilla al azar que elegí pertenece
				//al cluster percolador.
				//La idea es la siguiente: analizar la etiqueta de cada celda de la primera fila del cuadrado y ver si
				//tiene la misma etiqueta con alguna celda de la última fila y si coincide además con
				//la etiqueta de la celda al azar


				for (int y=1; y<=nyC; y++){
					for (int x=1; x<=nxC; x++){
						if (gate==1){
							if ((label[y][1]!=0) && (label[y][1]==label[x_1][y_1]) && (label[y][1]==label[x][nyC])){
								gate = 0;		//La primera vez que se cumplan estas condiciones setea la gate en 0,
												//no me interesa revisar más
								contador++;		//Aumenta en uno el contador, que nos dice el número de veces 
												//que la casilla al azar pertenece al cluster percolador.
								break;			//Hace salir del ciclo "for x"
							}
						}
					}
					if (gate==0){		//Si la gate está en 0 entonces salgo del ciclo "for y"
						break;
					}
				}
			}
			Outfile << p << " " << (double)contador/num << endl;		//Escribo en el archivo la probabilidad de ocupación seguido de la
																		//probabilidad de que una celda ocupada elegida al azar pertenezca al cluster percolador
		}
		//Cierro el archivo Outfile
		Outfile.close();
	}
	t1 = clock();		//Tiempo final del script
	double time = (double(t1-t0)/CLOCKS_PER_SEC);
	cout << "Execution Time: " << time << endl;		//Printeo el tiempo de execución
	return 0;
}