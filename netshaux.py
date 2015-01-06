import subprocess
import time

ssid = input('SSID: ')
pw   = input('PW: ')

while(not(len(pw) >= 8 and len(pw) <= 63)):
    print('A senha da rede é curta ou extensa. (Mínimo 8 caracteres, máximo 63).')
    ssid = input('SSID: ')
    pw   = input('PW: ')

#Inicia a rede
subprocess.call('netsh wlan set hostednetwork mode=allow ssid=' + ssid + 'key=' + pw, shell=True)

for i in range(3, 0, -1):
    time.sleep(3)
    print('Dispositivo habilitado em ' + str(i) + ' segundo(s).')

subprocess.call('netsh wlan start hostednetwork')

#Desabilita a rede
ret = input('Desativar WiFi?')
if(ret.lower() == 'yes'):
    subprocess.call('netsh wlan stop hostednetwork')
    for i in range(3, 0, -1):
        time.sleep(3)
        print('Finalizando operação em ' + str(i) + 'segundo(s).')

subprocess.call('netsh wlan set hostednetwork mode=disallow')
            
print('Conexão desativada.')
