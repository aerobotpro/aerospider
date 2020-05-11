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
vps
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
literally
anything
you
can
think
of
or
generate
"""

class toggle:
    def toggle(bol):
        if bol == True:
            char = str(Fore.GREEN + "ON" + Fore.WHITE)
        else:
            char = str(Fore.RED + "OFF" + Fore.WHITE)
        return char
    
    
def main():
    global aloca, ver, sound_is_on, check_host, host_info
    data = aloca
    last_login = "N/A"
    login_counter = "N/A"
    try:
        last_login = str(data['last_login'])
        login_counter = str(data['login_counter'])
    except:
        pass
    cont = True
    date = str(datetime.now())
    date = date.split()[0]
    session = data['session_id']
    #logins = data['login_counter']
    #last_login = data['last_login']
    ip = data['ip']
    announcement = data['announcement']
    print()
    print(Fore.BLUE)
    print(f"{Fore.GREEN} ╔═══════════════════════════════════════════════════════════════════════════════════╗")
    print(f"{Fore.GREEN} ║   {Fore.RESET}█████╗ ███████╗██████╗  ██████╗     ███████╗██████╗ ██╗██████╗ ███████╗██████╗  {Fore.GREEN}║")
    print(f"{Fore.GREEN} ║  {Fore.RESET}██╔══██╗██╔════╝██╔══██╗██╔═══██╗    ██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗ {Fore.GREEN}║")
    print(f"{Fore.GREEN} ║  {Fore.RESET}███████║█████╗  ██████╔╝██║   ██║    ███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝ {Fore.GREEN}║")
    print(f"{Fore.GREEN} ║  {Fore.RESET}██╔══██║██╔══╝  ██╔══██╗██║   ██║    ╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗ {Fore.GREEN}║")
    print(f"{Fore.GREEN} ║  {Fore.RESET}██║  ██║███████╗██║  ██║╚██████╔╝    ███████║██║     ██║██████╔╝███████╗██║  ██║ {Fore.GREEN}║")
    print(f"{Fore.GREEN} ║  {Fore.RESET}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ {Fore.GREEN}║")   
    print(f"{Fore.GREEN} ╚═══════════════════════════════════════════════════════════════════════════════════╝")
    print(f"{Fore.GREEN} ╔═══════════════════════════════════════════════════════════════════════════════════╗")
    #diff = 20 - len(user_key) - int(diff * "  ")
    print(f"{Fore.GREEN} ║ {Fore.WHITE}Update Version: [{ver}] | | Date: [{date}] | | User: [{user_key}]{Fore.GREEN} ")
    print(f"{Fore.GREEN} ╚═══════════════════════════════════════════════════════════════════════════════════╝")
    print()
    print(f"{Fore.YELLOW}Announcements:")
    print(f"{Fore.GREEN}{announcement}{Fore.WHITE}") 
    print('===>')
    print(f"{Fore.RESET}[Menu - Enter A Number]")
    print('[1] - Spider Search (Cloudflare Bypass)')
    print('[2] - Portscanner')
    print('[3] - Pinger')
    print('[4] - Lookup')
    print('[5] - Support Ticket')
    print('[6] - More Info')
    print('[7] - Settings')
    print('[8] - Update')
    print('-');print('-');print('-');print('-')
    menu = str(input('===>:'))


    if menu == "1":
        host = str(input("===> Enter A Domain To Begin Spidering:\n===>:"))
        print(Fore.RED + '==>' + Fore.GREEN + f'Spidering {host}...')
        print(Fore.YELLOW + '==>' + Fore.GREEN)
    #    sleep(.2);print("<-------------------|>\r", end="");sleep(.2);print("<-------------------\\>\r", end="");sleep(.2);print("<------------------_->\r", end="");sleep(.2);print("<----------------/--->\r", end="")
    #    sleep(.2);print("<--------------|----->\r", end="");sleep(.2);print("<------------\\------->\r", end="");sleep(.2);print("<----------_--------->\r", end="");sleep(.2);print("<-------/------------>\r", end="")
    #    sleep(.2);print("<----|--------------->\r", end="");sleep(.2);print("<---\\---------------->\r", end="");sleep(.2);print("<--_----------------->\r", end="");sleep(.2);print("<-/------------------>\r", end="")
    #    sleep(.2);print("<|------------------->\r", end="");sleep(.2);print("<\\------------------->\r", end="");sleep(.2);print("<_------------------->\r", end="");sleep(.2);print("</------------------->\r", end="")
    #    sleep(.2);print("<|------------------->\r", end="");sleep(.2);print("<\\------------------->\r", end="");sleep(.2);print("<_------------------->\r", end="");sleep(.2);print("</------------------->\r", end="")
    #    sleep(.2);print("<|------------------->\r", end="")
        print(Fore.GREEN + '==>')
        #for filename in glob.glob('*.txt'):
            #subdomainlist = open(filename).read().splitlines()
        subdomainlist = lists.domains.splitlines()
        for sublist in subdomainlist:
            try:
                r = requests.get(str(f'http://isitup.org/{host}.json'))
                json = r.json()
                domain = str(json['domain'])
                port = str(json['port'])
                status_code = str(json['status_code'])
                if status_code == "1":
                    status_code = Fore.GREEN + "Yes"
                else:
                    status_code = Fore.RED + "No"
                response = str(json['response_code'])
                timer = str(json['response_time'])
                hosts = str(sublist) + "." + str(host)
                showip = socket.gethostbyname(str(hosts))
                re=requests.get('https://json.geoiplookup.io/' + str(showip))
                dat = re.json();isp=dat['isp'];org=dat['org'];hostname=dat['hostname']
                if sound_is_on == True:
                    print('\a')#beep
                print(f"{Fore.WHITE}|| {Fore.GREEN}Connected: {Fore.WHITE}{str(showip)} {Fore.GREEN}--> {Fore.WHITE}{str(hosts)} {Fore.GREEN}<=== {Fore.WHITE}||")
                if host_info == True:
                    print(f"{Fore.WHITE}|| ISP: {Fore.YELLOW}{isp} {Fore.CYAN}- {Fore.WHITE}Org: {Fore.YELLOW}{org} {Fore.CYAN}- {Fore.WHITE}Hostname: {Fore.YELLOW}{hostname} {Fore.WHITE}||")
                if check_host == True:
                    print(f"{Fore.WHITE}|| [Probes] || ==> Reachable: {status_code}{Fore.WHITE} || Status Code: {Fore.GREEN}{response} {Fore.WHITE}|| Port Used: {Fore.GREEN}{port} {Fore.WHITE}|| Response Time: {Fore.GREEN}{timer} {Fore.BLUE}sec/s{Fore.WHITE} ||")
                print()
            except:
                        pass
        print(Fore.RESET)                
        done = input("==> \n\nDone!\nHit Enter To Restart Or CTRL+C To Exit!")
        init_()







    if menu == "2":
        this = input("Enter A Host To Scan:")
        #if sound_is_on == True:
        #    winsound.Beep(1024, 100)
        link = str('https://api.hackertarget.com/nmap/?q={}'.format(this))
        r = requests.get(link)
        leave = input(r.text + "\nHit Enter To Continue.")
        init_()






        
    if menu == "4":
        try:
            host = input("Enter an IP or Hostname:")
            #if sound_is_on == True:
             #   winsound.Beep(2096, 100)            
            re=requests.get('https://json.geoiplookup.io/' + host)
            data_=re.json();re_ip = data_['ip'];re_isp = data_['isp'];re_org = data_['org']
            re_hostname = data_['hostname'];re_city = data_['city'];re_country = data_['country_name']
            re_asn = data_['asn'];re_curr = data_['currency_code']
            print(Fore.WHITE + "\r", end="")
            print(f"""
