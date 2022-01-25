# TCP Client side
from socket import *

from client import modifiedSentence

serverName = '192.168.3.61'
serverPort = 12000
TCP_client_socket = socket(AF_INET, SOCK_STREAM)
TCP_client_socket.connect((serverName, serverPort))

#print('The TCP client is ready to send data')
modifiedSentence = TCP_client_socket.recv(20480)
print('From Server;',modifiedSentence.decode())
#TCP_client_socket.close()

# message = open('xjtlu.jpg','rb')
# image_data = message.read()
# TCP_client_socket.send(image_data)
# print("Image xjtlu.jpg sented")
#
# image_data = TCP_client_socket.recv(20480)
# f = open('xjtlu2.jpg', 'wb')
# f.write(image_data)
# f.close()
# print('Image xjtlu2.jpg has been saved')

