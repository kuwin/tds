import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
# =======================[ NHẬP KEY ]=======================
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
\033[1;34m[\033[1;33m●\033[1;34m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;32m ██╗  ██╗██╗   ██╗ ██████╗ ████████╗
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;35m ╚██╗██╔╝██║   ██║██╔═══██╗╚══██╔══╝
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;33m  ╚███╔╝ ██║   ██║██║   ██║   ██║   
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;34m  ██╔██╗ ██║   ██║██║   ██║   ██║   
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;36m ██╔╝ ██╗╚██████╔╝╚██████╔╝   ██║   
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;31m ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;32m     ██████╗ ███████╗██╗   ██╗
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;35m     ██╔══██╗██╔════╝██║   ██
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;33m     ██║  ██║█████╗  ██║   ██║
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;34m     ██║  ██║██╔══╝  ╚██╗ ██╔╝
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;36m     ██████╔╝███████╗ ╚████╔╝ 
\033[1;34m[\033[1;33m●\033[1;34m]         \033[1;31m     ╚═════╝ ╚══════╝  ╚═══╝  
\033[1;34m[\033[1;33m●\033[1;34m]   \033[1;31m𝐓𝐨𝐨𝐥 𝐂𝐡𝐚̂́𝐭 𝐋𝐮̛𝐨̛̣𝐧𝐠 𝐓𝐚̣𝐨 𝐍𝐞̂𝐧 𝐓𝐡𝐮̛𝐨̛𝐧𝐠 𝐇𝐢𝐞̣̂𝐮:\033[1;32m 🌺 Xuột Dev 🌺 
\033[1;34m[\033[1;33m●\033[1;34m]   \033[1;31m\033[1;31m𝐍𝐡𝐨́𝐦 𝐙𝐚𝐥𝐨 : \033[1;32mhttps://zalo.me/g/bprmyn080
\033[1;34m[\033[1;33m●\033[1;34m]   \033[1;31m\033[1;31m𝐘𝐨𝐮𝐭𝐮𝐛𝐞 : \033[1;32m https://youtube.com/@ShareToolFacebook
\033[1;34m[\033[1;33m●\033[1;34m]   \033[1;31m\033[1;31mTelegram: \033[1;32m https://t.me/xuotdev_tool
\033[1;34m[\033[1;33m●\033[1;34m]   \033[1;31m\033[1;31mWeb Share Tool :\033[1;32m xuotdev.blogspot.com/?m=1
\033[1;34m[\033[1;33m●\033[1;34m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══
\033[1;31m[\033[1;32m●\033[1;31m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══
\033[1;33m               ╔════════════════════════╗
\033[1;33m               ║  \033[1;31mVượt Link Để Lấy Key  \033[1;33m║
\033[1;33m               ╚════════════════════════╝
\033[1;31m[\033[1;32m●\033[1;31m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
ngay=int(strftime('%d'))
#cách 2 randon link 
#ngay=random.randrange(100000)
# key1=str(ngay*24122006*241226)
# key = 'xuotdev'+key1
# key2 = 'xuotdev'
# url = 'https://toolsiuvip.tk/api/keyfree.php?key='+key
# token_link1s = '4027f152-feea-4b6c-8d74-1193a3976d7b'
# link1s = requests.get(f'https://web1s.com/api?token={token_link1s}&url={url}').json()
# if link1s['status']=="error": 
# 	print(link1s['message'])
# 	quit()
# else:
# 	link_key=link1s['shortenedUrl']
# print(f"""\033[1;34m
# ┏\033[1;32mLink Vượt Key:\033[1;34m {link_key}\033[1;34m""")
# keynhap = input('\033[1;34m┗━➤\033[1;32mKey Đã Vượt: \033[1;34m')
# if keynhap == key:
#     print('Đang Check Key...')
#     sleep(2)
#     print('Key Đúng Mời Bạn Dùng Tool')
#     sleep(1.001)
# elif keynhap == key2:
#     print('Đang Check Key...')
#     sleep(2)
#     print('Key Đúng Mời Bạn Dùng Tool')
#     sleep(1.001)
# else:
#     print('Đang Check Key...')
#     sleep(2)
#     print("Key Sai Vui Lòng Vượt Link Lại")
print('')
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
print("\033[1;34m[\033[1;33m●\033[1;34m]   \033[1;32m╔══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\033[1;31m══\x1b[1;94m══\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m═══╗")
print("\033[1;34m[\033[1;33m●\033[1;34m]   \033[1;32m║  \033[1;31m𝐂𝐡𝐚̀𝐨 𝐌𝐨̣𝐢 𝐍𝐠𝐮̛𝐨̛̀𝐢 Đ𝐞̂́𝐧 𝐕𝐨̛́𝐢 𝐓𝐨𝐨𝐥 🌺 𝐗𝐮𝐨̣̂𝐭 𝐃𝐞𝐯 🌺 \033[1;32m ║ ")
print("\033[1;34m[\033[1;33m●\033[1;34m]   \033[1;32m╚══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\033[1;31m══\x1b[1;94m══\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m═══╝")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool Encode 5 Lớp\033[1;33m [ Độc Quyền ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool Buff View Story Bằng Pro5\033[1;33m [ New ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool Buff TV Gourp Bằng Pro5\033[1;33m [ New ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool Reg Pro5 + Úp AVT\033[1;33m [ New ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool Chuyển QTV Pro5\033[1;33m [ New ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool Tool TTC Instagram Vipig\033[1;33m [ New ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool Buff Folow Bằng Pro5\033[1;33m [ New ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool Cày Xu TTC Pro5\033[1;33m [ Độc Quyền ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool Cày Xu TDS Pro5\033[1;33m [ New ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool SHARE ẢO ĐA LUỒNG MAX SPEED\033[1;33m [ VIP ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool TDS Tiktok\033[1;33m [ VIP ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mTool Buff View Tiktok [Zefoy]\033[1;33m [ Mới ]")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Get Cookie Page Thường & Page Pro5")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Encode AnOrin")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Tăng Menber Group Bằng Pro5 AnOrin")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTool Tăng Share Ảo Bằng Page Pro5 Version 1.0 AnOrin")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")
print("\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;31m[\033[1;33m0\033[1;31m] \033[1;32mThoát Tool\033[1;31m [ 🌺 Xuột Dev 🌺 ]")
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
chon = int(input('\033[1;34m[\033[1;33m●\033[1;34m] \033[1;38mNhập Số \033[1;37m: \033[1;33m'))
try:
    exec(open('xuott/{}'.format(chon),'rb').read())
except:
    print (" Sai Lựa Chọn ")
    exit()

# if chon == 1 :
# 	exec(requests.get('https://run.mocky.io/v3/b8a55602-8108-4ecf-8334-ed14fb2375d2').text)
# if chon == 2 :
# 	exec(requests.get('https://run.mocky.io/v3/cf0c4d55-2c35-44cb-839b-a3960d81d110').text)
# if chon == 3 :
# 	exec(requests.get('https://run.mocky.io/v3/80babb3b-003d-44b8-81e4-7eb79980bc34').text)
# if chon == 4 :
# 	exec(requests.get('https://run.mocky.io/v3/737661de-5fc3-4c14-b164-2ad46d891ead').text)
# if chon == 5 :
# 	exec(requests.get('https://run.mocky.io/v3/0e123935-5946-41b9-b9dd-e574b4a76206').text)
# if chon == 6 :
# 	exec(requests.get('https://run.mocky.io/v3/14be2431-4c21-4067-a038-cc075bce960f').text)
# if chon == 7 :
# 	exec(requests.get('https://run.mocky.io/v3/c09fd780-105d-4c92-8d1d-7d938d923f61').text)
# if chon == 8 :
# 	exec(requests.get('https://run.mocky.io/v3/89304259-f5c5-4426-aeb1-25b49c4d477d').text)
# if chon == 9 :
# 	exec(requests.get('https://run.mocky.io/v3/c1269420-d1ae-4afb-840b-09959382aaaf').text)
# if chon == 10 :
# 	exec(requests.get('https://run.mocky.io/v3/19754f54-8815-4c52-8b77-ff36e696488f').text)
# if chon == 0 :
# 	exec(requests.get('https://run.mocky.io/v3/ad6c087c-1784-4e96-b453-11b38c66e276').text)
# if chon == 11 :
# 	exec(requests.get('https://run.mocky.io/v3/2901e1bb-2410-4d41-984f-1ca131cc5351').text)
# if chon == 12 :
# 	exec(requests.get('https://run.mocky.io/v3/cd273024-7b3d-40fd-92df-32d3305c7bc1').text)
# if chon == 13 :
# 	exec(requests.get('https://run.mocky.io/v3/dc84321a-be1d-4e91-bbb1-a3fa319c2783').text)
# if chon == 14 :
# 	exec(requests.get('https://run.mocky.io/v3/c7495db1-bd6b-46a5-8740-e451585e7b3e').text)
# elif chon == 16 :
#  exec(requests.get('https://run.mocky.io/v3/94c0852d-7373-474f-ae39-b2dd2b8d78aa').text)
# elif chon == 17 :
#  exec(requests.get('https://run.mocky.io/v3/1e0c4843-6aa2-4af0-8955-55fe1e1c4d34').text)
# else :
# 	print (" Sai Lựa Chọn ")
# 	exit()


