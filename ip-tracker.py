#!/usr/bin/python
# -*- coding: utf-8 -*-

#github.com/ALLENVIN
#DONT BE A COPY CAT 

#AUTHOR : ALLEN SMITH (ALLENVIN)
#OPEN SOURCE :)
#DON'T FORGET TO GIVE CREDIT TO THE AUTHOR

import requests,json,os
from requests import get
from os import system
from json import loads
import random
import sys
import time
import subprocess
import socket
try:
	import phonenumbers
except ImportError:
	os.system('pip install phonenumbers')
	time.sleep(0)
	try:
		import phonenumbers
	except ImportError:
		exit('Module phonenumbers not installed, Install Manually (pip install phonenumbers)')
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

#os.system('pip install phonenumbers')
#time.sleep(1)

#Colour
H = ('\x1b[1;90m')
R = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
G = ('\x1b[92;1m')


#REQUESTS
ip= requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
#loc1 = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['city'].upper()

#LOAD
def load():
    animation = "|/-\\"
    for i in range(100):
          time.sleep(0.1)
          sys.stdout.write("\r\x1b[1;91mLoading...\x1b[1;90m" + animation[i %        len(animation)])
          sys.stdout.flush()

#LOGO2
def logo2():
    print("\033[1;32m ═══════════════════════════════════════════════════════")
    print("""                      
___  ___      _             _     _     _               
|  \/  |     | |           | |   (_)   | |              
| .  . | ___ | |__    _ __ | |__  _ ___| |__   ___ _ __ 
| |\/| |/ _ \| '_ \  | '_ \| '_ \| / __| '_ \ / _ \ '__|
| |  | | (_) | |_) | | |_) | | | | \__ \ | | |  __/ |   
\_|  |_/\___/|_.__/  | .__/|_| |_|_|___/_| |_|\___|_|   
                     | |                                
                     |_|                                
   """)
    print("\033[1;32m ═══════════════════════════════════════════════════════")
 


def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.1)
system('clear')
load()
system("clear")

#LOGO
def logo():
   print("""\033[0;91m
	
 _____              _     _     _               
|_   _|            | |   (_)   | |              
  | | _ __    _ __ | |__  _ ___| |__   ___ _ __ 
  | || '_ \  | '_ \| '_ \| / __| '_ \ / _ \ '__|
 _| || |_) | | |_) | | | | \__ \ | | |  __/ |   
 \___/ .__/  | .__/|_| |_|_|___/_| |_|\___|_|   
     | |     | |                                
     |_|     |_|                              
\x1b[1;96m=======================================================\x1b[0;m""")

#BANNER
def mrxtop():
      print("""\x1b[92;1m
$$\      $$\ $$$$$$$\  $$\   $$\ 
$$$\    $$$ |$$  __$$\ $$ |  $$ |
$$$$\  $$$$ |$$ |  $$ |\$$\ $$  |
$$\$$\$$ $$ |$$$$$$$  | \$$$$  / 
$$ \$$$  $$ |$$  __$$<  $$  $$<  
$$ |\$  /$$ |$$ |  $$ |$$  /\$$\ 
$$ | \_/ $$ |$$ |  $$ |$$ /  $$ |
\__|     \__|\__|  \__|\__|  \__|                
\x1b[1;96m==========================================\x1b[0;m
\x1b[1;97m[+] 𝚃𝙾𝙾𝙻 𝙽𝙰𝙼𝙴 >> 🇽 𝙿𝙷𝙸𝚂𝙷𝙴𝚁\x1b[0;m
\x1b[1;97m[+] 𝙰𝚄𝚃𝙷𝙾𝚁 >> 𝙰𝙻𝙻𝙴𝙽 𝚂𝙼𝙸𝚃𝙷\x1b[0;m
\x1b[1;97m[+] 𝚆𝙷𝙰𝚃𝚂𝙰𝙿𝙿 >> +2348164404128\x1b[0;m
\x1b[1;97m[+] 𝙶𝙸𝚃𝙷𝚄𝙱 >> 𝙰𝙻𝙻𝙴𝙽𝚅𝙸𝙽\x1b[0;m
\x1b[1;96m==========================================\x1b[0;m""")
def inf():
      mengetik("\t\033[0;91m<<☠︎︎𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝙰𝙻𝙻𝙴𝙽'𝚂 𝚄𝙽𝙸𝚅𝙴𝚁𝚂𝙴☠︎︎>>!")
      mengetik("\t\033[0;91m    <<𝙽𝙾 𝙻𝙾𝙲𝙰𝚃𝙸𝙾𝙽 𝙸𝚂 𝙷𝙸𝙳𝙳𝙴𝙽>>\n\x1b[1;96m==========================================\x1b[0;m")


