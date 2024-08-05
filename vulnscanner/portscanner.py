import socket
from IPy import IP

class PortScan:

    output_port = []
    output_banner = []

    def __init__(self, target_ip, port_limit):
        self.target_ip = target_ip
        self.port_limit = port_limit
    
    def analyse_target(self):
        try:
            IP(self.target_ip)
            return self.target_ip
        except ValueError:
            return socket.gethostbyname(self.target_ip)

    def scan_target(self):
        self.scanner(self.analyse_target())

    def scanner(self,ip):
        for port in range(self.port_limit+1):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.5)
            try:
                sock.connect((ip, port))
                try:
                    banner=sock.recv(1024)
                    self.output_port.append(port)
                    self.output_banner.append(banner.decode().strip('\r\n'))
                except:
                    self.output_port.append(port)
                    self.output_banner.append("null")
                finally:
                    sock.close()
            except:
                pass

