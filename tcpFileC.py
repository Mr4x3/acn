import socket
import os
def Main():
    servAddr='127.0.0.1'
    port=6000
    s=socket.socket()
    s.connect((servAddr,port))
    print(os.listdir())
    msg=input('Write File Name')
    s.send(msg.encode())
    d=s.recv(1024).decode()
    print(d)
    l=[]
    k=''
    for i in open(msg):
        k=k+i
    print(k)
    s.send(k.encode())
    s.close()

if __name__=='__main__':
    Main()
