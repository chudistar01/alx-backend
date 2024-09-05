#!/usr/bin/env python3

'''Task 1
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, first_value = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''Returns thhe value in thhe dictionary
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]