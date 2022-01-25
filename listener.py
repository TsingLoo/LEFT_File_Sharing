import socket,threading,config

#listener.py helps host find and connect its peer online

#to find if there is a peer online connected to host
def listener_fun(peer_ip_address):
    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock0.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock0.bind(('', config.port0))
    sock0.listen(2)

    while True:
        connection,addr = sock0.accept()
        config.peer_online = True
        print("My peer connects me! He is" , peer_ip_address)
        config.old_file_dict = {}
        #sock0.close()

#call listener thread
def call_listener(peer_ip_address):
    listener_thread = threading.Thread(target=listener_fun, args=(peer_ip_address,))
    listener_thread.start()

