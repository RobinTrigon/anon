#!/usr/bin/env python3
import time
import os
import subprocess
import sys
import requests
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('\033[1;38;5;196m[+]\033[1;38;5;040m  Your New Ip -> \033[1;38;5;154m '+str(ma_ip()))

print('''\033[1;38;5;013m
           +-+ +-+ +-+ +-+
           |A| |N| |O| |N|
           +-+ +-+ +-+ +-+''')
print("\033[1;38;5;154m                  anonymous tour by \033[1;38;5;051m RobinTrigon\n")
print("\033[0m \n")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[!] Riding............ ")
time.sleep(5)

time.sleep(3)
os.system("service tor start")
x = "10"
lin = "0"
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\n ')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
