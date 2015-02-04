import socket
import SocketOperation
import os

def Main():
    host='127.0.0.1'
    port=8002
    s=socket.socket()
    s.connect((host,port))
    print(s.recv(1024).decode()) #Option String Recieve
    option=input('> ')
    s.send(bytes(option,'utf-8')) #Option Send
    print('Hai Man Which File You Want To Send: ')
    print(os.listdir())
    l=input('> ')
    s.send(bytes(l,'utf-8')) #file name send
    so=SocketOperation.SocketOperation.SendFile(s,l)
    s.close()
"""        while x:
            x=z.read(1024)
            print('Reading...')
            s.send(x)"""

if __name__=='__main__':
    Main()
    
