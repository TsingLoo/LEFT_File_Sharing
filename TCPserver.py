# TCP Server side
from socket import *
server_port = 12000
TCP_server_socket = socket(AF_INET, SOCK_STREAM)
TCP_server_socket.bind(('', server_port))
TCP_server_socket.listen(2)
print('The TCP server is ready to receive data')

while True:
    connectionSocket, addr = TCP_server_socket.accept()

    image_data = connectionSocket.recv(20480)
    f = open('xjtlu1.jpg','wb')
    f.write(image_data)
    f.close()
    print('Image xjtlu1.jpg has been saved')

    message = open('xjtlu1.jpg', 'rb')
    image_data = message.read()
    connectionSocket.send(image_data)
    print("Image xjtlu1.jpg sented")

    break

connectionSocket.close()
TCP_server_socket.close()
