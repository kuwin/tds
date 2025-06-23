import os,sys,re
import datetime
# Kiểm tra xem tệp lưu trữ trạng thái đã tồn tại chưa
if not os.path.exists("cache_tds.txt"):
    # Đoạn mã A - Chạy khi tệp lưu trữ trạng thái không tồn tại )
    os.system('pip  install colorama')
    os.system('pip install requests')
    os.system('pip3 install beautifulsoup4')
    # Lưu trạng thái đã chạy đoạn mã A
    with open("cache_tds.txt", "w") as state_file:
        state_file.write("Đây là tệp ghi nhớ")
else:
    # Đoạn mã B - Chạy khi tệp lưu trữ trạng thái đã tồn tại và bỏ qua đoạn mã A
    print('        Đã cài thư viện cần thiết')
from colorama import Back, Fore, Fore, Style, init
import requests
from bs4 import BeautifulSoup
import time
from time import sleep
import json

os.system('clear')
init(autoreset=True)
# Lấy thời gian hiện tại
current_time = datetime.datetime.now()

# Chuyển đổi thời gian thành chuỗi dạng ngày/tháng/năm giờ:phút:giây
time = current_time.strftime("%H:%M:%S")
# Chuyển đổi thời gian thành chuỗi dạng ngày/tháng/năm giờ:phút:giây

text = f"""
{Fore.LIGHTMAGENTA_EX}┏────────────────────────────────────────────────┓
│                                                │
{Fore.LIGHTMAGENTA_EX}│     {Fore.LIGHTCYAN_EX} ██▀──────────────────────────────▀██    {Fore.LIGHTMAGENTA_EX}  │
{Fore.LIGHTMAGENTA_EX}│      {Fore.LIGHTBLUE_EX}▄█▀───████████──██▀▀▀▄▄───██▀▀▀──▀█▄ {Fore.LIGHTMAGENTA_EX}     │
{Fore.LIGHTMAGENTA_EX}│   {Fore.LIGHTGREEN_EX}   ██▀─────███─────██───██───██▄▄▄──▀██   {Fore.LIGHTMAGENTA_EX}   │
{Fore.LIGHTMAGENTA_EX}│     {Fore.LIGHTBLUE_EX}  ▀█─────███─────██▄▄▄▀▀───▄▄▄██──▄█▀    {Fore.LIGHTMAGENTA_EX}  │
{Fore.LIGHTMAGENTA_EX}│      {Fore.LIGHTCYAN_EX}██▄──────────────────────────────▄██    {Fore.LIGHTMAGENTA_EX}  │
│                                                │
{Fore.LIGHTMAGENTA_EX}┗────────────────────────────────────────────────┛
"""

lines = text.split('\n')

for line in lines:
    sys.stdout.write("\r" + line)
    sys.stdout.flush()
    sleep(0.1)
    print()  # xuống dòng sau mỗi dòng text

print()  # kết thúc với dòng trống

chucode1 =f'{Back.WHITE }{Fore.LIGHTMAGENTA_EX}CODER:{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}Phạm Minh Hải    {Back.WHITE }{Fore.LIGHTMAGENTA_EX}YOUTUBE:{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}Dame Conghe'
dongchucode1 = chucode1.split('\n')

for cchucode1 in dongchucode1:
    for i in range(len(cchucode1) + 1):   
        sys.stdout.write("\r" + cchucode1[:i])
        sys.stdout.flush()
        sleep(0.02)
    print() # xuống dòng sau mỗi dòng text
        
print() # kết thúc với dòng trống

chucode2=f'{Back.WHITE }{Fore.LIGHTMAGENTA_EX}TIK TOK:{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}Dame Conghe        {Back.WHITE }{Fore.LIGHTMAGENTA_EX}FACEBOOK:{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}Dame Conghe'
dongchucode2 = chucode2.split('\n')

for cchucode2 in dongchucode2:
    for i in range(len(cchucode2) + 1):   
        sys.stdout.write("\r" + cchucode2[:i])
        sys.stdout.flush()
        sleep(0.02)
    print() # xuống dòng sau mỗi dòng text


#TDS9JSOyVmdlNnI6IiclZXZzJCLis2b0tWa0lWYohmbp1WbhhGUiojIyV2c1Jye
#thông tin
vs= 'https://ghichu.vn/fTZnA'

