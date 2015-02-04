import socket
import sys

def Main():
    server='127.0.0.1'
    port=12000
    s=socket.socket()
    s.bind((server,port))
    s.listen(2)
    con,address=s.accept()
    con.send(bytes('What Do You Want To Do, Is It Upload "u" The File',\
                   'utf-8')) #Send Text
    k=con.recv(1024)
    if k==b'u':
        fn=con.recv(1024) #file name recv
        print('File About To Recieve: '+fn.decode())
        with open('New_'+str(fn.decode()),'wb') as z:
            r=con.recv(1024) #Recv Bytes
            while r!=b'':
                z.write(r)
                r=con.recv(1024)
                print('Recieving..')
    con.close()
"""        while r:
            z.write(r)
            r=con.recv(1024)
            print('Writing...')
    con.close()
    s.close()"""
"""    print('We Are Connected To: '+str(address))
    d=con.recv(1024) #Recieve File Name
    print('so this is the File '+str(d.decode()))
    k=open('file','wb')
    l=con.recv(2048)
    while l:
        print('Receiving...')
        k.write(l)
        l=con.recv(2048)
    k.close()
    con.close()
    s.close()"""


if __name__=='__main__':
    Main()
        
        
