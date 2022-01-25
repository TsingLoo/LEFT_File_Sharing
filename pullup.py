import scanner
import receiver

peer_ip_address = "192.168.3.65"



if __name__ == "__main__":

    scanner.call_scanner(peer_ip_address)
    receiver.call_reveiver()

