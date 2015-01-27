import socket

def Main():
    server='127.0.0.1'
    port=5000
    s=socket.socket()
    s.bind((server,port))
    s.listen(2)
    con,addr=s.accept()
    print('connecn from'+str(addr))
    while True:
        d=con.recv(1024).decode()
        print('data recieved was: '+str(d))
        x=input('Server Write.>').encode()
        con.send(x)
    s.close()

if __name__=='__main__':
    Main()
