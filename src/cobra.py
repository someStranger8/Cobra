import os
def hackwin():
    os.system("cat \Windows\System32\config")
def hackmac():
    os.system("cat /var/db/dslocal/nodes/Default/users")
def hacklin():
    os.system("cat /etc/passwd")
    os.system("cat /etc/shadow")
def ddos():
    ddos=input("[*] enter ip or URL: ")
    os.system("ping "+ ddos+"")
def sqlinject():
    os.system("pip3 install sqlmap")
    clear()
    os.system("sqlmap --sqlmap-shell")
def exploit():
    clear()
    os.system("msfconsole")
def shell():
    i=1
    while i < 10:
        dodo=input("root@kali:~# ")
        os.system(dodo)
    i+=1
def hackwifi():
    os.system("apt install fern-wifi-cracker -y")
    clear()
    os.system("fern-wifi-cracker")
def hackpasswd():
    email=input("[*] enter email: ")
    os.system("pip3 install h8mail")
    clear()
    os.system("h8mail -t "+ email+"")
def clear():
    os.system("clear")
def mitm():
    os.system("apt instal wireshark -y")
    clear()
    os.system("sudo wireshark")
def scan():
    nmap=input("[*] enter ip or URL: ")
    os.system("apt install nmap -y")
    clear()
    os.system("nmap "+ nmap+"")
def hackweb():
    os.system("pip3 install websploit")
    clear()
    os.system("websploit")
def hackphone():
    os.system("apt install scrcpy -y")
    clear()
    os.system("scrcpy")
def hackdrone():
    os.system("pip3 install dronesploit")
    clear()
    os.system("dronesploit")
print("its time to hack the world")
