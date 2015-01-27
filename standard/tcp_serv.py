import socket

def Main():
    host='127.0.0.1'
    port=7000
    s=socket.socket()
    s.bind((host,port))
    s.listen(1)
    connection,addr=s.accept()
    print('connectn from'+ str(addr))
    while True:
        data=connection.recv(1024).decode()
        if not data:
            break
        print('from user recievd'+str(data))
        data=str(data).upper()
        print('Sending'+str(data))
        connection.send(data.encode())
    connection.close()

if __name__=='__main__':
    Main()
