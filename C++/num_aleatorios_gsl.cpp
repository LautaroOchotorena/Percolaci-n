#include <iostream>
#include <fstream>
#include <gsl/gsl_rng.h> 		//para compilar usar -lgsl -lgslcblas
#include <gsl/gsl_randist.h>
using namespace std;

int main(int argc,char **argv){
ofstream Outfile;
Outfile.open("num_aleatorios_gsl.txt");		//Escribiré en este archivo
int contador=0;			//Contador de cuántos números aleatorios voy
const gsl_rng_type * T;
gsl_rng * r;
gsl_rng_env_setup();
for (int x=1; x<=215; x++){
	gsl_rng_default_seed = 3*x;		//Cambio la semilla cada 215 números
	T = gsl_rng_default;
	r = gsl_rng_alloc (T);
	for (int y=1; y<=215; y++){ //Uso 215 básicamente porque en mi algoritmo principal (el del computo)
								//cambia la semilla cada 215 en el peor de los casos (en realidad depende del
								//número de filas del cuadrado, pero el cuadrado más grande que tomo es de 215x215)
		contador++;
		Outfile << contador << " " << (double) gsl_rng_uniform(r) << "\n";		//Escribo en el archivo la cantidad de
																				//número aleatorios que voy  y el número aleatorio
	}
}
gsl_rng_free (r);
Outfile.close();
}
