"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""

import socket
import json
from threading import Thread
from threading import Lock

global lock
global server_data 

lock = Lock()
server_data = {}

def send_server_data():
    global server_data
    s = socket.socket()          
    print "Socket successfully created"
    port = 6666
    s.bind(('localhost', port))         
    print "socket binded to %s" %(port)
    s.listen(1)      
    print "socket is listening"
    while True: 
  
        # Establish connection with client. 
        c, addr = s.accept()      
        print 'Got connection from', addr 

        # send server details 
        lock.acquire()     # critical section
        data = json.dumps(server_data).encode('utf-8')
        lock.release()     #critical section end
        print data
        c.sendall(data)
        # Close the connection with the client
        "waiting for acknowledgement"
        tmp = c.recv(1024)
        print tmp
        c.close()
    s.close()

def add_server():
    global server_data
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('localhost', 7777))
    print(" add server socket done")
    sk.listen(1)
    while True:
        conn, addr = sk.accept()
        b = b''
        while 1:
            tmp = conn.recv(1024)
            if not tmp:
                break
            b += tmp
        new_server = json.loads(b.decode('utf-8'))
        print(new_server)
        lock.acquire()  # critical section
        server_data = dict(server_data.items() + new_server.items())
        lock.release()     #critical section end
        print server_data
    sk.close()
    

if __name__ == "__main__":
    Thread(target = send_server_data).start()
    Thread(target = add_server).start()
