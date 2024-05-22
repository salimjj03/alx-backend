#!/usr/bin/env pythom3
"""
BasicCache that inherits from BaseCaching and
is a caching system.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    BasicCache that inherits from BaseCaching and
    is a caching system.
    """

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

        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                value = list(self.cache_data)[-1]
                del self.cache_data[value]
                print("DISCARD: {}".format(value))
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """

        if self.cache_data.get(key) is None or key is None:
            return None
        return self.cache_data.get(key)
