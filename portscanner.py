import socket
#import threading
from IPy import IP

def scan_target(host, port_max):
    host_IP = get_IP(host)
    print(f"[-_-] Scanning target at {host_IP}")
    for port in range(int(port_max)+1):
        scanner(host_IP,port)

def get_IP(hostname):
    try:
        ip = IP(hostname)
        return(ip)
    except:
        return socket.gethostbyname(hostname)


def scanner(ipaddr,port_num):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1.0)
    try:
        sock.connect((ipaddr,port_num))
        try:
            banner = sock.recv(1024)
            print(f"[+] Port {port_num} is open : " + str(banner.decode()))
        except:
            print(f"[+] Port {port_num} is open")
    except:
        pass
        #print(f"[-] Port {port_num} is closed")

if __name__=="__main__":
    targets = input("Enter target/s(seperated by \',\'): \n")
    port_limit = input("Enter port: \n")
    if ',' in targets:
        for target in targets.split(','):
            scan_target(target.strip(' '), port_limit)
    else:
        scan_target(targets, port_limit)


