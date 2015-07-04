#import socket module

from socket import *
import datetime

serverSocket = socket(AF_INET, SOCK_STREAM) #creates socket

#Prepare a sever socket
#serverName = '127.0.0.1'
serverPort = 80
serverSocket.bind(('', serverPort)) #associates socket with this port
serverSocket.listen(1) #tells socket to listen for requests

while True:

    #Create the Server Connection 

    print 'SERVER CONNECTION READY!!!'
    connectionSocket, addr =  serverSocket.accept() #creates a socket specifically for this client
    print "SOURCE ADDRESS: \n", addr
    try:
        message = connectionSocket.recv(1024) #receives message from client
        print "message: \n" , message
        filename = message.split()[1]
        
        f = open(filename[1:])
        outputdata = f.read()
        
        now = datetime.datetime.now()

        #Send one HTTP header line into socket
        first_header = "HTTP/1.1 200 OK"
        header_info = {
			"Date": now.strftime("%Y-%m-%d %H:%M"),
			"Content-Length": len(outputdata),
			"Keep-Alive": "timeout=%d,max=%d" %(10,100),
			"Connection": "Keep-Alive",
			"Content-Type": "text/html"
		}
        following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
        print "following_header:", following_header
        connectionSocket.send("%s\r\n%s\r\n\r\n" %(first_header, following_header))#sends a 200 OK 
        
        #connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n') #sends a 200 OK 

        #Send the content of the requested file to the client

        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i]) #output all of the data in the file
        connectionSocket.close() #closes the socket for this client

        print "FILE RECIEVED"
        
    except IOError:
        #Send response message for file not found
        connectionSocket.send('Error 404 File Not Found\n\n') #send an error message to be printed on the page

        connectionSocket.close() #close the socket for the client
serverSocket.close() #close the server socket
