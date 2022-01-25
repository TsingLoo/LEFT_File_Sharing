#config.py maintains the global variables to help different threads work with each other

#to help scanner remember what was in the share folder
global old_file_dict

#to mark whether the host has a peer online
global peer_online

#is reserved for find and connect the peer
global port0

global port1


port0 = 23020
port1 = 50000 - port0
peer_online = False
old_file_dict = {}

