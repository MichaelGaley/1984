import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname('192.168.1.73')
port = 9999

serversocket.bind((host, port))
print("[STARTING SERVICES....]")

serversocket.listen(5)
print("[WAITING ON CONNECTION....]")

while True:
    clientsocket, address = serversocket.accept()
    print("GOT CONNECTION FROM %s" % str(address))

    msg = 'Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()