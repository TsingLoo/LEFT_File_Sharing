import socket
import struct
import sys
import os
import time

if __name__ == '__main__':

    file_name = '.\\share\\Total.pdf'

    #print(socket.gethostname())
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.3.61', 12000))

    # 定义文件头信息；
    print(os.stat(file_name).st_size)

    file_head = struct.pack('128sq', os.path.basename(file_name).encode(),
                            os.stat(file_name).st_size)


    sock.send(file_head)
   # print(struct.unpack('256sl',file_head))

    received_size = int(sock.recv(2014).decode())
   # print(received_size)
    read_file = open(file_name, "rb")
    read_file.seek(received_size)
    while True:
        # time.sleep(1)
        file_data = read_file.read(131072)

        if not file_data:
            break

        sock.send(file_data)

    read_file.close()
    sock.close()

