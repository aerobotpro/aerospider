#updater needs to packaged into 'updater.exe' Use bat file
import requests
from time import sleep
import os.path
from os import path, remove, rename, getcwd
import urllib.request


#Current filenames
main = "aero_spider.exe"
update = "update.exe"

def animation():
    print("Checking For Updates...\\\\\\\\\r", end="")
    sleep(.5)
    print("Checking For Updates...||||\r", end="")
    sleep(.5)
    print("Checking For Updates...////\r", end="")
    sleep(.5)
    print("Checking For Updates...----\r", end="")
    sleep(.5)
animation()
def download():
    final = 1
    with open("update.exe", 'wb') as handle:
        response = requests.get("https://host-info.net/cdn/spider/update/update.exe", stream=True)
        if not response.ok:
            bye = input("Failed To Download Update!!! Hit Enter To Exit And Try Again!\r", end="")
            exit(0)

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
        final = 0
    return final

animation()
if download() == 0:
    if path.exists('update.exe') == True:
        try:
            animation()
            remove(str(getcwd())+"/aero_spider.exe")
        except:
            print("Oops! I couldn't clean up old file!\r",end="")
        try:
            rename('update.exe', 'aero_spider.exe')
        except:
            print("Oops! I couldn't rename the new file!\r",end="")
        exits = input("Updated Successfully!!!! ~Press Enter To Exit Updater!\r")
elif path.exists(file_name) == False:
    exits = input("Failed To Update! Contact Developer! ~Press Enter To Exit Updater!\r")            
            