#URID
def urid():
     print("\t\033[93;1m     𝙷𝙴𝙻𝙻𝙾!   :     👋  \033[92;1m")
     print("\t\033[93;1m     𝚈𝙾𝚄𝚁 𝚁𝙴𝙶𝙸𝙾𝙽  : \033[92;1m" + loc )
     print("\t\033[93;1m     𝚈𝙾𝚄𝚁 𝙸𝙿 : \033[92;1m"  + ip + "\n\x1b[1;96m======================================================\x1b[0;m")


#MENU1
def menu1():
    print("\n\033[97;1m     ☠︎︎ SELECT SCAN METHOD ☠︎︎\x1b[0m")
    print("")
    print("\033[92;1m  [1] 𝙸𝙿 𝙿𝙷𝙸𝚂𝙷𝙴𝚁 ")
    print("\033[92;1m  [2] 𝙼𝙾𝙱 𝙿𝙷𝙸𝚂𝙷𝙴𝚁 ")
    print("\033[1;91m  [0] 𝙴𝚇𝙸𝚃\n")
    
#MENU2
def menu2():
    logo()
    urid()
    print("")
    print("\033[92;1m  [1] 𝚂𝚃𝙰𝚁𝚃 𝙵𝚄𝙻𝙻 𝚂𝙲𝙰𝙽")
    print("\033[93;1m  [2] 𝚂𝙲𝙰𝙽 𝚅𝙸𝙲𝚃𝙸𝙼 𝙲𝙾𝚄𝙽𝚃𝚁𝚈")
    print("\033[94;1m  [3] 𝚂𝙲𝙰𝙽 𝚅𝙸𝙲𝚃𝙸𝙼 𝚁𝙴𝙶𝙸𝙾𝙽")
    print("\033[96;1m  [4] 𝚂𝙲𝙰𝙽 𝚅𝙸𝙲𝚃𝙸𝙼 𝚃𝙸𝙼𝙴 𝚉𝙾𝙽𝙴")
    print("\033[96;1m  [5] 𝚂𝙲𝙰𝙽 𝚅𝙸𝙲𝚃𝙸𝙼 𝙸𝙽𝚃𝙴𝚁𝙽𝙴𝚃 𝙾𝙿𝙴𝚁𝙰𝚃𝙾𝚁")
    print("\033[97;1m  [6] 𝚂𝙲𝙰𝙽 𝚅𝙸𝙲𝚃𝙸𝙼 𝙲𝙸𝚃𝚈")
    print("\033[1;91m  [0] 𝙼𝙰𝙸𝙽 𝙼𝙴𝙽𝚄")
    print("")
os.system('xdg-open https://wa.me/+2348164404128?text=Hello%20Mr%20MRX%20Thanks%20For%20Premium%20Tool%20')
	

#-------01
def ip_scan():
       ip1 = input('\x1b[1;98m𝙴𝙽𝚃𝙴𝚁 𝙸𝙿 >> ')
       load()
       system('clear')
       print("\x1b[1;96m==========================================\x1b[0;m")
       print("\t👿🇮  🇵   🇪 🇽 🇵 🇴 🇸 🇪 🇩 👿")
       ip = get(f'http://ip-api.com/json/{ip1}')
       ip2 = loads(ip.text)
       if ip2 ["status"] == "success":
       	print ('status :',ip2["status"])
       	print ('Country :',ip2["country"])
       	print ('Country code :',ip2["countryCode"])
       	print ('Region Name :',ip2["regionName"])
     #  	print ('continent :',ip2["continent"])
    #   	print ('continentCode :',ip2["continentCode"])
       #	print ('district :',ip2["district"])
       	print ('zip :',ip2["zip"])
       	print ('lat :',ip2["lat"])
       	print ('lon :',ip2["lon"])
    #   	print ('offset :',ip2["offset"])
      # 	print ('currency :',ip2["currency"])
       	print ('org :',ip2["org"])
       	print ('as :',ip2["as"])
  #     	print ('asname :',ip2["asname"])
       #	print ('moblie :',ip2["moblie"])
  #     	print ('hosting :',ip2["hosting"])
       #	print ('geo :',ip2["geo"])
       #	print ('dns :',ip2["dns"])
   #    	print ('proxy :',ip2["proxy"])
       	print ('City :',ip2["city"])
       	print ('status :',ip2["status"])
       	print ('Time zone :',ip2["timezone"])
       	print ('Operator Internet :',ip2["isp"])
       	print ('Ip :',ip2["query"])
       	print("\x1b[1;96m==========================================\x1b[0;m")
       elif ip2["status"] == "fail":
       	mengetik('\x1b[0;91m\t[!] 𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝙸𝙿')
       retry = input("\n𝚂𝙲𝙰𝙽 𝙰𝙶𝙰𝙸𝙽 𝚢/𝚗 >> ")
       if retry == "y" or retry == "Y":
              system("clear")
              log_sel2()
       elif retry == "n" or retry == "N":
              system("clear")
              log_sel1()
      	
