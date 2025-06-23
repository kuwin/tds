from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import requests
import socket
from pystyle import *
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
import os, sys
import requests
import os, sys
import time
from time import strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
ip = requests.post('https://api.proxyscrape.com/ip.php').text
# Đánh Dấu Bản Quyền
lthd_tool = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
lthd = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
# Phần List
list_id_name_page = []
count = 0
dem = 0
# import lib
import os,sys,requests,threading
from time import sleep
from datetime import datetime
try:
    import requests
except:
    print(luc+"Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải... ")
    os.system("pip install requests")

#today nand clear

os.system('cls')

data_machine = []

today = date.today()

os.system('clear')
#daystime

now = datetime.now()

thu = now.strftime("%A")

ngay_hom_nay = now.strftime("%d")

thang_nay = now.strftime("%m")

nam_ = now.strftime("%Y")
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
# ====================== [ FUNCTION ] ====================== 
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f"""
\033
██╗░░░██╗██╗░░░░░░█████╗░███╗░░██╗░██████╗░
██║░░░██║██║░░░░░██╔══██╗████╗░██║██╔════╝░
╚██╗░██╔╝██║░░░░░██║░░██║██╔██╗██║██║░░██╗░
░╚████╔╝░██║░░░░░██║░░██║██║╚████║██║░░╚██╗
░░╚██╔╝░░███████╗╚█████╔╝██║░╚███║╚██████╔╝
░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚══╝░╚═════╝░
╔═══════════════════════════════════════════════════════╗
{a}{yellow}Tool Get Cookie Pro5
╚═══════════════════════════════════════════════════════╝"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;31m─────────────────────────────────────────────────────────')
def getcookie(x, cookie):
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_id_name_page[x].split('|')[0]
    name_page = list_id_name_page[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    #print(f'\033[1;31m| \033[1;34m{name_page} \033[1;31m| \033[1;35m{uid_page} \033[1;31m| \033[1;97m{cookie9}')
    open('cookie_pro5.txt',"a").write(cookie9+'\n')
def getcookie1(x, cookie):
    time = datetime.now().strftime("%H:%M:%S")
    uid_page = list_id_name_page[x].split('|')[0]
    name_page = list_id_name_page[x].split('|')[1]
    list1 = (f'i_user={uid_page};')
    cookie9 = (f'{cookie}{list1}')
    #print(f'{name_page}\n')
    open('cookie_pro5.txt',"a").write(cookie9+' | '+uid_page+' | '+name_page+'\n')
# =================[ START TOOL ]===========================
clear()
banner()
cookie = input(lthd_tool+luc+'Vui Lòng Nhập Cookie Facebook Chứa Page Pro5'+trang+': '+vang)
headers={
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
            'cookie': cookie,
        }
try:
    url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
    getdatainfo = requests.get(url_profile,headers=headers).text
except:
    print(do+'COOKIE DIE, VUI LÒNG KIỂM TRA LẠI!')
try:
    fb_dtsg = getdatainfo.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
    jazoest = getdatainfo.split('{"name":"jazoest","value":"')[1].split('"},')[0]
except:
    try:
        fb_dtsg = getdatainfo.split(',"f":"')[1].split('","l":null}')[0]
        jazoest = getdatainfo.split('&jazoest=')[1].split('","e":"')[0]
    except:
        print(do+'COOKIE DIE, VUI LÒNG KIỂM TRA LẠI!')
clear()
banner()
# Get List UID + NAME Page Pro5
headers_getid = {
    'cookie': cookie, 
}
data = {
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
    'doc_id': '5300338636681652'
}
getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = headers_getid, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']

for i in getidpro5:
    uid_page = i['profile']['id']
    name_page = i['profile']['name']
    gomlist = f'{uid_page}|{name_page}'
    list_id_name_page.append(gomlist)
# DỮ LIỆU ĐÃ GET
print(lthd_tool+luc+'Đã Tìm Thấy '+trang+str(len(list_id_name_page))+luc+' Page Pro5')
# NHẬP ĐÓ VIEW BẠN MUỐN TĂNG
thanh()
sleep(3)
# RUN CODE
chon=input(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Lưu Cookie Kèm Tên Page & Uid Page [y/n]: ")
if chon == 'Y' or chon == 'y':
    for x in range(len(list_id_name_page)):
        dem=dem+1
        threading.Thread(target=getcookie1,args=(x, cookie, )).start()
    sleep(3)
    print(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Đã Lưu Cookie Pro5 Vào cookie_pro5.txt")
if chon == 'N' or chon == 'n':
    for x in range(len(list_id_name_page)):
        dem=dem+1
        threading.Thread(target=getcookie,args=(x, cookie, )).start()
    sleep(3)
    print(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Đã Lưu Cookie Pro5 Vào cookie_pro5.txt")