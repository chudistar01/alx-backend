#!/usr/bin/env python3

'''Task 2
'''


from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Subclass thhhat inherits from base class
    '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Assign value to dictionary
        '''

        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''Returns thhe value in thhe dictionary
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
