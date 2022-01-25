import json
import queue
import time
import os
import threading
from socket import *
share_folder_path = os.path.join(os.getcwd(),'share')
print(os.getcwd())


def scanner_fun():

    print(share_folder_path)
    #new_file_detected_event = threading.Event()
    differ = {}

    file_dict = {}
    while True:
        time.sleep(0.5)
        old_file_dict = file_dict.copy()
        file_dict = {}

        print(share_folder_path)
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
            #new_file_detected_event.set()
        print(":::::::scan over :::::::")

def call_scanner():

    scanner_thread = threading.Thread(target = scanner_fun,args=())
    scanner_thread.start()

