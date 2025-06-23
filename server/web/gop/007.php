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
import os, sys
import requests
import os, sys
import time
from time import strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
ip = requests.post('https://api.proxyscrape.com/ip.php').text
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__ZALO__ = '0777374145'
__ADMIN__ = 'An Orin'
__FACEBOOK__ = 'anorintool'
__VERSION__ = '1.0'
def banner():
 banner = f"""
\033[1;34m┌──────────────────────── ONLINE ────────────────────────┐
\033[1;35m║   \033[1;39mTOOL GỘP NHIỀU CHỨC NĂNG BY PHONG                    \033[1;35m║
\033[1;35m║   \033[1;39mFACEBOOK           :  nphong.dev                     \033[1;35m║
\033[1;35m║   \033[1;39mZALO               :  0826687013                     \033[1;35m║
\033[1;35m║   \033[1;39mTELEGRAM           :  T.ME/NPHONG                    \033[1;35m║
\033[1;35m║   \033[1;39mBOT SPAM NO KEY    :  T.ME/SPAMTHOIGICANG            \033[1;35m║
\033[1;35m║   \033[1;39mWEBSITE SHARE CODE :  SHOPNVP.EU.ORG                 \033[1;35m║
\033[1;34m└────────────────────────────────────────────────────────┘
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================

# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
sleep(1)
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;35mTool TDS Fb Full Job ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;35mTool TDS Pro5 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;35mTool TDS Pro5 Đa Luồng ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;35mTool TDS Fb VIP ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;35mTool TDS Tiktok ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;35mTool TDS INSTAGRAM MAX SPEED ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;35mTool TTC Pro5 Ver1 ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;35mTool TTC Pro5 Ver2 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;35mTool TTC Instagram Vipig ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTiện Ích Facebook  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;35mTool REG PAGE PRO5 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;35mTool GET TOKEN PAGE PRO5 ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;35mTool GET TOKEN FULL QUYỀN TỪ COOKE ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;35mTool CHUYỂN QUYỀN QUẢN TRỊ PAGE ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;35mTool REG PAGE VỊ TRÍ ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;35mTool CHUYỂN PAGE VỊ TRÍ + UP AVATAR ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool BUFF          \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;35mTool BUFF FOLLOW BẰNG PAGE PRO5 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;35mTool BUFF CMT PRO5 ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;35mTool BUFF VIEW STORY PRO5 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;35mTool BUFF CẢM XÚC STORY PRO5")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;35mTool BUFF MEM GROUP PRO5 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;34mNhập Số \033[1;31m[\033[1;33m21\033[1;31m] \033[1;35mTool BUFF VIEW TIKTOK")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Share ảo + Spam\033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;35mNhập Số \033[1;31m[\033[1;33m22\033[1;31m] \033[1;35mTool SHARE ẢO  ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;35mNhập Số \033[1;31m[\033[1;33m23\033[1;31m] \033[1;35mTool SHARE ẢO MAX SPEED ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;35mNhập Số \033[1;31m[\033[1;33m24\033[1;31m] \033[1;35mTool SHARE ẢO 2 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;35mNhập Số \033[1;31m[\033[1;33m25\033[1;31m] \033[1;35mTool SPAM SMS VÀ CALL VER1 ")
print("\033[1;35m[\033[1;37m>.<\033[1;36m] \033[1;37m=> \033[1;35mNhập Số \033[1;31m[\033[1;33m26\033[1;31m] \033[1;35mTool SPAM SMS VÀ CALL VER2 ")
print("\033[1;36m[\033[1;37m>.<\033[1;35m] \033[1;37m=> \033[1;35mNhập Số \033[1;31m[\033[1;33m27\033[1;31m] \033[1;35mTool SPAM SMS VÀ CALL VER3 ")
print("\033[1;31m────────────────────────────────────────────────────────────")
chon = int(input('\033[1;31m[\033[1;37m>.<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if chon == 1 :
	exec(requests.get('https://run.mocky.io/v3/84a51c3c-3921-4ae7-a094-8ed43ada2e07').text)
if chon == 2 :
	exec(requests.get('https://run.mocky.io/v3/0f6cde73-c1c6-4fa8-bab2-8915b22680a8').text)
if chon == 3 :
	exec(requests.get('https://run.mocky.io/v3/48dc1455-75ac-47b9-b1d1-f749dd5b1176').text)
if chon == 4 :
	exec(requests.get('https://run.mocky.io/v3/045fed81-4580-43c9-8af4-aae8bdf8a898').text)
if chon == 5 :
	exec(requests.get('https://run.mocky.io/v3/a4b5a32f-3b9a-4410-81d0-709266d21e31').text)
elif chon == 6 :
	exec(requests.get('https://run.mocky.io/v3/bc3bc50a-e1be-4fe5-ba41-36bf5bd7b106').text)
if chon == 7 :
	exec(requests.get('https://run.mocky.io/v3/6a205a8e-f595-4b17-99f3-6151a2d832ca').text)
if chon == 8 :
	exec(requests.get('https://run.mocky.io/v3/bb36435a-4140-42c3-9853-310aae8b7daa').text)
if chon == 9 :
	exec(requests.get('https://run.mocky.io/v3/ea85c2ec-9c6f-4afc-aee1-0ceb4037edaa').text)
if chon == 10 :
	exec(requests.get('https://run.mocky.io/v3/6d56a02f-ee25-4df2-8a7a-c35c6fbf41f1').text)
if chon == 11 :
	exec(requests.get('https://run.mocky.io/v3/373f9a90-c213-4688-89d8-aa815b47b94f').text)
if chon == 12 :
	exec(requests.get('https://run.mocky.io/v3/68677a2e-e0c1-4294-86cd-a4e946f41744').text)
if chon == 13 :
	exec(requests.get('https://run.mocky.io/v3/9ce21daa-7e94-4441-b513-273867f7ef2c').text)
if chon == 14 :
	exec(requests.get('https://run.mocky.io/v3/035187ad-7608-4724-b435-c3a7e4042d8b').text)
if chon == 15 :
	exec(requests.get('https://run.mocky.io/v3/d8a4f077-f7f1-41ce-b5ee-4ad2d4006707').text)
if chon == 16 :
	exec(requests.get('https://run.mocky.io/v3/3e229353-036b-4dd7-90dc-85c497f8b83a').text)
if chon == 17 :
	exec(requests.get('https://run.mocky.io/v3/78d03480-acb9-4ec0-a593-78b3dbc087af').text)
elif chon == 18 :
	exec(requests.get('https://run.mocky.io/v3/2117e8e0-f312-4acc-a68c-92d97c5e1735').text)
elif chon == 19 :
	exec(requests.get('https://run.mocky.io/v3/e8e2dd26-bb90-410c-85ba-99f88f9a0933').text)
elif chon == 20 :
	exec(requests.get('https://run.mocky.io/v3/4084effb-070e-4292-8eec-0a511fa8f9ca').text)
elif chon == 21 :
 exec(requests.get('https://run.mocky.io/v3/ecc7afdd-b78c-456f-a3d3-98240aab37e8').text)
elif chon == 22 :
 exec(requests.get('https://run.mocky.io/v3/9243ed92-4ae9-4378-9316-b4286ed10e2f').text)
elif chon == 23 :
 exec(requests.get('https://run.mocky.io/v3/b3d61829-b1b0-4e98-8d6a-a455f586ac68').text)
elif chon == 24 :
 exec(requests.get('https://run.mocky.io/v3/9c10b11d-8429-40f7-b563-0629f8fff86b').text)
if chon == 25 :
	exec(requests.get('https://run.mocky.io/v3/09341862-6b56-4fd9-9207-354e3d0d3693').text)
if chon == 26 :
	exec(requests.get('https://run.mocky.io/v3/304fe2a2-b214-4fe8-8271-172c93575ea7').text)
if chon == 27 :
	exec(requests.get('https://run.mocky.io/v3/2c090b12-4228-4634-957c-47f9ae1747b3').text)
else :
	exit()