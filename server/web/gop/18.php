import requests
import os
import json
from datetime import timezone, datetime, timedelta
import requests
from time import sleep
import threading
os.system('clear')
#Thay thế giá trị này bằng cookie của bạn
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
#import màu
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

#Đánh Dấu Bản Quyền

hdang = trang + "~" + trang + "[" + do + "+" + trang + "] " + trang + "=> "

hdang = trang + "~" + trang + "[" + do + "÷" + trang + "] " + trang + "=> "

thanh = trang + "-------------------------------------------------------------------------"

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
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo=f"""
\033
██╗░░░██╗██╗░░░░░░█████╗░███╗░░██╗░██████╗░
██║░░░██║██║░░░░░██╔══██╗████╗░██║██╔════╝░
╚██╗░██╔╝██║░░░░░██║░░██║██╔██╗██║██║░░██╗░
░╚████╔╝░██║░░░░░██║░░██║██║╚████║██║░░╚██╗
░░╚██╔╝░░███████╗╚█████╔╝██║░╚███║╚██████╔╝
░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚══╝░╚═════╝░
\033[1;31m╔═══════════════════════════════════════════════════════╗
{a}{yellow}Tool Buff Comment Pro5
{a}{luc}TIME CREATE: {today} : {time}
{a}{luc}TIME END: {today} : {time}
{a}{luc}YOUR IP: {ip}\033[1;31m
╚═══════════════════════════════════════════════════════╝
  """
    print(logo)
#=======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
logo()
ck_fb= input(" \033[1;97m[\033[1;31m+_+\033[1;97m] => \033[1;32mNhập Cookie Chứa Page Pro5: \033[1;97m")
print("=========================================================")
print("\033[38;5;11mĐang Get Token..",end='\r')


hed_gettoken = {
    'authority': 'www.instagram.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'no-cache',
    'cookie': ck_fb,
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
}
try:
    token_fb = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token', headers=hed_gettoken).url.split('#access_token=')[1].split('&data_access_expiration_time')[0]
except:
    print(' \033[1;97m[\033[1;31m+_+\033[1;97m] => Get Token Thất Bại, Vui Lòng Xem Lại Cookie')
    sleep(5)
    quit()

header={
    'cookie': ck_fb,
}

def Start():
    get_ = requests.get('https://graph.facebook.com/me/accounts?access_token='+token_fb).json()['data']
    for access in get_:
        tok = access['access_token']
        uid_page=access['id']
        name=access['name']
        try:
            url = f"https://graph.facebook.com/{id_post}/comments?method=post&access_token={tok}&message={noidung}"
            r = requests.post(url)
            a=r.text
            if ['id'] in r:
                print(f'\033[1;31m[\033[1;33mvLong\033[1;31m] \033[1;31m| {tim}Uid: \033[1;97m{uid_page} \033[1;31m| {blue}Name: \033[1;97m{name} \033[1;31m| {green}Commet Port: \033[1;97m{id_post} \033[1;31m| \033[0m \033[1m\033[38;5;51mSuccess')
            #print(['id'])
            else:
                print(f'\033[1;31m[\033[1;33mvLong\033[1;31m] \033[1;31m| {tim}Uid: \033[1;97m{uid_page} \033[1;31m| {blue}Name: \033[1;97m{name} \033[1;31m| {green}Comment Port: \033[1;97m{id_post} \033[1;31m| Fail')
        except:
            print("Fail")
def Start1():
    get_ = requests.get('https://graph.facebook.com/me/accounts?access_token='+token_fb).json()['data']
    for access in get_:
        tok = access['access_token']
        uid_page=access['id']
        name=access['name']
        try:
            url = f"https://graph.facebook.com/{id_post}/comments?method=post&access_token={tok}&message={noidung} @[{id_bb}:0]"
            r = requests.post(url)
            a=r.text
            if ['id'] in r:
                print(f'\033[1;31m[\033[1;33mvLong\033[1;31m] \033[1;31m| {tim}Uid: \033[1;97m{uid_page} \033[1;31m| {blue}Name: \033[1;97m{name} \033[1;31m| {green}Comment Port: \033[1;97m{id_post} \033[1;31m| \033[0m \033[1m\033[38;5;51mSuccess')
            #print(['id'])
            else:
                print(f'\033[1;31m[\033[1;33mvLong\033[1;31m] \033[1;31m| {tim}Uid: \033[1;97m{uid_page} \033[1;31m| {blue}Name: \033[1;97m{name} \033[1;31m| {green}Comment Port: \033[1;97m{id_post} \033[1;31m| Fail')
        except:
            print("Fail")

chon=input(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Comment Tag Id(Y/n): ")
if chon == 'N' or chon == 'n':
    id_post=input(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Nhập Id Post: ")
    noidung=input(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Nhập Nội Dung: ")
    print("=========================================================")
    Start()
else:
    id_post=input(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Nhập Id Post: ")
    noidung=input(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Nhập Nội Dung: ")
    id_bb=input(" \033[1;97m[\033[1;31m+_+\033[1;97m] => Nhập Id Bạn Bè Cần Tag: ")
    print("=========================================================")
    Start1()