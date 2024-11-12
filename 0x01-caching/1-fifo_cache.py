#!/usr/bin/env python3
"""Task 1
"""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Subclass thhhat inherits from base class
    """
    def __init__(self):
        """instance method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign value to dictionary
        """
        if key is None or item is None:
            return
        
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Returns the value in thhe dictionary
        """
        return self.cache_data.get(key, None)
