import socket

def Main():
    servAddr='127.0.0.1'
    port=5000
    s=socket.socket()
    s.connect((servAddr,port))
    msg=input('.>')
    print('is it')
    while msg!='q':
        s.send(msg.encode())
        d=s.recv(1024).decode()
        print('server have responded:'+str(d))
        msg=input('.>')
    s.close()

if __name__=='__main__':
    Main()
