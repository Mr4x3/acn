""" Module Created By Vivek Sharma (http://doyl.in)For Simplified TCP Operations"""
#!/usr/bin/python

import socket
class SocketOperation:

    def __init__(self,address):
        self.s=socket.socket()
        self.s.bind(address)
        self.s.listen(2)
    def mirror(self,s):
        if s[-1]!='\n':
            s+='\r\n'
    def GetFile(self,connection,filename): #Recv Stream From SendFile And Convert To File
        print('File You Are About To Recv:',filename)
        with open('New_'+str(filename),'wb') as z:
            r=connection.recv(1024) #Recv Bytes
            while r!=b'': #check For Binary End Of File
                z.write(r)
                r=connection.recv(1024)
                print('Rececing...')
    def SendFile(socket,filename):  #Stream The File (Throwing)
        with open(filename,'rb') as z:
            x=z.read(1024) #Read File With 1024 B
            while x!=b'':
                s.send(x)
                x=z.read(1024)
                print('Sending {0}..'.format(filename))