#------02
def ip_count():
       ip1 = input('\x1b[1;98m𝙴𝙽𝚃𝙴𝚁 𝙸𝙿 >>')
       load()
       system('clear')
       print("\x1b[1;96m==========================================\x1b[0;m")
       print("\t👿🇮 🇵   🇪 🇽 🇵 🇴 🇸 🇪 🇩 👿")
       ip = get(f'http://ip-api.com/json/{ip1}')
       ip2 = loads(ip.text)
       if ip2 ["status"] == "success":
       	print ('status :',ip2["status"])
       	print ('Country :',ip2["country"])
       	print("\x1b[1;96m==========================================\x1b[0;m")
       elif ip2["status"] == "fail":
       	mengetik('\x1b[0;91m\t[!] 𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝙸𝙿')
       retry = input("\n𝚂𝙲𝙰𝙽 𝙰𝙶𝙰𝙸𝙽 𝚢/𝚗 >> ")
       if retry == "y" or retry == "Y":
              system("clear")
              log_sel2()
       elif retry == "n" or retry == "N":
              system("clear")
              log_sel1()
       	
      	
      	
 #------03	
def ip_reg():
       ip1 = input('\x1b[1;98m𝙴𝙽𝚃𝙴𝚁 𝙸𝙿 >>')
       load()
       system('clear')
       print("\x1b[1;96m==========================================\x1b[0;m")
       print("\t👿🇮 🇵   🇪 🇽 🇵 🇴 🇸 🇪 🇩 👿")
       ip = get(f'http://ip-api.com/json/{ip1}')
       ip2 = loads(ip.text)
       if ip2 ["status"] == "success":
       	print ('status :',ip2["status"])
       	print ('Country :',ip2["country"])
       	print ('Region Name :',ip2["regionName"])
       	print("\x1b[1;96m==========================================\x1b[0;m")
       elif ip2["status"] == "fail":
        	mengetik('\x1b[0;91m\t[!] 𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝙸𝙿')
       retry = input("\n𝚂𝙲𝙰𝙽 𝙰𝙶𝙰𝙸𝙽 𝚢/𝚗 >> ")
       if retry == "y" or retry == "Y":
              system("clear")
              log_sel2()
       elif retry == "n" or retry == "N":
              system("clear")
              log_sel1()
        	
       	
       	
 #-------04
def ip_tzone():
       ip1 = input('\x1b[1;98m𝙴𝙽𝚃𝙴𝚁 𝙸𝙿 >>')
       load()
       system('clear')
       print("\x1b[1;96m==========================================\x1b[0;m")
       print("\t👿🇮 🇵   🇪 🇽 🇵 🇴 🇸 🇪 🇩 👿")
       ip = get(f'http://ip-api.com/json/{ip1}')
       ip2 = loads(ip.text)
       if ip2 ["status"] == "success":
       	print ('status :',ip2["status"])
       	print ('Country :',ip2["country"])
       	print ('Time zone :',ip2["timezone"])
       	print("\x1b[1;96m==========================================\x1b[0;m")
       elif ip2["status"] == "fail":
        	mengetik('\x1b[0;91m\t[!] 𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝙸𝙿')
       retry = input("\n𝚂𝙲𝙰𝙽 𝙰𝙶𝙰𝙸𝙽 𝚢/𝚗 >> ")
       if retry == "y" or retry == "Y":
              system("clear")
              log_sel2()
       elif retry == "n" or retry == "N":
              system("clear")
              log_sel1()
        	
       	
 #--------05
def ip_inop():
       ip1 = input('\x1b[1;98m𝙴𝙽𝚃𝙴𝚁 𝙸𝙿 >>')
       load()
       system('clear')
       print("\x1b[1;96m==========================================\x1b[0;m")
       print("\t👿🇮 🇵   🇪 🇽 🇵 🇴 🇸 🇪 🇩 👿")
       ip = get(f'http://ip-api.com/json/{ip1}')
       ip2 = loads(ip.text)
       if ip2 ["status"] == "success":
           print ('status :',ip2["status"])
           print('Country :',ip2["country"])
           print('Operator Internet :',ip2["isp"])
           print("\x1b[1;96m==========================================\x1b[0;m")
       elif ip2["status"] == "fail":
           mengetik('\x1b[0;91m\t[!] 𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝙸𝙿')
       retry = input("\n𝚂𝙲𝙰𝙽 𝙰𝙶𝙰𝙸𝙽 𝚢/𝚗 >> ")
       if retry == "y" or retry == "Y":
              system("clear")
              log_sel2()
       elif retry == "n" or retry == "N":
              system("clear")
              log_sel1()
           

 #-------06 
