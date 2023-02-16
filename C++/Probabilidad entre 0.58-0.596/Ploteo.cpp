#include <iostream>
#include <fstream>		//Para crear y escribir archivos
#include <cmath>
#include <string>		//Para manejar strings
#include <sstream>		//Para solucionar un problema particular

using namespace std;

//Lo que hace este script es plotear los datos de los archivos "Computo_n", 
//uno puede variar el l para decidir cuáles quiere
int main(int argc,char **argv){
		string str;
		string str_2;
		str_2 = "xmgrace";
		for (int l=20;l<=43;l++){
		str = " -block Computo_n";
		stringstream ss;
		ss << 5*l;
		str += ss.str() + " -bxy 1:2";
		str_2 += str;
	}
	const char *command = str_2.c_str();  //Necesario este paso porque sino no capta el system
	system(command);
}