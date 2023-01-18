import socket
socket_conn = socket.socket()
socket_conn.connect(('localhost',8888))
name = input("Key in a name: ")
socket_conn.send(bytes(name,'utf-8'))
print(socket_conn.recv(1001).decode())
