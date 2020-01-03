import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

target = input('Which Website to Scan: ')

print('first Checkpoint')

def port_scan(port):
    print('Second Checkpoint')
    try: 
        con = s.connect((target,port))
        return True
    except:
        return False

print('Checkpoint 3')


for x in range(1000):
    print('in the loop')
    if port_scan(x):
        print('Port ',x,' is open')
    
