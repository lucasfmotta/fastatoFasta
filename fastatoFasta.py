#!/usr/bin/python3

import os

directorio = os.listdir(os.curdir)
fastas = []
for file in directorio:
	if file.endswith('.fasta'):
		fastas.append(file)

if not fastas:
	print('No .fasta files found')
	quit()

for file in fastas:
	fasta = open(file)
	newfile = open(file.replace('fasta', 'FASTA'), 'a')
	for line in fasta:
		if line.startswith('>'):
			newfile.write(line)
			continue
		line = line.rstrip()
		newfile.write(line)
	newfile.close()
	fasta.close()
