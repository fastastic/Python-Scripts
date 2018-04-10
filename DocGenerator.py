# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys
import subprocess
import io

#################################################################
# DocGenerator.py v1.0						#
# 								#
# Genera un README.md del script pasado por parámetros.	Si se 	#
# ejecuta en un entorno Vagrant (especificar con un flag), el 	#
# README.md se traslada al directorio "/vagrant" para que sea	#
# accesible desde Windows.					#
#								#
# En un futuro, podría hacer que directamente el script se suba	#
# directamente al git indicando la ruta del repositorio y	#
# credenciales (mirar como indicar pwd sin que se muestre por	#
# pantalla. 							#
#								#			
# Puntos a documentar:						#
#	--> Título del script, que es lo que se ejecuta.	#
#	--> Descripción/Objetivo del script, qué es lo que hace.#
#	--> Argumentos del script, cómo se ejecuta.		#
#	--> Procesos con los que se relaciona			#
#	--> Orígen de los datos					#
#	--> Salida esperada					#
#	--> Propietario del script				#
#	--> Ruta en el GIT del script				#
#	--> Había documentación previa del script?		#
#								#	 
#################################################################

def Usage():
	print "Usage:"
	print "	./DocGenerator.py", "[nombre del script a documentar]"
	return

if len(sys.argv) != 2:
	Usage()
	exit()

# Creamos el archivo si no existía, en modo APPEND+READ
fd = open("README.md", "a+")

script = sys.argv[1]
script = script.split(".")
script = script[0]

# Creamos el título del script
fd.write("# " + script + "\n\n")

# Pedimos que se introduzca cuál es el objetivo del script
fd.write("## " + "Descripción\n")
objetivo = raw_input("Explica cuál es la descripción del script: \n")
fd.write(objetivo + "\n\n")

# Argumentos del script
	# Formas:
		# 1. Ponerlos a mano
		# 2. Buscar en el script alguna funcion de Usage, o donde se comprueba el numero de parametros
		# 3. ??

fd.write("## " + "Argumentos del script\n")
fd.write("\n\n")  #De momento dejamos el espacio en blanco

# Procesos con los que se relaciona
fd.write("## Procesos con los que se relaciona\n")
procesos_relaciona = raw_input("Indica cuáles son los procesos con los que se relaciona el script: \n")
fd.write(procesos_relaciona + "\n\n")

# Orígenes de los datos
fd.write("## Orígenes de los datos\n")
origen = raw_input("Indica el orígen de los datos del script: \n")
fd.write(origen + "\n\n")

	 # Cómo los recibimos o cómo los vamos a buscar
fd.write("### Cómo los recibimos o cómo los vamos a buscar\n")
forma = raw_input("Indica cómo recibimos los datos del script o como los vamos a buscar: \n")
fd.write(forma + "\n\n")

	# Tienen cadenas de planificador?
fd.write("### Tienen cadenas de planificador?\n")
cadenas = raw_input("Indica si el script tiene cadenas de planificador: \n")
fd.write(cadenas + "\n\n")
	
	# Dependencias
fd.write("### Dependencias\n")
dependencias = raw_input("Indica si el script tiene alguna dependencia: \n")
fd.write(dependencias + "\n\n")	


# Salida esperada
	# Posibles soluciones:
		# 1. A mano.
		# 2. Preguntar si se puede ejecutar el script
		# 3. Mirar a ver si hay alguna forma de testear el script
fd.write("## Salida esperada\n")

ejecutar = raw_input("¿Quieres ejecutar el script y volcar la salida en el fichero? [S]|[N]: ")
if ejecutar == "S" or "s":
	cmd = raw_input("Introduce el comando para ejecutar el script indicando los parámetros")
	out = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)
	fd.write(out + "\n")

#seguir aqui, preguntando para añadir la descripcion de la salida y demas
#acabar puntos
#si flag -v vagrant mover el readme a /vagrant para tenerlo accesible en windows

	  	





