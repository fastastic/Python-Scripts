#!/usr/bin/env python

#migrate.py
#Lo que prentende este scripts es migrar todos los archivos del directorio /vagrant que
#tenga la extension pasada por parametro y migrarla a /home/vagrant para organizar mejor
#los archivos

import os
import sys
import io
import subprocess

def usage():
	print "Usage:", "./migrate.py <extension>"
	return

if len(sys.argv) != 2:
	usage()
	exit()

arg = sys.argv[1]
print "Nombre script: ", sys.argv[0]
print "Argumento: ", arg

src_path = "/vagrant/"
dst_path = os.environ["PWD"]
print "src_path: ", src_path
print "dst_path: ", dst_path

os.chdir(src_path)
#lsla = subprocess.Popen(["ls", "-la"], stdout = subprocess.PIPE)

files = []

f = open(os.devnull, 'w')
sys.stderr = f

print 'Moviendo archivos', "." + arg, "a", dst_path, "..."
parameter = src_path + "*." + arg
cmd = "mv " + parameter + " " + dst_path
print cmd
subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)

#for line in lsla.stdout.readlines():
#	splitted = line.split()
#	file = splitted[len(splitted)-1] #cogemos el nombre del archivo
#	extension = file.split(".")
#	print extension[len(extension)-1]
#
#	if arg == extension[len(extension)-1]:
		
 
