#!/usr/bin/env pythom3
"""
BasicCache that inherits from BaseCaching and
is a caching system.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    BasicCache that inherits from BaseCaching and
    is a caching system.
    """

    def __init__(self):
        """
        thr constructor method
        """
        super().__init__()
        self.count = {}

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item
        value for the key key.
        If key or item is None, this method should not do anything.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:

        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded and following
        by a new line
        """

        if key in self.cache_data:
            self.count[key] += 1
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                high = 10000
                for k, v in self.count.items():
                    if v < high:
                        value = k
                        high = v

                del self.cache_data[value]
                del self.count[value]
                print("DISCARD: {}".format(value))
            self.cache_data[key] = item
            if self.count.get(key) is None:
                self.count[key] = 1
            else:
                self.count[key] += 1

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """

        if self.cache_data.get(key) is None or key is None:
            return None

        if self.count.get(key) is None:
            self.count[key] = 1
        else:
            self.count[key] += 1
        return self.cache_data.get(key)
