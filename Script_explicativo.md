Bueno, la función de este script es guiar a quien lo lea para que pueda entender qué es cada cosa.<br>
Recomiendo ver esta explicación junto al pdf de la presentación.

Primero algunas observaciones:<br>
1) n es mi número de filas del cuadrado<br>
2) La probabilidad de ocupación la defino como la probabilidad en que una celda esté ocupada o no<br>
3) La probabilidad de percolación (depende de mi prob de ocupación y del n) la defino como la probabilidad en que exista un cluster que conecte la parte de arriba con la de abajo en un cuadrado de nxn.<br>
4) Los scripts que hice funcionan pero se pueden optimizar más para que tarde menos, optimizarlo iba a generar bastante confusión a la hora de leerlo, no consideré que fuera necesario.<br>

Recomiendo ver primero el script "Computo.py" de la carpeta "Python" y luego fijarse en los otros scripts pero en todos traté de detallar lo más posible para que se entienda.


En este mismo directorio: 

Se encuentra un archivo llamado "Percolación.py", se lo invoca con un parámetro que será la probabilidad de ocupación (entre 0 y 1). Una vez invocado el script despliega una interfaz gráfica en la que se puede ver
cómo funciona la percolación para esa probabilidad de ocupación, cada 0.3 segundos cambia para que se pueda ver varias iteraciones. Los cuadrantes de un mismo color (que no sea negro) representan los cluster o bloques conectados, los cuadrantes en negro son celdas no activas. Uno puede parar y reanudar este script pulsando cualquier tecla del teclado. Se cierra pulsando la x en la interfaz gráfica.


En la carpeta "Python":

Se encuentra un archivo llamado "Computo.py", fue el archivo principal en el que escribí lo necesario para obtener los datos para después analizar, no resultó efeciente usar python por lo que decidí cambiarme a C++, pero básicamente es el mismo script adaptado.<br>
La idea del script "Computo.py" es hacer archivos "Computo_n_python.dat" en el que n será el número de filas del cuadrado, y en este archivo de texto en la primera columna se ve la probabilidad de ocupación mientras que en la segunda columna la probabilidad de percolación.<br>
Además ese script genera un archivo "extrapolación_python" en el que en la primera columna indica el N y la segunda la probabilidad de ocupación tal que sea la primera probabilidad de ocupación en tener una probabilidad de percolación de 0.5 o más.


En la carpeta "C++":

	En el directorio:

	Se encuentran los scripts que usé para testear la distribución uniforme de los números aleatorios.<br>
	Por una parte usando rand de C++ se encuentra el archivo "num_aleatorios_rand.cpp" y por otra parte está
	la que corresponde a la librería GSL "num_aleatorios_gsl.cpp". En ambos scripts lo que hago es escribir en un archivo de texto cuántos números aleatorios voy seguido del número aleatorio. Esto sirve para luego graficar.


	En la carpeta "Probabilidad entre 0-1":

	Se encuentra el script "Computo.cpp" que hace archivos "Computo_n", donde n es el número de filas y en este archivo de texto se vuelcan los datos de la probabilidad de percolación (segunda columna) en base a la probabilidad de ocupación (primera columna, esta varía entre 0 y 1). El número de iteraciones que se toma es de 100 y la cantidad de puntos obtenidos son 50 para cada "Computo_n".<br>
	Además ese script genera un archivo "Extrapolación" en el que en la primera columna indica el n y la segunda la probabilidad de ocupación tal que sea la primera probabilidad de ocupación en tener una probabilidad de percolación de 0.5 o más. Esta "Extrapolación" no la usaré hasta más adelante porque no tiene mucho sentido graficarla ahora.<br>
	También se encuentra un archivo "Ploteo.cpp" que básicamente es para plotear todos los gráficos (o los que uno desee) juntos en grace, para ahorrar tiempo nada más.


	En la carpeta "Probabilidad entre 0.4-0.6":

	Es el mismo script que el de "Probabilidad entre 0-1", sólo que la probabilidad de ocupación varía entre 0.4 y 0.6.<br>
	También se encuentra un archivo "Ploteo.cpp" que básicamente es para plotear todos los gráficos (o los que uno desee) juntos en grace, para ahorrar tiempo nada más.


	En la carpeta "Probabilidad entre 0.58-0.596":

	Es el mismo script que el de "Probabilidad entre 0-1", sólo que la probabilidad de ocupación varía entre 0.58 y 0.596, además de que para cada "Computo_n" ahora obtengo 51 puntos (me di cuenta tarde de que puse 51 y no 50, mala mia). En este caso sí uso el archivo de texto "Extrapolación" porque ya considero que puedo estimar un valor de la probabilidad crítica.<br>
	También se encuentra un archivo "Ploteo.cpp" que básicamente es para plotear todos los gráficos (o los que uno desee) juntos en grace, para ahorrar tiempo nada más.


	En la carpeta "Promedio tamaño cluster":

	Se encuentra el script "Computo.cpp" que genera un archivo "Computo_n200" (cuadrado 200x200) en el que en la primera columna marca la probabilidad de ocupación (que varía entre 0 y 1) y la segunda columna el promedio del tamaño del cluster esperado cuando se elige una celda ocupada al azar. En el script "Computo.cpp" se toman 4000 iteraciones y se recolecta 50 puntos.


	En la carpeta "Número de Clusters totales":

	Se encuentra un script "Computo.cpp" que genera archivos de texto "Computo_n", donde n es la cantidad de filas (en este caso n va de 5 en 5, empezando en 175 y terminando en 200), en el que la primera columna marca la probabilidad de ocupación (variando entre 0 y 1) y la segunda columna el promedio de número de clusters en base a esa probabilidad de ocupación. En el script "Computo.cpp" se toman 100 iteraciones y se recolectan 50 puntos para cada "Computo_n".<br>
	También se encuentra un archivo "Ploteo.cpp" que básicamente es para plotear todos los gráficos (o los que uno desee) juntos en grace, para ahorrar tiempo nada más.


	En la carpeta "P_infinito":

	Se encuentra el script "Computo.cpp" que genera un archivo de texto "Computo_n100" (cuadrado 100x100) en el que la primera columna es la probabilidad de ocupación (variando entre 0 y 1) y la segunda columna la probabilidad de que una celda ocupada elegida al azar pertenezca al cluster percolador.<br>
	Para "Computo_n100" se toman 4000 iteraciones y se recolectan 500 puntos.