# Sử dụng thư viện requests để tải trang web
response1 = requests.get(vs)

# Kiểm tra xem tải trang thành công hay không (HTTP status code 200 là thành công)
if response1.status_code == 200:
    # Parse nội dung HTML bằng BeautifulSoup
    soup1 = BeautifulSoup(response1.text, 'html.parser')

    # Tìm thẻ <textarea> bằng class 'content'
    textarea = soup1.find('textarea', {'class': 'content'})

    # Lấy nội dung bên trong thẻ <textarea>
    if textarea:
        content = textarea.string.strip()  # Sử dụng .string để lấy nội dung và .strip() để loại bỏ khoảng trắng thừa

    else:
        print('KIỂM TRA MẠNG CỦA BẠN')
if content=='Version 1.1.0' :

    print('Version 1.1.0')
    print('--------------------------------------------------')
    while True:
        if not os.path.exists("cache_tds_token.txt"):
            token=input(f'{Fore.LIGHTGREEN_EX}Nhập token:{Fore.LIGHTBLUE_EX} ')
            thongtin='https://traodoisub.com/api/?fields=profile&access_token='+token
            doithongtin=requests.get(thongtin)
            laythongtin=doithongtin.json()
            kiemtra1=laythongtin.get('success')
            if kiemtra1==200:
                name=laythongtin.get('data').get('user')
                printname=f"{Fore.LIGHTGREEN_EX}Tên:{Fore.LIGHTBLUE_EX} {name}"
                for i in range(len(printname)+1):
                    sys.stdout.write("\r" + printname[:i])
                    sys.stdout.flush()
                    sleep(0.02)
                xu=laythongtin.get('data').get('xu')
                xudie=laythongtin.get('data').get('xudie')
                printxu=f"\n{Fore.LIGHTGREEN_EX}Xu:{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX} {xu}"
                prntxu=printxu.split('\n')
                for pnt in prntxu:
                    for i in range(len(pnt)+1):
                        sys.stdout.write("\r" + pnt[:i])
                        sys.stdout.flush()
                        sleep(0.02)
                    print()
        #print()
    #    sleep(1)
                printxudie=f"{Fore.LIGHTGREEN_EX}Xu die:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{xudie}"
                for i in range(len(printxudie)+1):
                    sys.stdout.write("\r" + printxudie[:i])
                    sys.stdout.flush()
                sleep(0.02)
    #        sleep(1)
                with open("cache_tds_token.txt", "w") as state_file:
                    state_file.write(token)
                break
            else:
                print(f'{Back.LIGHTRED_EX}Sai token vui lòng nhập lại')
                sleep(1)
                continue

        
        else:
            with open('cache_tds_token.txt') as f:
                lines = f.readlines()
                token=lines[0]
#tokenfb=input('Nhập token FB: ')
    #token='TDS9JSOyVmdlNnI6IiclZXZzJCLis2b0tWa0lWYohmbp1WbhhGUiojIyV2c1Jye'
            thongtin='https://traodoisub.com/api/?fields=profile&access_token='+token
            doithongtin=requests.get(thongtin)
            laythongtin=doithongtin.json()
            kiemtra1=laythongtin.get('success')
            if kiemtra1==200:
                name=laythongtin.get('data').get('user')
                printname=f"{Fore.LIGHTGREEN_EX}Tên:{Fore.LIGHTBLUE_EX} {name}"
                for i in range(len(printname)+1):
                    sys.stdout.write("\r" + printname[:i])
                    sys.stdout.flush()
                    sleep(0.02)
        
        #sleep(1)
                xu=laythongtin.get('data').get('xu')
                xudie=laythongtin.get('data').get('xudie')
                printxu=f"\n{Fore.LIGHTGREEN_EX}Xu:{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX} {xu}"
                prntxu=printxu.split('\n')
                for pnt in prntxu:
                    for i in range(len(pnt)+1):
                        sys.stdout.write("\r" + pnt[:i])
                        sys.stdout.flush()
                        sleep(0.02)
                    print()
        #print()
    #    sleep(1)
                printxudie=f"{Fore.LIGHTGREEN_EX}Xu die:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{xudie}"
                for i in range(len(printxudie)+1):
                    sys.stdout.write("\r" + printxudie[:i])
                    sys.stdout.flush()
                    sleep(0.02)
    #    sleep(1)
                break
            else:
                print(f'{Back.LIGHTRED_EX}Sai token vui lòng nhập lại')
                sleep(1)
                continue

    print('\n'+'--------------------------------------------------')
