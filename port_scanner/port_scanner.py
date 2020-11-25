import socket
import colorama
from colorama import Fore, Style

target = input("Enter IP adress to scan: ")

def port_scanner(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False

for port in range(1,1024):
    result = port_scanner(port)
    if result:
        print(f"{Fore.GREEN}Port {port} is open!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Port {port} is closed.{Style.RESET_ALL}")