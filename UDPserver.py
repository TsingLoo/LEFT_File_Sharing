#UDP Server side

from socket import  *

server_port = 12000
UDP_server_socket = socket(AF_INET, SOCK_DGRAM)
UDP_server_socket.bind(('', server_port)) #'' represents INADDR_ANY, which is used to bind to all interfaces

print('The UDP Server is ready to receive data')

while True:
    message, UDP_clinet_address  = UDP_server_socket.recvfrom(20480)
    f = open('xjtlu1.jpg', 'wb')
    f.write(message)
    f.close()
    print('Image xjtlu1.jpg has been saved')

    message = open('xjtlu1.jpg', 'rb')
    image_data = message.read()
    UDP_server_socket.sendto(image_data, UDP_clinet_address)
    print("Image xjtlu1.jpg sented")

    break

UDP_server_socket.close()
