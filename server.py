import os;
import time

UbuntuAddress = "192.168.3.61"
WinAddress = "192.168.3.11"

ShareFolderPath = "d:\\share\\"

while True:
    time.sleep(0.5)
    for root,dirs,files in os.walk(ShareFolderPath):
      print("--------"+ShareFolderPath+"--------")
      print(files)
      print(type(files))
      print(files[1])
      print(type(files[1]))
      print("--------Here is the detailed information for--------")
      for file in files:
       #print("--------Here is the detailed information for--------")
       print(file)
       print(type(file))
# Server side
from socket import *
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(2)
print('The TCP is ready to receive')

while True:
    connectionSocket, addr = server_socket.accept()
    print('Message From: ')
    print(addr)
    sentence = connectionSocket.recv(20480).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    print(capitalizedSentence)
connectionSocket.close()