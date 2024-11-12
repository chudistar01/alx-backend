from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache system."""

    def __init__(self):
        """Initialize LFUCache."""
        super().__init__()
        self.cache_data = {}
        self.freq_map = defaultdict(OrderedDict)
        self.key_freq = {}  
        self.min_freq = 0

    def __update_freq(self, key):
        """Update the frequency of a key."""
        freq = self.key_freq[key]
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_freq[key] += 1
        new_freq = self.key_freq[key]
        self.freq_map[new_freq][key] = None

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.__update_freq(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.freq_map[self.min_freq].popitem(last=False)
                del self.cache_data[lfu_key]
                del self.key_freq[lfu_key]
                print(f"DISCARD: {lfu_key}")
            self.cache_data[key] = item
            self.key_freq[key] = 1
            self.freq_map[1][key] = None
            self.min_freq = 1

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        self.__update_freq(key)
        return self.cache_data[key]

