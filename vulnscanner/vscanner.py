import portscanner.portscanner as portscanner

# Prompt the user for target(hostname/IP:port limit(500 means first 500 ports))
target_host = input("Enter The Hostname/IP: ")
port_lmit = int(input("Enter Port Number(20 means forst 20 ports.): "))
vulnfile = input("Enter The Path For vulnarable software banner names. ")

target = portscanner.PortScan(target_host,port_lmit)
target.scan_target()

with open(vulnfile,'r') as file:
    count = 0
    for banner in target.output_banner:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print("\n")
                print('-----------------------------------------------------------------------------------')
                print(f"[!!] VULNERABLE SOFTWARE AT: PORT {target.output_port[count]} AND SERVICE {banner}")
                print('-----------------------------------------------------------------------------------')
        count+=1

    




