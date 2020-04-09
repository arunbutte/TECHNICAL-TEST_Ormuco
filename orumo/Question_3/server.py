"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""
import socket
import json
from threading import Thread
import time

#cache file imported
import lru_cache

class Server:
    ip = "localhost"
    port = 8888
    cache_operation = {}

    def __init__(self):
        ''' start the server to listen at the port for incoming connections
             and Add the server details in central server
            '''
        Thread(target = self.start_server).start()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 7777))
        server_details = { self.ip : self.port}
        data = json.dumps(server_details).encode('utf-8')
        print data
        sock.sendall(data)
        sock.close()
        
    def start_server(self):
        cache = lru_cache.LRUCache(1024)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = socket.socket()          
        print "Socket successfully created"
        s.bind((self.ip, self.port))         
        print "socket binded to %s" %(self.port)
        s.listen(1)      
        print "socket is listening"
        while True: 
            # Establish connection with client. 
            connn, addr = s.accept()      
            print 'Got connection from', addr
            data = b''
            while 1:
                print " here" 
                tmp = connn.recv(1024)
                if not tmp:
                    break
                else:
                    data = data + tmp
            print data
            self.cache_operation = json.loads(data.decode('utf-8'))
            result = getattr(cache, self.cache_operation['operation'])(self.cache_operation['params'])
            connn.sendall(result)   
            connn.close()
        s.close()
    

if __name__ == "__main__":
    s = Server()
