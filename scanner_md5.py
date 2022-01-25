import os
import time
import hashlib
from socket import *

file_dict = {}
single_file_hash_combined = ""
single_folder_hash_combined = ""

def get_bytes_md5(filename):            #feed a string,return a md5 hash
    md5 = hashlib.md5()
    md5.update(filename) # an argument in bytes type is required by update
    value = md5.hexdigest()
    #print(value)
    return  value

def get_string_md5(string): #feed a string,return a md5
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8')) # an argument in bytes type is required by update
    value = md5.hexdigest()
    #print(value)
    return  value

UbuntuAddress = "192.168.3.61"
WinAddress = "192.168.3.11"


ShareFolderPath = "d:\\share\\"


while True:
    time.sleep(0.5)
    print(":::::::scan start:::::::")
    single_folder_hash_combined = ""
    for root,dirs,files in os.walk(ShareFolderPath):

      # print(files)
      # print(type(files))
      # print(files[1])
      # print(type(files[1]))
      # print(type(root))  the tpye of root is str
      # get_md5(root)
        print("-------- Here is the detailed information for "+ root + " --------")
        single_file_hash_combined = ""
        for file in files:
            file_path  = os.path.join(root, file)
            f = open(file_path,'rb')
            single_file_hash = get_bytes_md5(f.read())
            f.close()
            single_file_hash_combined = single_file_hash_combined + single_file_hash
            #extensions = os.path.splitext(file_path)[1]
            #print(file_path)
            #print(extensions)
        #print("--------Here is the detailed information for--------")
        # print(file)
        # print(type(file))
        single_folder_hash = get_string_md5(single_file_hash_combined)
        single_folder_hash_combined = single_folder_hash_combined + single_folder_hash
        share_hash = get_string_md5(single_folder_hash_combined)
        print("the hash for this folder is " + single_folder_hash)
    print("the hash for share folder" + ShareFolderPath  +" is " + share_hash)
    print(":::::::scan over:::::::")
    print()



from socket import *
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(2)
print('The TCP based program is now running')

while True:
    connectionSocket, addr = server_socket.accept()
    print('Message From: ')
    print(addr)
    sentence = connectionSocket.recv(20480).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    print(capitalizedSentence)
connectionSocket.close()