\n
{Fore.GREEN}╔═══════════════════════════════════╗
{Fore.GREEN}║{Fore.YELLOW}IP:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{re_ip}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Hostname:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{re_hostname}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}ISP:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{re_isp}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}City:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{re_city}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Country:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{re_city}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Organization:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{re_org}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}ASN:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{re_asn}{Fore.WHITE}]
{Fore.GREEN}╚═══════════════════════════════════╝{Fore.WHITE}
""")
            poop = input("Hit Enter ==>")
        except:
            wa = input("Failed - Check your internet connection!")
            init_()
        init_()





        
            
    if menu == "5":
        message = input("Enter Your Message:")
        args = list(str(f'discord_client.exe --user 632636197784269758 **Message Received!** *Sent From Spider User:* `{user_key}` | | `{ip}` | | **Message:** `' + message + "`").split())
        print(Fore.RED);print('[\\\\\\\\\r', end="");sleep(.2);print('--------\r', end="");sleep(.2);print('////////\r', end="");sleep(.2);print('||||||||\r', end="");sleep(.2)
        print(Fore.YELLOW);print('[\\\\\\\\\r', end="");sleep(.2);print('--------\r', end="");sleep(.2);print('////////\r', end="");sleep(.2);print('||||||||\r', end="");sleep(.2)
        print(Fore.GREEN);print('[\\\\\\\\\r', end="");sleep(.2);print('--------\r', end="");sleep(.2);print('////////\r', end="");sleep(.2);print('||||||||\r', end="");sleep(.2)
        try:
            p = Popen(args, stdout=PIPE, stderr=STDOUT)
            sleep(3)
            os.kill(p.pid, signal.SIGTERM)
        except Exception as e:
            if debug == True:
                ee = input(str(e))
            print(f"Failed To Send! - [Make sure our discord_client is in the same folder and check internet connection] "+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            init_()
            
        print(Fore.WHITE + f"Your Message Has Been Sent! {Fore.WHITE}"+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r', end="");sleep(.5)
        print(Fore.RED + f"Your Message Has Been Sent! {Fore.WHITE}"+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r', end="");sleep(.5)
        print(Fore.CYAN + f"Your Message Has Been Sent! {Fore.WHITE}"+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r', end="");sleep(.5)
        print(Fore.BLUE + f"Your Message Has Been Sent! {Fore.WHITE}"+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r', end="");sleep(.5)
        print(Fore.GREEN + f"Your Message Has Been Sent! {Fore.WHITE}"+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r', end="");sleep(.5)
        print(Fore.YELLOW + f"Your Message Has Been Sent! {Fore.WHITE}"+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\r', end="");sleep(.5)
        init_()    







    if menu == "3":
        host = input('Enter a host to ping:')
        pinger(host, 10)
        init_()







        
    if menu == "6":
        print(f"""
