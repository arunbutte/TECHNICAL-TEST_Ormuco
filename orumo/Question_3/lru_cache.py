"""
Created on Tue Apr  7 17:09:31 2020

@author: Arun_Arun
"""

import sys

class LRUCache:
    cache_size = None
    cache = {}
    cache_keys = []
    
    def __init__(self, cache_size):
        self.cache_size = cache_size

        
    def retrieve_cache_data(self, params):
        if params[0] in self.cache.keys():
            self.cache_keys.remove(params[0])
            self.cache_keys.insert(0,params[0])
            return self.cache[params[0]]
        else:
            return "cache miss"

        
    def update_cache_data(self, params):
        if params[0] in self.cache.keys():
            self.cache_keys.remove(params[0])
            self.cache_keys.insert(0,params[0])
            self.cache[params[0]] = params[1]
            return self.cache[params[0]]
        else:
            return "cache miss"

        
    def remove_cache_data(self, params):
        if params[0] in self.cache.keys():
            self.cache_keys.remove(params[0])
            del self.cache[params[0]]
            return 1
        else:
            return "cache miss"

    
    def clear_cache_data(self, params):
        self.cache_size = None
        self.cache.clear()
        del self.cache_keys[:]
        return 1

    def add_cache_data (self, params):
        if params[0] in self.cache.keys():
            return " cache value already exists, call update cache function"
        else:
            while sys.getsizeof(self.cache) + sys.getsizeof(params[1]) > self.cache_size:
                print (sys.getsizeof(self.cache))
                print self.cache_size
                del self.cache[self.cache_keys[-1]]
                self.cache_keys.pop()

            
            self.cache_keys.insert(0,params[0])
            self.cache[params[0]] = params[1]
            return self.cache[params[0]]  
                


