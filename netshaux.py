#! /usr/bin/env python

import subprocess
import time
import datetime
import sys

def printUsage(help=True):
	print(''' 

 _   _      _       _                      
| \ | |    | |     | |                     
|  \| | ___| |_ ___| |__   __ _ _   ___  __
| . ` |/ _ \ __/ __| '_ \ / _` | | | \ \/ /
| |\  |  __/ |_\__ \ | | | (_| | |_| |>  < 
\_| \_/\___|\__|___/_| |_|\__,_|\__,_/_/\_\ 
					- Auxiliar para Hotspot WiFi''')

	if help:
		print('''
Uso:     {0} <rede> <senha>
Exemplo: {1} Nachos 12345
			'''.format(sys.argv[0], sys.argv[0]))

#ssid = input('SSID: ')
#pw   = input('PW: ')

#while(not(len(pw) >= 8 and len(pw) <= 63)):
#    print('A senha da rede é curta ou extensa. (Mínimo 8 caracteres, máximo 63).')
#    ssid = input('SSID: ')
#    pw   = input('PW: ')

def main():
	if len(sys.argv) < 3:
		printUsage()
		sys.exit()

	printUsage(False)
	
	ssid = sys.argv[1]
	pw   = sys.argv[2]

	#Inicia a rede
	subprocess.call("netsh wlan set hostednetwork mode=allow ssid=" + ssid + " key=" + pw, shell=True)

	for i in range(3, 0, -1):
	    time.sleep(1)
	    print("Dispositivo habilitado em " + str(i) + " segundo(s).")
	subprocess.call('netsh wlan start hostednetwork')

	print("Conexão iniciada às {}.".format(datetime.datetime.now().time().strftime('%H:%M:%S')))
	#Desabilita a rede
	opt = input("Desativar WiFi? [Digite 'sim' ou 's']: ")
	while True:
		if(opt.lower() == "s" or opt.lower() == "sim"):
			break
		print("Opção incorreta. Para desativar, digite 'sim' ou 's'.")
		opt = input('Desativar WiFi? ')
		continue

	subprocess.call("netsh wlan stop hostednetwork")
	for i in range(3, 0, -1):
		time.sleep(1)
		print("Finalizando operação em " + str(i) + " segundo(s).")
	subprocess.call("netsh wlan set hostednetwork mode=disallow")
	print("Conexão desativada às {}.".format(datetime.datetime.now().time().strftime('%H:%M:%S')))

if __name__ == '__main__':
	main()

#Script auxiliar para criação de Hotspot WiFi pelo utilitário NETSH do Windows
