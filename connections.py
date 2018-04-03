#!/usr/bin/env python

import os
import io
import subprocess

cmd = subprocess.Popen(["netstat"], stdout = subprocess.PIPE)
cmd1 = subprocess.Popen(["tail", "-n+30"], stdin = cmd.stdout, stdout = subprocess.PIPE)
cmd2 = cmd1.communicate()[0]

IPs = []
stop = 0

for line in cmd.stdout.readlines():
	splitted = line.split()

	if splitted[0] == "Active":
		stop = 1

	if splitted[len(splitted)-1] == "ESTABLISHED" and stop == 0:
		IPs.append(splitted[len(splitted)-2])

num = len(IPs)
result = list(set(IPs))

print("Hi ha un total de", num, "connexions TCP a les IP: ")

for i in result:
	print result


