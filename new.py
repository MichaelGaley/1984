import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

s.connect((host, port))
print("[CONNECTION ESSTABLLISHED]")

msg = s.recv(1024)
print("[CONNECTION COMPLETE!!!!]")

s.close()
print(msg.decode('ascii'))