#Cấu hình
    while True:
        idtiktok=input(f'{Fore.LIGHTGREEN_EX}Nhập ID TIKTOK muốn cấu hình: {Fore.LIGHTBLUE_EX}')
      #  idtiktok='Dame Conghe✅'
        url='https://traodoisub.com/api/?fields=tiktok_run&id='+idtiktok+'&access_token='+token
#idfb='100063637627681'
    #url='https://traodoisub.com/api/?fields=run&id='+idfb+'&access_token='+token
        laydulieu=requests.get(url)
        data=laydulieu.json()
        success=data.get('success')
#print(data)
        if success==200:
            cauhinh=data.get('data').get('msg')
            idtt=data.get('data').get('uniqueID')
            idtk=data.get('data').get('id')
            ch=f"{Fore.LIGHTGREEN_EX}{cauhinh}"+"\n"
            for i in range(len(ch)+1):
                sys.stdout.write("\r" + ch[:i])
                sys.stdout.flush()
                sleep(0.02)
        #sleep(1)
            idz=f"{Fore.LIGHTGREEN_EX}ID: {Fore.LIGHTBLUE_EX}{idtk}"+"\n"
            for i in range(len(idz)+1):
                sys.stdout.write("\r" + idz[:i])
                sys.stdout.flush()
                sleep(0.02)
    #    sleep(1)
            idttz=f"{Fore.LIGHTGREEN_EX}Acc tiktok đang chạy: {Fore.LIGHTBLUE_EX}{idtt}"
            for i in range(len(idttz)+1):
                sys.stdout.write("\r" + idttz[:i])
                sys.stdout.flush()
                sleep(0.02)
        #    sleep(1)
            break
        else:
            print(f'{Back.LIGHTRED_EX}Tài khoản chưa được cấu hình hoặc không tồn tại')
            continue
    print("\n"+'--------------------------------------------------')
    kieujob=f"""{Fore.LIGHTGREEN_EX}Chọn kiểu cày xu:
[1]: {Fore.LIGHTBLUE_EX}Like{Fore.LIGHTGREEN_EX}
[2]: {Fore.LIGHTBLUE_EX}Follow
[3]: {Fore.LIGHTBLUE_EX}LIKE{Fore.LIGHTYELLOW_EX}(Dừng sau .... Job)
[4]: {Fore.LIGHTBLUE_EX}FOLLOW{Fore.LIGHTYELLOW_EX}(Dừng sau ... Job)"""
    ac=kieujob.split("\n")
    for abc in ac:
        for i in range(len(abc)+1):
                sys.stdout.write("\r" + abc[:i])
                sys.stdout.flush()
                sleep(0.02)
        print()
    sleep(1)
    while True:
        so=int(input(f"{Fore.LIGHTGREEN_EX}Nhập kiểu cày xu:{Fore.LIGHTBLUE_EX} "))
        if so ==2:
            pass
            break
        elif so==1:
            pass
            break
        elif so ==3:
            pass
            break
        elif so==4:
            pass
            break
        else:
            print(f'{Back.LIGHTRED_EX}HÃY NHẬP ĐÚNG NHIỆM VỤ')
            continue
    nhapdelay=int(input(f"{Fore.LIGHTGREEN_EX}Nhập delay sau mỗi lần nhận nhiệm vụ: {Fore.LIGHTBLUE_EX} "))
    maxnv=int(input(f"{Fore.LIGHTGREEN_EX}Nhận xu sau bao nhiêu nhiệm vụ [8-15] :{Fore.LIGHTBLUE_EX} "))
    print('--------------------------------------------------')
    batdau=0
    demso=1
    kolap=False
    if so==1:
        requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token='+token).json()
        print(f'{Back.LIGHTGREEN_EX}Khởi tạo nhiệm vụ LIKE')
