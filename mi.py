import sys
import struct
strToPrint = ""
with open('dest.txt','rb') as f:

    byte = f.read(1)
    print(byte)

    while byte:
        byte = f.read(1)
        print(byte)
        print(byte.hex())
        DecFromBytes = int.from_bytes(byte, byteorder=sys.byteorder)
        print(DecFromBytes)
        xorResult = DecFromBytes^5
        chrToPrint = chr(xorResult)
        print(chrToPrint)

        #print(struct.pack(">H",xorResult).decode("utf-8"))
        strToPrint = strToPrint + chrToPrint
    f.close()

#strToPrint.encode("gbk")
print(strToPrint)


#print(str)

#print(bxor(key1,key2))

#message = hex^key1

#print(type(message))

#b = bytes(message)


#print(b.decode())
