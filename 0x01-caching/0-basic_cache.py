#!/usr/bin/env python3

'''First task in cache project
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A subclass thhat inherits from BaseCaching(base clas
    '''

    def put(self, key, item):
        '''Assign to the dictionary from the base class a key and a value
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Returns thhe value in thhe dictionary
        '''
        return self.cache_data(key, None)