#    flag=True
#Danh sách nv
        while True :
            
            while True :
                urllike = "https://traodoisub.com/api/?fields=tiktok_like&access_token="+token
                payload={}
                files={}
                headers = {}
                responelike = requests.request("GET", urllike, headers=headers, data=payload, files=files)
                getjoblike=responelike.json()
                if 'cache' in getjoblike:
                    items = getjoblike['data']
                    if not items:
                        print(f'{Fore.LIGHTRED_EX}Hết nhiệm vụ')   
                        sleep(10)
                    else:
                        for i in items:
                            if batdau<maxnv:
                                likejobid=i['id']
                                likejoblink=i['link']
                                match = re.search(r'@([^/]+)/video/', likejoblink)
                                if match:
                                    username = match.group(1)
                                    print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}{demso}{Fore.LIGHTYELLOW_EX}] {Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}♦️{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}{time} {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}LIKE {Fore.LIGHTMAGENTA_EX}♦️{Style.RESET_ALL} @{username}")
                                os.system(f'termux-open-url {likejoblink}')
                                for i in range(nhapdelay, -1, -1):
                                    dmng=str(i)
                                    print(f'{Fore.LIGHTGREEN_EX}Nhận JOB sau: {Back.LIGHTRED_EX}{dmng}',end='\r')
                                    sleep(1)
                                duyetxu=requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_CACHE&id='+likejobid+'&access_token='+token).json()
                                batdau +=1
                                demso+=1
                            elif batdau>=maxnv and not kolap:
                                kolap=True
                                nhanxu=requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token='+token).json()
                                if 'success' in nhanxu:
                                    xua=nhanxu['data']['xu']
                                    jobcsa=nhanxu['data']['job_success']
                                    nhanxua=nhanxu['data']['msg']
                                    print(f'{Fore.LIGHTCYAN_EX}Nhận thành công {jobcsa} nhiệm vụ {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}{nhanxua} {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{xua}')
                                    print('--------------------------------------------------')
                                batdau=0
                                kolap=False
                 
                elif 'fail_count' in getjoblike:
                    print(f'{Fore.LIGHTYELLOW_EX}Bạn đã bị block .\nĐừng lo,tình trạng này chỉ  xuất hiện trong thời gian ngắn.\nHãy chạy lại tool và chuyển sang job like .')
                    input('Nhấn bất kì để chạy tiếp hoặc CTRL+Z+ENTER để chạy lại tool')
                elif 'error' in getjoblike:
                    print('CÓ VẺ JOB LIKE SẮP HẾT')
    elif so==2:
  
      requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token='+token).json()
      print(f'{Back.LIGHTGREEN_EX}Khởi tạo nhiệm vụ FOLLOW')
      while True:
          while True:
              url = "https://traodoisub.com/api/?fields=tiktok_follow&access_token="+token
              payload={}
              files={}
              headers = {}
              respone = requests.request("GET", url, headers=headers, data=payload, files=files)
              getjobfollow=respone.json()
            # getjobfollow=requests.get('https://traodoisub.com/api/?fields=tiktok_follow&access_token='+token).json()
              if 'cache' in getjobfollow :
                  itemsf = getjobfollow['data']
                  if not itemsf:
                      print(f'{Fore.LIGHTRED_EX}HẾT NHIỆM VỤ')
                      break
                  else:
                      for il in itemsf:
                          if batdau<maxnv:
                              followjobid=il['id']
                              realid=il['real_id']
                              print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}{demso}{Fore.LIGHTYELLOW_EX}] {Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}♦️{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}{time} {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}FOLLOW {Fore.LIGHTMAGENTA_EX}♦️{Style.RESET_ALL} {realid}")
                              followjoblink=il['link']
                              os.system(f'termux-open-url {followjoblink}')
                              for i in range(nhapdelay, -1, -1):
                                  print(Fore.LIGHTGREEN_EX+'Nhận job sau: '+Back.LIGHTRED_EX+str(i),end='\r')
                                  sleep(1)
                              duyetxuf=requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id='+
                              followjobid+'&access_token='+token).json()
                              #print(duyetxuf)
                              demso+=1
                              batdau+=1
                          elif batdau>=maxnv and not kolap:
                              kolap=True
                              nhanxuf=requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token='+token).json()
                              #print(nhanxuf)
                              if "success" in nhanxuf:
                                  xufl=nhanxuf['data']['xu']
                                  jobflcs=nhanxuf["data"]['job_success']
                                  xuflthem=nhanxuf['data']['msg']
                                  print(f'{Fore.LIGHTCYAN_EX}Nhận thành công {jobflcs} nhiệm vụ {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}{xuflthem} {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{xufl}')
                                  print('--------------------------------------------------')
                              batdau=0
                              kolap=False
                              
              elif 'fail_count' in getjobfollow:
                  print(f'{Fore.LIGHTYELLOW_EX}Bạn đã bị block .\nĐừng lo,tình trạng này chỉ  xuất hiện trong thời gian ngắn.\nHãy chạy lại tool và chuyển sang job like .')
                  input('Nhấn bất kì để chạy tiếp hoặc CTRL+Z+ENTER để chạy lại tool')
              elif'error' in getjobfollow:
                  print("CÓ VẺ JOB FOLLOW SẮP HẾT")
    if so==3:
        maxjob=int(input(f'{Fore.LIGHTGREEN_EX}Nhập max job:{Fore.LIGHTBLUE_EX} '))
        print('--------------------------------------------------')
        requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token='+token).json()
        print(f'{Back.LIGHTGREEN_EX}Khởi tạo nhiệm vụ LIKE')
