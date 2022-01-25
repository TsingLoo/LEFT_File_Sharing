import argparse
#UDP Client side
from socket import *

parser = argparse.ArgumentParser(description="This is description!")
parser.add_argument('--ip', action='store', required=True, dest='ip', help='The ip of the address')
parser.add_argument('--port', action='store', required=True, dest='port', help='The port')
parser = parser.parse_args()
UDP_server_name = int(parser.ip)
UDP_server_port = int(parser.port)
UDP_client_socket = socket(AF_INET, SOCK_DGRAM)

print('The UDP Client is ready to send data')

message = open('xjtlu.jpg','rb')
image_data = message.read()
UDP_client_socket.sendto(image_data,(UDP_server_name,UDP_server_port))
print("Image xjtlu.jpg sented")

message , UDP_server_address = UDP_client_socket.recvfrom(20480)
f = open('xjtlu2.jpg', 'wb')
f.write(message)
f.close()
print('Image xjtlu2.jpg has been saved')

UDP_client_socket.close()