def ip_city():
       ip1 = input('\x1b[1;98m𝙴𝙽𝚃𝙴𝚁 𝙸𝙿 >>')
       load()
       system('clear')
       print("\x1b[1;96m==========================================\x1b[0;m")
       print("\t👿🇮 🇵   🇪 🇽 🇵 🇴 🇸 🇪 🇩 👿")
       ip = get(f'http://ip-api.com/json/{ip1}')
       ip2 = loads(ip.text)
       if ip2 ["status"] == "success":
       	print ('status :',ip2["status"])
       	print ('City :',ip2["city"])
       	print("\x1b[1;96m==========================================\x1b[0;m")
       elif ip2["status"] == "fail":
           mengetik('\x1b[0;91m\t[!] 𝙸𝙽𝚅𝙰𝙻𝙸𝙳 𝙸𝙿')
       retry = input("\n𝚂𝙲𝙰𝙽 𝙰𝙶𝙰𝙸𝙽 𝚢/𝚗 >> ")
       if retry == "y" or retry == "Y":
              system("clear")
              log_sel2()
       elif retry == "n" or retry == "N":
              system("clear")
              log_sel1()
                  
               
               
                                
#PHONE                                
def phone():
    logo2()
    urid()
    print("")
    mengetik("\x1b[1;91mNOTE: ENTER NO. WITH COUNTRY CODE\n\t\x1b[92;1me.g(+XXXXXXXXXXX)")
    print("\x1b[1;96m==========================================\x1b[0;m")
    mobileNo=input("\x1b[1;97mENTER MOBLIE NUMBER >> \x1b[92;1m")
    load()
    print("")
    print("\x1b[1;96m==========================================\x1b[0;m")
    print("\t👿🇲 🇴 🇧    🇪 🇽 🇵 🇴 🇸 🇪 🇩 👿")
    mobileNo=phonenumbers.parse(mobileNo)
    print(timezone.time_zones_for_number(mobileNo))
    print(carrier.name_for_number(mobileNo,"en"))
    print(geocoder.description_for_number(mobileNo,"en"))
    print("\x1b[92;1mValid Mobile Number:",phonenumbers.          is_valid_number(mobileNo))
    print("\x1b[92;1mChecking possibility of Number:",phonenumbers.is_possible_number(mobileNo))
    print("\x1b[1;96m==========================================\x1b[0;m")
    retry = input("\n𝚂𝙲𝙰𝙽 𝙰𝙶𝙰𝙸𝙽 𝚢/𝚗 >> ")
    if retry == "y" or retry == "Y":
          log_sel1()
    elif retry == "n" or retry == "N":
           system("clear")
           load()
           system("clear")
           log_sel1()


#LOG_SEL2           
def log_sel2():
	menu2()
	sel = input("\033[93;1m  CHOOSE: ")
	if sel == "":
		print("\t\033[91;1m  SELECT A VALID OPTION -_")
		time.sleep(0.5)
		system("clear")
		log_sel2()
	elif sel =="1" or sel =="01":
		system("clear")
		ip_scan()
	elif sel =="2" or sel =="02":
		system("clear")
		ip_count()
	elif sel =="3" or sel =="03":
		system("clear")
		ip_reg()
	elif sel =="4" or sel =="04":
		system("clear")
		ip_tzone()
	elif sel =="5" or sel =="05":
	    system("clear")
	    ip_inop()
	elif sel =="6" or sel =="06":
	    system("clear")
	    ip_city()
	elif sel =="0" or sel =="00":
		system("clear")
		log_sel1()
		load()
		sys.exit()
	else:
		print("")
		print("\033[91;1m  SELECT VALID OPTION")
		print("")
		system("clear")
		log_sel2()
		
		
#LOG_SEL1
def log_sel1():
	mrxtop()
	inf()
	menu1()
	sel = input("\033[93;1m  CHOOSE: ")
	if sel == "":
		print("\t\033[91;1m  SELECT A VALID OPTION -_")
		system("clear")
		log_sel1()
	elif sel =="1" or sel =="01":
		system("clear")
		log_sel2()
	elif sel =="2" or sel =="02":
		system("clear")
		phone()
	elif sel =="0" or sel =="00":
		system("clear")
		mengetik("\n\033[91;1m LOGING OUT OF ALLEN'S UNIVERSE :)")
		load()
		sys.exit()
		
log_sel1()
#coded by (ALLEN SMITH)