#    flag=True
#Danh sách nv
        run=True
        while run :
            urllike = "https://traodoisub.com/api/?fields=tiktok_like&access_token="+token
            payload={}
            files={}
            headers = {}
            responelike = requests.request("GET", urllike, headers=headers, data=payload, files=files)
            getjoblike=responelike.json()
            if 'cache' in getjoblike:
                items = getjoblike['data']
                if not items:
                    print(f'{Fore.LIGHTRED_EX}Hết nhiệm vụ')            
                    
                else:
                    for i in items:
                        if batdau<maxnv:
                            likejobid=i['id']
                            likejoblink=i['link']
                            match = re.search(r'@([^/]+)/video/', likejoblink)
                            if match:
                                username = match.group(1)
                                print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}{demso}{Fore.LIGHTYELLOW_EX}] {Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}♦️{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}{time} {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}LIKE {Fore.LIGHTMAGENTA_EX}♦️{Style.RESET_ALL} @{username}")
                            os.system(f'termux-open-url {likejoblink}')
                            for i in range(nhapdelay, -1, -1):
                                dmng = str(i)
                                sys.stdout.write(f'{Fore.LIGHTGREEN_EX}Nhận JOB sau: {Back.LIGHTRED_EX}{dmng}{Style.RESET_ALL}' + '\r')
                                sys.stdout.flush()
                                sleep(1)
    # Xóa dòng trước đó
                                sys.stdout.write(' ' * len(f'{Fore.LIGHTGREEN_EX}Nhận JOB sau: {Back.LIGHTRED_EX}{dmng}') + '\r')
                                sys.stdout.flush()
                          
                            duyetxu=requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_CACHE&id='+likejobid+'&access_token='+token).json()
                            batdau +=1
                            demso+=1
                            if demso== maxjob+1:
                                print(f'{Fore.LIGHTCYAN_EX}ĐÃ ĐẠT MAX JOB')
                                run=False
                                break
                        elif batdau>=maxnv and not kolap:
                            kolap=True
                            nhanxu=requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_LIKE&id=TIKTOK_LIKE_API&access_token='+token).json()
                            if 'success' in nhanxu:
                                xua=nhanxu['data']['xu']
                                jobcsa=nhanxu['data']['job_success']
                                nhanxua=nhanxu['data']['msg']
                                print(f'{Fore.LIGHTCYAN_EX}Nhận thành công {jobcsa} nhiệm vụ {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}{nhanxua} {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{xua}')
                                print('--------------------------------------------------')
                            batdau=0
                            kolap=False
                           
                 
            elif 'fail_count' in getjoblike:
                print(f'{Fore.LIGHTYELLOW_EX}Bạn đã bị block .\nĐừng lo,tình trạng này chỉ  xuất hiện trong thời gian ngắn.\nHãy chạy lại tool và chuyển sang job like .')
                input('Nhấn bất kì để chạy tiếp hoặc CTRL+Z+ENTER để chạy lại tool')
            elif 'error' in getjoblike:
                print('CÓ VẺ JOB LIKE SẮP HẾT')
    elif so==4:
      maxjob=int(input(f'{Fore.LIGHTGREEN_EX}Nhập max job:{Fore.LIGHTBLUE_EX} '))
      print('--------------------------------------------------')
      requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token='+token).json()
      run=True
      print(f'{Back.LIGHTGREEN_EX}Khởi tạo nhiệm vụ FOLLOW')
      while run:
              url = "https://traodoisub.com/api/?fields=tiktok_follow&access_token="+token
              payload={}
              files={}
              headers = {}
              respone = requests.request("GET", url, headers=headers, data=payload, files=files)
              getjobfollow=respone.json()
            # getjobfollow=requests.get('https://traodoisub.com/api/?fields=tiktok_follow&access_token='+token).json()
              if 'cache' in getjobfollow :
                  itemsf = getjobfollow['data']
                  if not itemsf:
                      print(f'{Fore.LIGHTRED_EX}HẾT NHIỆM VỤ')
              
                  else:
                      for il in itemsf:
                          if batdau<maxnv:
                              followjobid=il['id']
                              realid=il['real_id']
                              print(f"{Fore.LIGHTYELLOW_EX}[{Style.RESET_ALL}{demso}{Fore.LIGHTYELLOW_EX}] {Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}♦️{Style.RESET_ALL} {Fore.LIGHTCYAN_EX}{time} {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}FOLLOW {Fore.LIGHTMAGENTA_EX}♦️{Style.RESET_ALL} {realid}")
                              followjoblink=il['link']
                              os.system(f'termux-open-url {followjoblink}')
                              for i in range(nhapdelay, -1, -1):
                                dmng = str(i)
                                sys.stdout.write(f'{Fore.LIGHTGREEN_EX}Nhận JOB sau: {Back.LIGHTRED_EX}{dmng}{Style.RESET_ALL}' + '\r')
                                sys.stdout.flush()
                                sleep(1)
    # Xóa dòng trước đó
                                sys.stdout.write(' ' * len(f'{Fore.LIGHTGREEN_EX}Nhận JOB sau: {Back.LIGHTRED_EX}{dmng}') + '\r')
                                sys.stdout.flush()
                              duyetxuf=requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id='+
                              followjobid+'&access_token='+token).json()
                              #print(duyetxuf)
                              demso+=1
                              batdau+=1
                              if demso==maxjob+1:
                                  print(f'{Fore.LIGHTCYAN_EX}Đã ĐẠT MAX JOB')
                                  run=False
                                  break
                          elif batdau>=maxnv and not kolap:
                              kolap=True
                              nhanxuf=requests.post('https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token='+token).json()
                              #print(nhanxuf)
                              if "success" in nhanxuf:
                                  xufl=nhanxuf['data']['xu']
                                  jobflcs=nhanxuf["data"]['job_success']
                                  xuflthem=nhanxuf['data']['msg']
                                  print(f'{Fore.LIGHTCYAN_EX}Nhận thành công {jobflcs} nhiệm vụ {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTGREEN_EX}{xuflthem} {Fore.LIGHTMAGENTA_EX}♦️ {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{xufl}')
                                  print('--------------------------------------------------')
                              batdau=0
                              kolap=False
                              
              elif 'fail_count' in getjobfollow:
                  print(f'{Fore.LIGHTYELLOW_EX}Bạn đã bị block .\nĐừng lo,tình trạng này chỉ  xuất hiện trong thời gian ngắn.\nHãy chạy lại tool và chuyển sang job like .')
                  input('Nhấn bất kì để chạy tiếp hoặc CTRL+Z+ENTER để chạy lại tool')
              elif'error' in getjobfollow:
                  print("CÓ VẺ JOB FOLLOW SẮP HẾT")     
