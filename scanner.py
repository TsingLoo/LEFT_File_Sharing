import time,os,threading,config,receiver,sender

#scanner.py scans the share folder at 10Hz, by comparing the current file dict and old file dict, the scanner can tell what is new for sending

share_folder_path = os.path.join(os.getcwd(),'share')

def scanner_fun(peer_ip_address):

    #the difference between the current file dict and the old file dict
    differ = {}

    #the current file dict
    file_dict = {}

    while True:
        #the old_file_dict copy the lastest file_dict
        config.old_file_dict = file_dict.copy()
        time.sleep(0.1)

        #reset the file dict
        file_dict = {}

        #scan the share folder
        for root,dirs,files in os.walk(share_folder_path):

            for file in files:

                #get file size,get file mtime
                file_path = os.path.join(root, file).replace(os.getcwd(),'.') #str class
                fsize = os.path.getsize(file_path)
                update_time = os.path.getmtime(file_path)
                #the default send type is B, where the bool is set as False
                file_mtime_size = (update_time,fsize,False) #tuple class
                file_path = receiver.switch_path(file_path)

                #keep the information in the dict
                file_dict[file_path]= file_mtime_size

            #get the difference of the current file dict and old file dict
            differ = set(file_dict.items()).difference(set(config.old_file_dict.items()))

        #if there is difference
        if(differ):


            for item in differ:

                #if the file_name has been recorded in the dict, then the difference is called by content update, sent type A is called
                if(config.old_file_dict.__contains__(item[0])):

                    print("TYPE A")
                    itemlist = list(item[1])
                    itemlist[2] = True

                    item = (item[0], tuple(itemlist))



                print("I will send ", item[0])
                #time.sleep(3)
                sender.call_sender(peer_ip_address, item)


def call_scanner(peer_ip_address):

    scanner_thread = threading.Thread(target = scanner_fun,args=(peer_ip_address,))
    scanner_thread.start()

