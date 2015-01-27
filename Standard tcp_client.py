"""Program Created By Vivek Sharma http://doyl.in"""

import socket

def Main():
    host='127.0.0.1'
    port=7000
    s=socket.socket()
    s.connect((host,port))

    message=input('.>')
    while message!='q':
        s.send(message.encode()) #Message Send By Turning To Stream
        data=s.recv(1024).decode() #Stream Recv
        print('recieved from server:'+str(data))
        message=input('.>')
    s.close()

if __name__=='__main__':
    Main()
