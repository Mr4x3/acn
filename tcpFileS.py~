import socket
import os

def Main():
    server='127.0.0.1'
    port=6000
    s=socket.socket()
    s.bind((server,port))
    s.listen(2)
    con,addr=s.accept()
    print('connecn from'+str(addr))
    d=con.recv(1024).decode()
    print('Name Of File About To Recieve: '+str(d))
    l='Now Start Transection Of File'
    con.send(l.encode())
    k=con.recv(10240).decode()
    r=open('kl','w')
    r.write(k)
    r.close()
        
    s.close()
    print('Written Bro')

if __name__=='__main__':
    Main()