\n\n\n\n\n\n
{Fore.GREEN}╔═══════════════════════════════════╗
{Fore.GREEN}║      {Fore.YELLOW} AeroSpider - Info {Fore.GREEN}          ║
{Fore.GREEN}╚═══════════════════════════════════╝
{Fore.GREEN}╔════════════════════════════════════
║{Fore.YELLOW}Update Version:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{ver}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Connected From:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{ip}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Current Session:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{session}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Date:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{date}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Proxies:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}None{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Total Logins:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{login_counter}{Fore.WHITE}]
{Fore.GREEN}║{Fore.YELLOW}Last Login:
{Fore.GREEN}║{Fore.WHITE}[{Fore.GREEN}{last_login}{Fore.WHITE}]
{Fore.GREEN}╚════════════════════════════════════{Fore.WHITE}



""")
        done = input("==> \n\nHit Enter ==>")
        init_()




        
    if menu == "7":
        print(f"""
{Fore.GREEN}╔════════════════════════════════════
{Fore.GREEN}║{Fore.WHITE}[1] {Fore.YELLOW}Toggle Sounds{Fore.GREEN} - {Fore.WHITE}[{toggle.toggle(sound_is_on)}]
{Fore.GREEN}║{Fore.WHITE}[2] {Fore.YELLOW}Activate Probes [When Spidering]{Fore.GREEN} - {Fore.WHITE}[{toggle.toggle(check_host)}]
{Fore.GREEN}║{Fore.WHITE}[3] {Fore.YELLOW}Show Host Info [When Spidering]{Fore.GREEN} - {Fore.WHITE}[{toggle.toggle(host_info)}]
{Fore.GREEN}║{Fore.WHITE}[Enter] {Fore.YELLOW}Back To Main {Fore.WHITE}<==
{Fore.GREEN}╚════════════════════════════════════{Fore.WHITE}
""")
        get = str(input('===>:'))
        if get == "1":
            sound_is_on = not sound_is_on
            print("Set!")
            
        if get == "2":
            check_host = not check_host
            print("Set!")

        if get == "3":
            host_info = not host_info
            print("Set!")
        if get == "4":
            pass
        init_()



        
    if menu == "8":
        thi = input("New Updates Coming Soon! | You will see new updates in ANNOUNCEMENTS!")
        init_()





        
    else:
        print(Fore.RED + "Invalid Selection!\r", end="");sleep(.5);print(Fore.WHITE + "Invalid Selection!\r", end="");sleep(.5)
        print(Fore.YELLOW + "Invalid Selection!\r" + Fore.WHITE, end="");sleep(.5)
        init_()



            
def pinger(host, range_):
    for x in range(0, 11):
        response = os.system("ping -n 1 " + host)
        print(Fore.YELLOW + f'\n\nProbe #{str(int(range_ - x))}' + Fore.WHITE)
        if response == 0:
            print(host, Fore.GREEN + """

            >>>>>>>is up! %^)
            
            """+ Fore.WHITE)    
        else:
            print(host, Fore.Red + """
            
            >>>>>>>is down! %^0
            
            """ + Fore.WHITE)
        sleep(1)    
            


def init_():
    main()    

class from_auth:
    def auth():
        global aloca, user_key
        init()
        ################## API
        print(Fore.YELLOW, end="")
        user = str(input(f'Enter Username:'))
        print(Fore.WHITE)

        ver = '1.0.0.1'
        try:
            host = socket.gethostname()
            client = str(socket.gethostbyaddr(host))
        except:
            client = "N/A"
        print("Connecting To Aero-Bot Services...")
        try:
            url = str(f'https://host-info.net/cdn/spider/api.php?user_key={user}&client={client}&update=1.0.0.0')
            if debug == True:
                print(f"URL USED: [{url}]")
            r = requests.get(url, allow_redirects=True)
            if debug == True:
                wait = input(r.text)    
            data = r.json()
            aloca = data
            user_key = user
            re = data['response']

            if re == "non_existing" and r.status_code == 200:
                done = input("==> \n\nUnknown username! Try again!\r")
                from_auth.auth()
            
            if re == "new" and r.status_code == 200:
                done = input("==> \n\nWelcome! Please Hit CTRL+C To Finish The Activation Process Then Restart!")
                exit(1)
                
            if re == "banned" and r.status_code == 200:
                done = input(Fore.RED + Back.WHITE+"==> \n\nYour client has been banned! Hit CTRL+C To Exit!")
                exit(1)
            
            if re == "ok" and r.status_code == 200:
                winsound.Beep(1024, 100)
                winsound.Beep(2048, 25)
                winsound.Beep(3049, 25)
                root = tkinter.Tk()
                root.withdraw()    
                messagebox.showinfo(f"Welcome {user_key}!","Logged in via host-info.net!")
                init_()
                
            if r.status_code == 300 or r.status_code == 301:
                open(str(data['update_file_name']), 'wb').write(r.content)
                
              
                
        except Exception as poo:
            print(str(poo))
            done = input("==> \n\nFatal API Error! Hit CTRL+C To Exit!")
            exit(1)
########################################        
from_auth.auth()     

   
