import socket,struct,threading,config

#sender.py aims to send files to given address and port

def sender_fun(peer_ip_address,file_to_be_sent): #True for type A: delete original file and update
                                                           #False for type B: recover

        file_name = file_to_be_sent[0]

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((peer_ip_address, config.port1))
        except Exception as e:
            config.peer_online = False

        #print(sock.connect_ex((peer_ip_address, 12000)))


        # 定义文件头信息；
        file_head = struct.pack('256sq?', file_name.encode(),file_to_be_sent[1][1],file_to_be_sent[1][2])


        try:
           sock.send(file_head)
        except:
            return 0

        received_size = int(sock.recv(2014).decode())

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

def call_sender(peer_ip_address,file_to_be_sent):
    sender_thread = threading.Thread(target = sender_fun,args=(peer_ip_address,file_to_be_sent,))
    sender_thread.start()

