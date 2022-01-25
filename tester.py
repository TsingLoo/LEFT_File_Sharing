import json
import queue
import sys
import time
import os
import threading
from socket import *
from multiprocessing import Manager
import argparse

# def _argparse():
#     parser = argparse.ArgumentParser(description="This is description!")
#     parser.add_argument('--peer_address',action ='store',required=True,dest = 'path',help = 'The address of peer computer')
#
# parser = _argparse()

peer_address = '192.168.3.11'

share_folder_path = os.path.join(os.getcwd(),'share')

new_file_detected_event = threading.Event()

change_file = None


def scanner():
    file_dict = {}
    while True:
        time.sleep(0.5)
        old_file_dict = file_dict.copy()
        file_dict = {}



        print(":::::::scan start:::::::")
        #single_folder_hash_combined = ""
        for root,dirs,files in os.walk(share_folder_path):


            # print(files)
            # print(type(files))
            # print(files[1])
            # print(type(files[1]))
            # print(type(root)) the tpye of root is str
            # get_md5(root)
            # print("-------- Here is the detailed information for "+ root + " --------")
            #single_file_hash_combined = ""
            for file in files:

                file_path = os.path.join(root, file).replace(os.getcwd(),'.') #str class
                fsize = os.path.getsize(file_path)

                update_time = os.path.getmtime(file_path) #float class
                file_mtime_size = (update_time,fsize,False) #tuple class

                file_dict[file_path]= file_mtime_size

                #extensions = os.path.splitext(file_path)[1]
                #print(extensions)
                #print("--------Here is the detailed information for--------")
                # print(file)
                # print(type(file))

            changed_file_path_list = []
            differ = set(file_dict.items()).difference(set(old_file_dict.items()))
            #differ = set(file_dict.items()) ^ set(old_file_dict.items()) #right hand side info is new; set class

        if(differ):
            for item in differ:
                changed_file_path_list.append(item[0])

            #print(changed_file_path_array)

            print("A change detected !")
            change_file_path_json = json.dumps(changed_file_path_list)    #str class
            change_file_path_json_encoded = change_file_path_json.encode()
            #change_file = change_file_path_json
            global change_file
            change_file =change_file_path_json_encoded
            print(change_file)
            # print(changed_file_path_array)
            new_file_detected_event.set()
        print(":::::::scan over :::::::")

def receiver():
    print("receiver acvated! ")
    server_name = peer_address
    server_port = 13000
    TCP_client_socket = socket(AF_INET,SOCK_STREAM)
    TCP_client_socket.connect((server_name,server_port))
    print("receiver acvated! ")

    change_file_receive = TCP_client_socket.recv(2048)
    change_file_path_list_receive = json.loads( change_file_receive.decode())
    print(change_file_path_list_receive)






def listener():

    global change_file
    new_file_detected_event.wait()
    #print(change_file)
    server_port = 13000
    TCP_server_socket = socket(AF_INET, SOCK_STREAM)
    TCP_server_socket.bind(('192.168.3.11',server_port))
    TCP_server_socket.listen(2)
    #TCP_server_socket.connect((peer_address,server_port))
    print("The listener activated!")

    while True:
        connection_socket,addr = TCP_server_socket.accept()
        connection_socket.send(change_file)
        new_file_list = connection_socket.recv(20480).decode()


if __name__ == "__main__":

    print(sys.platform)
    scanner_thread = threading.Thread(target = scanner,args=())
    receiver_thread = threading.Thread(target = receiver,args=())
    listener_thread = threading.Thread(target = listener,args=())
    scanner_thread.start()
    receiver_thread.start()
    listener_thread.start()