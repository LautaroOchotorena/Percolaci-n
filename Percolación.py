#! /usr/bin/env python3
#Requiere la instalación de pygame!!
import pygame
import numpy as np
import random
import time
import sys #Para acceder a los argumentos del script
p=float(sys.argv[1])		#Seteamos el número de probabilidad

pygame.init()

width, height = 900, 900		#Ancho y alto de la pantalla
screen=pygame.display.set_mode((height,width))		#Creación de la pantalla
bg= 25, 25, 25			#Seleccionamos el color que vamos a elegir ((25,25,25) es un negro)

pauseExect = False
screen.fill(bg)			#Pintamos el fondo del color elegido

#Número de celdas que uno quiere formar (en el eje x como en el eje y)
nxC, nyC = 20,20

#Dimensión de las celdas
dimCw= width/nxC
dimCh= height/nyC

#Estado de las celdas, 0 indica que no está activa y 1 que lo está. Al principio pongo todo en 0
gameState = np.zeros((nxC+1,nyC+1))


running=True
#Bucle de ejecución
while running:
	label = np.zeros((nxC,nyC))
	largest_label = 0
	screen.fill(bg)		#Esto sirve para que borre lo que sucedió en el paso anterior (así no se solapan iteraciones)
	for event in pygame.event.get():
	#El siguiente comando es para salir del loop
		if event.type == pygame.QUIT:	#Si uno apreta la "x" de la interfaz saldrá del juego
			running = False
		#Lo siguiente cambia el estado de pauseExect al pulsar una tecla, es para poder parar y reanudar el juego
		if event.type == pygame.KEYDOWN:
			pauseExect = not pauseExect
	for y in range(0,nyC):
		for x in range (0,nxC):
			#Lo siguiente funciona de tal modo que si se pulsa una tecla el pauseExect cambia a True y no entra en este if
			#por lo que el sistema sigue dibujando el gameState anterior, dando ilusión a que se paró
			#Para reanudar el juego pulsar de nuevo una tecla
			if pauseExect==False:
				n = random.random()		#Doy un número aleatorio entre 0 y 1
				if(n<=p):					#Si el número aleatorio salió menor a mi probabilidad de ocupación
					gameState[x,y]=1		#Seteo la celda como ocupada
				else:
					gameState[x,y]=0 				#Caso contrario seteo la celda como desocupada
			if gameState[x,y]==1:				#Si la celda está ocupada
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
	for y in range(0,nyC):
		for x in range (0,nxC):
			#Esto es el polígono de cada celda
			poly =  [((x)*dimCw, y*dimCh),
					((x+1)*dimCw, y*dimCh),
					((x+1)*dimCw, (y+1)*dimCh),
					((x)*dimCw, (y+1)*dimCh)]
			if gameState[x,y]==1:
				#si el gameState es 1 me rellena la celda con un color de cluster (escrito en forma RGB). 
				#La idea de poner (249*label[x,y] % 250, 100*label[x,y] % 250, 9*label[x,y] % 150+100) es para que cada cluster tenga un color diferente
				#Notar que RGB cada variable va de 0 a 250 por eso meto módulo 250 para que de un número entre 0 y 249
				pygame.draw.polygon(screen, (249*label[x,y] % 250, 100*label[x,y] % 250, 9*label[x,y] % 150+100) , poly, 0)
			#Caso contrario me contornea la celda con un color grisaseo con un grosor de 1 (osea poco)
			#para dar ilusión de separación de celdas
			else:
				pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
	pygame.display.flip()
	time.sleep(0.3)		#Le pongo un sleep para que no vaya tan rápido y pueda verse el cambio de iteraciones
#Finalmente cerramos la ventana
pygame.display.quit()
pygame.quit()
exit()