import socket
conn = socket.socket()
print('The Socket has been succesfully created')
conn.bind(('localhost',8888))

conn.listen(3)
print('waiting for connections')

while True:
    socket_conn,host=conn.accept()
    name =socket_conn.recv(1001).decode()
    print("Client is succesfully connected", host,name)
    socket_conn.send(bytes("Remote server active",'utf-8'))
    socket_conn.close()
