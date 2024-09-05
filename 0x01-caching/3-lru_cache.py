#!/usr/bin/env python3

'''Task 3
'''


from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Subclass thhhat inherits from base class
    '''
    def __init__(self):
        '''init function
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Assign value to dictionary
        '''

        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item
                

    def get(self, key):
        '''Returns thhe value in thhe dictionary
        '''
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)