else:
    print("Version 1.1.0")
    newversion = 'https://ghichu.vn/pyamj'


    datanewversion= requests.get(newversion)

# Kiểm tra xem tải trang thành công hay không (HTTP status code 200 là thành công)
    if datanewversion.status_code == 200:
        # Parse nội dung HTML bằng BeautifulSoup
        boctach = BeautifulSoup(datanewversion.text, 'html.parser')
    
        # Tìm thẻ <textarea> bằng class 'content'
        trongdata = boctach.find('textarea', {'class': 'content'})
    
        # Lấy nội dung bên trong thẻ <textarea>
        if trongdata:
            inversionlink = trongdata.string.strip()  # Sử dụng .string để lấy nội dung và .strip() để loại bỏ khoảng trắng thừa
            print('-------------------------------------------------')
            inphienban=f'''
{Fore.LIGHTRED_EX}Tool đã có phiên bản mới.!!!!!!
{Fore.LIGHTCYAN_EX}Hãy xem video mới nhất trên kênh 
{Fore.LIGHTMAGENTA_EX}TikTok:{Fore.LIGHTBLUE_EX}Dame Conghe✅   {Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}YOUTUBE:{Fore.LIGHTBLUE_EX}Dame Conghe{Style.RESET_ALL} 
        {Fore.LIGHTMAGENTA_EX}Facebook:{Fore.LIGHTBLUE_EX}Dame Conghe
{Fore.LIGHTYELLOW_EX}{Back.LIGHTRED_EX}Hoặc{Style.RESET_ALL}{Fore.LIGHTYELLOW_EX} truy cập link dưới để trực tiếp lấy tool :
{Fore.LIGHTRED_EX}    <<♦️♦️ {Style.RESET_ALL}{inversionlink} {Fore.LIGHTRED_EX}♦️♦️>>'''
            animation = inphienban.split('\n')
    
            for aanimation in animation:
                for i in range(len(aanimation) + 1):   
                    sys.stdout.write("\r" + aanimation[:i])
                    sys.stdout.flush()
                    sleep(0.02)
                print() # xuống dòng sau mỗi dòng text
            print('-------------------------------------------------')
            inphienban1=f'''{Fore.LIGHTYELLOW_EX}•Xem video có tool mới nhất :
{Fore.LIGHTCYAN_EX}(+)Youtube:{Fore.LIGHTMAGENTA_EX}Nhập 1
{Fore.LIGHTCYAN_EX}(+)TikTok:{Fore.LIGHTMAGENTA_EX}Nhập 2
{Fore.LIGHTYELLOW_EX}•Bài viết fb có tool mới nhất:{Fore.LIGHTMAGENTA_EX}Nhập 3
{Fore.LIGHTYELLOW_EX}•Truy cập web lấy tool trực tiếp :{Fore.LIGHTMAGENTA_EX}Nhập 4'''
            animation1= inphienban1.split('\n')
    
            for aanimation1 in animation1:
                for i in range(len(aanimation) + 1):   
                    sys.stdout.write("\r" + aanimation1[:i])
                    sys.stdout.flush()
                    sleep(0.02)
                print() # xuống 
            print('-------------------------------------------------')
        truycaplink=int(input('Nhập lựa chọn của bạn: '))
        if truycaplink==4:
            os.system(f'termux-open-url {inversionlink}')
        elif truycaplink==1:
            vdyoutube=requests.get('https://ghichu.vn/pyamjfor')
            boctach1 = BeautifulSoup(vdyoutube.text, 'html.parser')
    
        # Tìm thẻ <textarea> bằng class 'content'
            trongdata1 = boctach1.find('textarea', {'class': 'content'})
        # Lấy nội dung bên trong thẻ <textarea>
            if trongdata1:
                linkyt = trongdata1.string.strip()  # Sử dụng
                os.system(f'termux-open-url {linkyt}')
        elif truycaplink==2:
            vdtiktok=requests.get('https://ghichu.vn/cYGzS')
            boctach2 = BeautifulSoup(vdtiktok.text, 'html.parser')
    
        # Tìm thẻ <textarea> bằng class 'content'
            trongdata2 = boctach2.find('textarea', {'class': 'content'})
        # Lấy nội dung bên trong thẻ <textarea>
            if trongdata2:
                linktt= trongdata2.string.strip()  # Sử dụng
                os.system(f'termux-open-url {linktt}')
        elif truycaplink==3:
            
            postfb=requests.get('https://ghichu.vn/54n6Z')
            boctach3 = BeautifulSoup(postfb.text, 'html.parser')
    
        # Tìm thẻ <textarea> bằng class 'content'
            trongdata3 = boctach3.find('textarea', {'class': 'content'})
        # Lấy nội dung bên trong thẻ <textarea>
            if trongdata3:
                linkfb= trongdata3.string.strip()  # Sử dụng
                os.system(f'termux-open-url {linkfb}')
        print('-------------------------------------------------')
    else:
        print('KIỂM TRA MẠNG CỦA BẠN')