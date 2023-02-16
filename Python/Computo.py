#! /usr/bin/env python3
import numpy as np 		#Para escribir matrices
import random 			#Para los números aleatorios
import time 			#Para calcular el tiempo de ejecución
g = open('extrapolación_python','w') #Genero un archivo de texto en el que ponga en la primera columna el número
									 #de filas del cuadrado y la segunda columna la probabilidad de ocupación 
									 #más baja tal que logre una
									 #probabilidad de percolación de más de 0.5

inicio = time.time() #Para calcular el tiempo de inicio del script
num=100 #número de iteraciones

#Bucle de ejecución
for r in range(1,8): #Este r va variando la cantidad de filas y columnas, 5*r
	nxC, nyC = 5*r,5*r 	#Es el número de filas y columnas de mi cuadrado
	f = open('Computo_n%d_python.dat' % (5*r),'w') #En estos archivos de texto volcaré la probabilidad de ocupación 
												   #seguido de la probabilidad de percolación (acá ya tenemos fijo 
												   #el número de columnas y filas) 
	f.write('#probabilidad_de_ocupación probabilidad_de_percolación\n')
	gameState = np.zeros((nxC+1,nyC+1)) #Es una matriz de ceros en el que indicará el estado de las celdas,
										# 0 indica que no está ocupada y 1 que lo está.
	Var_2=True #Esta es una gate para su uso posterior
	for t in range(1,50+1): #Esta t hace variar la probabilidad de ocupación
		p=t/50				#como se ve acá
		numPer=0			#Una vez seteado la probabilidad de ocupación contaré el número de veces 
							#que el programa percola


		#Lo siguiente serán las reglas del programa para dada una probabilidad de ocupación


		for h in range(0,num):  #Este h hace repetir el programa num-veces para que uno tenga más muestreos
								#de una misma probabilidad de ocupación
			label = np.zeros((nxC,nyC))  #Seteo la matriz label (etiqueta) la cual es usada por el algoritmo que empleamos
			largest_label = 0 					#Seteo la etiqueta más alta como 0
			for y in range(0,nyC):					#Ahora bien, comienzo analizando la fila "y"
				for x in range (0,nxC):		#Comienzo con la columna "x"
					n = random.random()				#Doy un número aleatorio entre 0 y 1
					if(n<=p):				#Si el número aleatorio salió menor a mi probabilidad de ocupación
						gameState[x,y]=1 	#cambio la componente (x,y) de la matriz para que esté ocupada esa celda
						izquierda = gameState[(x-1),y]  #Seteo izquierda como el estado de la celda izquierda a la actual
						arriba = gameState[x,(y-1)]			#Seteo arriba como el estado de la celda izquierda a la actual
						if (izquierda == 0) and (arriba == 0):     #Si las celdas izquierda y arriba no están ocupadas
							largest_label = largest_label + 1      #Aumento en uno la etiqueta más alta
							label[x,y] = largest_label			   #Seteo la etiqueta como el número actual de la etiqueta más alta

						elif (izquierda == 1) and (arriba == 0):   #Si la celda izquierda está ocupada y la de arriba no
							label[x,y] = label[(x-1),y]			   #seteo la etiqueta como la etiqueta de la celda izquierda

						elif (izquierda == 0) and (arriba == 1):   #Si la celda arriba está ocupada y la izquierda no
							label[x,y] = label[x,(y-1)]			   #seteo la etiqueta como la etiqueta de la celda de arriba

						else:							#Si la celda de arriba y la izquierda están ambas ocupadas
							label[x,y]=label[x,(y-1)]	#seteo la etiqueta como la etiqueta de arriba y lo que hago luego
														#es cambiar todas las etiquetas del valor
														#de la etiqueta izquierda, las cambio al valor de la etiqueta de arriba,
														#así me quedan que las celdas pertenecen al mismo cluster
							if (label[x,(y-1)]!=label[x-1][y]):
								for z in range(0,nyC):
									for j in range(0,nxC):
										if label[j,z]==label[(x-1),y]:
											label[j,z] = label[x,(y-1)]
					else:
						gameState[x,y]=0 			#En caso de que el número aleatorio haya sido mayor al de la probabilidad de
													#ocupación, seteo la celda como que no está ocupada
			Var=True			#Es una gate, luego la explico


			#Lo siguiente analiza si hay o no percolación y cuenta cuántas hay (una sola vez por iteración).
			#La idea es la siguiente: analizar la etiqueta de cada celda de la primera fila del cuadrado y ver si
			#tiene la misma etiqueta con alguna celda de la última fila. Esto indica que hay percolación


			for y in range (0,nxC):
				for x in range (0,nxC):
					if Var==True: 		#Si esta gate está en true analizo lo siguiente
						if (label[y,0]!=0) and (label[y,0]==label[x,nyC-1]):
							numPer= numPer + 1 			#Aumento en uno el número de percolación
							Var=False  			#Una vez visto que percoló setearlo en falso para que no vuelva a contar que percoló
							break		 #Esto hace salir del "for x in range (0,nxC)"
				if Var==False:
					break #Esto hace salir del "for y in range (0,nxC)"
		f.write('%f %f\n' % (p,numPer/num))  #Escribo el número de ocupación seguido de la probabilidad de percolación (numPer/num)

		#Lo que sigue es para poder hacer la extrapolación. Anota en el archivo (de extrapolación) el primer punto en el que
		#la probabilidad de percolación es mayor o igual a 0.5


		if (Var_2==True):		#Esto funciona parecido al Var
			if (numPer/num>=0.5): 			#Veo si la probabilidad de percolación es más grande que 0.5
				Var_2=False 		#Setearlo en falso permitirá que no se contabilice más que la primera vez que se cumpla esto
				g.write('%d %f\n' % (nxC,p))		#Escribo en el archivo (que se usará para extrapolar) el número
													#de filas del cuadrado y la probabilidad de ocupación tal que la
													#probabilidad de percolación supera 0.5

#Finalmente cerramos los archivos
	f.close()
g.close()

fin = time.time() 		#Tiempo final del script
print(fin-inicio) 		#Printeo el tiempo de execución