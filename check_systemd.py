#!/usr/bin/env python

import io
import os
import subprocess

cmd = subprocess.Popen(["systemctl"], stdout = subprocess.PIPE)

failed = []
start = 0

# en vez de mirar si failed o no miro si loaded o active ya que si esta loaded significa que esta failed ya que se inserta mierda al principio de todo como para poner una senyal o algo


for line in cmd.stdout.readlines():
	splitted = line.split()
	
	if len(splitted) > 0 and start == 1:
		
		if splitted[2] == "loaded":
			strng = splitted[1].split(".")
			typ = strng[len(strng) -1]
			
			if typ == "service":
				failed.append(splitted[1])
	
	if start == 0:
		start = 1

if len(failed) == 0:
	print "Felicitats, tots els serveis estan correctes"

else:
	print "Hi ha", len(failed), "servei(s) fallit(s)"
	for i in failed:
		print i


