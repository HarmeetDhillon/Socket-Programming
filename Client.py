from socket import *
import sys

clientSocket = socket(AF_INET, SOCK_STREAM) #creates socket

server_address = ('127.0.0.1', 80)#create connection at this given port

print >>sys.stderr, 'CONNECTING TO %s AT PORT  %s' % server_address

clientSocket.connect(server_address)#connect to server at given address
filename=raw_input("ENTER THE FILENAME:   ")
f = open(filename[0:])
outputdata = f.read()#read the input file into variable 
print "HTML CODE OF THE GIVEN FILE:", outputdata #display the html code of the file

clientSocket.close() #close the connection
