"""Program Created By Vivek Sharma http://doyl.in"""

import socket

def Main():
    host='127.0.0.1'
    port=7000
    s=socket.socket()   #socket Created
    s.bind((host,port))  #Port Binded
    s.listen(1) # Waiting
    conn,addr=s.accept() #accept With Connection And Address
    print('connectn from'+ str(addr))
    c=conn.makefile('wb',0)
    d=conn.recv(1024)
    c.write(d)
    conn.close()

if __name__=='__main__':
    Main()
    
