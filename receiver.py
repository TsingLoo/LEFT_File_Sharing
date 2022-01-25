import socket,threading,os,struct,time,shutil,config

#receiver.py firstly saves the coming file in 'temp_file' folder,after the transmitting is finished, the saved file will be moved to share folder

def receiver_fun(connection):

        #file_info_size = struct.calcsize('256sq?') = 265
        buf = connection.recv(265)

        if buf:
            #unpack the file information
            file_path_name, file_size, receive_type = struct.unpack('256sq?', buf)
            file_path_name = file_path_name.decode().strip('\00')

            #call switch_path() method to help support Win and Linux better
            file_path_name = switch_path(file_path_name)
            (hierarchy,file_basename) = os.path.split(file_path_name)

            #if the receive_type is A, then the exsisting file in share folder will be deleted and retransmitted
            if (receive_type):
                os.remove(file_path_name)


            #to recover the hierarchy of oringinal folder
            if not os.path.exists(hierarchy):
                os.makedirs(hierarchy)

            #the temp file path in 'temp_share' folder
            file_new_name = os.path.join('temp_share', file_basename)
            #the final file path in share folder
            file_final = os.path.join(hierarchy,file_basename)

            #reset the received_size
            received_size = 0

            #if the receive_type is B and there is already an completed file in share folder,there is no need to retransmitting the file
            if os.path.exists(file_final) and os.path.getsize(file_final) == file_size:
                connection.send(str(file_size).encode())

            #the transmitting will be started/recovered
            else:
                #if there is a file already in the temp_folder and not completed yet, the 'received_size' will be given to peer sender to help recover from a break
                if os.path.exists(file_new_name):
                    received_size = os.path.getsize(file_new_name)
                connection.send(str(received_size).encode())

                w_file = open(file_new_name, 'ab')

                #to show the progress of the current transmitting
                #temp = 0

                while not received_size == file_size:
                    r_data = connection.recv(131072)
                    received_size += len(r_data)
                    w_file.write(r_data)
                    #progress = round(received_size/file_size,2)
                    #if(not progress == temp):
                    #    print(str(progress) +" completed")
                    #    temp = progress
                w_file.close()
                #endtime = time.time()

                #if the transmitting finished, then move the file
                try:
                    shutil.move(file_new_name,hierarchy)
                except:
                    os.remove(file_path_name)
                    shutil.move(file_new_name,hierarchy)
                #to shot the transmitting speed
                #time_consume = endtime - starttime
                #benchmark = round(file_size/time_consume/1024/1024,2)
                #print((str)(benchmark) + " MBps")

                #get the mtime
                update_time = os.path.getmtime(file_path_name)
                fsize = os.path.getsize(file_path_name)
                file_mtime_size = (update_time, fsize, False)

                #help scanner remember this file, so that the scanner will not take this file as a change which should be sen
                config.old_file_dict[file_path_name]= file_mtime_size
                print(file_path_name + " is finishted!")

            connection.close()

def switch_path(path):

    path = path.replace('\\','/')
    return path

def call_reveiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', config.port1))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        thread = threading.Thread(target=receiver_fun, args=(connection,))
        thread.start()

