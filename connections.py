#!/usr/bin/env python

import os
import io
import subprocess

cmd = "netstat | tail -n+3"
ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr= subprocess.STDOUT)
out = ps.communicate()[0]

end = 0
IPs = set()
s = 0 

for line in out.split('\n'):
	splitted = line.split()

	if len(splitted) > 0 and splitted[0] == "Active":		
		end = 1
	
	if len(splitted) > 0 and splitted[len(splitted)-1] == "ESTABLISHED" and splitted[0] == "tcp":
		IPs.add(splitted[len(splitted)-2])
		s += 1


print "Hi ha un nombre de", len(IPs), "(", s, ")", "connexions TCP a les IPs:"

for i in IPs:
	print i


