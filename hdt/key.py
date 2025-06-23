# Kramer/Specter Deobf by KhanhNguyen9872
# file name: [x.py] (py - 3.11)
# dump -> code 22

import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("clear")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
banner = f"""
\033[1;95m╭─⋞─────────────────────────────────────────────────────╮
\033[1;31m██╗  ██╗██████╗ ████████╗  ████████╗ ██████╗  ██████╗ ██╗     
\033[1;32m██║  ██║██╔══██╗╚══██╔══╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
\033[1;33m███████║██║  ██║   ██║        ██║   ██║   ██║██║   ██║██║     
\033[1;34m██╔══██║██║  ██║   ██║        ██║   ██║   ██║██║   ██║██║     
\033[1;30m██║  ██║██████╔╝   ██║        ██║   ╚██████╔╝╚██████╔╝███████╗
\033[1;37m╚═╝  ╚═╝╚═════╝    ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ 
\033[1;37m Youtube : \033[1;32mhttps://youtube.com/@HDT-TOOL
\033[1;37m Nhóm Zalo : \033[1;32mhttps://zalo.me/g/bprmyn080
\033[1;37m Link Tool: \033[1;32m https://user-traffic.net/eNc0R
\033[1;95m╰─────────────────────────────────────────────────────⋟─╯ 
\033[1;37m────────────────────────────────────────────────────────────"""
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.00)
menu=f"""
\033[1;31m[\033[1;32m●\033[1;31m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══"""
for h in menu:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.00)
# ngay=int(strftime('%d'))
# key1=str(ngay*1246881818+2888181472) 
# key = 'HDTTOOL_/'+key1
# keyv1 = 'code'
# url = 'https://tooltranthuong.blogspot.com/p/key_25.html?key='+key
# token_link1s = '4027f152-feea-4b6c-8d74-1193a3976d7b'
# link1s = requests.get(f'https://web1s.com/api?token={token_link1s}&url={url}').json()
# if link1s['status']=="error": 
#     print(link1s['message'])
#     quit()
# else:
#     link_key=link1s['shortenedUrl']
# h=open('keyhdt.txt',mode='a+')
# h=open('keyhdt.txt',mode='r')
# thien=h.read()
# h.close()
print()
# if thien== keyv1 or thien== key:
if 1:
    print(dau,'\033[1;33m Chào Mọi Người Đến Với Tool - HDT-TOOL')
    sleep(1)
    # exec(requests.get('https://run.mocky.io/v3/6d14dda1-5e08-4212-b4ee-41a4fb62b1e1').text)
    exec(open('hdt/menu.py','rb').read())
else:
    print('\033[1;34m[\033[1;33m●\033[1;34m]\033[1;32m    [  Nhập Link Để Lấy Key Miễn Phí Mỗi Ngày  ]')
    print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
print('\033[1;31m[\033[1;32m●\033[1;31m] \033[1;34mĐường Link Lấy Key :\033[1;32m '+link_key)
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
keynhap = input('\033[1;31m[\033[1;32m●\033[1;31m] \033[1;34mNhập Key Đã Vượt\033[1;32m :\033[1;36m ')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
if keynhap == key or keynhap== keyv1:
    print(dau,'\033[1;32mKey Đúng Rồi ! Mời Bạn Vào Tool !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    sleep(2)
    h=open('keyhdt.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://run.mocky.io/v3/6d14dda1-5e08-4212-b4ee-41a4fb62b1e1').text)
else:
    print(dau,'\033[1;33mKey Sai Rồi ! Hãy Nhập Lại Key Nha !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")