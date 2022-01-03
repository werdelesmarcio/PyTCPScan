#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PyTCPScan Version 1.2 (beta)

import socket
import sys
import subprocess
from datetime import datetime

pathfile = './utils/'
if pathfile not in sys.path:
	sys.path.append(pathfile)

from banner import *

#Limpa a tela ao executar a aplicação
subprocess.call('clear', shell=True) 

banner()

# Quando não for informado nenhum parametro
if len(sys.argv) != 4:
	print("\n [!]ERROR: Missing input arguments.\n")
	print(" [!]Usage: ./pyTCPScan.py [target] [initial_port] [final_port]\n")
	sys.exit(1)

# Criando o socket de conexão para testar as portas
def connect(IP, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
	
    try:
        s.connect((IP, port))
        return(1)
    except:
        return(2)

# Variáveis
IP = str(sys.argv[1])
host = socket.gethostbyname(IP)
ip = int(sys.argv[2])
fp = int(sys.argv[3])

# Iniciando o scan
print (" [*]Connecting to Target: %s\n [*]Scanning ports between %s and %s ..." % (IP, ip, fp))
print (' ')
print (' [!]Please wait, scanning remote host', host)
print (' [*]This may take a while, be patient.')
print (' ')

# Checando a hora que iniciou o Scan
t1 = datetime.now()

# Laço que testa as portas no range
try:
	for port in range(ip, fp+1):
	    e = connect(IP, port)
	    if e == 1:
	    	print (' [+]POSITIVE TO Port {}:	Status: OPEN'.format(port))
	    
# Se control+c for pressionado encerra a aplicação
except KeyboardInterrupt:
	print ('\n You pressed Ctrl+C')
	print (' The application has been stopped prematurely.')
	sys.exit()

# Se o Host não pôde ser resolvido	
except socket.gaierror:
	print ('Hostname could not be resolved. Exiting')
	sys.exit()

# Se foi impossível conectar com o alvo	
except socket.error:
	print ('Could not connect to target')
	sys.exit()
	
# Checa o termino do scan
t2 = datetime.now()

tempoTotal = t2 - t1

print ('-' * 50)
print
print (' [!]Scanning Completed in: ', tempoTotal)  # Banner indicando o tempo de scan
print
print ('-' * 50)
 
print("\n ---Finished---\n")

