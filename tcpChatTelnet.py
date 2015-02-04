import socket

def Main():
    server='192.168.0.100'
    port=7000
    s=socket.socket()
    s.bind((server,port))
    s.listen(4)
    con,addr=s.accept() # this is cool program Where You can chat with anyone Who have telnet
    print('Connection from'+str(addr))
    con.send(b'You Are Now Connected To '+ server.encode()) # Check out Standard tcp_client.py For Comments N' Understanding
    con.send(b'\n Say >.')
    d=con.recv(1024)
    while d!=b'q\r\n' or 'q':
        print('{0} Said:'.format(addr)+d.decode())
        x=input('Say >. ')
        con.send(b'\n')
        con.send(bytes(server+' Says >. '+x,'utf-8'))
        con.send(b'\n Say Something: ')
        d=con.recv(1024)
    s.close()

if __name__=='__main__':
    Main()
