"""Program Created By Vivek Sharma http://doyl.in"""

import socket

def Main():
    host='127.0.0.1'
    port=7000
    s=socket.socket()   #socket Created
    s.bind((host,port))  #Port Binded
    s.listen(1) # Waiting
    connection,addr=s.accept() #accept With Connection And Address
    print('connectn from'+ str(addr))
    while True:
        data=connection.recv(1024).decode() # Recv Data Over Connection
        if not data:
            break
        print('From User Recievd'+str(data))
        data=str(data).upper()
        print('Sending: '+str(data))
        connection.send(data.encode()) #Sending Data
    connection.close()

if __name__=='__main__':
    Main()
