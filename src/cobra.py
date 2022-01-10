
# imports
import os
from tdqm import trange

# define clear
clear = lambda: os.system("clear")


# web exploitation class
def web_exploit():
    # ddos
    def ping_flood(attack):
        os.system("ping "+ attack+"")
    
    # sql injection
    def sqlinject():
        # load
        for i in trange():
            os.system("pip3 install sqlmap")
        
        # start
        os.system("sqlmap --sqlmap-shell")
    
    def hackweb():
        # load
        for i in trange():
            os.system("pip3 install websploit")
        
        # start
        os.system("websploit")


# os exploitation class
def os_exploit():
    # windows passwd file
    def hackwin():
        os.system("cat \Windows\System32\config")
    
    # mac os passwd file
    def hackmac():
        os.system("cat /var/db/dslocal/nodes/Default/users")
    
    # linux passwd file
    def hacklin():
        os.system("cat /etc/passwd")
        os.system("cat /etc/shadow")
    
    # brute force attack
    def brute_force(username, wordlist, ip):
        # load
        for i in trange():
            os.system("sudo apt install hydra -y")
        
        # brute force   
        os.system("hydra -l "+ username+" -P "+ wordlist+" ssh://"+ ip+"")
        

# wifi exploit class
def wifi_exploit():
    # mitm
    def mitm():
        # load
        for i in trange():
            os.system("sudo apt instal wireshark -y")
       
        # start
        os.system("sudo wireshark")
    
    # hack wifi
    def hack_wifi():
        # load
        for i in trange():
            os.system("sudo apt install fern-wifi-cracker -y")
        
        # hack wifi
        os.system("fern-wifi-cracker")
    
    # scan
    def scan(nmap):
        # load
        for i in trange():
            os.system("sudo apt install nmap -y")
        
        # scan
        os.system("nmap "+ nmap+"")

# other tools
def tools():
    # metasploit
    def exploit():
        clear()
        os.system("msfconsole")
    
    # git
    def git(link):
        # clone link
        os.system("git clone "+ link)

    # hack phone
    def hackphone():
        # load
        for i in trange():
            os.system("sudo apt install scrcpy -y")
        
        # start
        os.system("scrcpy")
    
    # hack drone
    def hackdrone():
        # load
        for i in trange():
            os.system("pip3 install dronesploit")
        
        # start
        os.system("dronesploit")

print("its time to hack the world")
