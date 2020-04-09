"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""

import socket
import json
import time
import sys

class Client:
    ip = "localhost"
    port = 5555
    server_details = {}
    nearest_server = []

    def __init__(self, operation = None, data_key = None, mem_value = None):
        self.get_server_list( 'localhost', 6666)
        self.find_nearest_server()

    def get_server_list( self, central_server_host, central_server_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((central_server_host, central_server_port))
        data = " Client requesting server details"
        s.sendall(data)
        data = ""
        while True:
            print "aaaa"
            tmp = s.recv(1024)
            if not tmp:
                break
            else:
                data = data + tmp
                print data
        self.server_details = json.loads(data.decode('utf-8'))
        data = "server list received"
        s.sendall(data)
        print self.server_details
        s.close()

    def find_nearest_server(self):
        nearest_server_ping_time = 0
        for host,port in self.server_details.iteritems():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            time_before = time.time()
            try:
                sock.connect((host, port))
            except:
                print " server not recheable"
                continue
            result = time.time() - time_before
            if nearest_server_ping_time:
                if result < nearest_server_ping_time:
                    self.nearest_server = [host , port]
            else:
                self.nearest_server = [host , port]    
            print self.nearest_server
            sock.close()
    def perform_cache_operation(self, data):
        data_send = json.dumps(data).encode('utf-8')
        print data_send
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.connect((self.nearest_server[0], self.nearest_server[1]))
        pp = s1.sendall(data_send)
        print self.nearest_server[1]
        print pp
        result = ""
        while True:
            print "aaaa"
            tmp = s1.recv(1024)
            if not tmp:
                break
            else:
                result = result + tmp
                print result
        s1.close()
        
        
        


if __name__ == "__main__":
    c = Client()
    data = {}

    print "Adding cache dataa : key - 1 , value : helloo"
    data['operation'] = 'add_cache_data'
    data['params'] = [1,'helloo'] 
    c.perform_cache_operation(data)

    print "Retrieve cache dataa at key - 1 "
    data['operation'] = 'retrieve_cache_data'
    data['params'] = [1]
    c.perform_cache_operation(data)

    print "Update cache dataa at key - 1, value: Hello again "
    data['operation'] = 'update_cache_data'
    data['params']= [1, "Hello again"]
    c.perform_cache_operation(data)
        

    print "Clearing Cache "
    data['operation'] = 'clear_cache_data'
    data['params'] = []
    c.perform_cache_operation(data)
        
    
