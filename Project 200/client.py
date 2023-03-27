import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

while True:
    data = client.recv(1024)
    if not data:
        break
    print('Q.   ', data.decode('utf-8'))
    
    # Take input from user
    message = input('>> ')
    
    # Send message to server
    client.send(message.encode('utf-8'))

client.close()
