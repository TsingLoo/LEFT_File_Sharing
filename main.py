import argparse,socket,scanner,receiver,config,listener,os
#main.py calls all the necessary thread to finish the job

#use argparse module to support command
ap = argparse.ArgumentParser()
ap.add_argument('-i',"--ip",required=True,help="type in the ip address of peer")
peer_ip_addressdict = vars(ap.parse_args())
peer_ip_address = peer_ip_addressdict['ip']



if __name__ == "__main__":

    if not os.path.exists('temp_share'):
        os.makedirs('temp_share')

    #call listener thread, which aims to find if there is a peer online connected to host
    listener.call_listener(peer_ip_address)

    #if there is no peer online, the host will try to find its peer
    while not config.peer_online:
        try:
            #a sock object is created to find and connect the peer
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #'config.port' is reserved for find and connect the peer
            sock.connect((peer_ip_address, config.port0))
            #Once the connection is built, the 'config.peer_online' will be marked as True, which means the host gets his peer right now
            config.peer_online = True

            print("I have connected my peer! He is " , peer_ip_address)

            #'config.old_file_dict' is cleared, which means the memory of scanner is cleared, each file in share will be marked as a change
            config.old_file_dict = {}

        #if fail to find and connect the peer
        except Exception as e:
            print("If the program stuck in this stage, please go to the config.py and reset the port between 20000 to 30000,except 25000. And then wait for seconds then restart main.py ")

    #call scanner thread, which aims to check whether there is some changes in share folder, if there is a change, then the scanner thread will call the sender thread to send the file
    scanner.call_scanner(peer_ip_address)
    #call receiver thread, which aims to waiting for coming files and checks whether to update exsisting files
    receiver.call_reveiver()

