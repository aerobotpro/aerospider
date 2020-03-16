import socket, requests
from time import sleep
import glob, os
import signal
from colorama import Fore, Back, Style, init
from datetime import datetime
from tkinter import messagebox
import tkinter
import winsound
from subprocess import run, PIPE, STDOUT, Popen
sound_is_on = False
check_host = True
host_info = True
debug = False
aloca = {}
user_key = str()
ver = "1.0.0.1"
class lists:
    domains = """
ftp
cpanel
webmail
mail
www
www1
www2
www3
www4
www5
ns1
ns2
forums
blog
mx
bbs
ww42
support
host
portal
test
shop
mail2
vpn
secure
smtp
remote
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
00
exchange
public
private
cloud
1
2
phpmyadmin
php
admin
owa
gw
store
2tty
gov
vps
govyty
hgfgdf
news
1rer
lkjkui
root
user
stealth
group
dev
dl
cdn
api
auth
visitor
user
server
hosting
alpha
beta
delta
charlie
foxtrot
gamma
shield
net
mitigation
security
employee
staff
management
classified
teamspeak
mil
payment
source
panel
dashboard
null
space
it
supply
utilities
watchdog
netcl
cli
client
json
xml
ssh
http
httpd
apache
nginx
akamai
ovh
nfo
nfoserver
balancer
balance
switch
"""
print("{Fore.GREEN} ╔═══════════════════════════════════════════════════════════════════════════════════╗")
print("{Fore.GREEN} ║   {Fore.RESET}█████╗ ███████╗██████╗  ██████╗     ███████╗██████╗ ██╗██████╗ ███████╗██████╗  {Fore.GREEN}║")
print("{Fore.GREEN} ║  {Fore.RESET}██╔══██╗██╔════╝██╔══██╗██╔═══██╗    ██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗ {Fore.GREEN}║")
print("{Fore.GREEN} ║  {Fore.RESET}███████║█████╗  ██████╔╝██║   ██║    ███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝ {Fore.GREEN}║")
print("{Fore.GREEN} ║  {Fore.RESET}██╔══██║██╔══╝  ██╔══██╗██║   ██║    ╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗ {Fore.GREEN}║")
print("{Fore.GREEN} ║  {Fore.RESET}██║  ██║███████╗██║  ██║╚██████╔╝    ███████║██║     ██║██████╔╝███████╗██║  ██║ {Fore.GREEN}║")
print("{Fore.GREEN} ║  {Fore.RESET}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ {Fore.GREEN}║")   
print("{Fore.GREEN} ╚═══════════════════════════════════════════════════════════════════════════════════╝")
subdomainlist = lists.domains.splitlines()
for sublist in subdomainlist:
    try:
        #r = requests.get(str(f'http://isitup.org/{host}.json'))
        #json = r.json()
       # domain = str(json['domain'])
       # port = str(json['port'])
        #status_code = str(json['status_code'])
        #if status_code == "1":
        #    status_code = Fore.GREEN + "Yes"
       # else:
        #    status_code = Fore.RED + "No"
        response = str(json['response_code'])
        timer = str(json['response_time'])
        hosts = str(sublist) + "." + str(host)
        showip = socket.gethostbyname(str(hosts))
        re=requests.get('https://json.geoiplookup.io/' + str(showip))
        dat = re.json();isp=dat['isp'];org=dat['org'];hostname=dat['hostname']

        print('\a')#beep
        print(f"{Fore.WHITE}|| {Fore.GREEN}Connected: {Fore.WHITE}{str(showip)} {Fore.GREEN}--> {Fore.WHITE}{str(hosts)} {Fore.GREEN}<=== {Fore.WHITE}||")

            print(f"{Fore.WHITE}|| ISP: {Fore.YELLOW}{isp} {Fore.CYAN}- {Fore.WHITE}Org: {Fore.YELLOW}{org} {Fore.CYAN}- {Fore.WHITE}Hostname: {Fore.YELLOW}{hostname} {Fore.WHITE}||")
        if check_host == True:
            print(f"{Fore.WHITE}|| [Probes] || ==> Reachable: {status_code}{Fore.WHITE} || Status Code: {Fore.GREEN}{response} {Fore.WHITE}|| Port Used: {Fore.GREEN}{port} {Fore.WHITE}|| Response Time: {Fore.GREEN}{timer} {Fore.BLUE}sec/s{Fore.WHITE} ||")
        print()
    except:
                pass
print(Fore.RESET)                
done = input("==> \n\nDone!\nHit Enter To Restart Or CTRL+C To Exit!")


   
